# -*- encoding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.staticfiles.templatetags.staticfiles import static

from django.core import serializers

from django.core.urlresolvers import reverse_lazy
from django.db.models import Max

from infa_web.parameters import ManageParameters
from infa_web.apps.restaurante_menus.models import *
from infa_web.apps.base.views import AjaxableResponseMixin

from infa_web.apps.restaurante_menus.forms import *
from infa_web.apps.articulos.forms import *

from infa_web.apps.base.constantes import *


from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json
import decimal
from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView

from infa_web.apps.restaurante_menus.fun_crud.dishes import DishDetailCreate, DishDetailUpdate, DishDetailRemove, GetDishDetail
from infa_web.apps.restaurante_menus.fun_crud.menus import MenuDetailCreate, MenuDetailUpdate, MenuDetailRemove, GetMenuDetail

# ingredients #
class IngredientsList(CustomListView):
	model = Ingredientes
	template_name = "ingredientes/list-ingredients.html"

class IngredientCreate(AjaxableResponseMixin,CustomCreateView):
	model = Ingredientes
	template_name = "ingredientes/ingredient.html"
	form_class = IngredientForm
	success_url=reverse_lazy("list-ingredients")
	success_message = "Ingrediente creado."

	def get_context_data(self, **kwargs):
		context = super(IngredientCreate, self).get_context_data(**kwargs)
		context['title'] = "Crear Ingrediente"
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-ingredient')

		context['url_foto'] = static(DEFAULT_IMAGE_ARTICLE)

		manageParameters = ManageParameters(self.request.db)
		typeInventory = manageParameters.get_param_value("type_costing_and_stock")
		context['typeInventory'] = typeInventory

		return context

	def post(self, request, *args, **kwargs):
		mutable_data = request.POST.copy()

		manageParameters = ManageParameters(self.request.db)
		minCodeIngredient = manageParameters.get_param_value("min_code_ingredients")

		maxCingre = Ingredientes.objects.using(request.db).aggregate(Max('cingre'))
		if maxCingre["cingre__max"]:
			cingre = maxCingre["cingre__max"] + 1
		else:
			cingre = minCodeIngredient

		mutable_data["cingre"] = cingre

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

		#current_article = Ingredientes.objects.using(self.request.db).get(pk=self.kwargs["pk"])

		manageParameters = ManageParameters(self.request.db)
		minCodeArlos = manageParameters.get_param_value("min_code_ingredients")
		typeInventory = manageParameters.get_param_value("type_costing_and_stock")
		context['typeInventory'] = typeInventory

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
			'cesdo' :  str(queryset.cesdo.nesdo)
		}
	return HttpResponse(json.dumps(data_arlo), content_type="application/json")
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
		context['url_foto'] = static(DEFAULT_IMAGE_DISHES)

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

		context['title'] = "Editar Plato"
		form_platosdeta = DishDetailForm(self.request.db)
		context['form_platosdeta'] = form_platosdeta

		plato = Platos.objects.using(self.request.db).get(pk=self.kwargs["pk"])

		context['url_foto'] = plato.foto.url

		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-dish',kwargs={'pk': self.kwargs["pk"]},)

		return context

@csrf_exempt
def DishDetailCRUD(request):
	data = json.loads(request.body)
	if ( data["action"] == "create" ):
		response = DishDetailCreate(data["data"].iteritems(),request.db)
	elif ( data["action"] == "edit" ):
		response = DishDetailUpdate(data["data"].iteritems(),request.db)
	else:
		response = DishDetailRemove(data["data"].iteritems(),request.db)

	return HttpResponse(json.dumps(response), content_type="application/json")
# dish #

# menu #
"""
class MenusList(CustomListView):
	model = Menus
	template_name = "menus/list-menus.html"
	form_class = MenuForm

	def get_context_data(self,**kwargs):
		context = super(MenusList, self).get_context_data(**kwargs)
		context['title'] = "Listar Menu"
		return context

class MenuCreate(AjaxableResponseMixin,CustomCreateView):
	model = Menus
	template_name = "menus/menu.html"
	form_class = MenuForm
	success_url=reverse_lazy("list-menus")

	def get_context_data(self,**kwargs):
		context = super(MenuCreate, self).get_context_data(**kwargs)

		context['title'] = "Crear Menu"
		form_menusdeta = MenuDetailForm(self.request.db)
		context['form_menusdeta'] = form_menusdeta

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-menu')
		context['url_foto'] = static(DEFAULT_IMAGE_MENUS)

		return context

	def post(self, request, *args, **kwargs):
		mutable_data = request.POST.copy()

		manageParameters = ManageParameters(self.request.db)
		minCodeMenu = manageParameters.get_param_value("min_code_menu")

		maxCmenu = Menus.objects.using(request.db).aggregate(Max('cmenu'))
		if maxCmenu["cmenu__max"]:
			cmenu = maxCmenu["cmenu__max"] + 1
		else:
			cmenu = minCodeMenu

		mutable_data["cmenu"] = cmenu

		request.POST = mutable_data

		return super(MenuCreate, self).post(request, *args, **kwargs)

class MenuUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Menus
	template_name = "menus/menu.html"
	form_class = MenuForm
	success_url=reverse_lazy("list-menus")

	def get_context_data(self,**kwargs):
		context = super(MenuUpdate, self).get_context_data(**kwargs)

		context['title'] = "Editar Menu"
		form_menusdeta = MenuDetailForm(self.request.db)
		context['form_menusdeta'] = form_menusdeta

		menu = Menus.objects.using(self.request.db).get(pk=self.kwargs["pk"])

		context['url_foto'] = menu.foto.url

		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-menu',kwargs={'pk': self.kwargs["pk"]},)

		return context
"""






