# -*- encoding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
import json

from django import forms

from infa_web.apps.base.constantes import EMPRESA

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

		print maxCarlos
		if maxCarlos["carlos__max"]:
			context['current_pk'] = maxCarlos["carlos__max"] + 1
		else:
			context['current_pk'] = EMPRESA["MIN_CARLOS"]
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
	template_name = "articulos/list-groups.html"
# Types Articles #
