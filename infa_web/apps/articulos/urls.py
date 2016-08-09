from django.conf.urls import patterns, include, url

urlpatterns = patterns('')


from django.conf.urls import patterns, include, url

from infa_web.apps.articulos.views import *

urlpatterns = patterns('',
	url(r'^articulos/add$', ArticleCreate.as_view(), {'title': 'Crear Articulos'}, name = 'add-article'),
)
