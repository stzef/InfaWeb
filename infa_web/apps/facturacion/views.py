from django.shortcuts import render,render_to_response
from django.views.generic import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from infa_web.parameters import ManageParameters

from infa_web.apps.base.value_letters import number_to_letter

from easy_pdf.views import PDFTemplateView

from infa_web.apps.movimientos.models import *
from infa_web.apps.facturacion.models import *
from infa_web.apps.terceros.models import *
from infa_web.apps.articulos.models import *
from infa_web.apps.facturacion.forms import *
from infa_web.apps.base.forms import *

manageParameters = ManageParameters()

class BillList(ListView):
	model = Fac
	template_name = "facturacion/list-billings.html"
	form_class = FacForm

	def get_context_data(self,**kwargs):
		context = super(BillList, self).get_context_data(**kwargs)
		context['title'] = "Listar Facturas"
		return context

def sum_function(value, prefix):
	value_sum = str(int(value[2:])+1)
	cant_space = 8-int(len(value_sum))
	return prefix+(cant_space*'0')+value_sum

@csrf_exempt
def BillSave(request):
	data = json.loads(request.body)
	response = {}
	fac_pk = ""
	vttotal = 0
	response["error"] = False
	response["message"] = "Factura Guardada con Exito"
	medios_pagos_total = 0
	vefe_t = 0
	vtar_t = 0
	vch_t = 0

	print (json.dumps(data,indent=4))
	#print json.dumps(data, indent=4)

	citerce = Tercero.objects.using(request.db).get(pk = data['citerce'])
	cesdo = Esdo.objects.using(request.db).get(pk = data['cesdo'])
	ctifopa = Tifopa.objects.using(request.db).get(pk = data['ctifopa'])
	ccaja = Caja.objects.using(request.db).get(pk = data['ccaja'])
	cvende = Vende.objects.using(request.db).get(pk = data['cvende'])
	cdomici = Domici.objects.using(request.db).get(pk = data['cdomici'])
	cemdor = Emdor.objects.using(request.db).get(pk = data['cemdor'])

	try:
		value = Fac.objects.using(request.db).all().latest('pk')
		fac_pk = sum_function(value.cfac, ccaja.ctimocj.prefijo)
	except Fac.DoesNotExist:
		fac_pk = ccaja.ctimocj.prefijo+'00001000'

	fac = Fac(
		cfac = fac_pk,
		femi = data['femi'],
		citerce = citerce,
		cesdo = cesdo,
		fpago = data['fpago'],
		ctifopa = ctifopa,
		descri = '-',
		vtbase = float(data['vtbase']),
		vtiva = float(data['vtiva']),
		vflete = float(data['vflete']),
		vdescu = float(data['vdescu']),
		vttotal = float(data['vttotal']),
		ventre = float(data['ventre']),
		vcambio = float(data['vcambio']),
		ccaja = ccaja,
		cvende = cvende,
		cdomici = cdomici,
		tpordes = 0,
		cemdor = cemdor,
		brtefte = float(data['brtefte']),
		prtefte = float(data['prtefte']),
		vrtefte = float(data['vrtefte'])
	)
	fac.save(using=request.db)

	mvsa = Mvsa(
		fmvsa = data['femi'],
		docrefe = fac.cfac,
		citerce = citerce,
		ctimo = ccaja.ctimocj,
		cesdo = cesdo,
		vttotal = float(data['vttotal']),
		descri = '-'
	)
	mvsa.save(using=request.db)

	for data_facpago in data["medios_pagos"]:
		mediopago = MediosPago.objects.using(request.db).get(pk = data_facpago['cmpago'])
		banmpago = Banfopa.objects.using(request.db).get(pk = data_facpago['banmpago'])
		medios_pagos_total += float(data_facpago['vmpago'])
		vefe_t += float(data_facpago['vmpago']) if mediopago.nmpago == 'Efectivo' else 0
		vtar_t += float(data_facpago['vmpago']) if mediopago.nmpago == 'Tarjeta' else 0
		vch_t += float(data_facpago['vmpago']) if mediopago.nmpago == 'Cheque' else 0
		fac_pago = Facpago(
			cfac = fac,
			it = data_facpago['it'],
			cmpago = mediopago,
			docmpago = data_facpago['docmpago'],
			banmpago = banmpago,
			vmpago = float(data_facpago['vmpago'])
		)
		fac_pago.save(using=request.db)

	value = float(data['vttotal'])
	ctimo = Timo.objects.using(request.db).get(pk = 3001)
	val_cont = 1
	while(val_cont != 0):

		try:
			mov = Movi.objects.using(request.db).all().latest('pk')
			movi_pk = sum_function(mov.cmovi, ccaja.ctimocj.prefijo)
		except Movi.DoesNotExist:
			movi_pk = ccaja.ctimocj.prefijo+'00001000'

		movi = Movi(
			cmovi = movi_pk,
			ctimo = ctimo,
			citerce = citerce,
			fmovi = data['femi'],
			descrimovi = '-',
			vttotal = medios_pagos_total,
			cesdo = cesdo,
			vefe = vefe_t,
			vtar = vtar_t,
			vch = vch_t,
			ventre = float(data['ventre']),
			vcambio = float(data['vcambio']),
			ccaja = ccaja,
			baseiva = float(data['vtbase']),
			vtiva = float(data['vtiva']),
			vtsuma = float(data['vttotal']),
			vtdescu = float(data['vdescu'])
		)
		movi.save(using=request.db)

		if not data["medios_pagos"]:
			movideta = Movideta(
				cmovi = movi,
				itmovi = 1,
				docrefe = fac.cfac,
				detalle = '-',
				vmovi = medios_pagos_total
			)
			movideta.save(using=request.db)
		else:
			for data_facpago in data["medios_pagos"]:
				mediopago = MediosPago.objects.using(request.db).get(pk = data_facpago['cmpago'])
				banmpago = Banfopa.objects.using(request.db).get(pk = data_facpago['banmpago'])
				movipago = Movipago(
					cmovi = movi,
					it = data_facpago['it'],
					cmpago = mediopago,
					docmpago = data_facpago['docmpago'],
					banmpago = banmpago,
					vmpago = float(data_facpago['vmpago'])
				)
				movipago.save(using=request.db)
				movideta = Movideta(
					cmovi = movi,
					itmovi = data_facpago['it'],
					docrefe = fac.cfac,
					detalle = '-',
					vmovi = float(data_facpago['vmpago'])
				)
				movideta.save(using=request.db)

		if(value > medios_pagos_total):
			ctimo = Timo.objects.using(request.db).get(pk = 4003)
			vefe_t = 0
			vtar_t = 0
			vch_t = 0
			data['ventre'] = 0
			data['vcambio'] = 0
			data['vtbase'] = 0
			data['vtiva'] = 0
			data['vttotal'] = 0
			data['vdescu'] = 0
			value -= medios_pagos_total
			medios_pagos_total = value
			data['medios_pagos'] = {}
		else:
			val_cont = 0

	for data_deta in data["mvdeta"]:
		carlos = Arlo.objects.using(request.db).get(pk = data_deta['carlos'])
		civa = Iva.objects.using(request.db).get(pk = data_deta['civa'])
		vt = float(data_deta['vunita']) * float(data_deta['canti'])
		viva = vt * float(civa.poriva)

		fac_deta = Facdeta(
			cfac = fac,
			itfac = data_deta['itfac'],
			carlos = carlos,
			nlargo = carlos.nlargo,
			ncorto = carlos.ncorto,
			canti = data_deta['canti'],
			civa = civa,
			niva = civa.niva,
			poriva = civa.poriva,
			pordes = data_deta['pordes'],
			vunita = float(data_deta['vunita']),
			viva = viva,
			vbase = vt,
			vtotal = float((vt + viva)),
			pvtafull = float(carlos.pvta1),
			vcosto = float(carlos.vcosto1)
		)

		mvsa_deta = Mvsadeta(
			cmvsa = mvsa,
			it = data_deta['itfac'],
			carlos = carlos,
			nlargo = carlos.nlargo,
			canti = data_deta['canti'],
			vunita =float(data_deta['vunita']),
			vtotal = float((vt + viva))
		)

		mvsa_deta.save(using=request.db)
		fac_deta.save(using=request.db)

	response["cfac"] = fac.cfac
	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def BillUpdate(request,pk):
	data = json.loads(request.body)
	response = {}
	fac_pk = ""
	vttotal = 0
	response["error"] = False
	response["message"] = "Factura Guardada con Exito"
	medios_pagos_total = 0
	vefe_t = 0
	vtar_t = 0
	vch_t = 0
	val_tot_mp = 0
	exclude_arlo = []

	print (json.dumps(data,indent=4))

	citerce = Tercero.objects.using(request.db).get(pk = data['citerce'])
	cesdo = Esdo.objects.using(request.db).get(pk = data['cesdo'])
	ctifopa = Tifopa.objects.using(request.db).get(pk = data['ctifopa'])
	ccaja = Caja.objects.using(request.db).get(pk = data['ccaja'])
	cvende = Vende.objects.using(request.db).get(pk = data['cvende'])
	cdomici = Domici.objects.using(request.db).get(pk = data['cdomici'])
	cemdor = Emdor.objects.using(request.db).get(pk = data['cemdor'])

	fac = Fac.objects.get(cfac = data['cfac'])
	fac.cesdo = cesdo
	fac.fpago = data['fpago']
	fac.ctifopa = ctifopa
	fac.vtbase = float(data['vtbase'])
	fac.vtiva = 0
	fac.vflete = float(data['vflete'])
	fac.vdescu = float(data['vdescu'])
	fac.vttotal = float(vttotal)
	fac.ventre = float(data['ventre'])
	fac.vcambio = float(data['vcambio'])
	fac.cvende = cvende
	fac.cdomici = cdomici
	fac.cemdor = cemdor
	fac.brtefte = float(data['brtefte'])
	fac.prtefte = float(data['prtefte'])
	fac.vrtefte = float(data['vrtefte'])
	fac.save(using=request.db)

	mvsa = Mvsa.objects.get(docrefe = fac.cfac)
	mvsa.vttotal = float(data['vttotal'])
	mvsa.save(using=request.db)

	movi_find = Movi.objects.filter(movideta__docrefe = fac.cfac)
	for data_facpago in data["medios_pagos"]:
		movi = movi_find.filter(ctimo__pk = 3001)
		mediopago = MediosPago.objects.using(request.db).get(pk = data_facpago['cmpago'])
		banmpago = Banfopa.objects.using(request.db).get(pk = data_facpago['banmpago'])
		medios_pagos_total += float(data_facpago['vmpago'])
		vefe_t += float(data_facpago['vmpago']) if mediopago.nmpago == 'Efectivo' else 0
		vtar_t += float(data_facpago['vmpago']) if mediopago.nmpago == 'Tarjeta' else 0
		vch_t += float(data_facpago['vmpago']) if mediopago.nmpago == 'Cheque' else 0

		try:
			fac_pago = Facpago.objects.get(cfac = fac.pk, it = data_facpago['it'])
			fac_pago.cmpago = mediopago
			fac_pago.docmpago = data_facpago['docmpago']
			fac_pago.banmpago = banmpago
			fac_pago.vmpago = float(data_facpago['vmpago'])
		except Facpago.DoesNotExist:
			fac_pago = Facpago(
				cfac = fac,
				it = data_facpago['it'],
				cmpago = mediopago,
				docmpago = data_facpago['docmpago'],
				banmpago = banmpago,
				vmpago = float(data_facpago['vmpago'])
			)

		try:
			movideta = movi[0].movideta_set.get(itmovi = data_facpago['it'])
			movideta.vmovi = float(data_facpago['vmpago'])
		except Movideta.DoesNotExist:
			movideta = Movideta(
				cmovi = movi[0],
				itmovi = data_facpago['it'],
				docrefe = fac.cfac,
				detalle = '-',
				vmovi = float(data_facpago['vmpago'])
			)
		fac_pago.save(using=request.db)
		movideta.save(using=request.db)

	movi = movi[0]
	movi.vttotal = (vefe_t + vtar_t + vch_t)
	movi.cesdo = cesdo
	movi.vefe = vefe_t
	movi.vtar = vtar_t
	movi.vch = vch_t
	movi.ventre = float(data['ventre'])
	movi.vcambio = float(data['vcambio'])
	movi.baseiva = float(data['vtbase'])
	movi.vtiva = float(data['vtiva'])
	movi.vtsuma = float(data['vttotal'])
	movi.vtdescu = float(data['vdescu'])
	movi.save(using=request.db)

	movi = movi_find.filter(ctimo__pk = 4003)
	movideta = movi[0].movideta_set.get(itmovi = 1)
	if(val_tot_mp < float(data['vttotal'])):
		movideta.vmovi = (float(data['vttotal']) - val_tot_mp)
		movi_vttotal = (float(data['vttotal']) - val_tot_mp)
	else:
		movideta.vmovi = 0
		movi_vttotal = 0
	movideta.save(using=request.db)

	movi = movi[0]
	movi.vttotal = movi_vttotal
	movi.save(using=request.db)

	for data_deta in data["mvdeta"]:
		carlos = Arlo.objects.using(request.db).get(pk = data_deta['carlos'])
		civa = Iva.objects.using(request.db).get(pk = data_deta['civa'])
		vt = float(data_deta['vunita']) * float(data_deta['canti'])
		viva = vt * float(civa.poriva)
		exclude_arlo.append(carlos.pk)

		try:
			fac_deta = Facdeta.objects.get(cfac = fac.pk,  carlos = carlos.pk)
			fac_deta.itfac = data_deta['itfac']
			fac_deta.nlargo = carlos.nlargo
			fac_deta.ncorto = carlos.ncorto
			fac_deta.canti = data_deta['canti']
			fac_deta.civa = civa
			fac_deta.niva = civa.niva
			fac_deta.poriva = civa.poriva
			fac_deta.pordes = data_deta['pordes']
			fac_deta.vunita = float(data_deta['vunita'])
			fac_deta.viva = viva
			fac_deta.vbase = vt
			fac_deta.vtotal = float((vt + viva))
			fac_deta.pvtafull = float(carlos.pvta1)
			fac_deta.vcosto = float(carlos.vcosto1)
		except Facdeta.DoesNotExist:
			fac_deta = Facdeta(
				cfac = fac,
				itfac = data_deta['itfac'],
				carlos = carlos,
				nlargo = carlos.nlargo,
				ncorto = carlos.ncorto,
				canti = data_deta['canti'],
				civa = civa,
				niva = civa.niva,
				poriva = civa.poriva,
				pordes = data_deta['pordes'],
				vunita = float(data_deta['vunita']),
				viva = viva,
				vbase = vt,
				vtotal = float((vt + viva)),
				pvtafull = float(carlos.pvta1),
				vcosto = float(carlos.vcosto1)
			)
		try:
			mvsa_deta = Mvsadeta.objects.get(cmvsa = mvsa.pk, carlos = carlos.pk)
			mvsa_deta.it = data_deta['itfac']
			mvsa_deta.carlos = carlos
			mvsa_deta.nlargo = carlos.nlargo
			mvsa_deta.canti = data_deta['canti']
			mvsa_deta.vunita =float(data_deta['vunita'])
			mvsa_deta.vtotal = float((vt + viva))
		except Mvsadeta.DoesNotExist:
			mvsa_deta = Mvsadeta(
				cmvsa = mvsa,
				it = data_deta['itfac'],
				carlos = carlos,
				nlargo = carlos.nlargo,
				canti = data_deta['canti'],
				vunita =float(data_deta['vunita']),
				vtotal = float((vt + viva))
			)
		fac_deta.save(using=request.db)
		mvsa_deta.save(using=request.db)
	Facdeta.objects.exclude(carlos__in = exclude_arlo).delete()
	Mvsadeta.objects.filter(cmvsa = mvsa.pk).exclude(carlos__in = exclude_arlo).delete()
	return HttpResponse(json.dumps(response), "application/json")

