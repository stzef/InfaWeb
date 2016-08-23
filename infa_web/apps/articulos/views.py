# -*- encoding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy 
from django.http import HttpResponse
import json
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from django import forms

from django.apps import apps

from infa_web.apps.base.constantes import EMPRESA
from infa_web.parameters import ManageParameters

from infa_web.apps.articulos.models import *
from infa_web.apps.base.views import AjaxableResponseMixin
from infa_web.apps.articulos.forms import *

from django.db.models import Max

# Articles #
@csrf_exempt
def SaveBreakdownArticle(request,pk):
	data = json.loads(request.body)
	print type(data)
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

			arlodesglo.save()
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
		print kwargs
		#context['article'] = Arlo.objects.get()
		context['article'] = get_object_or_404(Arlo,carlos=self.kwargs["pk"])
		context["partsArticle"] = Arlosdesglo.objects.filter(carlosp=self.kwargs["pk"])
		return context

class ArticleCreate(CreateView):
	model = Arlo
	template_name = "articulos/article.html"
	form_class = ArticleForm
	success_url=reverse_lazy("add-article")
	success_message = "Articulo creado."
		
	def get_context_data(self, **kwargs):
		context = super(ArticleCreate, self).get_context_data(**kwargs)
		maxCarlos = Arlo.objects.aggregate(Max('carlos'))
		context['title'] = "Crear Articulo"
		context['mode_view'] = 'create'
		context['url'] = 'add-article'

		context['url_foto1'] = DEFAULT_IMAGE_ARTICLE
		context['url_foto2'] = DEFAULT_IMAGE_ARTICLE
		context['url_foto3'] = DEFAULT_IMAGE_ARTICLE

		manageParameters = ManageParameters()
		minCodeArlos = manageParameters.get_param_value("min_code_arlos")
		typeInventory = manageParameters.get_param_value("type_costing_and_stock")
		context['typeInventory'] = typeInventory

		if maxCarlos["carlos__max"]:
			context['current_pk'] = maxCarlos["carlos__max"] + 1
		else:
			context['current_pk'] = minCodeArlos
		return context

@method_decorator(csrf_exempt, name='dispatch')
class ArticleCopy(UpdateView):
	model = Arlo
	template_name = "articulos/article.html"
	form_class = ArticleForm
	success_url=reverse_lazy("add-article")
	success_message = "Articulo creado."
		
	def get_context_data(self, **kwargs):
		context = super(ArticleCopy, self).get_context_data(**kwargs)
		maxCarlos = Arlo.objects.aggregate(Max('carlos'))
		context['title'] = "Copiar Articulo"
		context['mode_view'] = 'copy'
		context['url'] = 'add-article'

		context['url_foto1'] = current_article.foto1
		context['url_foto2'] = current_article.foto2
		context['url_foto3'] = current_article.foto3

		manageParameters = ManageParameters()
		minCodeArlos = manageParameters.get_param_value("min_code_arlos")
		typeInventory = manageParameters.get_param_value("type_costing_and_stock")
		context['typeInventory'] = typeInventory

		if maxCarlos["carlos__max"]:
			context['current_pk'] = maxCarlos["carlos__max"] + 1
		else:
			context['current_pk'] = minCodeArlos
		return context

class ArticleUpdate(UpdateView):
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

		current_article = Arlo.objects.get(pk=self.kwargs["pk"])

		manageParameters = ManageParameters()
		minCodeArlos = manageParameters.get_param_value("min_code_arlos")
		typeInventory = manageParameters.get_param_value("type_costing_and_stock")
		context['typeInventory'] = typeInventory

		context['url_foto1'] = current_article.foto1
		context['url_foto2'] = current_article.foto2
		context['url_foto3'] = current_article.foto3

		return context

class ArticleList(ListView):
	model = Arlo
	template_name = "articulos/list-articles.html"
# Articles #

# Groups #
class GroupCreate(AjaxableResponseMixin,CreateView):
	model = Gpo
	form_class = GpoForm
	template_name = "articulos/group.html"
	success_url=reverse_lazy("add-group")

class GroupUpdate(AjaxableResponseMixin,UpdateView):
	model = Gpo
	form_class = GpoForm
	template_name = "articulos/group.html"
	success_url=reverse_lazy("add-group")
	success_message = "was update successfully"

class GroupList(ListView):
	model = Gpo
	template_name = "articulos/list-groups.html"
# Groups #

# Types Articles #
class TypesArticleCreate(AjaxableResponseMixin,CreateView):
	model = Tiarlos
	form_class = TiarlosForm
	template_name = "articulos/tipe-article.html"
	success_url=reverse_lazy("add-type-article")

class TypesArticleUpdate(AjaxableResponseMixin,UpdateView):
	model = Tiarlos
	form_class = TiarlosForm
	template_name = "articulos/tipe-article.html"
	success_url=reverse_lazy("add-type-article")

class TypesArticleList(ListView):
	model = Tiarlos
	template_name = "articulos/list-types-articles.html"
# Types Articles #

# Brands #
class BrandCreate(AjaxableResponseMixin,CreateView):
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

class BrandUpdate(AjaxableResponseMixin,UpdateView):
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

class BrandsList(ListView):
	model = Marca
	template_name = "articulos/list-brands.html"
# Brands #

# API #
@csrf_exempt
def API_exists(request):
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
		19:{'name':'Timo','app':'inventarios'},
		20:{'name':'Mven','app':'inventarios'},
		21:{'name':'Mvendeta','app':'inventarios'},
		22:{'name':'Mvsa','app':'inventarios'},
		23:{'name':'Mvsadeta','app':'inventarios'},
		24:{'name':'Autorre','app':'terceros'},
		25:{'name':'Vende','app':'terceros'},
		26:{'name':'Ruta','app':'terceros'},
		27:{'name':'Personas','app':'terceros'},
		28:{'name':'Zona','app':'terceros'},
		29:{'name':'Tercero','app':'terceros'},
	}

	#print codeModels[1]["app"]
	#return JsonResponse({'exists':True})

	data = json.loads(request.body)
	model = apps.get_model(app_label=codeModels[data["model"]]["app"],model_name=codeModels[data["model"]]["name"])
	print "app_label="+codeModels[data["model"]]["app"]
	print "model_name="+codeModels[data["model"]]["name"]
	#model = apps.get_model(app_label="articulos",model_name="Arlo")


	filter_dict = {}
	filter_dict[data["field"]] = data["value"]
	print (filter_dict)
	print type(filter_dict)
	if model.objects.filter(**filter_dict).exists():
		return JsonResponse({'exists':True})
	else:
		return JsonResponse({'exists':False})

# API #
