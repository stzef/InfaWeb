# -*- encoding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.core.urlresolvers import reverse_lazy
from django.db.models import Max

from infa_web.parameters import ManageParameters
from infa_web.apps.restaurante_menus.models import *
from infa_web.apps.base.views import AjaxableResponseMixin
from infa_web.apps.restaurante_menus.forms import *
from infa_web.apps.base.constantes import *


from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json

from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView

# ingredients #

class IngredientCreate(AjaxableResponseMixin,CustomCreateView):
	model = Ingredientes
	template_name = "ingredientes/ingredient.html"
	form_class = IngredientForm
	success_url=reverse_lazy("list-ingredient")
	success_message = "Ingrediente creado."

	def get_context_data(self, **kwargs):
		context = super(IngredientCreate, self).get_context_data(**kwargs)
		context['title'] = "Crear Ingrediente"
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-ingredient')

		context['url_foto'] = DEFAULT_IMAGE_ARTICLE

		manageParameters = ManageParameters(self.request.db)
		typeInventory = manageParameters.get_param_value("type_costing_and_stock")
		context['typeInventory'] = typeInventory

		return context

	def post(self, request, *args, **kwargs):
		mutable_data = request.POST.copy()

		manageParameters = ManageParameters(self.request.db)
		minCodeArlos = manageParameters.get_param_value("min_code_arlos")

		maxCarlos = Arlo.objects.using(request.db).aggregate(Max('carlos'))
		if maxCarlos["carlos__max"]:
			carlos = maxCarlos["carlos__max"] + 1
		else:
			carlos = minCodeArlos

		mutable_data["carlos"] = carlos

		request.POST = mutable_data

		return super(IngredientCreate, self).post(request, *args, **kwargs)

class IngredientUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Ingredientes
	template_name = "ingredientes/ingredient.html"
	success_url=reverse_lazy("add-ingredient")
	form_class = IngredientForm

	def get_context_data(self, **kwargs):
		context = super(IngredientUpdate, self).get_context_data(**kwargs)
		context['title'] = "Editar Ingrediente"
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-ingredient',kwargs={'pk': self.kwargs["pk"]},)

		current_article = Ingredientes.objects.using(self.request.db).get(pk=self.kwargs["pk"])

		manageParameters = ManageParameters(self.request.db)
		minCodeArlos = manageParameters.get_param_value("min_code_arlos")
		typeInventory = manageParameters.get_param_value("type_costing_and_stock")
		context['typeInventory'] = typeInventory

		context['url_foto'] = current_article.foto
		return context

def Ingredients_list(request):
	data_arlo = {}
	data_arlo['arlo'] = {}
	orderBy = request.GET.get('orderBy')
	ingredientes = Ingredientes.objects.using(request.db).all()
	if request.GET.get('buscarPor'):
		ingredientes = ingredientes.filter(ningre__icontains = request.GET.get('buscarPor'))
	else:
		ingredientes
	arlo = Paginator(ingredientes.order_by(orderBy), 10)
	page = request.GET.get('page')
	arlo = arlo.page(page)
	if len(arlo.object_list) < 10:
		data_arlo['response'] = 0
	else:
		data_arlo['response'] = 1
	for queryset in arlo:
		data_arlo['arlo'][queryset.cingre] = {
			'cingre' :  queryset.cingre,
			'ningre' :  queryset.ningre,
			'canti' :  str(queryset.canti).replace(",", "."),
			'vcosto' :  str(queryset.vcosto).replace(",", "."),
			#'ifcostear' :  queryset.ifcostear,
			#'stomin' :  queryset.stomin,
			#'stomax' :  queryset.stomax,
			#'ifedinom' :  queryset.ifedinom,
			#'cesdo' :  queryset.cesdo,
			#'cunidad' :  queryset.cunidad,
			#'civa' :  queryset.civa,
			#'foto' :  queryset.foto,
		}
	return HttpResponse(json.dumps(data_arlo), content_type="application/json")

