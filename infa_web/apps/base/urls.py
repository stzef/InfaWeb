from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from infa_web.apps.base.views import *

urlGeneral = [
	url(r'^$', TemplateView.as_view(template_name = 'home/dashboard.html'), {'title': 'Inicio'}, name = 'dashboard'),
]

urlStates = [
	url(r'^states/$', StatesList.as_view(), {'title': 'Crear Estado'}, name = 'list-states'),
	url(r'^states/add/$', StateCreate.as_view(), {'title': 'Crear Estado'}, name = 'add-state'),
	url(r'^states/edit/(?P<pk>[0-9])/$', StateUpdate.as_view(), {'title': 'Editar Estado'}, name = 'edit-state'),
]

urlCities = [
	url(r'^cities/$', CitiesList.as_view(), {'title': 'Crear Ciudad'}, name = 'list-cities'),
	url(r'^cities/add/$', CityCreate.as_view(), {'title': 'Crear Ciudad'}, name = 'add-city'),
	url(r'^cities/edit/(?P<pk>[0-9])/$', CityUpdate.as_view(), {'title': 'Editar Ciudad'}, name = 'edit-city'),
]

urlDepartaments = [
	url(r'^departaments/$', DepartamentsList.as_view(), {'title': 'Crear Departamento'}, name = 'list-departaments'),
	url(r'^departaments/add/$', DepartamentCreate.as_view(), {'title': 'Crear Departamento'}, name = 'add-departament'),
	url(r'^departaments/edit/(?P<pk>[0-9])/$', DepartamentUpdate.as_view(), {'title': 'Editar Departamento'}, name = 'edit-departament'),
]

urlLocations = [
	url(r'^locations/$', LocationsList.as_view(), {'title': 'Crear Ubicacion'}, name = 'list-locations'),
	url(r'^locations/add/$', LocationCreate.as_view(), {'title': 'Crear Ubicacion'}, name = 'add-location'),
	url(r'^locations/edit/(?P<pk>[0-9])/$', LocationUpdate.as_view(), {'title': 'Editar Ubicacion'}, name = 'edit-location'),
]

urlpatterns = urlGeneral + urlStates + urlCities + urlDepartaments + urlLocations
