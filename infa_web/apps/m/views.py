from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


from infa_web.apps.terceros.models import Tercero

def mDashboard(request):
	return render(request, 'm/m_dashboard.html')

def mFacChooseClient(request):
	# Consultar cliente mostrador
	clienteMostrador = 1

	# Agregar contexto
	context = {
		'clienteMostrador' : clienteMostrador
	}

	return render(request, 'm/m_fac_choose_client.html', context)

def mFacSearchClient(request):
	# Consultar Terceros
	# Priorizar Consulta
	mostrador = 1
	terceros = Tercero.objects.using(request.db).exclude(idterce=mostrador)[:10]

	# Agregar a contexto
	context = {
		'terceros' : terceros
	}

	return render(request, 'm/m_fac_search_client.html', context)

def mFacOrder(request):
	return render(request, 'm/m_fac_order.html')

def mFacOrder2(request):
	return render(request, 'm/m_fac_order2.html')

def mFacChooseArtice(request):
	return render(request, 'm/m_fac_choose_article.html')

def mFacPay(request):
	return render(request, 'm/m_fac_pay.html')

def mThirdPartyAdd(request):
	return render(request, 'm/m_third_party_add.html')


## Request Ajax basadas en JSON
@csrf_exempt
def mThirtyPartyList(request):

	#filtro razonsocial | identificacion
	query = request.GET.get('q', None)

	# obtener terceros
	clienteMostrador = 1
	clientes = Tercero.objects.using(request.db).exclude(idterce=clienteMostrador)

	# filtrar clientes
	if query is not None:
		clientes = clientes.filter(
			Q(rasocial__icontains=query) | Q(idterce__contains=query)
		)

	# serializar respuesta
	data = serializers.serialize("json", clientes, fields=('idterce', 'rasocial'))

	return JsonResponse(data, safe=False)
	# responder