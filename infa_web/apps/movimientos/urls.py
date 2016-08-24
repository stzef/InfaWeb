from django.conf.urls import patterns, include, url
from infa_web.apps.movimientos.views import *

urlInputMovement = [
	url(r'^output-movement/add/$', OutputMovementCreate.as_view(), name = 'add-output-movements'),

	url(r'^input-movement/$', InputMovementList.as_view(), name = 'list-input-movements'),
	url(r'^input-movement/add/$', InputMovementCreate.as_view(), name = 'add-input-movement'),
	url(r'^input-movement/edit/(?P<pk>\d+)/$', InputMovementUpdate, name = 'edit-input-movement'),
]

urlpatterns = urlInputMovement
