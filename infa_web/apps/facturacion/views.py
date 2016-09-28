from django.shortcuts import render,render_to_response 
from django.views.generic import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy 
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
import json
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

	print (json.dumps(data,indent=4))
	#print json.dumps(data, indent=4)

	citerce = Tercero.objects.get(pk = data['citerce'])
	cesdo = Esdo.objects.get(pk = data['cesdo'])
	ctifopa = Tifopa.objects.get(pk = data['ctifopa'])
	ccaja = Caja.objects.get(pk = data['ccaja'])
	cvende = Vende.objects.get(pk = data['cvende'])
	cdomici = Domici.objects.get(pk = data['cdomici'])
	cemdor = Emdor.objects.get(pk = data['cemdor'])
	
	try:
		value = Fac.objects.all().latest('pk')
		fac_pk = sum_function(value.cfac, ccaja.ctimocj.prefijo)
	except Fac.DoesNotExist:
		fac_pk = ccaja.ctimocj.prefijo+'00001000'

	vttotal = [vttotal + (x['canti'] * x['vunita']) for x in data["mvdeta"]]

	fac = Fac(
			cfac = fac_pk, 
			femi = data['femi'], 
			citerce = citerce, 
			cesdo = cesdo, 
			fpago = data['fpago'], 
			ctifopa = ctifopa,
			descri = data['descri'],
			vtbase = float(data['vtbase']),
			vtiva = float(data['vtiva']),
			vflete = float(data['vflete']),
			vdescu = float(data['vdescu']),
			vttotal = float(vttotal[0]),
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
	fac.save()

	mvsa = Mvsa(
			fmvsa = data['femi'],
			docrefe = fac.cfac,
			citerce = citerce,
			ctimo = ccaja.ctimocj,
			cesdo = cesdo,
			vttotal = float(vttotal[0]),
			descri = '-'
		)
	mvsa.save()

	for data_facpago in data["medios_pagos"]:
		mediopago = MediosPago.objects.get(pk = data_facpago['cmpago'])
		banmpago = Banfopa.objects.get(pk = data_facpago['banmpago'])
		fac_pago = Facpago(
				cfac = fac,
				it = data_facpago['it'],
				cmpago = mediopago,
				docmpago = data_facpago['docmpago'],
				banmpago = banmpago,
				vmpago = float(data_facpago['vmpago'])
			)
	
	for data_deta in data["mvdeta"]:
		carlos = Arlo.objects.get(pk = data_deta['carlos'])
		civa = Iva.objects.get(pk = data_deta['civa'])
		vt = data_deta['vunita'] * data_deta['canti']
		viva = vt * civa.poriva

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
				vunita =float( data_deta['vunita']),
				vtotal = float((vt + viva))
			)

		mvsa_deta.save()
		fac_deta.save()

	try:
		value = Movi.objects.all().latest('pk')
		movi_pk = sum_function(value.cmovi, ccaja.ctimocj.prefijo)
	except Movi.DoesNotExist:
		movi_pk = ccaja.ctimocj.prefijo+'00001000'

	"""
	movi = Movi(
			cmovi = movi_pk,
			ctimo = ccaja.ctimocj,
			citerce = citerce,
			fmovi = data['femi'],
			descrimovi = '-',
			vttotal = float(vttotal),
			cesdo = cesdo,
		)
	"""

	#Crear Movi
	#Crear Movideta
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

	print (json.dumps(data,indent=4))
	#print json.dumps(data, indent=4)

	citerce = Tercero.objects.get(pk = data['citerce'])
	cesdo = Esdo.objects.get(pk = data['cesdo'])
	ctifopa = Tifopa.objects.get(pk = data['ctifopa'])
	ccaja = Caja.objects.get(pk = data['ccaja'])
	cvende = Vende.objects.get(pk = data['cvende'])
	cdomici = Domici.objects.get(pk = data['cdomici'])
	cemdor = Emdor.objects.get(pk = data['cemdor'])
	
	try:
		value = Fac.objects.all().latest('pk')
		fac_pk = sum_function(value.cfac, ccaja.ctimocj.prefijo)
	except Fac.DoesNotExist:
		fac_pk = ccaja.ctimocj.prefijo+'00001000'

	vttotal = [vttotal + (x['canti'] * x['vunita']) for x in data["mvdeta"]]

	fac = Fac(
			cfac = fac_pk, 
			femi = data['femi'], 
			citerce = citerce, 
			cesdo = cesdo, 
			fpago = data['fpago'], 
			ctifopa = ctifopa,
			descri = '-',
			vtbase = float(data['vtbase']),
			vtiva = 0,
			vflete = float(data['vflete']),
			vdescu = float(data['vdescu']),
			vttotal = float(vttotal),
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
	fac.save()

	mvsa = Mvsa(
			fmvsa = data['femi'],
			docrefe = fac.cfac,
			citerce = citerce,
			ctimo = ccaja.ctimocj,
			cesdo = cesdo,
			vttotal = float(vttotal),
			descri = '-'
		)
	mvsa.save()

	for data_facpago in data["medios_pagos"]:
		mediopago = MediosPago.objects.get(pk = data_facpago['cmpago'])
		banmpago = Banfopa.objects.get(pk = data_facpago['banmpago'])
		fac_pago = Facpago(
				cfac = fac,
				it = data_facpago['it'],
				cmpago = mediopago,
				docmpago = data_facpago['docmpago'],
				banmpago = banmpago,
				vmpago = float(data_facpago['vmpago'])
			)
	
	for data_deta in data["mvdeta"]:
		carlos = Arlo.objects.get(pk = data_deta['carlos'])
		civa = Iva.objects.get(pk = data_deta['civa'])
		vt = data_deta['vunita'] * data_deta['canti']
		viva = vt * civa.poriva

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
				vunita =float( data_deta['vunita']),
				vtotal = float((vt + viva))
			)

		mvsa_deta.save()
		fac_deta.save()

	try:
		value = Movi.objects.all().latest('pk')
		movi_pk = sum_function(value.cmovi, ccaja.ctimocj.prefijo)
	except Movi.DoesNotExist:
		movi_pk = ccaja.ctimocj.prefijo+'00001000'

	"""
	movi = Movi(
			cmovi = movi_pk,
			ctimo = ccaja.ctimocj,
			citerce = citerce,
			fmovi = data['femi'],
			descrimovi = '-',
			vttotal = float(vttotal),
			cesdo = cesdo,
		)
	"""

	#Crear Movi
	#Crear Movideta

	return HttpResponse(json.dumps(response), "application/json")

