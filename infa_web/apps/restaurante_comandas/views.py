from django.shortcuts import render

from infa_web.apps.restaurante_menus.models import Menus


def OrdersList(request):
	context = {}
	return render(request,"ordenes/list-orders.html",context)


def TakeOrder(request):
	print Menus.objects.using(request.db).all()
	context = {
		'menu' : Menus.objects.using(request.db).all()
	}
	return render(request,"ordenes/take-order.html",context)