class BillCreate(CreateView):
	model = Fac
	template_name = "facturacion/billing.html"
	form_class = FacForm

	def get_context_data(self,**kwargs):
		context = super(BillCreate, self).get_context_data(**kwargs)

		# Datos de Prueba
		#usuario = Usuario.objects.using(self.request.db).filter()[0]

		#talonario_MOS = usuario.ctalomos
		#talonario_POS = usuario.ctalopos
		# Datos de Prueba

		#medios_pago = [(serializers.serialize("json", [x],use_natural_foreign_keys=True, use_natural_primary_keys=True)) for x in MediosPago.objects.using(self.request.db).all()]
		medios_pago = MediosPago.objects.using(self.request.db).all()

		context['medios_pago'] = medios_pago

		context['title'] = "Facturar"
		context['form_movement_detail'] = FacdetaForm()
		context['form_medios_pagos'] = FacpagoForm

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('save-bill')

		context['data_validation'] = {}

		context['company_logo'] = manageParameters.get_param_value('company_logo')

		context['data_validation']['top_discount_bills'] = manageParameters.get_param_value('top_discount_bills')
		context['data_validation']['rounding_discounts'] = manageParameters.get_param_value('rounding_discounts')
		context['data_validation']['top_sales_invoice'] = manageParameters.get_param_value('top_sales_invoice')
		context['data_validation']['invoice_below_minimum_sales_price'] = manageParameters.get_param_value('invoice_below_minimum_sales_price')
		context['data_validation']['maximum_amount_items_billing'] = manageParameters.get_param_value('maximum_amount_items_billing')

		# Datos de Prueba
		context['data_validation']['maximum_number_items_billing'] = 2
		# Datos de Prueba

		context['data_validation']['formas_pago'] = {}
		context['data_validation']['formas_pago']['FORMA_PAGO_CONTADO'] = str(FORMA_PAGO_CONTADO)
		context['data_validation']['formas_pago']['FORMA_PAGO_CREDITO'] = str(FORMA_PAGO_CREDITO)

		context['data_validation']['medios_pago'] = {}
		context['data_validation']['medios_pago']['MEDIO_PAGO_EFECTIVO'] = str(MEDIO_PAGO_EFECTIVO)
		context['data_validation']['medios_pago']['DEFAULT_BANCO'] = str(DEFAULT_BANCO)

		context['data_validation_json'] = json.dumps(context['data_validation'])

		return context

