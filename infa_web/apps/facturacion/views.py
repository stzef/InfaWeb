from django.shortcuts import render,render_to_response
from django.template.loader import get_template

from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView
from django.contrib.staticfiles.templatetags.staticfiles import static

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from infa_web.apps.base.constantes import *

import json
import datetime
from infa_web.parameters import ManageParameters

from infa_web.apps.base.value_letters import number_to_letter

from easy_pdf.views import PDFTemplateView

from infa_web.apps.movimientos.models import *
from infa_web.apps.facturacion.models import *
from infa_web.apps.facturacion.bills_fn import *
from infa_web.apps.terceros.models import *
from infa_web.apps.usuarios.models import *
from infa_web.apps.articulos.models import *
from infa_web.apps.facturacion.forms import *
from infa_web.apps.base.forms import *
from infa_web.apps.base.utils import *
from infa_web.routines import costing_and_stock
from django.core.exceptions import ObjectDoesNotExist

def get_clear_data_fac(request_body):
	data = json.loads(request_body)

	data["vttotal"] = float(data["vttotal"])
	data["vdescu"] = float(data["vdescu"])

	for medio_pago in data["medios_pagos"]:
		medio_pago["cmpago"] = int(medio_pago["cmpago"])
		medio_pago["vmpago"] = float(medio_pago["vmpago"])

	for data_deta in data["mvdeta"]:
		data_deta["canti"] = float(data_deta["canti"])
		data_deta["pordes"] = int(data_deta["pordes"])
		data_deta["vtotal"] = float(data_deta["vtotal"])
		data_deta["vunita"] = float(data_deta["vunita"])

	print data["medios_pagos"]
	print data["mvdeta"]
	return data


class BillList(CustomListView):
	model = Fac
	template_name = "facturacion/list-billings.html"
	form_class = FacForm

	def get_context_data(self,**kwargs):
		context = super(BillList, self).get_context_data(**kwargs)
		context['title'] = "Listar Facturas"
		return context

def code_generate(Model, prefijo, value_get, request_db):
	try:
		value = str(Model.objects.using(request_db).latest(value_get))
		value_sum = str(int(value[2:]) + 1)
		cant_space = 8-int(len(value_sum))
		model_pk = prefijo + (cant_space * '0') + value_sum
	except Model.DoesNotExist:
		model_pk = prefijo+'00001000'
	return model_pk

def value_tot(query_array, code_find):
	return sum(float(data['vmpago']) for data in query_array if data['cmpago'] == code_find)

def save_fac(request_db, fac_array):
	fac = get_or_none(Fac, request_db, cfac = fac_array['fac_pk'])
	if fac is not None:
		fac.citerce = fac_array['citerce']
		fac.cesdo = fac_array['cesdo']
		fac.fpago = fac_array['fpago']
		fac.ctifopa = fac_array['ctifopa']
		fac.descri = fac_array['descri']
		fac.vtbase = fac_array['vtbase']
		fac.vtiva = fac_array['vtiva']
		fac.vflete = fac_array['vflete']
		fac.vdescu = fac_array['vdescu']
		fac.vttotal = fac_array['vttotal']
		fac.ventre = fac_array['ventre']
		fac.vcambio = fac_array['vcambio']
		fac.cvende = fac_array['cvende']
		fac.cdomici = fac_array['cdomici']
		fac.tpordes = fac_array['tpordes']
		fac.cemdor = fac_array['cemdor']
		fac.brtefte = fac_array['brtefte']
		fac.prtefte = fac_array['prtefte']
		fac.vrtefte = fac_array['vrtefte']
		fac.vefe = fac_array['vefe']
		fac.vtar = fac_array['vtar']
		fac.vch = fac_array['vch']
		fac.vcred = fac_array['vcred']
	else:
		fac = Fac(
			cfac = fac_array['fac_pk'],
			femi = fac_array['femi'],
			citerce = fac_array['citerce'],
			cesdo = fac_array['cesdo'],
			fpago = fac_array['fpago'],
			ctifopa = fac_array['ctifopa'],
			descri = fac_array['descri'],
			vtbase = fac_array['vtbase'],
			vtiva = fac_array['vtiva'],
			vflete = fac_array['vflete'],
			vdescu = fac_array['vdescu'],
			vttotal = fac_array['vttotal'],
			ventre = fac_array['ventre'],
			vcambio = fac_array['vcambio'],
			ccaja = fac_array['ccaja'],
			cvende = fac_array['cvende'],
			cdomici = fac_array['cdomici'],
			tpordes = fac_array['tpordes'],
			cemdor = fac_array['cemdor'],
			brtefte = fac_array['brtefte'],
			prtefte = fac_array['prtefte'],
			vrtefte = fac_array['vrtefte'],
			vefe = fac_array['vefe'],
			vtar = fac_array['vtar'],
			vch = fac_array['vch'],
			vcred = fac_array['vcred']
		)
	fac.save(using = request_db)
	return fac

def save_mvsa(request_db, mvsa_array):
	mvsa = get_or_none(Mvsa, request_db, docrefe = mvsa_array['docrefe'])
	if mvsa is not None:
		mvsa.citerce = mvsa_array['citerce']
		mvsa.vttotal = mvsa_array['vttotal']
	else:
		mvsa = Mvsa(
			fmvsa = mvsa_array['fmvsa'],
			docrefe = mvsa_array['docrefe'],
			citerce = mvsa_array['citerce'],
			ctimo = mvsa_array['ctimo'],
			cesdo = mvsa_array['cesdo'],
			vttotal = mvsa_array['vttotal'],
			descri = mvsa_array['descri']
		)
	mvsa.save(using = request_db)
	return mvsa

def save_movi(request_db, movi_array):
	movi = movi_find(movi_array['cfac'], request_db, movi_array['ctimo'].pk)
	if movi:
		movi = movi[0]
		movi.citerce = movi_array['citerce']
		movi.vttotal = movi_array['vttotal']
		movi.vefe = movi_array['vefe']
		movi.vtar = movi_array['vtar']
		movi.vch = movi_array['vch']
		movi.vcred = movi_array['vcred']
		movi.ventre = movi_array['ventre']
		movi.vcambio = movi_array['vcambio']
		movi.baseiva = movi_array['baseiva']
		movi.vtiva = movi_array['vtiva']
		movi.vtsuma = movi_array['vtsuma']
		movi.vtdescu = movi_array['vtdescu']
	else:
		movi = Movi(
			cmovi = movi_array['cmovi'],
			ctimo = movi_array['ctimo'],
			citerce = movi_array['citerce'],
			fmovi = movi_array['fmovi'],
			descrimovi = movi_array['descrimovi'],
			vttotal = movi_array['vttotal'],
			cesdo = movi_array['cesdo'],
			vefe = movi_array['vefe'],
			vtar = movi_array['vtar'],
			vch = movi_array['vch'],
			vcred = movi_array['vcred'],
			ventre = movi_array['ventre'],
			vcambio = movi_array['vcambio'],
			ccaja = movi_array['ccaja'],
			baseiva = movi_array['baseiva'],
			vtiva = movi_array['vtiva'],
			vtsuma = movi_array['vtsuma'],
			vtdescu = movi_array['vtdescu']
		)
	movi.save(using = request_db)
	return movi

