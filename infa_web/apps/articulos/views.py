from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

from infa_web.apps.articulos.models import *
from infa_web.apps.articulos.forms import *

class ArticleCreate(CreateView):
	model = Arlo
	template_name = "articulos/article.html"
	form = Article
	fields = "__all__"
	exclude = ["citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3"]

class ArticleUpdate(UpdateView):
	model = Arlo
	template_name = "articulos/article.html"
	form = Article
	fields = "__all__"
	exclude = ["citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3"]

class ArticleList(ListView):
	model = Arlo
	template_name = "articulos/list-articles.html"

	def get_context_data(self, **kwargs):
		context = super(ArticleList, self).get_context_data(**kwargs)
		context['now'] = "now"
		return context
