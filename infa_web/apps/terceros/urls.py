from django.conf.urls import patterns, include, url
from infa_web.apps.terceros.views import *

from django.contrib.auth.decorators import login_required

#url(r'^third-parties/$', login_required(ThirdPartyList.as_view()), {'title': 'Crear Tercero'}, name = 'list-third-parties'),
urlThirdParty = [
	url(r'^third-parties/$', ThirdPartyList.as_view(), {'title': 'Crear Tercero'}, name = 'list-third-parties'),
	url(r'^third-parties/add/$', ThirdPartyCreate.as_view(), {'title': 'Crear Tercero'}, name = 'add-third-party'),
	url(r'^third-parties/edit/(?P<pk>\d+)/$', ThirdPartyUpdate.as_view(), {'title': 'Editar Tercero'}, name = 'edit-third-party'),
]

urlAutorretenedor = [
	url(r'^autorretenedor/$', AutorrtenedorList.as_view(), name = 'list-autorretenedor'),
	url(r'^autorretenedor/add/$', AutorrtenedorCreate.as_view(), name = 'add-autorretenedor'),
	url(r'^autorretenedor/edit/(?P<pk>\d+)/$', AutorrtenedorUpdate.as_view(), name = 'edit-autorretenedor'),
]

urlRoute = [
	url(r'^routes/$', RoutesList.as_view(), name = 'list-routes'),
	url(r'^routes/add/$', RouteCreate.as_view(), name = 'add-route'),
	url(r'^routes/edit/(?P<pk>\d+)/$', RouteUpdate.as_view(), name = 'edit-route'),
]
urlZone = [
	url(r'^zones/$', ZonesList.as_view(), name = 'list-zones'),
	url(r'^zones/add/$', ZoneCreate.as_view(), name = 'add-zone'),
	url(r'^zones/edit/(?P<pk>\d+)/$', ZoneUpdate.as_view(), name = 'edit-zone'),
]

urlpatterns = urlThirdParty + urlAutorretenedor + urlRoute + urlZone
