from django.conf.urls import patterns, include, url
from infa_web.apps.movimientos.views import *

urlInputMovement = [
	url(r'^input-movement/$', InputMovementList.as_view(), name = 'list-input-movements'),
	url(r'^output-movement/$', OutputMovementList.as_view(), name = 'list-output-movements'),

	url(r'^output-movement/add/$', OutputMovementCreate.as_view(), name = 'add-output-movement'),
	url(r'^input-movement/add/$', InputMovementCreate.as_view(), name = 'add-input-movement'),

	url(r'^output-movement/edit/(?P<pk>\d+)/$', OutputMovementUpdate.as_view(), name = 'edit-output-movement'),
	url(r'^input-movement/edit/(?P<pk>\d+)/$', InputMovementUpdate.as_view(), name = 'edit-input-movement'),

	url(r'^movement/save/$', SaveMovement, name='save-movement'),
	url(r'^movement/edit/(?P<pk>\d+)/$', UpdateMovement, name='edit-movement'),

	url(r'^proccess/fn/costing_and_stock/$', proccess_fn_costing_and_stock, name='proccess_fn_costing_and_stock'),
	url(r'^proccess/view/costing_and_stock/$', proccess_view_costing_and_stock, name='proccess_view_costing_and_stock'),
	
	url(r'^proccess/fn/annulment/(?P<pk>\d+)/$', proccess_fn_annulment, name='proccess_fn_annulment'),
	url(r'^proccess/view/annulment/$', proccess_view_annulment, name='proccess_view_annulment'),
]

urlpatterns = urlInputMovement
