from django.conf.urls import patterns, include, url
from infa_web.apps.articulos.views import *

urlArticles = [
	url(r'^articles/$', ArticleList.as_view(), {'title': 'Crear Articulos'}, name = 'list-articles'),
	url(r'^articles/add/$', ArticleCreate.as_view(), {'title': 'Crear Articulos'}, name = 'add-article'),
	url(r'^articles/edit/(?P<pk>\d+)/$', ArticleUpdate.as_view(), {'title': 'Editar Articulos'}, name = 'edit-article'),
]

urlBreakdownArticles = [
	url(r'^articles/(?P<pk>\d+)/breakdown$', BreakdownArticle.as_view(), {'title': 'Desglozar Articulos'}, name = 'breakdown-article'),
	url(r'^articles/(?P<pk>\d+)/breakdown/save$', SaveBreakdownArticle, name = 'breakdown-article-save'),
]
urlGroups = [
	url(r'^groups/$', GroupList.as_view(), {'title': 'Crear Grupo'}, name = 'list-group'),
	url(r'^groups/add/$', GroupCreate.as_view(), {'title': 'Crear Grupo'}, name = 'add-group'),
	url(r'^groups/edit/(?P<pk>[0-9])+/$', GroupUpdate.as_view(), {'title': 'Editar Grupo'}, name = 'edit-group'),
]

urlTypesArticles = [
	url(r'^types-articles/$', TypesArticleList.as_view(), {'title': 'Crear Tipo de Articulo'}, name = 'list-types-articles'),
	url(r'^types-articles/add/$', TypesArticleCreate.as_view(), {'title': 'Crear Tipo de Articulo'}, name = 'add-type-article'),
	url(r'^types-articles/edit/(?P<pk>[0-9])+/$', TypesArticleUpdate.as_view(), {'title': 'Editar Tipo de Articulo'}, name = 'edit-type-article'),
]

urlpatterns = urlArticles + urlGroups + urlTypesArticles + urlBreakdownArticles