class BillEdit(UpdateView):
	model = Fac
	template_name = "facturacion/billing.html"
	form_class = FacForm

	def get_context_data(self,**kwargs):
		context = super(BillEdit, self).get_context_data(**kwargs)

		#medios_pago = [(serializers.serialize("json", [x],use_natural_foreign_keys=True, use_natural_primary_keys=True)) for x in MediosPago.objects.using(self.request.db).all()]
		medios_pago = MediosPago.objects.using(self.request.db).all()
		context['medios_pago'] = medios_pago

		context['title'] = "Facturar"
		context['form_movement_detail'] = FacdetaForm()
		context['form_medios_pagos'] = FacpagoForm

		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('update-bill',kwargs={'pk': self.kwargs["pk"]},)

		context['data_validation'] = {}

		context['company_logo'] = manageParameters.get_param_value('company_logo')

		context['data_validation']['top_discount_bills'] = manageParameters.get_param_value('top_discount_bills')
		context['data_validation']['rounding_discounts'] = manageParameters.get_param_value('rounding_discounts')
		context['data_validation']['top_sales_invoice'] = manageParameters.get_param_value('top_sales_invoice')
		context['data_validation']['invoice_below_minimum_sales_price'] = manageParameters.get_param_value('invoice_below_minimum_sales_price')
		context['data_validation']['maximum_amount_items_billing'] = manageParameters.get_param_value('maximum_amount_items_billing')

		context['data_validation']['formas_pago'] = {}
		context['data_validation']['formas_pago']['FORMA_PAGO_CONTADO'] = str(FORMA_PAGO_CONTADO)
		context['data_validation']['formas_pago']['FORMA_PAGO_CREDITO'] = str(FORMA_PAGO_CREDITO)

		context['data_validation']['medios_pago'] = {}
		context['data_validation']['medios_pago']['MEDIO_PAGO_EFECTIVO'] = str(MEDIO_PAGO_EFECTIVO)
		context['data_validation']['medios_pago']['DEFAULT_BANCO'] = str(DEFAULT_BANCO)

		context['data_validation_json'] = json.dumps(context['data_validation'])

		return context

