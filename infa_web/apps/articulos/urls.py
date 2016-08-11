from django.conf.urls import patterns, include, url
from infa_web.apps.articulos.views import *

urlArticles = [
	url(r'^articles/$', ArticleList.as_view(), {'title': 'Crear Articulos'}, name = 'list-article'),
	url(r'^articles/add/$', ArticleCreate.as_view(), {'title': 'Crear Articulos'}, name = 'add-article'),
	url(r'^articles/edit/(?P<pk>\d+)/$', ArticleUpdate.as_view(), {'title': 'Editar Articulos'}, name = 'edit-article'),
]
urlGroups = [
	url(r'^groups/$', GroupList.as_view(), {'title': 'Crear Grupo'}, name = 'list-group'),
	url(r'^groups/add/$', GroupCreate.as_view(), {'title': 'Crear Grupo'}, name = 'add-group'),
	url(r'^group/edit/(?P<pk>[0-9])+/$', GroupUpdate.as_view(), {'title': 'Editar Grupo'}, name = 'edit-group'),
]


urlpatterns = urlArticles + urlGroups
