from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from infa_web.apps.base.views import *

from django.contrib.auth.decorators import login_required
#url(r'^$', login_required(dashboard), name = 'dashboard'),

urlGeneral = [
	url(r'^$', TemplateView.as_view(template_name = 'home/index.html'), {'title': 'Inicio'}, name = 'inicio'),

	#url(r'^$', dashboard, name = 'dashboard'),
	url(r'^dashboard/$', login_required(dashboard), name = 'dashboard'),

	url(r'^general/defaults/$', login_required(defaults), name = 'appem_defaults'),
]

urlStates = [
	url(r'^states/$', login_required(StatesList.as_view()), name = 'list-states'),
	url(r'^states/add/$', login_required(StateCreate.as_view()), name = 'add-state'),
	url(r'^states/edit/(?P<pk>[0-9]+)/$', login_required(StateUpdate.as_view()), name = 'edit-state'),
]

urlCities = [
	url(r'^cities/$', login_required(CitiesList.as_view()), name = 'list-cities'),
	url(r'^cities/add/$', login_required(CityCreate.as_view()), name = 'add-city'),
	url(r'^cities/edit/(?P<pk>[0-9])+/$', login_required(CityUpdate.as_view()), name = 'edit-city'),
]

urlDepartaments = [
	url(r'^departaments/$', login_required(DepartamentsList.as_view()), name = 'list-departaments'),
	url(r'^departaments/add/$', login_required(DepartamentCreate.as_view()), name = 'add-departament'),
	url(r'^departaments/edit/(?P<pk>[0-9])+/$', login_required(DepartamentUpdate.as_view()), name = 'edit-departament'),
]

urlLocations = [
	url(r'^locations/$', login_required(LocationsList.as_view()), name = 'list-locations'),
	url(r'^locations/add/$', login_required(LocationCreate.as_view()), name = 'add-location'),
	url(r'^locations/edit/(?P<pk>[0-9])+/$', login_required(LocationUpdate.as_view()), name = 'edit-location'),
]

urlIva = [
	url(r'^iva/$', login_required(IvaList.as_view()), name = 'list-iva'),
	url(r'^iva/add/$', login_required(IvaCreate.as_view()), name = 'add-iva'),
	url(r'^iva/edit/(?P<pk>[0-9])+/$', login_required(IvaUpdate.as_view()), name = 'edit-iva'),
]

urlRegiva = [
	url(r'^reg-iva/$', login_required(RegIvasList.as_view()), name = 'list-reg-iva'),
	url(r'^reg-iva/add/$', login_required(RegIvaCreate.as_view()), name = 'add-reg-iva'),
	url(r'^reg-iva/edit/(?P<pk>[0-9])+/$', login_required(RegIvaUpdate.as_view()), name = 'edit-reg-iva'),
]

urlIDTypes = [
	url(r'^id-type/$', login_required(IDTypesList.as_view()),name = 'list-id-type'),
	url(r'^id-type/add/$', login_required(IDTypeCreate.as_view()),name = 'add-id-type'),
	url(r'^id-type/edit/(?P<pk>[0-9])+/$', login_required(IDTypeUpdate.as_view()),name = 'edit-id-type'),
]

urlSucursales = [
	url(r'^branch/$', login_required(BanchsList.as_view()),name = 'list-branchs'),
	url(r'^branch/add/$', login_required(BanchCreate.as_view()),name = 'add-branch'),
	url(r'^branch/edit/(?P<pk>[0-9])+/$', login_required(BanchUpdate.as_view()),name = 'edit-branch'),
]

urlParameters = [
	url(r'^parameters/$', login_required(ParametersList), name = 'list-parameter'),
	url(r'^parameters/save/$', login_required(ParametersSave), name = 'save-parameters'),
]

urlModels = [
	url(r'^models/find/$', login_required(ModelFind), name = 'model-find'),
	url(r'^models/find-one/$', login_required(ModelFindOne), name = 'model-find-one'),
]

urlpatterns = urlGeneral + urlStates + urlCities + urlDepartaments + urlLocations + urlIva + urlRegiva + urlParameters + urlSucursales + urlIDTypes + urlModels