def bill_proccess_view_annulment(request):
	form = CommonForm()
	return render(request,"facturacion/procesos/annulment.html",{"form":form})

@csrf_exempt
def bill_proccess_fn_annulment(request):
	data = json.loads(request.body)

	estado = Esdo.objects.using(request.db).get(pk=data["cesdo"])
	current_datetime = str(datetime.datetime.now())
	user = "Usuario Estatico"
	detaanula = data["detaanula"] + " " + current_datetime + " " + user

	factura = Fac.objects.using(request.db).get(pk=data["fact"])
	mvsa = Mvsa.objects.using(request.db).get(docrefe = factura.cfac)

	ctimo_rc_billing = manageParameters.get_param_value('ctimo_rc_billing')
	ctimo_cxc_billing = manageParameters.get_param_value('ctimo_cxc_billing')

	ctimos = Timo.objects.using(request.db).get(
		Q(ctimo=ctimo_rc_billing) | Q(ctimo=ctimo_cxc_billing)
	)
	
	movideta = Movideta.objects.using(request.db).get(docrefe = factura.cfac)
	movimiento = Movi.objects.using(request.db).get(cmovi = movideta.cmovi.cmovi,ctimo__in = ctimos)

	print "---------------------------------"
	print factura
	print "---------------------------------"
	print mvsa
	print "---------------------------------"
	print movimiento
	print "---------------------------------"

	movimiento.cesdo = estado
	movimiento.detaanula = detaanula


	factura.detaanula = detaanula
	factura.cesdo = estado

	mvsa.detaanula = detaanula
	mvsa.cesdo = estado


	factura.save(using=request.db)
	mvsa.save(using=request.db)
	movimiento.save(using=request.db)

	return HttpResponse(json.dumps({"message":"Se realizo exitosamente el cambio"}), content_type="application/json",status=200)

