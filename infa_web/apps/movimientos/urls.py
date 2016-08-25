from django.conf.urls import patterns, include, url
from infa_web.apps.movimientos.views import *

urlInputMovement = [
	url(r'^input-movement/$', InputMovementList.as_view(), name = 'list-input-movements'),

	url(r'^output-movement/add/$', OutputMovementCreate.as_view(), name = 'add-output-movements'),
	url(r'^input-movement/add/$', InputMovementCreate.as_view(), name = 'add-input-movement'),

	url(r'^movement/save/$', SaveMovement, name='save-movement'),
]

urlpatterns = urlInputMovement