def movi_find(fac, request_db, ctimo_billing):
	return Movi.objects.using(request_db).filter(movideta__docrefe = fac, ctimo__pk = ctimo_billing)

def ctimo_billing(ctimo_billing, request_db):
	manageParameters = ManageParameters(request_db)
	ctimo_billing = manageParameters.get_param_value(ctimo_billing)
	return Timo.objects.using(request_db).get(pk = ctimo_billing)

def save_movideta(request_db, movideta_array):
	movi = movi_find(movideta_array['docrefe'], request_db, movideta_array['ctimo'])
	movi =  Movi.objects.using(request_db).get(cmovi = (movideta_array['cmovi'].cmovi if not movi else (movi[0] if movi.count() > 1 else movi)))
	try:
		movideta = movi.movideta_set.using(request_db).get(itmovi = movideta_array['itmovi'])
		movideta.vmovi = movideta_array['vmovi']
	except Movideta.DoesNotExist:
		movideta = Movideta(
			cmovi = movi,
			itmovi = movideta_array['itmovi'],
			docrefe = movideta_array['docrefe'],
			detalle = movideta_array['detalle'],
			vmovi = movideta_array['vmovi']
		)
	movideta.save(using = request_db)
	return movideta

def save_fac_pago(request_db, fac_pago_array):
	fac_pago = get_or_none(Facpago, request_db, cfac = fac_pago_array['cfac'].pk, it = fac_pago_array['it'])
	if fac_pago is not None:
		fac_pago.cmpago = fac_pago_array['cmpago']
		fac_pago.docmpago = fac_pago_array['docmpago']
		fac_pago.banmpago = fac_pago_array['banmpago']
		fac_pago.vmpago = fac_pago_array['vmpago']
	else:
		fac_pago = Facpago(
			cfac = fac_pago_array['cfac'],
			it = fac_pago_array['it'],
			cmpago = fac_pago_array['cmpago'],
			docmpago = fac_pago_array['docmpago'],
			banmpago = fac_pago_array['banmpago'],
			vmpago = fac_pago_array['vmpago']
		)
	fac_pago.save(using=request_db)
	return fac_pago

def save_movi_pago(request_db, movi_pago_array):
	movi_pago = get_or_none(Movipago, request_db, cmovi = movi_pago_array['cmovi'].pk, it = movi_pago_array['it'])
	if movi_pago is not None:
		movi_pago.cmpago = movi_pago_array['cmpago']
		movi_pago.docmpago = movi_pago_array['docmpago']
		movi_pago.banmpago = movi_pago_array['banmpago']
		movi_pago.vmpago = movi_pago_array['vmpago']
	else:
		movi_pago = Movipago(
			cmovi = movi_pago_array['cmovi'],
			it = movi_pago_array['it'],
			cmpago = movi_pago_array['cmpago'],
			docmpago = movi_pago_array['docmpago'],
			banmpago = movi_pago_array['banmpago'],
			vmpago = movi_pago_array['vmpago']
		)
	movi_pago.save(using=request_db)
	return movi_pago

def save_fac_deta(request_db, fac_deta_array):
	fac_deta = get_or_none(Facdeta, request_db, cfac = fac_deta_array['cfac'].pk, itfac = fac_deta_array['itfac'])
	if fac_deta is not None:
		fac_deta.nlargo = fac_deta_array['nlargo']
		fac_deta.ncorto = fac_deta_array['ncorto']
		fac_deta.canti = fac_deta_array['canti']
		fac_deta.civa = fac_deta_array['civa']
		fac_deta.niva = fac_deta_array['niva']
		fac_deta.poriva = fac_deta_array['poriva']
		fac_deta.pordes = fac_deta_array['pordes']
		fac_deta.vunita = fac_deta_array['vunita']
		fac_deta.viva = fac_deta_array['viva']
		fac_deta.vbase = fac_deta_array['vbase']
		fac_deta.vtotal = fac_deta_array['vtotal']
		fac_deta.pvtafull = fac_deta_array['pvtafull']
		fac_deta.vcosto = fac_deta_array['vcosto']
	else:
		fac_deta = Facdeta(
			cfac = fac_deta_array['cfac'],
			itfac = fac_deta_array['itfac'],
			carlos = fac_deta_array['carlos'],
			nlargo = fac_deta_array['nlargo'],
			ncorto = fac_deta_array['ncorto'],
			canti = fac_deta_array['canti'],
			civa = fac_deta_array['civa'],
			niva = fac_deta_array['niva'],
			poriva = fac_deta_array['poriva'],
			pordes = fac_deta_array['pordes'],
			vunita = fac_deta_array['vunita'],
			viva = fac_deta_array['viva'],
			vbase = fac_deta_array['vbase'],
			vtotal = fac_deta_array['vtotal'],
			pvtafull = fac_deta_array['pvtafull'],
			vcosto = fac_deta_array['vcosto'],
		)
	fac_deta.save(using=request_db)
	return fac_deta

def save_mvsa_deta(request_db, mvsa_deta_array):
	mvsa_deta = get_or_none(Mvsadeta, request_db, cmvsa = mvsa_deta_array['cmvsa'].pk, carlos = mvsa_deta_array['carlos'].pk)
	if mvsa_deta is not None:
		mvsa_deta.it = mvsa_deta_array['it']
		mvsa_deta.carlos = mvsa_deta_array['carlos']
		mvsa_deta.nlargo = mvsa_deta_array['nlargo']
		mvsa_deta.canti = mvsa_deta_array['canti']
		mvsa_deta.vunita = mvsa_deta_array['vunita']
		mvsa_deta.vtotal = mvsa_deta_array['vtotal']
	else:
		mvsa_deta = Mvsadeta(
			cmvsa = mvsa_deta_array['cmvsa'],
			it = mvsa_deta_array['it'],
			carlos = mvsa_deta_array['carlos'],
			nlargo = mvsa_deta_array['nlargo'],
			canti = mvsa_deta_array['canti'],
			vunita = mvsa_deta_array['vunita'],
			vtotal = mvsa_deta_array['vtotal'],
		)
	mvsa_deta.save(using=request_db)
	return mvsa_deta

