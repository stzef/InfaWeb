from django.conf.urls import patterns, include, url
from infa_web.apps.facturacion.views import *

url = [
	url(r'^bill/billing/$', BillCreate.as_view(), name = 'create-bill'),
	url(r'^bill/save/$', BillSave, name = 'save-bill'),

	url(r'^bill/proccess/fn/annulment$', bill_proccess_fn_annulment, name = 'bill_proccess_fn_annulment'),
	url(r'^bill/proccess/view/annulment$', bill_proccess_view_annulment, name = 'bill_proccess_view_annulment'),
]

urlpatterns = url
