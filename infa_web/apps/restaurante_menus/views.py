# -*- encoding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse_lazy
from django.db.models import Max

from infa_web.parameters import ManageParameters
from infa_web.apps.restaurante_menus.models import *
from infa_web.apps.base.views import AjaxableResponseMixin
from infa_web.apps.restaurante_menus.forms import *

from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json

from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView

# ingredients #

class IngredientCreate(AjaxableResponseMixin,CustomCreateView):
	model = Ingredientes
	template_name = "ingredientes/ingredient.html"
	form_class = IngredientForm
	success_url=reverse_lazy("add-ingredient")
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
def load_deta(request):
	data = {
		"data": [
			{
				"DT_RowId": "row_1",
				"users": {
					"first_name": "Quynn",
					"last_name": "Contreras",
					"site": "1"
				},
				"sites": {
					"name": "Edinburgh"
				},
				"permission": [
					{
						"id": "3",
						"name": "Desktop"
					},
					{
						"id": "1",
						"name": "Printer"
					},
					{
						"id": "4",
						"name": "VMs"
					}
				]
			}
		]
	}
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

class DishCreate(CustomCreateView):
	model = Platos
	template_name = "platos/dish.html"
	form_class = DishForm

	def get_context_data(self,**kwargs):
		context = super(DishCreate, self).get_context_data(**kwargs)

		context['title'] = "Crear Plato"
		form_platosdeta = DishDetail(self.request.db)
		context['form_platosdeta'] = form_platosdeta

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-dish')

		return context

class DishUpdate(CustomUpdateView):
	model = Platos
	template_name = "platos/dish.html"
	form_class = DishForm

	def get_context_data(self,**kwargs):
		context = super(DishUpdate, self).get_context_data(**kwargs)

		context['title'] = "Editar Movimiento de Entrada"
		form_platosdeta = DishDetail(self.request.db)
		context['form_platosdeta'] = form_platosdeta

		context['platosdeta'] = list(Platosdeta.objects.using(self.request.db).filter(cplato=self.kwargs["pk"]))
		context['platosdeta_json'] = serializers.serialize("json", list(Platosdeta.objects.using(self.request.db).filter(cplato=self.kwargs["pk"])),use_natural_foreign_keys=True, use_natural_primary_keys=True)

		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-dish',kwargs={'pk': self.kwargs["pk"]},)

		return context
# dish #