@csrf_exempt
def BillSave(request):
	today = datetime.datetime.today()
	default_fecha = today.strftime("%Y-%m-%d %H:%M:%S")
	# Recibe parametros en JSON desde la vista
	data = get_clear_data_fac(request.body)
	response = {}
	fac_pk = ""
	response["error"] = False
	response["message"] = "Factura Guardada con Exito"

	# Datos de Prueba - Cambiar Posteriormente
	usuario_actual = Usuario.objects.using(request.db).all()[0]
	# Datos de Prueba - Cambiar Posteriormente

	# variable para total de medios de pago
	medios_pagos_total = 0

	# variable para total de pago en efectivo
	vefe_t = 0

	# variable para total de pago en tarjeta de credito
	vtar_t = 0

	# variable para total de pago en cheque
	vch_t = 0

	# variable para total de credito
	vncred_t = 0

	# Valores por defecto para calculos de facturacion
	default_vflete = 0
	default_brtefte = 0
	default_prtefte = 0
	default_ventre = 0

	# Busqueda a modelos de acuerdo a los parametros recibidos
	data_femi = data['femi'] + " " + today.strftime("%H:%M:%S") if 'femi' in data else default_fecha
	data_fpago = data['fpago']  if 'fpago' in data else default_fecha
	data_descri = data['descri'] if 'descri' in data else ""

	data_vdescu = float(data['vdescu'])
	data_vflete = float(data['vflete']) if 'vflete' in data else default_vflete

	data_ventre = float(data['ventre']) if 'ventre' in data else default_ventre

	data_brtefte = float(data['brtefte']) if 'brtefte' in data else default_brtefte
	data_prtefte = float(data['prtefte']) if 'prtefte' in data else default_prtefte


	data_vttotal = float(data['vttotal'])

	# Calculos
	calc_vcambio = calcular_valor_cambio(data_ventre,data_vttotal)

	calc_vflete = calcular_total_flete(data_brtefte,data_prtefte)
	calc_vtbase_vtiva = calcular_vtbase_vtiva(data['mvdeta'],request.db)
	#calc_vttotal = calcular_total(data['mvdeta'],data_vflete,data_vdescu)


	data_vcambio = float(data['vcambio']) if 'vcambio' in data else calc_vcambio
	data_vrtefte = float(data['vrtefte']) if 'vrtefte' in data else calc_vflete
	data_vtbase = float(data['vtbase']) if 'vtbase' in data else calc_vtbase_vtiva["vtbase"]
	data_vtiva = float(data['vtiva']) if 'vtiva' in data else calc_vtbase_vtiva["vtiva"]

	ctifopa = Tifopa.objects.using(request.db).get(pk = data['ctifopa'])
	#ccaja = Caja.objects.using(request.db).get(pk = data['ccaja'])
	ccaja = usuario_actual.ccaja

	citerce = Tercero.objects.using(request.db).get(pk = data['citerce'] if "citerce" in data else DEFAULT_TERCERO)
	cesdo = Esdo.objects.using(request.db).get(pk = data['cesdo'] if "cesdo" in data else DEFAULT_ACTIVO)
	cvende = Vende.objects.using(request.db).get(pk = data['cvende'] if "cvende" in data else DEFAULT_VENDE)
	cdomici = Domici.objects.using(request.db).get(pk = data['cdomici'] if "cdomici" in data else DEFAULT_DOMICILIARIO)
	cemdor = Emdor.objects.using(request.db).get(pk = data['cemdor'] if "cemdor" in data else DEFAULT_EMPACADOR)

	value_vttotal = float(data['vttotal'])
	ctimo = ctimo_billing('ctimo_rc_billing', request.db)
	val_cont = 1

	# sumatoria para cada forma de pago
	vefe_t = value_tot(data["medios_pagos"], 1000)
	vtar_t = value_tot(data["medios_pagos"], 1001)
	vch_t = value_tot(data["medios_pagos"], 1002)
	vncred_t = value_tot(data["medios_pagos"], 1003)

	medios_pagos_total = vefe_t + vtar_t + vch_t + vncred_t

	fac_pk = code_generate(Fac, ccaja.ctimocj.prefijo, 'cfac', request.db)

	# guarda los datos en factura
	fac = save_fac(
		request.db,
		{
			'fac_pk': fac_pk,
			'femi': data_femi,
			'citerce': citerce,
			'cesdo': cesdo,
			'fpago': data_fpago,
			'ctifopa': ctifopa,
			'descri': data_descri,
			'vtbase': data_vtbase,
			'vtiva': data_vtiva,
			'vflete': data_vflete,
			'vdescu': data_vdescu,
			'vttotal': data_vttotal,
			'ventre': data_ventre,
			'vcambio': data_vcambio,
			'ccaja': ccaja,
			'cvende': cvende,
			'cdomici': cdomici,
			'tpordes': 0,
			'cemdor': cemdor,
			'brtefte': data_brtefte,
			'prtefte': data_prtefte,
			'vrtefte': data_vrtefte,
			'vefe': vefe_t,
			'vtar': vtar_t,
			'vch': vch_t,
			'vcred': vncred_t
		}
	)

	# crea un movimiento de salida para los articulos recibidos en la factura
	mvsa = save_mvsa(
		request.db,
		{
			'fmvsa': data_femi,
			'docrefe': fac.cfac,
			'citerce': citerce,
			'ctimo': ccaja.ctimocj,
			'cesdo': cesdo,
			'vttotal': data_vttotal,
			'descri': data_descri
		}
	)

	while(val_cont != 0):
		movi_pk = code_generate(Movi, ctimo.prefijo, 'cmovi', request.db)

		movi = save_movi(
			request.db,
			{
				'cfac': fac.cfac,
				'cmovi': movi_pk,
				'ctimo': ctimo,
				'citerce': citerce,
				'fmovi': data_femi,
				'descrimovi': '-',
				'vttotal': medios_pagos_total,
				'cesdo': cesdo,
				'vefe': vefe_t,
				'vtar': vtar_t,
				'vch': vch_t,
				'vcred': vncred_t,
				'ventre': data_ventre,
				'vcambio': data_vcambio,
				'ccaja': ccaja,
				'baseiva': data_vtbase,
				'vtiva': data_vtiva,
				'vtsuma': data_vttotal,
				'vtdescu': data_vdescu
			}
		)

		if not data["medios_pagos"]:
			movideta = save_movideta(
				request.db,
				{
					'ctimo': ctimo.pk,
					'cmovi': movi,
					'itmovi': 1,
					'docrefe': fac.cfac,
					'detalle': '-',
					'vmovi': medios_pagos_total
				}
			)
		else:
			data_it = 1
			for data_facpago in data["medios_pagos"]:
				mediopago = MediosPago.objects.using(request.db).get(pk = data_facpago['cmpago'])
				banmpago = Banfopa.objects.using(request.db).get(pk = data_facpago['banmpago'] if 'banmpago' in data_facpago else DEFAULT_BANCO)

				data_facpago_docpago = data_facpago['docmpago'] if 'docmpago' in data_facpago else 0
				fac_pago = save_fac_pago(
					request.db,
					{
						'cfac': fac,
						'it': data_it,
						#'it': data_facpago['it'],
						'cmpago': mediopago,
						'docmpago': data_facpago_docpago,
						'banmpago': banmpago,
						'vmpago': float(data_facpago['vmpago'])
					}
				)

				movipago = save_movi_pago(
					request.db,
					{
						'cmovi': movi,
						'it': data_it,
						#'it': data_facpago['it'],
						'cmpago': mediopago,
						'docmpago': data_facpago_docpago,
						'banmpago': banmpago,
						'vmpago': float(data_facpago['vmpago'])
					}
				)

				movideta = save_movideta(
					request.db,
					{
						'cmovi': movi,
						'ctimo': ctimo.pk,
						'itmovi': data_it,
						#'itmovi': data_facpago['it'],
						'docrefe': fac.cfac,
						'detalle': '-',
						'vmovi': medios_pagos_total
					}
				)
				data_it += 1

		if(value_vttotal > medios_pagos_total):
			ctimo = ctimo_billing('ctimo_cxc_billing', request.db)
			cmo = 'CR'
			vefe_t = 0
			vtar_t = 0
			vch_t = 0
			vcred = 0
			data['ventre'] = 0
			data['vcambio'] = 0
			data['vtbase'] = 0
			data['vtiva'] = 0
			data['vttotal'] = 0
			data['vdescu'] = 0
			value_vttotal -= medios_pagos_total
			medios_pagos_total = value_vttotal
			data['medios_pagos'] = {}
		else:
			val_cont = 0

	itfac = 1
	for data_deta in data["mvdeta"]:
		carlos = Arlo.objects.using(request.db).get(pk = data_deta['carlos'])
		data_deta_civa = data_deta['civa'] if 'civa' in data_deta else carlos.ivas_civa.civa
		civa = Iva.objects.using(request.db).get(pk = data_deta_civa)
		vt = float(data_deta['vunita']) * float(data_deta['canti'])
		#viva = vt * (float(civa.poriva)/float(100))

		vtiva_vtbase = calcular_vtbase_vtiva_arlo(data_deta,request.db)

		print "---------------------------"
		print float(carlos.vcosto)
		print "---------------------------"
		fac_deta = save_fac_deta(
			request.db,
			{
				'cfac': fac,
				'itfac': itfac,
				'carlos': carlos,
				'nlargo': carlos.nlargo,
				'ncorto': carlos.ncorto,
				'canti': data_deta['canti'],
				'civa': civa,
				'niva': civa.niva,
				'poriva': civa.poriva,
				'pordes': data_deta['pordes'],
				'vunita': float(data_deta['vunita']),
				'viva': vtiva_vtbase["viva"],
				'vbase': vtiva_vtbase["vbase"],
				'vtotal': vt,
				'pvtafull': float(carlos.pvta1),
				'vcosto': float(carlos.vcosto)
			}
		)

		mvsa_deta = save_mvsa_deta(
			request.db,
			{
				'cmvsa': mvsa,
				'it': itfac,
				'carlos': carlos,
				'nlargo': carlos.nlargo,
				'canti': data_deta['canti'],
				'vunita': float(data_deta['vunita']),
				'vtotal': float(vt)
			}
		)
		costing_and_stock(False, True, {"carlos": carlos.carlos}, request.db)
		itfac = itfac + 1


	related_information = fac.get_related_information(request.db,True)
	response["related_information"] = related_information


	template = get_template("facturacion/partials/billing_documents.html")
	html = template.render({'mode_view':'edit','related_information_factura': fac.get_related_information(request.db,False) })
	response["html"] = html


	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def BillUpdate(request,pk):
	today = datetime.datetime.today()
	default_fecha = today.strftime("%Y-%m-%d %H:%M:%S")
	data = get_clear_data_fac(request.body)
	#data['femi'] = data['femi'] + " " + today.strftime("%H:%M:%S")
	response = {}
	fac_pk = ""
	response["error"] = False
	response["message"] = "Factura Guardada con Exito"
	medios_pagos_total = 0
	vefe_t = 0
	vtar_t = 0
	vch_t = 0
	vncred_t = 0
	val_tot_mp = 0
	exclude_arlo = []

	# Datos de Prueba - Cambiar Posteriormente
	usuario_actual = Usuario.objects.using(request.db).all()[0]
	# Datos de Prueba - Cambiar Posteriormente

	# Valores por defecto para calculos de facturacion
	default_vflete = 0
	default_brtefte = 0
	default_prtefte = 0
	default_ventre = 0

	ctimo = ctimo_billing('ctimo_rc_billing', request.db)
	#ctimo_cxc_billing = manageParameters.get_param_value('ctimo_cxc_billing')
	data_cfac = data['cfac']
	data_femi = data['femi'] + " " + today.strftime("%H:%M:%S") if 'femi' in data else default_fecha
	data_fpago = data['fpago']  if 'fpago' in data else default_fecha
	data_descri = data['descri'] if 'descri' in data else ""

	data_vdescu = float(data['vdescu'])
	data_vflete = float(data['vflete']) if 'vflete' in data else default_vflete

	data_vttotal = float(data['vttotal'])
	data_ventre = float(data['ventre']) if 'ventre' in data else default_ventre

	data_brtefte = float(data['brtefte']) if 'brtefte' in data else default_brtefte
	data_prtefte = float(data['prtefte']) if 'prtefte' in data else default_prtefte

	# Calculos
	calc_vcambio = calcular_valor_cambio(data_ventre,data_vttotal)

	calc_vflete = calcular_total_flete(data_brtefte,data_prtefte)
	calc_vtbase_vtiva = calcular_vtbase_vtiva(data['mvdeta'],request.db)
	#calc_vttotal = calcular_total(data['mvdeta'],data_vflete,data_vdescu)


	data_vcambio = float(data['vcambio']) if 'vcambio' in data else calc_vcambio
	data_vrtefte = float(data['vrtefte']) if 'vrtefte' in data else calc_vflete
	data_vtbase = float(data['vtbase']) if 'vtbase' in data else calc_vtbase_vtiva["vtbase"]
	data_vtiva = float(data['vtiva']) if 'vtiva' in data else calc_vtbase_vtiva["vtiva"]

	ctifopa = Tifopa.objects.using(request.db).get(pk = data['ctifopa'])
	#ccaja = Caja.objects.using(request.db).get(pk = data['ccaja'])
	ccaja = usuario_actual.ccaja

	citerce = Tercero.objects.using(request.db).get(pk = data['citerce'] if 'citerce' in data else DEFAULT_TERCERO)
	cesdo = Esdo.objects.using(request.db).get(pk = data['cesdo'] if 'cesdo' in data else DEFAULT_ACTIVO)
	cvende = Vende.objects.using(request.db).get(pk = data['cvende'] if 'cvende' in data else DEFAULT_VENDE)
	cdomici = Domici.objects.using(request.db).get(pk = data['cdomici'] if 'cdomici' in data else DEFAULT_DOMICILIARIO)
	cemdor = Emdor.objects.using(request.db).get(pk = data['cemdor'] if 'cemdor' in data else DEFAULT_EMPACADOR)

	vefe_t = value_tot(data["medios_pagos"], 1000)
	vtar_t = value_tot(data["medios_pagos"], 1001)
	vch_t = value_tot(data["medios_pagos"], 1002)
	vncred_t = value_tot(data["medios_pagos"], 1003)

	fac = save_fac(
		request.db,
		{
			'fac_pk': data_cfac,
			'femi': data_femi,
			'citerce': citerce,
			'cesdo': cesdo,
			'fpago': data_fpago,
			'ctifopa': ctifopa,
			'descri': data_descri,
			'vtbase': data_vtbase,
			'vtiva': data_vtiva,
			'vflete': data_vflete,
			'vdescu': data_vdescu,
			'vttotal': data_vttotal,
			'ventre': data_ventre,
			'vcambio': data_vcambio,
			'ccaja': ccaja,
			'cvende': cvende,
			'cdomici': cdomici,
			'tpordes': 0,
			'cemdor': cemdor,
			'brtefte': data_brtefte,
			'prtefte': data_prtefte,
			'vrtefte': data_vrtefte,
			'vefe': vefe_t,
			'vtar': vtar_t,
			'vch': vch_t,
			'vcred': vncred_t
		}
	)

	mvsa = save_mvsa(
		request.db,
		{
			'citerce': citerce,
			'docrefe': fac.cfac,
			'vttotal': data_vttotal,
		}
	)

	movi = save_movi(
		request.db,
		{
			'cfac': fac.cfac,
			'ctimo': ctimo,
			'vttotal': (vefe_t + vtar_t + vch_t),
			'citerce': citerce,
			'vefe': vefe_t,
			'vtar': vtar_t,
			'vch': vch_t,
			'vcred': vncred_t,
			'ventre': data_ventre,
			'vcambio': data_vcambio,
			'baseiva': data_vtbase,
			'vtiva': data_vtiva,
			'vtsuma': data_vttotal,
			'vtdescu': data_vdescu,
		}
	)

	for data_facpago in data["medios_pagos"]:
		mediopago = MediosPago.objects.using(request.db).get(pk = data_facpago['cmpago'])
		banmpago = Banfopa.objects.using(request.db).get(pk = data_facpago['banmpago'])
		medios_pagos_total += float(data_facpago['vmpago'])

		fac_pago = save_fac_pago(
			request.db,
			{
				'cfac': fac,
				'it': data_facpago['it'],
				'cmpago': mediopago,
				'docmpago': data_facpago['docmpago'],
				'banmpago': banmpago,
				'vmpago': float(data_facpago['vmpago'])
			}
		)

		movideta = save_movideta(
			request.db,
			{
				'docrefe': fac.cfac,
				'ctimo': ctimo.pk,
				'itmovi': data_facpago['it'],
				'detalle': '-',
				'vmovi': float(data_facpago['vmpago'])
			}
		)

	ctimo = ctimo_billing('ctimo_cxc_billing', request.db)
	movi = movi_find(fac.cfac, request.db, ctimo.pk)
	if movi:
		if(medios_pagos_total < data_vttotal):
			movi_vttotal = (data_vttotal - medios_pagos_total)
		else:
			movi_vttotal = 0

		movi = save_movi(
			request.db,
			{
				'cfac': fac.cfac,
				'ctimo': ctimo,
				'vttotal': movi_vttotal,
				'citerce': citerce,
				'vefe': 0,
				'vtar': 0,
				'vch': 0,
				'vcred': 0,
				'ventre': 0,
				'vcambio': 0,
				'baseiva': 0,
				'vtiva': 0,
				'vtsuma': 0,
				'vtdescu': 0,
			}
		)

		movideta = save_movideta(
			request.db,
			{
				'docrefe': fac.cfac,
				'ctimo': ctimo.pk,
				'itmovi': 1,
				'detalle': '-',
				'vmovi': movi_vttotal
			}
		)

	for data_deta in data["mvdeta"]:
		carlos = Arlo.objects.using(request.db).get(pk = data_deta['carlos'])
		civa = Iva.objects.using(request.db).get(pk = data_deta['civa'])
		vt = float(data_deta['vunita']) * float(data_deta['canti'])
		#viva = vt * float(civa.poriva)
		exclude_arlo.append(carlos.pk)

		vtiva_vtbase = calcular_vtbase_vtiva_arlo(data_deta,request.db)

		fac_deta = save_fac_deta(
			request.db,
			{
				'cfac': fac,
				'itfac': data_deta['itfac'],
				'carlos': carlos,
				'nlargo': carlos.nlargo,
				'ncorto': carlos.ncorto,
				'canti': data_deta['canti'],
				'civa': civa,
				'niva': civa.niva,
				'poriva': civa.poriva,
				'pordes': data_deta['pordes'],
				'vunita': float(data_deta['vunita']),
				'viva': vtiva_vtbase["viva"],
				'vbase': vtiva_vtbase["vbase"],
				'vtotal': float(vt),
				'pvtafull': float(carlos.pvta1),
				'vcosto': float(carlos.vcosto1)
			}
		)

		mvsa_deta = save_mvsa_deta(
			request.db,
			{
				'cmvsa': mvsa,
				'it': data_deta['itfac'],
				'carlos': carlos,
				'nlargo': carlos.nlargo,
				'canti': data_deta['canti'],
				'vunita': float(data_deta['vunita']),
				'vtotal': float(vt)
			}
		)
		costing_and_stock(False, True, {"carlos": carlos.carlos}, request.db)

	fac_deta = Facdeta.objects.using(request.db).exclude(carlos__in = exclude_arlo)
	fac_deta.delete()
	mvsa_deta = Mvsadeta.objects.using(request.db).filter(cmvsa = mvsa.pk).exclude(carlos__in = exclude_arlo)
	mvsa_deta.delete()

	related_information = fac.get_related_information(request.db,True)
	response["related_information"] = related_information

	template = get_template("facturacion/partials/billing_documents.html")
	html = template.render({'mode_view':'edit','related_information_factura': fac.get_related_information(request.db,False) })
	response["html"] = html

	return HttpResponse(json.dumps(response), "application/json")