@csrf_exempt
def GetIngredientsDish(request,pk):
	deta = Platosdeta.objects.using(request.db).filter(cplato=pk)

	ingredientes = Ingredientes.objects.using(request.db).all()
	ingredientes_json = []

	for ingrediente in ingredientes:
		ingredientes_json.append({"value":ingrediente.cingre,"label":ingrediente.ningre})

	data = {
		"data" :[] ,
		"options": {"ingredientes.cingre": ingredientes_json}
	}
	for item in deta:
		data["data"].append({
				"DT_RowId": "row_1",
				"ingredientes" : {
					"cingre" : str(item.cingre.cingre),
					"it" : str(item.it),
					"canti" : str(item.canti),
					"vunita" : str(item.vunita),
					"vtotal" : str(item.vtotal),
				},
				"cingres" : {
					"name" : str(item.cingre.ningre)
				}
			})
	return HttpResponse(json.dumps(data), content_type="application/json")

class IngredientsList(CustomListView):
	model = Ingredientes
	template_name = "ingredientes/list-ingredients.html"
# ingredients #

# dish #
class DishesList(CustomListView):
	model = Platos
	template_name = "platos/list-dishes.html"
	form_class = DishForm

	def get_context_data(self,**kwargs):
		context = super(DishesList, self).get_context_data(**kwargs)
		context['title'] = "Listar Platos"
		return context

@csrf_exempt
def DishDetailCreate(request):
	data = json.loads(request.body)
	response = { "data" : []  }

	for key, value in data["data"].iteritems():
		print value
		value["ingredientes"]["cingre"] = Ingredientes.objects.using(request.db).get(pk=value["ingredientes"]["cingre"])
		value["ingredientes"]["cplato"] = Platos.objects.using(request.db).get(pk=value["ingredientes"]["cplato"])
		platodeta = Platosdeta(**value["ingredientes"])

		response["data"].append({
			"DT_RowId": "row_1",
			"ingredientes" : {
				"it" : platodeta.it,
				"cingre" : platodeta.cingre.cingre,
				"canti" : platodeta.canti,
				"vunita" : platodeta.vunita,
				"vtotal" : platodeta.vtotal,
			},
			"cingres" : {
				"name" : str(platodeta.cingre.ningre)
			}
	})

		platodeta.save(using=request.db)
		print platodeta

	return HttpResponse(json.dumps(response), content_type="application/json")

class DishCreate(AjaxableResponseMixin,CustomCreateView):
	model = Platos
	template_name = "platos/dish.html"
	form_class = DishForm
	success_url=reverse_lazy("list-dishes")

	def get_context_data(self,**kwargs):
		context = super(DishCreate, self).get_context_data(**kwargs)

		context['title'] = "Crear Plato"
		form_platosdeta = DishDetailForm(self.request.db)
		context['form_platosdeta'] = form_platosdeta

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-dish')
		context['url_foto'] = DEFAULT_IMAGE_DISHES

		return context

	def post(self, request, *args, **kwargs):
		mutable_data = request.POST.copy()

		manageParameters = ManageParameters(self.request.db)
		minCodeDish = manageParameters.get_param_value("min_code_dish")

		maxCplato = Platos.objects.using(request.db).aggregate(Max('cplato'))
		if maxCplato["cplato__max"]:
			cplato = maxCplato["cplato__max"] + 1
		else:
			cplato = minCodeDish

		mutable_data["cplato"] = cplato

		request.POST = mutable_data

		return super(DishCreate, self).post(request, *args, **kwargs)

class DishUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Platos
	template_name = "platos/dish.html"
	form_class = DishForm
	success_url=reverse_lazy("list-dishes")

	def get_context_data(self,**kwargs):
		context = super(DishUpdate, self).get_context_data(**kwargs)

		context['title'] = "Editar Movimiento de Entrada"
		form_platosdeta = DishDetailForm(self.request.db)
		context['form_platosdeta'] = form_platosdeta

		plato = Platos.objects.using(self.request.db).get(pk=self.kwargs["pk"])

		context['url_foto'] = plato.foto

		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-dish',kwargs={'pk': self.kwargs["pk"]},)

		return context
# dish #
