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


from infa_web.apps.movimientos.models import *
from infa_web.apps.facturacion.models import *
from infa_web.apps.terceros.models import *
from infa_web.apps.articulos.models import *
from infa_web.apps.facturacion.forms import *
from infa_web.apps.base.forms import *

manageParameters = ManageParameters()

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

		context['title'] = "Facturar"
		context['form_movement_detail'] = FacdetaForm()
		context['form_medios_pagos'] = FacpagoForm

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('save-bill')

		context['data_validation'] = {}
		context['data_validation']['top_discount_bills'] = manageParameters.get_param_value('top_discount_bills')
		context['data_validation']['rounding_discounts'] = manageParameters.get_param_value('rounding_discounts')
		context['data_validation']['top_sales_invoice'] = manageParameters.get_param_value('top_sales_invoice')
		context['data_validation']['invoice_below_minimum_sales_price'] = manageParameters.get_param_value('invoice_below_minimum_sales_price')
		context['data_validation_json'] = json.dumps(context['data_validation'])

		return context

def bill_proccess_view_annulment(request):
	form = CommonForm()
	return render(request,"facturacion/procesos/annulment.html",{"form":form})

def bill_proccess_fn_annulment(request):
	data = json.loads(request.body)

	return HttpResponse(json.dumps({"message":"Se realizo exitosamente el cambio"}), content_type="application/json",status=200)