class BillPrint(PDFTemplateView):
	template_name = "facturacion/print_bill_format_half_letter.html"

	def get_context_data(self, **kwargs):
		context = super(BillPrint, self).get_context_data(**kwargs)
		data = self.request.GET

		# Datos de Prueba
		usuario = Usuario.objects.using(self.request.db).filter()[0]

		talonario_MOS = usuario.ctalomos
		talonario_POS = usuario.ctalopos
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

		#print deta_vttotal # .vmpago

		"""
		cont_vttotal = 0
		cred_vttotal = 0
		for dv in deta_vttotal:
			if(dv.cmpago.cmpago in [1000]):
				cont_vttotal += dv.vmpago
			else:
				cred_vttotal += dv.vmpago
		"""


		v = 0
		for dv in deta_vttotal:
			v += dv.vmpago
		factura.saldo = factura.vttotal - v
		factura.abono = v

		"""
		factura.cont_vttotal = cont_vttotal
		factura.cred_vttotal = cred_vttotal
		factura.saldo = factura.vttotal - cred_vttotal
		"""

		for index in range(0,max_items_factura):
			factura_deta.append(False)

		factura.vttotal_letter = number_to_letter(factura.vttotal)
		factura.text_bill = manageParameters.get_param_value('text_bill')

		context['factura'] = factura
		context['factura_deta'] = factura_deta
		context['usuario'] = usuario

		context['data'] = data
		context['title'] = 'Impresion de Facturas'
		return context
