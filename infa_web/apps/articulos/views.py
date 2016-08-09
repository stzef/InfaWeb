from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

from infa_web.apps.articulos.models import *
from infa_web.apps.articulos.forms import *

class ArticleCreate(CreateView):
	model = Arlo
	template_name = "articulos/add-article.html"
	form = Article
	fields = ["carlos","cbarras","cgpo","ncorto","nlargo","canti","vcosto","ifcostear","ifpvfijo","cesdo","ciudad","ivas_civa","stomin","stomax","pvta1","pvta2","pvta3","pvta4","pvta5","pvta6","citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3","ifedinom","refe","cmarca","ifdesglo","mesesgara","cubica","porult1","porult2","porult3","porult4","porult5","porult6","foto1","foto2","foto3",]

class ArticleUpdate(UpdateView):
	model = Arlo
	template_name = "articulos/edit-article.html"
	form = Article
	fields = ["carlos","cbarras","cgpo","ncorto","nlargo","canti","vcosto","ifcostear","ifpvfijo","cesdo","ciudad","ivas_civa","stomin","stomax","pvta1","pvta2","pvta3","pvta4","pvta5","pvta6","citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3","ifedinom","refe","cmarca","ifdesglo","mesesgara","cubica","porult1","porult2","porult3","porult4","porult5","porult6","foto1","foto2","foto3",]

class ArticleDelete(DeleteView):
	model = Arlo
	success_url = reverse_lazy('add-article')
	template_name = "articulos/delete-article.html"

class ArticleList(DeleteView):
	model = Arlo
	success_url = reverse_lazy('add-article')
	template_name = "articulos/delete-article.html"

class ArticleList(ListView):
	model = Arlo
	template_name = "articulos/list-articles.html"

	def get_context_data(self, **kwargs):
		context = super(ArticleList, self).get_context_data(**kwargs)
		context['now'] = "now"
		return context