class BillCreate(CustomCreateView):
	model = Fac
	template_name = "facturacion/billing.html"
	form_class = FacForm

	def get_context_data(self,**kwargs):
		context = super(BillCreate, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)

		# Datos de Prueba
		#usuario = Usuario.objects.using(self.request.db).filter()[0]

		#talonario_MOS = usuario.ctalomos
		#talonario_POS = usuario.ctalopos
		# Datos de Prueba

		#medios_pago = [(serializers.serialize("json", [x],use_natural_foreign_keys=True, use_natural_primary_keys=True)) for x in MediosPago.objects.using(self.request.db).all()]
		medios_pago = MediosPago.objects.using(self.request.db).all()

		context['medios_pago'] = medios_pago

		context['title'] = "Facturas"
		context['form_movement_detail'] = FacdetaForm(self.request.db)
		context['form_medios_pagos'] = FacpagoForm(self.request.db)

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('save-bill')

		context['data_validation'] = manageParameters.to_dict()

		context['company_logo'] = manageParameters.get_param_value('company_logo')

		#context['data_validation']['top_discount_bills'] = manageParameters.get_param_value('top_discount_bills')
		#context['data_validation']['rounding_discounts'] = manageParameters.get_param_value('rounding_discounts')
		#context['data_validation']['top_sales_invoice'] = manageParameters.get_param_value('top_sales_invoice')
		#context['data_validation']['invoice_below_minimum_sales_price'] = manageParameters.get_param_value('invoice_below_minimum_sales_price')
		#context['data_validation']['maximum_amount_items_billing'] = manageParameters.get_param_value('maximum_amount_items_billing')
		#context['data_validation']['invoice_without_stock'] = manageParameters.get_param_value('invoice_without_stock')

		# Datos de Prueba
		context['data_validation']['maximum_number_items_billing'] = 10
		# Datos de Prueba

		context['data_validation']['formas_pago'] = {}
		context['data_validation']['formas_pago']['FORMA_PAGO_CONTADO'] = str(FORMA_PAGO_CONTADO)
		context['data_validation']['formas_pago']['FORMA_PAGO_CREDITO'] = str(FORMA_PAGO_CREDITO)

		context['data_validation']['medios_pago'] = {}
		context['data_validation']['medios_pago']['MEDIO_PAGO_EFECTIVO'] = str(MEDIO_PAGO_EFECTIVO)
		context['data_validation']['medios_pago']['DEFAULT_BANCO'] = str(DEFAULT_BANCO)

		context['is_fac_anulada'] = False

		context['data_validation_json'] = json.dumps(context['data_validation'])

		return context

