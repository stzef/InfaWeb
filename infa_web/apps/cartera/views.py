# -*- coding: utf-8 -*-
from django.shortcuts import render

from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView
from infa_web.apps.base.constantes import *
from infa_web.parameters import ManageParameters
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse_lazy


from easy_pdf.views import PDFTemplateView
from infa_web.apps.movimientos.models import *
from infa_web.apps.usuarios.models import *
from infa_web.apps.movimientos.forms import *
from infa_web.apps.facturacion.bills_fn import *
from infa_web.apps.facturacion.views import value_tot,code_generate
from infa_web.apps.base.utils import *
from django.core import serializers

def save_movi(data_array,request):
	request_db = request.db
	movi = get_or_none(Movi, request_db, cmovi=data_array['cmovi'])

	# sumatoria para cada forma de pago
	data_array['vefe'] = float(value_tot(data_array["mpagos"], 1000))
	data_array['vtar'] = float(value_tot(data_array["mpagos"], 1001))
	data_array['vch'] = float(value_tot(data_array["mpagos"], 1002))
	data_array['vcred'] = float(value_tot(data_array["mpagos"], 1003))

	usuario_actual = Usuario.objects.using(request_db).get(user=request.user)

	#ccaja = Cakja.objects.using(request_db).get(ccaja = data_array['ccaja'])
	caja = usuario_actual.ccaja

	data_array["vttotal"] = data_array['vefe']+data_array['vtar']+data_array['vch']+data_array['vcred']

	data_code = code_generate(Movi, caja.ctimocj.prefijo,'cmovi',1000,None, request_db)
	data_array['cmovi'] = data_code["model_pk"]

	#vtbase_vtiva = calcular_vtbase_vtiva(data_array["deta"],request_db)
	#data_array["baseiva"] = vtbase_vtiva["vtbase"]
	data_array["baseiva"] = data_array["vttotal"]
	#data_array["vtiva"] = vtbase_vtiva['vtiva']
	data_array["vtiva"] = 0
	data_array["vtsuma"] = data_array["vttotal"]

	timo = Timo.objects.using(request_db).get(ctimo = data_array["ctimo"])
	tercero = Tercero.objects.using(request_db).get(citerce = data_array['citerce'])
	estado = Esdo.objects.using(request_db).get(cesdo = data_array['cesdo'])

	data_array["vcambio"] = float(calcular_valor_cambio(data_array["ventre"],data_array["vttotal"]))
	if movi:
		movi = movi
		movi.citerce = tercero
		movi.vttotal = data_array["vttotal"]
		movi.vefe = data_array['vefe']
		movi.vtar = data_array['vtar']
		movi.vch = data_array['vch']
		movi.vcred = data_array['vcred']
		movi.ventre = data_array['ventre']
		movi.vcambio = data_array["vcambio"]
		movi.baseiva = data_array["baseiva"]
		movi.vtiva = data_array["vtiva"]
		movi.vtsuma = data_array['vtsuma']
		movi.vtdescu = data_array['vtdescu']
	else:
		movi = Movi(
			cmovi = data_array['cmovi'],
			ctimo = timo,
			citerce = tercero,
			fmovi = data_array['fmovi'],
			descrimovi = data_array['descrimovi'],
			vttotal = data_array["vttotal"],
			cesdo = estado,
			vefe = data_array['vefe'],
			vtar = data_array['vtar'],
			vch = data_array['vch'],
			vcred = data_array['vcred'],
			ventre = float(data_array['ventre']),
			vcambio = data_array["vcambio"],
			ccaja = caja,
			baseiva = float(data_array["baseiva"]),
			vtiva = float(data_array["vtiva"]),
			vtsuma = float(data_array['vtsuma']),
			vtdescu = float(data_array['vtdescu'])
		)
	movi.save(using = request_db)
	return movi

def save_movi_deta(movi,data_array_deta,request_db):
	Movideta.objects.using(request_db).filter(cmovi = movi.cmovi).delete()
	array = []
	it = 1
	for movideta_array in data_array_deta:
		movideta = Movideta(
			cmovi = movi,
			#itmovi = movideta_array['itmovi'],
			itmovi = it,
			docrefe = movideta_array['docrefe'],
			detalle = movideta_array['detalle'],
			vmovi = movideta_array['vmovi']
		)
		movideta.save(using = request_db)
		array.append(movideta)
		it += 1
	return array

def save_movi_pago(movi,data_array_mpagos,request_db):
	Movipago.objects.using(request_db).filter(cmovi = movi.cmovi).delete()
	array = []
	it = 1
	for data_medio_pago in data_array_mpagos:
		cmpago = MediosPago.objects.using(request_db).get(cmpago=data_medio_pago['cmpago'])
		banmpago = Banfopa.objects.using(request_db).get(cbanfopa=data_medio_pago['banmpago'])
		movi_pago = Movipago(
			cmovi = movi,
			#it = data_medio_pago['it'],
			it = it,
			cmpago = cmpago,
			docmpago = data_medio_pago['docmpago'],
			banmpago = banmpago,
			vmpago = data_medio_pago['vmpago']
		)
		movi_pago.save(using=request_db)
		array.append(movi_pago)
		it += 1
	return array

class PaymentCreate(CustomCreateView):
	model = Movi
	template_name = "cartera/payment.html"
	form_class = MoviForm

	def get_context_data(self,**kwargs):
		context = super(PaymentCreate, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)
		context['form_movideta'] = MoviDetailForm(self.request.db)
		context['form_medios_pagos'] = MovipagoForm(self.request.db)

		context['mode_view'] = 'create'
		context['title'] = 'Creacion de Abono'
		context['url'] = reverse_lazy('save-payment')
		return context

class PaymentEdit(CustomUpdateView):
	model = Movi
	template_name = "cartera/payment.html"
	form_class = MoviForm

	def get_context_data(self,**kwargs):
		context = super(PaymentCreate, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)
		context['form_movideta'] = MoviDetailForm(self.request.db)
		context['form_medios_pagos'] = MovipagoForm(self.request.db)

		context['title'] = 'Edición de Abono'
		context['mode_view'] = 'edit'
		context['url'] = reverse_lazy('update-payment',kwargs={'pk': self.kwargs["pk"]},)
		return context

@csrf_exempt
def PaymentSave(request):
	data = json.loads(request.body)
	response = {}

	movi = save_movi(data,request)

	save_movi_deta(movi, data["deta"], request.db)
	save_movi_pago(movi, data["mpagos"], request.db)

	response = movi.get_related_information(request.db,True)

	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def PaymentUpdate(request):
	data = json.loads(request.body)

	movi = save_movi(data,request)

	save_movi_deta(movi, data["deta"], request.db)
	save_movi_pago(movi, data["mpagos"], request.db)

	response = movi.get_related_information(request.db,True)
	return HttpResponse(json.dumps(response), "application/json")

def get_cartera_tercero(request,citerce):
	tercero = Tercero.objects.using(request.db).get(citerce = citerce)

	manageParameters = ManageParameters(request.db)
	ctimo = manageParameters.get_param_value("ctimo_cxc_billing")

	#cartera = Movi.objects.using(request.db).filter(ctimo = ctimo, cesdo = cesdo,citerce = self.citerce,vttotal__gt=0)
	cartera = Movi.objects.using(request.db).filter(ctimo = ctimo,citerce = citerce,vttotal__gt=0)
	vttotal = 0
	for movi in cartera:
		movi.vttotal
		vttotal += movi.vttotal
	response = {
		"cartera" : serializers.serialize('json', cartera),
		"vttotal" : str(vttotal)
	}
	return HttpResponse(json.dumps(response), "application/json")
