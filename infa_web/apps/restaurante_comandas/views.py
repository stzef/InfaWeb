from django.shortcuts import render
import json
import datetime
from infa_web.apps.restaurante_menus.models import *
from infa_web.apps.restaurante_comandas.models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def OrdersList(request):
	context = {}
	return render(request, "ordenes/list-orders.html", context)


def GetCommandsOrder(request, cmesa):
	comandas = Coda.objects.using(request.db).filter(cmesa=cmesa)

	return comandas

@csrf_exempt
def SaveCommand(request):

	data = json.loads(request.body)

	mesero = Meseros.objects.using(request.db).filter()[0]
	talocoda = Talocoda.objects.using(request.db).filter()[0]
	ccoda = 1

	dataCoda = {

		'ccoda' : ccoda,
		'ctalocoda' : talocoda,
		'cmesa' : Mesas.objects.using(request.db).get(cmesa= data["cmesa"]),
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
		canti = float(codadeta[data["cols"]["canti"]["i"]])
		vunita = float(codadeta[data["cols"]["vunita"]["i"]])

		item = {
			'it' : it,
			'cmenu' : Menus.objects.using(request.db).get(cmenu= cmenu),
			'nlargo' : "",
			'canti' : canti,
			'vunita' : vunita,
			'vtotal' : canti * vunita,
		}
		dataCodadeta.append(item)
		it += 1

	coda = create_Coda({"coda":dataCoda,"deta":dataCodadeta},request.db)

	return HttpResponse(json.dumps({}), "application/json")

def create_Coda(data,name_db):
	if not isinstance(data,list):
		data = [data]

	#print data

	coda = None
	for item in data:
		item["coda"]["ccoda"] = 1000
		coda = Coda(**item["coda"])
		coda.save(using=name_db)
		for deta in item["deta"]:
			deta["ccoda"] = coda
			codadeta = Codadeta(**deta)
			codadeta.save(using=name_db)
	return coda


def TakeOrder(request):
	gruposMenu = GposMenus.objects.using(request.db).all().order_by("orden")
	for grupoMenu in gruposMenu:
		grupoMenu.menus = Menus.objects.using(request.db).filter(cgpomenu=grupoMenu)

	mesas = Mesas.objects.using(request.db).all()

	context = {
		'gruposMenu' : gruposMenu,
		'mesas' : mesas
	}
	return render(request, "ordenes/take-order.html", context)
