from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from django.contrib.staticfiles.templatetags.staticfiles import static
from infa_web.parameters import ManageParameters

import json
import datetime
from infa_web.apps.restaurante_menus.models import *
from infa_web.apps.restaurante_comandas.models import *
from infa_web.apps.restaurante_comandas.forms import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


from infa_web.apps.base.utils import get_current_user
from django.db.models import Max

from django.contrib.auth.models import User
from infa_web.apps.usuarios.models import Usuario

# pedido actual
# pedido anterior -> listar las comandas

def OrdersList(request):
	context = {}
	return render(request, "ordenes/list-orders.html", context)


def GetCommandsOrder(request, cmesa):
	comandas = Coda.objects.using(request.db).filter(cmesa=cmesa)

	return comandas

def generar_ccoda(talocoda,request_db):
	maxCcoda = Coda.objects.using(request_db).filter(ctalocoda=talocoda).aggregate(Max('ccoda'))
	if maxCcoda["ccoda__max"]:
		ccoda = maxCcoda["ccoda__max"] + 1
	else:
		ccoda = 1
	return ccoda

@csrf_exempt
def SaveSummary(request):
	data = json.loads(request.body)

	mesa = Mesas.objects.using(request.db).get(cmesa= data["cmesa"])

	comandas = Coda.objects.using(request.db).filter(cmesa=mesa,cresupedi__isnull=True)
	totales = sum( [ comanda.vttotal for comanda in comandas] )
	try:
		cresupedi = Resupedi.objects.latest('cresupedi').cresupedi + 1
	except Exception as e:
		cresupedi = 1

	resupedi = Resupedi(
		cresupedi=cresupedi,
		fresupedi = "2017-01-01",
		vttotal = totales,
		detaanula = "",
		ifcortesia = False,
	)

	resupedi.save(using=request.db)
	for comanda in comandas:
		comanda.cresupedi = resupedi
		comanda.save(using=request.db)

	resupedi = serializers.serialize("json", [resupedi],fields=('cresupedi','vttotal','detaanula','ifcortesia'),use_natural_foreign_keys=True)
	resupedi = json.loads(resupedi)[0]


	return HttpResponse(json.dumps(resupedi), "application/json")

@csrf_exempt
def SaveCommand(request):
	data = json.loads(request.body)

	mesero = Meseros.objects.using(request.db).filter()[0]
	talocoda = Talocoda.objects.using(request.db).filter()[0]
	ccoda = generar_ccoda(talocoda,request.db)
	mesa = Mesas.objects.using(request.db).get(cmesa= data["cmesa"])

	dataCoda = {
		'ccoda' : ccoda,
		'ctalocoda' : talocoda,
		'cmesa' : mesa,
		#'cesdo' : CESTADO_ACTIVO,
		'cmero' : mesero,
		#'cresupedi' : models.ForeignKey(Resupedi),
		'detaanula' : "",
		'vttotal' : 0,
		'fcoda' : "2017-02-02",
	}

	dataCodadeta = []
	it = 0
	for codadeta in data["deta"]:

		cmenu = codadeta[data["cols"]["cmenu"]["i"]]
		menu = Menus.objects.using(request.db).get(cmenu= cmenu)

		canti = float(codadeta[data["cols"]["canti"]["i"]])
		vunita = float(codadeta[data["cols"]["vunita"]["i"]])


		item = {
			'it' : it,
			'cmenu' : menu,
			'nlargo' : "",
			'canti' : canti,
			'vunita' : vunita,
			'vtotal' : canti * vunita,
		}
		dataCoda["vttotal"] += item["vtotal"]
		dataCodadeta.append(item)
		it += 1

	coda = create_Coda({"coda":dataCoda,"deta":dataCodadeta},request.db)
	coda = serializers.serialize("json", coda,use_natural_foreign_keys=True)
	coda = json.loads(coda)[0]


	return HttpResponse(json.dumps(coda), "application/json")

def create_Coda(data,name_db):
	if not isinstance(data,list):
		data = [data]

	list_coda = []
	coda = None
	for item in data:
		coda = Coda(**item["coda"])
		coda.save(using=name_db)
		for deta in item["deta"]:
			deta["ccoda"] = coda
			codadeta = Codadeta(**deta)
			codadeta.save(using=name_db)
		list_coda.append(coda)
	return list_coda

def TakeOrder(request):

	mesero = get_current_user(request.db,request.user,mesero=True)

	gruposMenu = GposMenus.objects.using(request.db).all().order_by("orden")
	for grupoMenu in gruposMenu:
		grupoMenu.menus = Menus.objects.using(request.db).filter(cgpomenu=grupoMenu)

	mesas = Mesas.objects.using(request.db).all()
	mesas_activas = Mesas.objects.using(request.db).filter(cmesa__in=Coda.objects.using(request.db).filter(cmero=mesero).values('cmesa'))

	print mesas_activas

	context = {
		'gruposMenu' : gruposMenu,
		'mesas' : mesas,
		'mesas_activas' : mesas_activas,
		'mesero' : mesero
	}
	return render(request, "ordenes/take-order.html", context)

def OrderSummary(request):
	mesas = Mesas.objects.using(request.db).all()

	for mesa in mesas:
		query = Coda.objects.using(request.db).filter(cresupedi__isnull=True,cmesa=mesa)
		mesa.vttotal = 0
		mesa.mesero = None
		if query.exists():
			mesa.comandas = query
			totales = sum( [ comanda.vttotal for comanda in mesa.comandas] )
			mesa.vttotal = totales
			mesa.mesero = mesa.comandas[0].cmero

	context = {
		'mesas' : mesas,
		'form_medios_pagos' : ResupedipagoForm(request.db)
	}
	return render(request, "ordenes/summary.html", context)

class OrderPrint(PDFTemplateView):
	template_name = "ordenes/print/format_half_letter.html"

	def get_context_data(self, **kwargs):
		context = super(OrderPrint, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)
		data = self.request.GET

		# Datos de Prueba
		"""usuario = Usuario.objects.using(self.request.db).filter()[0]

		talonario_MOS = usuario.ctalomos
		talonario_POS = usuario.ctalopos"""
		# Datos de Prueba

		formato = data.get('formato')
		cresupedi = data.get('cresupedi')

		resupedi = Resupedi.objects.using(self.request.db).filter(cresupedi=cresupedi)
		comandas = Coda.objects.using(self.request.db).filter(cresupedi=resupedi)
		for comanda in comandas:
			comandas.deta = Codadeta.objects.using(self.request.db).filter(ccoda=comanda)
		print comandas

		if formato or formato == "half_letter":
			self.template_name = "ordenes/print/format_half_letter.html"
			#context['orientation'] = 'portrait'
			context['orientation'] = 'landscape'

		elif formato == "neckband":
			self.template_name = "ordenes/print/format_half_letter.html"
			#context['orientation'] = 'portrait'
			context['orientation'] = 'landscape'
		else:
			self.template_name = "ordenes/print/format_half_letter.html"
			#context['orientation'] = 'portrait'
			context['orientation'] = 'landscape'

		data.company_logo = static(manageParameters.get_param_value('company_logo'))

		context['data'] = data
		context['title'] = 'Impresion de Resumen de Pedido'
		context['comandas'] = comandas

		return context
