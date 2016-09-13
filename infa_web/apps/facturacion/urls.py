from django.conf.urls import patterns, include, url
from infa_web.apps.facturacion.views import *

url = [
	url(r'^bill/billing/$', BillCreate.as_view(), name = 'create-bill'),
	url(r'^bill/save/$', BillSave, name = 'save-bill'),
]

urlpatterns = url
