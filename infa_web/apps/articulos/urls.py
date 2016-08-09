from django.conf.urls import patterns, include, url

urlpatterns = patterns('')


from django.conf.urls import patterns, include, url

from infa_web.apps.articulos.views import *

urlpatterns = patterns('',
	url(r'^articles$', ArticleList.as_view(), {'title': 'Crear Articulos'}, name = 'list-article'),
	url(r'^articles/add$', ArticleCreate.as_view(), {'title': 'Crear Articulos'}, name = 'add-article'),
	url(r'^article/edit/(?P<pk>[0-9]{2})$', ArticleUpdate.as_view(), {'title': 'Crear Articulos'}, name = 'edit-article'),
	url(r'^article/delete/(?P<pk>[0-9]{2})$', ArticleDelete.as_view(), {'title': 'Crear Articulos'}, name = 'delete-article'),
)
