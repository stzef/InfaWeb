from django.conf.urls import patterns, include, url
from infa_web.apps.terceros.views import *

from django.contrib.auth.decorators import login_required

urlThirdParty = [
	url(r'^third-parties/$', login_required(ThirdPartyList.as_view()), {'title': 'Crear Tercero'}, name = 'list-third-parties'),
	url(r'^third-parties/add/$', login_required(ThirdPartyCreate.as_view()), {'title': 'Crear Tercero'}, name = 'add-third-party'),
	url(r'^third-parties/edit/(?P<pk>\d+)/$', login_required(ThirdPartyUpdate.as_view()), {'title': 'Editar Tercero'}, name = 'edit-third-party'),
]

urlAutorretenedor = [
	url(r'^autorretenedor/$', login_required(AutorrtenedorList.as_view()), name = 'list-autorretenedor'),
	url(r'^autorretenedor/add/$', login_required(AutorrtenedorCreate.as_view()), name = 'add-autorretenedor'),
	url(r'^autorretenedor/edit/(?P<pk>\d+)/$', login_required(AutorrtenedorUpdate.as_view()), name = 'edit-autorretenedor'),
]

urlRoute = [
	url(r'^routes/$', login_required(RoutesList.as_view()), name = 'list-routes'),
	url(r'^routes/add/$', login_required(RouteCreate.as_view()), name = 'add-route'),
	url(r'^routes/edit/(?P<pk>\d+)/$', login_required(RouteUpdate.as_view()), name = 'edit-route'),
]
urlZone = [
	url(r'^zones/$', login_required(ZonesList.as_view()), name = 'list-zones'),
	url(r'^zones/add/$', login_required(ZoneCreate.as_view()), name = 'add-zone'),
	url(r'^zones/edit/(?P<pk>\d+)/$', login_required(ZoneUpdate.as_view()), name = 'edit-zone'),
]

urlpatterns = urlThirdParty + urlAutorretenedor + urlRoute + urlZone
