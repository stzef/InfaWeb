from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
import json

from django import forms

from infa_web.apps.base.constantes import EMPRESA

from infa_web.apps.articulos.models import *
from infa_web.apps.articulos.forms import *

from django.db.models import Max

# Articles #
@csrf_exempt
def SaveBreakdownArticle(request,pk):
	data = json.loads(request.body)
	print type(data)
	response = {}
	response['data'] = {}
	response['data']['algo'] = data
	return HttpResponse(json.dumps(response), "application/json")

class BreakdownArticle(FormView):
	model = Arlosdesglo
	template_name = 'articulos/breakdown-article.html'
	form_class = BreakdownArticleForm

	def get_context_data(self,**kwargs):
		context = super(BreakdownArticle, self).get_context_data(**kwargs)
		print kwargs
		context['article'] = Arlo.objects.get(carlos=self.kwargs["pk"])
		return context

class ArticleCreate(CreateView):
	model = Arlo
	template_name = "articulos/article.html"
	form_class = ArticleForm
	success_url=reverse_lazy("add-article")
	success_message = "Articulo creado."
	
	def get_context_data(self, **kwargs):
		ctx = super(ArticleCreate, self).get_context_data(**kwargs)
		maxCarlos = Arlo.objects.aggregate(Max('carlos'))
		print maxCarlos
		if maxCarlos["carlos__max"]:
			ctx['pk'] = maxCarlos["carlos__max"] + 1
		else:
			ctx['pk'] = EMPRESA["MIN_CARLOS"]
		return ctx

class ArticleUpdate(UpdateView):
	model = Arlo
	template_name = "articulos/article.html"
	success_url=reverse_lazy("add-article")
	form_class = ArticleForm
	def get_context_data(self, **kwargs):
		ctx = super(ArticleUpdate, self).get_context_data(**kwargs)
		ctx['pk'] = self.kwargs["pk"]
		return ctx

class ArticleList(ListView):
	model = Arlo
	template_name = "articulos/list-articles.html"
# Articles #

# Groups #
class GroupCreate(CreateView):
	model = Gpo
	form_class = GpoForm
	template_name = "articulos/group.html"
	success_url=reverse_lazy("add-group")

class GroupUpdate(UpdateView):
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
class TypesArticleCreate(CreateView):
	model = Tiarlos
	form_class = TiarlosForm
	template_name = "articulos/tipe-article.html"
	success_url=reverse_lazy("add-tipe-article")

class TypesArticleUpdate(UpdateView):
	model = Tiarlos
	form_class = TiarlosForm
	template_name = "articulos/tipe-article.html"
	success_url=reverse_lazy("add-tipe-article")

class TypesArticleList(ListView):
	model = Tiarlos
	template_name = "articulos/list-groups.html"
# Types Articles #