class BillCreate(CreateView):
	model = Fac
	template_name = "facturacion/billing.html"
	form_class = FacForm

	def get_context_data(self,**kwargs):
		context = super(BillCreate, self).get_context_data(**kwargs)

		# Datos de Prueba
		usuario = Usuario.objects.filter()[0]

		talonario_MOS = usuario.ctalomos
		talonario_POS = usuario.ctalopos
		# Datos de Prueba

		#medios_pago = [(serializers.serialize("json", [x],use_natural_foreign_keys=True, use_natural_primary_keys=True)) for x in MediosPago.objects.all()]
		medios_pago = MediosPago.objects.all()
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

		#medios_pago = [(serializers.serialize("json", [x],use_natural_foreign_keys=True, use_natural_primary_keys=True)) for x in MediosPago.objects.all()]
		medios_pago = MediosPago.objects.all()
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

def bill_proccess_fn_annulment(request):
	data = json.loads(request.body)

	current_datetime = str(datetime.datetime.now())
	user = "Usuario Estatico"

	factura = Fac.objects.get(pk=data["fact"])
	mvsa = Mvsa.objects.get(docrefe = factura.cfac)
	movimientos = Movi.objects.filter()

	for movimiento in movimientos:
		movimiento.detaanula = detaanula
		movimiento.cesdo = estado
		movimiento.save()

	detaanula = data["detaanula"] + " " + current_datetime + " " + user
	estado = Esdo.objects.get(pk=data["cesdo"])

	factura.detaanula = detaanula
	factura.cesdo = estado

	mvsa.detaanula = detaanula
	mvsa.cesdo = estado


	factura.save()
	mvsa.save()

	return HttpResponse(json.dumps({"message":"Se realizo exitosamente el cambio"}), content_type="application/json",status=200)

class BillPrint(PDFTemplateView):
	template_name = "facturacion/print_bill_format_half_letter.html"

	def get_context_data(self, **kwargs):
		context = super(BillPrint, self).get_context_data(**kwargs)
		data = self.request.GET

		# Datos de Prueba
		usuario = Usuario.objects.filter()[0]

		talonario_MOS = usuario.ctalomos
		talonario_POS = usuario.ctalopos
		# Datos de Prueba

		formato = data.get('formato')
		cfac = data.get('cfac')

		if formato or formato == "half_letter":
			self.template_name = "facturacion/print_bill_format_half_letter.html"
			context['orientation'] = 'letter'

		elif formato == "neckband":
			self.template_name = "facturacion/print_bill_format_half_letter.html"
			context['orientation'] = 'letter'

		else:
			self.template_name = "facturacion/print_bill_format_half_letter.html"
			context['orientation'] = 'letter'

		factura = Fac.objects.get(cfac=cfac)
		factura_deta = list(Facdeta.objects.filter(cfac=factura))

		max_items_factura = 10 - len(factura_deta)

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

