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

urlBrands = [
	url(r'^brands/$', BrandsList.as_view(), {'title': 'Crear Marca'}, name = 'list-brands'),
	url(r'^brands/add/$', BrandCreate.as_view(), {'title': 'Crear Marca'}, name = 'add-brand'),
	url(r'^brands/edit/(?P<pk>[0-9])+/$', BrandUpdate.as_view(), {'title': 'Editar Marca'}, name = 'edit-brand'),
]

urlIva = [
	url(r'^iva/$', IvaList.as_view(), {'title': 'Crear IVA'}, name = 'list-iva'),
	url(r'^iva/add/$', IvaCreate.as_view(), {'title': 'Crear IVA'}, name = 'add-iva'),
	url(r'^iva/edit/(?P<pk>[0-9])+/$', IvaUpdate.as_view(), {'title': 'Editar IVA'}, name = 'edit-iva'),
]

urlRegiva = [
	url(r'^reg-iva/$', RegIvasList.as_view(), {'title': 'Crear Regimen de Iva'}, name = 'list-reg-iva'),
	url(r'^reg-iva/add/$', RegIvaCreate.as_view(), {'title': 'Crear Regimen de Iva'}, name = 'add-reg-iva'),
	url(r'^reg-iva/edit/(?P<pk>[0-9])+/$', RegIvaUpdate.as_view(), {'title': 'Editar Regimen de Iva'}, name = 'edit-reg-iva'),
]

urlpatterns = urlGeneral + urlStates + urlCities + urlDepartaments + urlLocations + urlBrands + urlIva + urlRegiva
