from django.conf.urls import include, url
from django.views.generic import TemplateView
from infa_web.apps.base.views import *

from django.contrib.auth.decorators import login_required,permission_required
#url(r'^$', login_required(dashboard), name = 'dashboard'),

urlGeneral = [
	url(r'^$', TemplateView.as_view(template_name = 'home/index.html'), {'title': 'Inicio'}, name = 'inicio'),

	#url(r'^$', dashboard, name = 'dashboard'),
	url(r'^dashboard/$',login_required(dashboard), name = 'dashboard'),

	url(r'^send_email_get_demo/$',send_email_get_demo, name = 'send_email_get_demo'),

	url(r'^general/defaults/$', login_required(defaults), name = 'appem_defaults'),
]

urlStates = [
	url(r'^states/$', permission_required('base.list_esdo')(login_required(StatesList.as_view())), name = 'list-states'),
	url(r'^states/add/$', permission_required('base.add_esdo')(login_required(StateCreate.as_view())), name = 'add-state'),
	url(r'^states/edit/(?P<pk>[0-9]+)/$', permission_required('base.change_esdo')(login_required(StateUpdate.as_view())), name = 'edit-state'),
]

urlCities = [
	url(r'^cities/$', permission_required('base.list_ciudad')(login_required(CitiesList.as_view())), name = 'list-cities'),
	url(r'^cities/add/$', permission_required('base.add_ciudad')(login_required(CityCreate.as_view())), name = 'add-city'),
	url(r'^cities/edit/(?P<pk>[0-9])+/$', permission_required('base.change_ciudad')(login_required(CityUpdate.as_view())), name = 'edit-city'),
]

urlDepartaments = [
	url(r'^departaments/$', permission_required('base.list_departamento')(login_required(DepartamentsList.as_view())), name = 'list-departaments'),
	url(r'^departaments/add/$', permission_required('base.add_departamento')(login_required(DepartamentCreate.as_view())), name = 'add-departament'),
	url(r'^departaments/edit/(?P<pk>[0-9])+/$', permission_required('base.change_departamento')(login_required(DepartamentUpdate.as_view())), name = 'edit-departament'),
]

urlLocations = [
	url(r'^locations/$', permission_required('base.list_bode')(login_required(LocationsList.as_view())), name = 'list-locations'),
	url(r'^locations/add/$', permission_required('base.add_bode')(login_required(LocationCreate.as_view())), name = 'add-location'),
	url(r'^locations/edit/(?P<pk>[0-9])+/$', permission_required('base.change_bode')(login_required(LocationUpdate.as_view())), name = 'edit-location'),
]

urlIva = [
	url(r'^iva/$', permission_required('base.list_iva')(login_required(IvaList.as_view())), name = 'list-iva'),
	url(r'^iva/add/$', permission_required('base.add_iva')(login_required(IvaCreate.as_view())), name = 'add-iva'),
	url(r'^iva/edit/(?P<pk>[0-9])+/$', permission_required('base.change_iva')(login_required(IvaUpdate.as_view())), name = 'edit-iva'),
]

urlRegiva = [
	url(r'^reg-iva/$', permission_required('base.list_regiva')(login_required(RegIvasList.as_view())), name = 'list-reg-iva'),
	url(r'^reg-iva/add/$', permission_required('base.add_regiva')(login_required(RegIvaCreate.as_view())), name = 'add-reg-iva'),
	url(r'^reg-iva/edit/(?P<pk>[0-9])+/$', permission_required('base.change_regiva')(login_required(RegIvaUpdate.as_view())), name = 'edit-reg-iva'),
]

urlIDTypes = [
	url(r'^id-type/$', permission_required('base.list_tiide')(login_required(IDTypesList.as_view())),name = 'list-id-type'),
	url(r'^id-type/add/$', permission_required('base.add_tiide')(login_required(IDTypeCreate.as_view())),name = 'add-id-type'),
	url(r'^id-type/edit/(?P<pk>[0-9])+/$', permission_required('base.change_tiide')(login_required(IDTypeUpdate.as_view())),name = 'edit-id-type'),
]

urlSucursales = [
	url(r'^branch/$', permission_required('base.list_sucursales')(login_required(BanchsList.as_view())),name = 'list-branchs'),
	url(r'^branch/add/$', permission_required('base.add_sucursales')(login_required(BanchCreate.as_view())),name = 'add-branch'),
	url(r'^branch/edit/(?P<pk>[0-9])+/$', permission_required('base.change_sucursales')(login_required(BanchUpdate.as_view())),name = 'edit-branch'),
]

urlTalonarios = [
	url(r'^cheque_book/$', permission_required('base.list_talo')(login_required(ChequeBooksList.as_view())),name = 'list-cheque-books'),
	url(r'^cheque_book/add/$', permission_required('base.add_talo')(login_required(ChequeBookCreate.as_view())),name = 'add-cheque-book'),
	url(r'^cheque_book/edit/(?P<pk>[0-9])+/$', permission_required('base.change_talo')(login_required(ChequeBookUpdate.as_view())),name = 'edit-cheque-book'),
]

urlCajas = [
	url(r'^caja/$', permission_required('base.list_cajas')(login_required(CajasList.as_view())),name = 'list-cajas'),
	url(r'^caja/add/$', permission_required('base.add_cajas')(login_required(CajaCreate.as_view())),name = 'add-caja'),
	url(r'^caja/edit/(?P<pk>[0-9])+/$', permission_required('base.change_cajas')(login_required(CajaUpdate.as_view())),name = 'edit-caja'),
]

urlParameters = [
	url(r'^parameters/$', permission_required('base.list_parameters')(login_required(ParametersList)), name = 'list-parameter'),
	url(r'^parameters/save/$', permission_required('base.save_parameters')(login_required(ParametersSave)), name = 'save-parameters'),
]

urlModels = [
	url(r'^models/find/$', login_required(ModelFind), name = 'model-find'),
	url(r'^models/find-one/$', login_required(ModelFindOne), name = 'model-find-one'),
]

urlpatterns = urlGeneral + urlStates + urlCities + urlDepartaments + urlLocations + urlIva + urlRegiva + urlParameters + urlSucursales + urlTalonarios + urlCajas + urlIDTypes + urlModels
