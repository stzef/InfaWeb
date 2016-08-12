from django.conf.urls import patterns, include, url
from infa_web.apps.terceros.views import *

urlThirdParty = [
	url(r'^third-parties/$', ThirdPartyList.as_view(), {'title': 'Crear Tercero'}, name = 'list-third-parties'),
	url(r'^third-parties/add/$', ThirdPartyCreate.as_view(), {'title': 'Crear Tercero'}, name = 'add-third-party'),
	url(r'^third-parties/edit/(?P<pk>\d+)/$', ThirdPartyUpdate.as_view(), {'title': 'Editar Tercero'}, name = 'edit-third-party'),
]

urlpatterns = urlThirdParty