class BillEdit(CustomUpdateView):
	model = Fac
	template_name = "facturacion/billing.html"
	form_class = FacForm

	def get_context_data(self,**kwargs):
		context = super(BillEdit, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)

		# Datos de Prueba
		#usuario = Usuario.objects.using(self.request.db).filter()[0]

		#talonario_MOS = usuario.ctalomos
		#talonario_POS = usuario.ctalopos
		# Datos de Prueba

		#medios_pago = [(serializers.serialize("json", [x],use_natural_foreign_keys=True, use_natural_primary_keys=True)) for x in MediosPago.objects.using(self.request.db).all()]
		medios_pago = MediosPago.objects.using(self.request.db).all()

		context['medios_pago'] = medios_pago

		context['title'] = "Facturar"
		context['form_movement_detail'] = FacdetaForm(self.request.db)
		context['form_medios_pagos'] = FacpagoForm(self.request.db)

		context['mode_view'] = 'edit'
		#context['url'] = reverse_lazy('save-bill')
		context['url'] = reverse_lazy('update-bill',kwargs={'pk': self.kwargs["pk"]},)

		context['data_validation'] = manageParameters.to_dict()

		context['company_logo'] = manageParameters.get_param_value('company_logo')

		#context['data_validation']['top_discount_bills'] = manageParameters.get_param_value('top_discount_bills')
		#context['data_validation']['rounding_discounts'] = manageParameters.get_param_value('rounding_discounts')
		#context['data_validation']['top_sales_invoice'] = manageParameters.get_param_value('top_sales_invoice')
		#context['data_validation']['invoice_below_minimum_sales_price'] = manageParameters.get_param_value('invoice_below_minimum_sales_price')
		#context['data_validation']['maximum_amount_items_billing'] = manageParameters.get_param_value('maximum_amount_items_billing')
		#context['data_validation']['invoice_without_stock'] = manageParameters.get_param_value('invoice_without_stock')

		# Datos de Prueba
		context['data_validation']['maximum_number_items_billing'] = 10
		# Datos de Prueba

		context['data_validation']['formas_pago'] = {}
		context['data_validation']['formas_pago']['FORMA_PAGO_CONTADO'] = str(FORMA_PAGO_CONTADO)
		context['data_validation']['formas_pago']['FORMA_PAGO_CREDITO'] = str(FORMA_PAGO_CREDITO)

		context['data_validation']['medios_pago'] = {}
		context['data_validation']['medios_pago']['MEDIO_PAGO_EFECTIVO'] = str(MEDIO_PAGO_EFECTIVO)
		context['data_validation']['medios_pago']['DEFAULT_BANCO'] = str(DEFAULT_BANCO)

		context['data_validation_json'] = json.dumps(context['data_validation'])

		factura = Fac.objects.using(self.request.db).get(pk=self.kwargs["pk"])
		related_information = factura.get_related_information(self.request.db,False)
		context['related_information_factura'] = related_information

		cesdo_anulado = Esdo.objects.using(self.request.db).get(cesdo=CESDO_ANULADO)

		context['is_fac_anulada'] =  True if factura.cesdo == cesdo_anulado else False

		context['facdeta_json'] = serializers.serialize("json", list(Facdeta.objects.using(self.request.db).filter(cfac=self.kwargs["pk"]).order_by('itfac')),use_natural_foreign_keys=True, use_natural_primary_keys=True)
		context['facpagos_json'] = serializers.serialize("json", list(Facpago.objects.using(self.request.db).filter(cfac=self.kwargs["pk"]).order_by('it')),use_natural_foreign_keys=True, use_natural_primary_keys=True)

		return context

