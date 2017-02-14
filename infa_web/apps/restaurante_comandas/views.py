from django.shortcuts import render

from infa_web.apps.restaurante_menus.models import *
from infa_web.apps.restaurante_comandas.models import *


def OrdersList(request):
	context = {}
	return render(request,"ordenes/list-orders.html",context)


def GetCommandsOrder(request, cmesa):
	comandas = Coda.objects.using(request.db).filter(cmesa=cmesa)

	return comandas

def TakeOrder(request):
	gruposMenu = GposMenus.objects.using(request.db).all()
	for grupoMenu in gruposMenu:
		grupoMenu.menus = Menus.objects.using(request.db).filter(cgpomenu=grupoMenu)

	mesas = Mesas.objects.using(request.db).all()

	context = {
		'gruposMenu' : gruposMenu,
		'mesas' : mesas
	}
	return render(request,"ordenes/take-order.html",context)
