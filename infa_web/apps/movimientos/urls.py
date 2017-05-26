from django.conf.urls import include, url
from .views import *

from django.contrib.auth.decorators import login_required,permission_required

#url(r'^input-movement/$', login_required(InputMovementList.as_view()), name = 'list-input-movements'),
urlInputMovement = [
	url(r'^input-movement/$', permission_required('movimientos.list_mven')(login_required(InputMovementList.as_view())), name = 'list-input-movements'),
	url(r'^output-movement/$', permission_required('movimientos.list_mvsa')(login_required(OutputMovementList.as_view())), name = 'list-output-movements'),
	url(r'^cartera/$', permission_required('movimientos.add_movi')(login_required(CarteraList.as_view())), name = 'list-cartera'),
	url(r'^cartera/detalle/(?P<pk>\d+)/$', permission_required('movimientos.add_movi')(login_required(CarteraDetalle.as_view())), name = 'detail-cartera'),

	url(r'^output-movement/add/$', permission_required('movimientos.add_mven')(login_required(OutputMovementCreate.as_view())), name = 'add-output-movement'),
	url(r'^input-movement/add/$', permission_required('movimientos.add_mvsa')(login_required(InputMovementCreate.as_view())), name = 'add-input-movement'),

	url(r'^output-movement/edit/(?P<pk>\d+)/$', permission_required('movimientos.change_mven')(login_required(OutputMovementUpdate.as_view())), name = 'edit-output-movement'),
	url(r'^input-movement/edit/(?P<pk>\d+)/$', permission_required('movimientos.change_mvsa')(login_required(InputMovementUpdate.as_view())), name = 'edit-input-movement'),

	url(r'^movement/save/$', permission_required('movimientos.add_movi')(login_required(SaveMovement)), name='save-movement'),
	url(r'^movement/edit/(?P<pk>\d+)/$', permission_required('movimientos.change_movi')(login_required(UpdateMovement)), name='edit-movement'),

	url(r'^proccess/fn/costing_and_stock/$', permission_required('movimientos.change_movi')(login_required(proccess_fn_costing_and_stock)), name='proccess_fn_costing_and_stock'),
	url(r'^proccess/view/costing_and_stock/$', permission_required('movimientos.change_movi')(login_required(proccess_view_costing_and_stock)), name='proccess_view_costing_and_stock'),

	url(r'^proccess/fn/annulment/(?P<pk>\d+)/$', permission_required('movimientos.change_movi')(login_required(proccess_fn_annulment)), name='proccess_fn_annulment'),
	url(r'^proccess/view/annulment/$', permission_required('movimientos.change_movi')(login_required(proccess_view_annulment)), name='proccess_view_annulment'),
]

urlpatterns = urlInputMovement