def bill_proccess_view_annulment(request):
	form = CommonForm(request.db)
	return render(request,"facturacion/procesos/annulment.html",{"form":form})

@csrf_exempt
def bill_proccess_fn_annulment(request):
	manageParameters = ManageParameters(request.db)
	response = {"message":"Se realizo exitosamente el cambio"}
	data = json.loads(request.body)

	estado = Esdo.objects.using(request.db).get(pk=data["cesdo"])
	current_datetime = str(datetime.datetime.now())
	user = "Usuario Estatico"
	detaanula = data["detaanula"] + " " + current_datetime + " " + user

	try:
		factura = Fac.objects.using(request.db).get(cfac=data["cfac"])

		ctimo_rc_billing = manageParameters.get_param_value('ctimo_rc_billing')
		ctimo_cxc_billing = manageParameters.get_param_value('ctimo_cxc_billing')

		ctimos = list(Timo.objects.using(request.db).filter(Q(ctimo=ctimo_rc_billing) | Q(ctimo=ctimo_cxc_billing)))

		try:
			mvsa = Mvsa.objects.using(request.db).get(docrefe = factura.cfac)
		except Mvsa.DoesNotExist:
			response["message"] = "No existe un movimiento de salida asociado a la factura."
			return HttpResponse(json.dumps(response), content_type="application/json",status=400)

		try:
			movideta = Movideta.objects.using(request.db).filter(docrefe = factura.cfac)

			movis = list(set(map(lambda x: x.cmovi, movideta)))
			response["movimientos"] = []
			for t_movi in movis:
				#movimiento = Movi.objects.using(request.db).filter(cmovi = movideta.cmovi,ctimo__in = ctimos)[0]
				#movimiento = Movi.objects.using(request.db).filter(cmovi = movideta.cmovi,ctimo__in = ctimos)[0]

				movi = Movi.objects.using(request.db).get(pk=t_movi.pk)

				data_mov = {
					"esdo_last" : movi.cesdo.nesdo,
					'esdo_mew' :estado.nesdo,
					'vttotal' : str(movi.vttotal),
				}

				movi.cesdo = estado
				movi.detaanula = detaanula
				movi.save(using=request.db)


				data_mov["cmovi"] = movi.cmovi
				response["movimientos"].append(data_mov)

		except Movi.DoesNotExist:
			response["message"] = "No existe un movimiento asociado a la factura."
			return HttpResponse(json.dumps(response), content_type="application/json",status=400)

		response["factura"] = {
			"esdo_last" : factura.cesdo.nesdo,
			'esdo_mew' :estado.nesdo,
			'vttotal' : str(factura.vttotal),
		}

		response["mvsa"] = {
			"esdo_last" : mvsa.cesdo.nesdo,
			'esdo_mew' :estado.nesdo,
			'vttotal' : str(mvsa.vttotal),
		}

		factura.detaanula = detaanula
		factura.cesdo = estado
		mvsa.detaanula = detaanula
		mvsa.cesdo = estado

		factura.save(using=request.db)
		mvsa.save(using=request.db)

		response["factura"]["cfac"] = factura.cfac
		response["mvsa"]["cmvsa"] = mvsa.cmvsa

		return HttpResponse(json.dumps(response), content_type="application/json",status=200)
	except Fac.DoesNotExist:
		response["message"] = "La Factura no existe."
		return HttpResponse(json.dumps(response), content_type="application/json",status=400)

