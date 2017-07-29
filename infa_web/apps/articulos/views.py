# -*- encoding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.db.models import Max
from django import forms

from infa_web.apps.base.constantes import EMPRESA
from infa_web.parameters import ManageParameters
from infa_web.apps.articulos.models import *
from infa_web.apps.base.views import AjaxableResponseMixin
from infa_web.apps.articulos.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
import json

from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView

# Articles #
"""
@csrf_exempt
def SaveBreakdownArticle(request,pk):
	data = json.loads(request.body)
	itglo = 0
	for item in data:
		#return HttpResponse(json.dumps(item), "application/json")

		response = {}

		cesdo = Esdo.objects.get(cesdo=item["cesdo"])
		carlosp = Arlo.objects.get(carlos=item["carlosp"])
		carlosglo = Arlo.objects.get(carlos=item["carlosglo"])

		#itglo = item["itglo"]
		cantiglo = item["cantiglo"]
		costoglo = item["costoglo"]
		vtoglo = item["vtoglo"]

		if Arlosdesglo.objects.filter(carlosp=carlosp,carlosglo=carlosglo).exists():
			response["message"] = "Edicion Exitosa"
			arlodesglo = Arlosdesglo.objects.get(carlosp=carlosp,carlosglo=carlosglo)
			arlodesglo.cesdo = cesdo
			arlodesglo.cantiglo = cantiglo
			arlodesglo.costoglo = costoglo
			arlodesglo.vtoglo = vtoglo

			arlodesglo.save(using=request.db)
		else:
			response["message"] = "Creacion Exitosa"
			Arlosdesglo.objects.create(
				cesdo=cesdo,
				carlosp=carlosp,
				carlosglo=carlosglo,
				itglo=itglo,
				cantiglo=cantiglo,
				costoglo=costoglo,
				vtoglo=vtoglo
			)
		itglo += 1

	return HttpResponse(json.dumps(response), "application/json")

class BreakdownArticle(FormView):
	model = Arlosdesglo
	template_name = 'articulos/breakdown-article.html'
	form_class = BreakdownArticleForm

	def get_context_data(self,**kwargs):
		context = super(BreakdownArticle, self).get_context_data(**kwargs)
		#context['article'] = Arlo.objects.using(self.request.db).get()
		context['article'] = get_object_or_404(Arlo,carlos=self.kwargs["pk"])
		context["partsArticle"] = Arlosdesglo.objects.using(self.request.db).filter(carlosp=self.kwargs["pk"])
		return context
		#class DepartamentsList(CustomListView):
"""

class ArticleCreate(AjaxableResponseMixin,CustomCreateView):
	model = Arlo
	template_name = "articulos/article.html"
	form_class = ArticleForm
	success_url=reverse_lazy("add-article")
	success_message = "Articulo creado."

	def get_context_data(self, **kwargs):
		context = super(ArticleCreate, self).get_context_data(**kwargs)
		context['title'] = "Crear Articulo"
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

		return super(ArticleCreate, self).post(request, *args, **kwargs)

@method_decorator(csrf_exempt, name='dispatch')
class ArticleCopy(CustomUpdateView):
	model = Arlo
	template_name = "articulos/article.html"
	form_class = ArticleForm
	success_url=reverse_lazy("add-article")
	success_message = "Articulo creado."

	def get_context_data(self, **kwargs):
		context = super(ArticleCopy, self).get_context_data(**kwargs)
		maxCarlos = Arlo.objects.using(self.request.db).aggregate(Max('carlos'))
		context['title'] = "Copiar Articulo"
		context['mode_view'] = 'copy'
		context['url'] = reverse_lazy('add-article')

		context['url_foto1'] = current_article.foto1.url
		context['url_foto2'] = current_article.foto2.url
		context['url_foto3'] = current_article.foto3.url

		manageParameters = ManageParameters(self.request.db)
		minCodeArlos = manageParameters.get_param_value("min_code_arlos")
		typeInventory = manageParameters.get_param_value("type_costing_and_stock")
		context['typeInventory'] = typeInventory

		if maxCarlos["carlos__max"]:
			context['current_pk'] = maxCarlos["carlos__max"] + 1
		else:
			context['current_pk'] = minCodeArlos
		return context

class ArticleUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Arlo
	template_name = "articulos/article.html"
	success_url=reverse_lazy("add-article")
	form_class = ArticleForm

	def get_context_data(self, **kwargs):
		context = super(ArticleUpdate, self).get_context_data(**kwargs)
		context['title'] = "Editar Articulo"
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

def article_list(request):
	data_arlo = {}
	data_arlo['arlo'] = {}
	orderBy = request.GET.get('orderBy')
	#arlos = Arlo.objects.using(request.db).all()
	arlos = Arlo.objects.using(request.db).all()
	if request.GET.get('buscarPor'):
		arlos = arlos.filter(nlargo__icontains = request.GET.get('buscarPor'))
	else:
		arlos
	arlo = Paginator(arlos.order_by(orderBy), 10)
	page = request.GET.get('page')
	arlo = arlo.page(page)
	if len(arlo.object_list) < 10:
		data_arlo['response'] = 0
	else:
		data_arlo['response'] = 1
	for queryset in arlo:
		data_arlo['arlo'][queryset.carlos] = {
			'carlos': queryset.carlos,
			'nlargo': queryset.nlargo,
			'cbarras': queryset.cbarras,
			'canti': 0,
			'vcosto': str(queryset.vcosto).replace(",", "."),
			'cesdo': queryset.cesdo.nesdo,
			'cmarca': queryset.cmarca.nmarca,
			'cancalcu': str(queryset.canti).replace(",", "."),
			'cgrupo': queryset.cgpo.ngpo
		}
	return HttpResponse(json.dumps(data_arlo), content_type="application/json")

class ArticleList(CustomListView):
	model = Arlo
	template_name = "articulos/list-articles.html"
# Articles #

# Groups #
class GroupCreate(AjaxableResponseMixin,CustomCreateView):
	model = Gpo
	form_class = GpoForm
	template_name = "articulos/group.html"
	success_url=reverse_lazy("add-group")

	def get_context_data(self, **kwargs):
		context = super(GroupCreate, self).get_context_data(**kwargs)
		context['title'] = "Crear Grupo"
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-group')

		return context

class GroupUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Gpo
	form_class = GpoForm
	template_name = "articulos/group.html"
	success_url=reverse_lazy("add-group")
	success_message = "was update successfully"

	def get_context_data(self, **kwargs):
		context = super(GroupUpdate, self).get_context_data(**kwargs)
		context['title'] = "Editar Grupo"
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-group',kwargs={'pk': self.kwargs["pk"]},)
		return context

class GroupList(CustomListView):
	model = None
	queryset = None
	template_name = "articulos/list-groups.html"

	def get_queryset(self):
		if self.queryset is not None:
			queryset = self.queryset
			if isinstance(queryset, QuerySet):
				queryset = queryset.all()
		elif self.model is not None:
			queryset = self.model._default_manager.using(self.request.db).all()
		else:
			queryset = Gpo.objects.using(self.request.db).all()

		ordering = self.get_ordering()
		if ordering:
			if isinstance(ordering, six.string_types):
				ordering = (ordering,)
			queryset = queryset.order_by(*ordering)
		return queryset
# Groups #

# Types Articles #
class TypesArticleCreate(AjaxableResponseMixin,CustomCreateView):
	model = Tiarlos
	form_class = TiarlosForm
	template_name = "articulos/tipe-article.html"
	success_url=reverse_lazy("add-type-article")

class TypesArticleUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Tiarlos
	form_class = TiarlosForm
	template_name = "articulos/tipe-article.html"
	success_url=reverse_lazy("add-type-article")

class TypesArticleList(CustomListView):
	model = Tiarlos
	template_name = "articulos/list-types-articles.html"

# Types Articles #

# Unidades #
class UnitCreate(AjaxableResponseMixin,CustomCreateView):
	model = Unidades
	form_class = UnidadesForm
	template_name = "articulos/unit.html"
	success_url=reverse_lazy("add-unit")

class UnitUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Unidades
	form_class = UnidadesForm
	template_name = "articulos/unit.html"
	success_url=reverse_lazy("add-unit")

class UnitsList(CustomListView):
	model = Unidades
	template_name = "articulos/list-units.html"

# Unidades #

# Brands #
class BrandCreate(AjaxableResponseMixin,CustomCreateView):
	model = Marca
	form_class = BrandForm
	template_name = "base/brand.html"
	success_url=reverse_lazy("add-brand")

	def get_context_data(self, **kwargs):
		context = super(BrandCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Marca'
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-brand')

		return context

class BrandUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Marca
	form_class = BrandForm
	template_name = "base/brand.html"
	success_url=reverse_lazy("add-brand")

	def get_context_data(self, **kwargs):
		context = super(BrandUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Marca'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-brand',kwargs={'pk': self.kwargs["pk"]},)

		return context

class BrandsList(CustomListView):
	model = Marca
	template_name = "articulos/list-brands.html"
# Brands #

# API #
codeModels = {
	1:{'name':'Tiarlos','app':'articulos'},
	2:{'name':'Gpo','app':'articulos'},
	3:{'name':'Marca','app':'articulos'},
	4:{'name':'Unidades','app':'articulos'},
	5:{'name':'Arlo','app':'articulos'},
	6:{'name':'Arlosdesglo','app':'articulos'},
	7:{'name':'Bode','app':'base'},
	8:{'name':'Esdo','app':'base'},
	9:{'name':'Modules','app':'base'},
	10:{'name':'Parameters','app':'base'},
	11:{'name':'Ubica','app':'base'},
	12:{'name':'Departamento','app':'base'},
	13:{'name':'Ciudad','app':'base'},
	14:{'name':'Iva','app':'base'},
	15:{'name':'Regiva','app':'base'},
	16:{'name':'Tiide','app':'base'},
	17:{'name':'Invinicab','app':'inventarios'},
	18:{'name':'Invinideta','app':'inventarios'},
	19:{'name':'Timo','app':'base'},
	20:{'name':'Mven','app':'movimientos'},
	21:{'name':'Mvendeta','app':'movimientos'},
	22:{'name':'Mvsa','app':'movimientos'},
	23:{'name':'Mvsadeta','app':'movimientos'},
	24:{'name':'Autorre','app':'terceros'},
	25:{'name':'Vende','app':'terceros'},
	26:{'name':'Ruta','app':'terceros'},
	27:{'name':'Personas','app':'terceros'},
	28:{'name':'Zona','app':'terceros'},
	29:{'name':'Tercero','app':'terceros'},
	30:{'name':'Fac','app':'facturacion'},
	31:{'name':'Facdeta','app':'facturacion'},
	32:{'name': 'MediosPago','app':'base'},

	33:{'name': 'Ingredientes','app':'restaurante_menus'},
	34:{'name': 'Platos','app':'restaurante_menus'},
	35:{'name': 'Menus','app':'restaurante_menus'},

}

from django.core import serializers
@csrf_exempt
def API_exists(request):
	data = json.loads(request.body)
	model = apps.get_model(app_label=codeModels[data["model"]]["app"],model_name=codeModels[data["model"]]["name"])

	filter_dict = {}
	filter_dict[data["field"]] = data["value"]
	if model.objects.using(request.db).filter(**filter_dict).exists():
		return JsonResponse({'exists':True})
	else:
		return JsonResponse({'exists':False})

@csrf_exempt
def API_get_object(request):
	data = json.loads(request.body)
	model = apps.get_model(app_label=codeModels[data["model"]]["app"],model_name=codeModels[data["model"]]["name"])

	filter_dict = {}
	filter_dict[data["field"]] = data["value"]
	if model.objects.using(request.db).filter(**filter_dict).exists():
		object_db = serializers.serialize("json", [model.objects.using(request.db).get(**filter_dict)],use_natural_foreign_keys=True, use_natural_primary_keys=True)
		return JsonResponse({'object':object_db})
	else:
		return JsonResponse({'object':None})

# API #
