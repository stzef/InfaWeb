from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from infa_web.apps.base.views import *

from django.contrib.auth.decorators import login_required
#url(r'^$', login_required(dashboard), name = 'dashboard'),

urlGeneral = [
	url(r'^$', TemplateView.as_view(template_name = 'home/index.html'), {'title': 'Inicio'}, name = 'inicio'),

	#url(r'^$', dashboard, name = 'dashboard'),
	url(r'^dashboard/$', dashboard, name = 'dashboard'),
]

urlStates = [
	url(r'^states/$', StatesList.as_view(), name = 'list-states'),
	url(r'^states/add/$', StateCreate.as_view(), name = 'add-state'),
	url(r'^states/edit/(?P<pk>[0-9]+)/$', StateUpdate.as_view(), name = 'edit-state'),
]

urlCities = [
	url(r'^cities/$', CitiesList.as_view(), name = 'list-cities'),
	url(r'^cities/add/$', CityCreate.as_view(), name = 'add-city'),
	url(r'^cities/edit/(?P<pk>[0-9])+/$', CityUpdate.as_view(), name = 'edit-city'),
]

urlDepartaments = [
	url(r'^departaments/$', DepartamentsList.as_view(), name = 'list-departaments'),
	url(r'^departaments/add/$', DepartamentCreate.as_view(), name = 'add-departament'),
	url(r'^departaments/edit/(?P<pk>[0-9])+/$', DepartamentUpdate.as_view(), name = 'edit-departament'),
]

urlLocations = [
	url(r'^locations/$', LocationsList.as_view(), name = 'list-locations'),
	url(r'^locations/add/$', LocationCreate.as_view(), name = 'add-location'),
	url(r'^locations/edit/(?P<pk>[0-9])+/$', LocationUpdate.as_view(), name = 'edit-location'),
]

urlIva = [
	url(r'^iva/$', IvaList.as_view(), name = 'list-iva'),
	url(r'^iva/add/$', IvaCreate.as_view(), name = 'add-iva'),
	url(r'^iva/edit/(?P<pk>[0-9])+/$', IvaUpdate.as_view(), name = 'edit-iva'),
]

urlRegiva = [
	url(r'^reg-iva/$', RegIvasList.as_view(), name = 'list-reg-iva'),
	url(r'^reg-iva/add/$', RegIvaCreate.as_view(), name = 'add-reg-iva'),
	url(r'^reg-iva/edit/(?P<pk>[0-9])+/$', RegIvaUpdate.as_view(), name = 'edit-reg-iva'),
]

urlIDTypes = [
	url(r'^id-type/$', IDTypesList.as_view(),name = 'list-id-type'),
	url(r'^id-type/add/$', IDTypeCreate.as_view(),name = 'add-id-type'),
	url(r'^id-type/edit/(?P<pk>[0-9])+/$', IDTypeUpdate.as_view(),name = 'edit-id-type'),
]

urlParameters = [
	url(r'^parameters/$', ParametersList, name = 'list-parameter'),
	url(r'^parameters/save/$', ParametersSave, name = 'save-parameters'),
]

urlModels = [
	url(r'^models/find/$', ModelFind, name = 'model-find'),
	url(r'^models/find-one/$', ModelFindOne, name = 'model-find-one'),
]

urlpatterns = urlGeneral + urlStates + urlCities + urlDepartaments + urlLocations + urlIva + urlRegiva + urlParameters + urlIDTypes + urlModels