class BillPrint(PDFTemplateView):
	template_name = "facturacion/print_bill_format_half_letter.html"

	def get_context_data(self, **kwargs):
		context = super(BillPrint, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)
		data = self.request.GET

		# Datos de Prueba
		"""usuario = Usuario.objects.using(self.request.db).filter()[0]

		talonario_MOS = usuario.ctalomos
		talonario_POS = usuario.ctalopos"""
		# Datos de Prueba

		formato = data.get('formato')
		cfac = data.get('cfac')

		if formato or formato == "half_letter":
			self.template_name = "facturacion/print_bill_format_half_letter.html"
			#context['orientation'] = 'portrait'
			context['orientation'] = 'landscape'

		elif formato == "neckband":
			self.template_name = "facturacion/print_bill_format_half_letter.html"
			#context['orientation'] = 'portrait'
			context['orientation'] = 'landscape'

		else:
			self.template_name = "facturacion/print_bill_format_half_letter.html"
			#context['orientation'] = 'portrait'
			context['orientation'] = 'landscape'

		factura = Fac.objects.using(self.request.db).get(cfac=cfac)
		factura_deta = list(Facdeta.objects.using(self.request.db).filter(cfac=factura))

		max_items_factura = 10 - len(factura_deta)

		deta_vttotal = Facpago.objects.using(self.request.db).filter(cfac=factura)


		"""
		cont_vttotal = 0
		cred_vttotal = 0
		for dv in deta_vttotal:
			if(dv.cmpago.cmpago in [1000]):
				cont_vttotal += dv.vmpago
			else:
				cred_vttotal += dv.vmpago
		"""


		factura.abono = factura.vefe + factura.vtar + factura.vch + factura.vcred

		factura.saldo = factura.vttotal - factura.abono

		"""
		factura.cont_vttotal = cont_vttotal
		factura.cred_vttotal = cred_vttotal
		factura.saldo = factura.vttotal - cred_vttotal
		"""

		for index in range(0,max_items_factura):
			factura_deta.append(False)

		factura.vttotal_letter = number_to_letter(factura.vttotal)
		factura.text_bill = manageParameters.get_param_value('text_bill')
		factura.company_logo = static(manageParameters.get_param_value('company_logo'))

		context['factura'] = factura
		context['factura_deta'] = factura_deta
		"""context['usuario'] = usuario"""

		context['data'] = data
		context['title'] = 'Impresion de Facturas'
		return context

