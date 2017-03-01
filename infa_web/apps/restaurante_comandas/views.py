from django.shortcuts import render
import json
import datetime
from infa_web.apps.restaurante_menus.models import *
from infa_web.apps.restaurante_comandas.models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


from infa_web.apps.base.utils import get_current_user
from django.db.models import Max

from django.contrib.auth.models import User
from infa_web.apps.usuarios.models import Usuario


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
	resupedi = Resupedi(
		cresupedi=Resupedi.objects.latest('cresupedi').cresupedi + 1,
		fresupedi = "2017-01-01",
		vttotal = totales,
		detaanula = "",
		ifcortesia = False,
	)

	resupedi.save(using=request.db)
	for comanda in comandas:
		comanda.cresupedi = resupedi
		comanda.save(using=request.db)


	return HttpResponse(json.dumps(data), "application/json")

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
		print query
		if query.exists():
			mesa.comandas = query
			totales = sum( [ comanda.vttotal for comanda in mesa.comandas] )
			mesa.vttotal = totales
			mesa.mesero = mesa.comandas[0].cmero

	context = {
		'mesas' : mesas,
	}
	return render(request, "ordenes/summary.html", context)
