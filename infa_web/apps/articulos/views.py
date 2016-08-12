from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django import forms

from infa_web.apps.articulos.models import *
from infa_web.apps.articulos.forms import *

# Articles #
class ArticleCreate(CreateView):
	model = Arlo
	template_name = "articulos/article.html"
	form_class = ArticleForm
	success_url=reverse_lazy("add-article")
	success_message = "Articulo creado."

class ArticleUpdate(UpdateView):
	model = Arlo
	template_name = "articulos/article.html"
	form_class = ArticleForm

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

class GroupList(ListView):
	model = Gpo
	template_name = "articulos/list-groups.html"
# Groups #
