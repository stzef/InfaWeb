from django.conf.urls import patterns, include, url
from infa_web.apps.movimientos.views import *

from django.contrib.auth.decorators import login_required

urlInputMovement = [
	url(r'^input-movement/$', login_required(InputMovementList.as_view()), name = 'list-input-movements'),
	url(r'^output-movement/$', login_required(OutputMovementList.as_view()), name = 'list-output-movements'),

	url(r'^output-movement/add/$', login_required(OutputMovementCreate.as_view()), name = 'add-output-movement'),
	url(r'^input-movement/add/$', login_required(InputMovementCreate.as_view()), name = 'add-input-movement'),

	url(r'^output-movement/edit/(?P<pk>\d+)/$', login_required(OutputMovementUpdate.as_view()), name = 'edit-output-movement'),
	url(r'^input-movement/edit/(?P<pk>\d+)/$', login_required(InputMovementUpdate.as_view()), name = 'edit-input-movement'),

	url(r'^movement/save/$', login_required(SaveMovement), name='save-movement'),
	url(r'^movement/edit/(?P<pk>\d+)/$', login_required(UpdateMovement), name='edit-movement'),

	url(r'^proccess/fn/costing_and_stock/$', login_required(proccess_fn_costing_and_stock), name='proccess_fn_costing_and_stock'),
	url(r'^proccess/view/costing_and_stock/$', login_required(proccess_view_costing_and_stock), name='proccess_view_costing_and_stock'),
	
	url(r'^proccess/fn/annulment/(?P<pk>\d+)/$', login_required(proccess_fn_annulment), name='proccess_fn_annulment'),
	url(r'^proccess/view/annulment/$', login_required(proccess_view_annulment), name='proccess_view_annulment'),
]

urlpatterns = urlInputMovement