def report_view_bill_payment_methods(request):
	form = ReportVentaForm(request.db)
	form_common = CommonForm(request.db)
	return render(request,"facturacion/reportes/views/ventas_formas_pago.html",{"title":"Reporte de Ventas Por Formas de Pago","form":form,"form_common":form_common})

class report_fn_bill_payment_methods(PDFTemplateView):
	template_name = "facturacion/reportes/fn/ventas_formas_pago.html"

	def get_context_data(self, **kwargs):
		cesdo_anulado = Esdo.objects.using(self.request.db).get(cesdo=CESDO_ANULADO)

		context = super(report_fn_bill_payment_methods, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)
		data = self.request.GET

		cvende = data["cvende"]
		citerce = data["citerce"]
		ctifopa = data["ctifopa"]

		context['title'] = 'Reporte de Ventas Por Medios de Pagos y Rango de Fechas'
		cells = {
			"cvende":{"show":True},
			"citerce":{"show":True},
			"ctifopa":{"show":True},
		}
		context['header'] = {
			"Rango de Fechas" : data["fecha_inicial"] + " - " + data["fecha_final"]
		}


		query_facturas = {}
		"""
		query_facturas = {
			"cmven__fmven__gte" : data["start_date"].replace(hour=0, minute=0, second=0, microsecond=0)
			"cmven__fmven__lte" : data["end_date"].replace(hour=0, minute=0, second=0, microsecond=0)
		}
		"""
		if(ctifopa):
			query_facturas["ctifopa__ctifopa"] = ctifopa
			context['title'] += " Por Medios De Pagor"
			context['header']["Medio de Pago"] = Tifopa.objects.using(self.request.db).get(ctifopa=ctifopa).ntifopa
			cells["ctifopa"]["show"] = False
		if(cvende):
			query_facturas["cvende__cvende"] = cvende
			context['title'] += " Por Vendedor"
			context['header']["Vendedor"] = Vende.objects.using(self.request.db).get(cvende=cvende).nvende
			cells["cvende"]["show"] = False
		if(citerce):
			query_facturas["citerce__citerce"] = citerce
			context['title'] += " Por Cliente"
			context['header']["Cliente"] = Tercero.objects.using(self.request.db).get(citerce=citerce).rasocial
			cells["citerce"]["show"] = False

		totales = {}

		facturas = Fac.objects.using(self.request.db).filter(**query_facturas)

		totales["subtotal"] = 0
		totales["total"] = 0

		totales["fpago"] = {
			"efectivo":0,
			"tarjeta":0,
			"cheque":0,
			"nota_credito":0,
		}

		for factura in facturas:
			if factura.cesdo != cesdo_anulado:
				factura.data_report = {}
				totales["subtotal"] += factura.vttotal
				totales["total"] += factura.vttotal

				totales["fpago"]["efectivo"] += factura.vefe
				totales["fpago"]["tarjeta"] += factura.vtar
				totales["fpago"]["cheque"] += factura.vch
				totales["fpago"]["nota_credito"] += factura.vcred

		context['data'] = data
		context['facturas'] = facturas
		context['cells'] = cells
		context['totales'] = totales

		context['colspan_total'] = 5
		for k,v in cells.iteritems():
			if v["show"] == False:
				context['colspan_total'] -= 1

		return context

def report_view_bill(request):
	form = ReportVentaForm(request.db)
	form_common = CommonForm(request.db)
	return render(request,"facturacion/reportes/views/ventas.html",{"title":"Reporte de Ventas","form":form,"form_common":form_common})

class report_fn_bill(PDFTemplateView):
	template_name = "facturacion/reportes/fn/ventas.html"

	def get_context_data(self, **kwargs):

		cesdo_anulado = Esdo.objects.using(self.request.db).get(cesdo=CESDO_ANULADO)

		context = super(report_fn_bill, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)
		data = self.request.GET


		context['title'] = 'Reporte de Ventas Por Rango de Fechas'
		cells = {
			"cvende":{"show":True},
			"citerce":{"show":True}
		}
		context['header'] = {
			"Rango de Fechas" : data["fecha_inicial"] + " - " + data["fecha_final"],
		}
		cvende = data["cvende"]
		citerce = data["citerce"]

		query_facturas = {}
		"""
		query_facturas = {
			"cmven__fmven__gte" : data["start_date"].replace(hour=0, minute=0, second=0, microsecond=0)
			"cmven__fmven__lte" : data["end_date"].replace(hour=0, minute=0, second=0, microsecond=0)
		}
		"""
		if(cvende):
			query_facturas["cvende__cvende"] = cvende
			context['title'] += " Por Vendedor"
			context['header']["Vendedor"] = Vende.objects.using(self.request.db).get(cvende=cvende).nvende
			cells["cvende"]["show"] = False
		if(citerce):
			query_facturas["citerce__citerce"] = citerce
			context['title'] += " Por Cliente"
			context['header']["Cliente"] = Tercero.objects.using(self.request.db).get(citerce=citerce).rasocial
			cells["citerce"]["show"] = False

		totales = {}

		facturas = Fac.objects.using(self.request.db).filter(**query_facturas)

		totales["subtotal"] = 0
		totales["total"] = 0
		totales["vtt_otros"] = 0
		totales["vtt_base_iva"] = 0
		totales["vtt_iva"] = 0

		for factura in facturas:
			factura.data_report = {}
			totales["subtotal"] += factura.vttotal
			totales["total"] += factura.vttotal

			factura.data_report["otros_valores"] = factura.vflete
			factura.data_report["vt_base_iva"] = factura.vtbase
			factura.data_report["vt_iva"] = factura.vtiva

			if factura.cesdo != cesdo_anulado:
				totales["vtt_otros"] += factura.data_report["otros_valores"]
				totales["vtt_base_iva"] += factura.data_report["vt_base_iva"]
				totales["vtt_iva"] += factura.data_report["vt_iva"]

		context['data'] = data
		context['facturas'] = facturas
		context['cells'] = cells
		context['totales'] = totales


		context['colspan_total'] = 4
		for k,v in cells.iteritems():
			if v["show"] == False:
				context['colspan_total'] -= 1

		return context