class MenuCreate(AjaxableResponseMixin,CustomCreateView):
	model = Arlo
	# template_name = "articulos/article.html"
	template_name = "menus/menu.html"
	form_class = ArticleForm
	success_url=reverse_lazy("add-article")
	success_message = "Menu creado."

	def get_context_data(self, **kwargs):
		context = super(MenuCreate, self).get_context_data(**kwargs)
		context['title'] = "Crear Menu"
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-article')

		context['url_foto1'] = DEFAULT_IMAGE_ARTICLE
		context['url_foto2'] = DEFAULT_IMAGE_ARTICLE
		context['url_foto3'] = DEFAULT_IMAGE_ARTICLE

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

		return super(MenuCreate, self).post(request, *args, **kwargs)

class MenuUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Arlo
	# template_name = "articulos/article.html"
	template_name = "menus/menu.html"
	success_url=reverse_lazy("add-article")
	form_class = ArticleForm

	def get_context_data(self, **kwargs):
		context = super(MenuUpdate, self).get_context_data(**kwargs)
		context['title'] = "Editar Menu"
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-article',kwargs={'pk': self.kwargs["pk"]},)

		current_article = Arlo.objects.using(self.request.db).get(pk=self.kwargs["pk"])

		manageParameters = ManageParameters(self.request.db)
		minCodeArlos = manageParameters.get_param_value("min_code_arlos")
		typeInventory = manageParameters.get_param_value("type_costing_and_stock")
		context['typeInventory'] = typeInventory

		context['url_foto1'] = current_article.foto1.url
		context['url_foto2'] = current_article.foto2.url
		context['url_foto3'] = current_article.foto3.url
		return context

class MenusList(CustomListView):
	model = Arlo
	# template_name = "articulos/list-articles.html"
	template_name = "menus/list-menus.html"

# Articles #














@csrf_exempt
def MenuDetailCRUD(request):
	data = json.loads(request.body)
	if ( data["action"] == "create" ):
		response = MenuDetailCreate(data["data"].iteritems(),request.db)
	elif ( data["action"] == "edit" ):
		response = MenuDetailUpdate(data["data"].iteritems(),request.db)
	else:
		response = MenuDetailRemove(data["data"].iteritems(),request.db)

	return HttpResponse(json.dumps(response), content_type="application/json")
# menu #

# Groups #
"""
class GroupCreate(AjaxableResponseMixin,CustomCreateView):
	model = GposMenus
	form_class = GposMenusForm
	template_name = "menus/group.html"
	success_url=reverse_lazy("add-menu-group")

	def get_context_data(self, **kwargs):
		context = super(GroupCreate, self).get_context_data(**kwargs)
		context['title'] = "Crear Grupo"
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-menu-group')

		return context

class GroupUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = GposMenus
	form_class = GposMenusForm
	template_name = "menus/group.html"
	success_url=reverse_lazy("add-group")
	success_message = "was update successfully"

	def get_context_data(self, **kwargs):
		context = super(GroupUpdate, self).get_context_data(**kwargs)
		context['title'] = "Editar Grupo"
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-menu-group',kwargs={'pk': self.kwargs["pk"]},)
		return context

class GroupList(CustomListView):
	model = None
	queryset = None
	template_name = "menus/list-groups.html"

	def get_queryset(self):
		if self.queryset is not None:
			queryset = self.queryset
			if isinstance(queryset, QuerySet):
				queryset = queryset.all()
		elif self.model is not None:
			queryset = self.model._default_manager.using(self.request.db).all()
		else:
			queryset = GposMenus.objects.using(self.request.db).all()

		ordering = self.get_ordering()
		if ordering:
			if isinstance(ordering, six.string_types):
				ordering = (ordering,)
			queryset = queryset.order_by(*ordering)
		return queryset
"""
# Groups #
