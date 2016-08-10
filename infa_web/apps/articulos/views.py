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
	success_url=reverse_lazy("add-article")
	exclude = ["citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3"]
	success_message = "Articuo creado."

class ArticleUpdate(UpdateView):
	model = Arlo
	template_name = "articulos/article.html"
	form = Article
	fields = "__all__"
	exclude = ["citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3"]

class ArticleList(ListView):
	model = Arlo
	template_name = "articulos/list-articles.html"

class GroupCreate(CreateView):
	model = Gpo
	template_name = "articulos/group.html"
	form = Article
	fields = "__all__"
	success_url=reverse_lazy("add-group")
	exclude = ["citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3"]

class GroupUpdate(UpdateView):
	model = Gpo
	template_name = "articulos/group.html"
	form = Article
	fields = "__all__"
	exclude = ["citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3"]

class GroupList(ListView):
	model = Gpo
	template_name = "articulos/list-groups.html"
