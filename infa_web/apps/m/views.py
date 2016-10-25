import json

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from infa_web.apps.terceros.models import Tercero
from infa_web.apps.terceros.forms import ThirdPartyForm
from infa_web.apps.articulos.models import Arlo
from infa_web.apps.base.models import MediosPago
from infa_web.apps.base.models import Tifopa
from infa_web.apps.facturacion.models import Facpago
from infa_web.apps.facturacion.forms import FacpagoForm
from infa_web.custom.generic_views import CustomCreateView
from infa_web.parameters import ManageParameters
from infa_web.apps.base.constantes import FORMA_PAGO_CONTADO


def mDashboard(request):
	return render(request, 'm/m_dashboard.html')

def mFacOptionsArticle(request):

	# obtener articulo & cliente
	codigoDelArticulo = request.GET.get('carlo', None)
	pkCliente = request.GET.get('client', None)
	parametros = ManageParameters(request.db)

	context = {
		'parametros' : parametros.to_dict(),
		'parametros_json' : json.dumps(parametros.to_dict())
	}

	# obtener valor del articulo para el cliente
	if codigoDelArticulo is not None and pkCliente is not None:
		cliente = Tercero.objects.using(request.db).get(pk=pkCliente)
		articulo = Arlo.objects.using(request.db).get(carlos=codigoDelArticulo) 


		listaDePrecio = cliente.clipre
		valorUnitarioArticulo = getattr(articulo, 'pvta' + str(listaDePrecio))
		valorMinimoDelArticulo = articulo.pvta6

		# agregar datos al contexto
		context["valorUnitario"] = valorUnitarioArticulo
		context["valorMinimoDelArticulo"] = valorMinimoDelArticulo


	return render(request, 'm/m_fac_options_article.html', context)

def mFacChooseClient(request):
	# Consultar cliente mostrador
	clienteMostrador = 1
	form = ThirdPartyForm(request.db)

	# Agregar contexto
	context = {
		'clienteMostrador' : clienteMostrador,
		'form' : form
	}

	return render(request, 'm/m_fac_choose_client.html', context)

def mFac(request):

	clienteMostrador = 1

	context = {
		'clienteMostrador' : clienteMostrador
	}

	return render(request, 'm/m_fac.html', context)

def mFacSearchClient(request):
	# Consultar Terceros
	# Priorizar Consulta
	mostrador = 1

	terceros = Tercero.objects.using(request.db).exclude(idterce=mostrador).order_by('-pk')[:1]

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

	formasDePago = Tifopa.objects.using(request.db).all()
	mediosDePago = MediosPago.objects.using(request.db).all()
	formPagosDeFactura = FacpagoForm(request.db)
	parametros = ManageParameters(request.db)
	pagoContado = FORMA_PAGO_CONTADO

	context = {
		'formasPago' : formasDePago,
		'mediosPago' : mediosDePago,
		'pagoContado' : pagoContado,
		'parametros' : parametros.to_dict(),
		'parametros_json' : json.dumps(parametros.to_dict()),
		'form' : formPagosDeFactura
	}

	return render(request, 'm/m_fac_pay.html', context)

class mThirdPartyAdd(CustomCreateView):

	model = Tercero
	template_name = "m/m_third_party_add.html"
	form_class = ThirdPartyForm
	success_url = "/m/search-client"

## Request Ajax basadas en JSON
@csrf_exempt
def mThirtyPartyList(request):

	# filtro razonsocial | identificacion
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

@csrf_exempt
def mArticlesList(request):

	# filtro codigo | nombre del articulo
	query = request.GET.get('q', None)

	#filtrar articulos
	if query is not None:
		articulos = Arlo.objects.using(request.db).filter(
			Q(carlos__icontains=query) | Q(ncorto__icontains=query)
		)

		data = serializers.serialize("json", articulos, fields=('carlos', 'ncorto', 'pvta1'))
		return JsonResponse(data, safe=False)

	else:
		return JsonResponse({}, safe=False)