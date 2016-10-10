from django.conf.urls import patterns, include, url
from infa_web.apps.facturacion.views import *

from django.contrib.auth.decorators import login_required

#url(r'^bill/billing/$', login_required(BillCreate.as_view()), name = 'create-bill'),
url = [
	url(r'^bill/billing/$', BillCreate.as_view(), name = 'create-bill'),
	url(r'^bill/billing/(?P<pk>\d+)/$', BillEdit.as_view(), name = 'edit-bill'),

	url(r'^bill/list/$', BillList.as_view(), name = 'list-bill'),

	url(r'^bill/save/$', BillSave, name = 'save-bill'),
	url(r'^bill/save/(?P<pk>\d+)/$', BillUpdate, name = 'update-bill'),
	
	url(r'^bill/print/$', BillPrint.as_view(), name = 'print-bill'),

	url(r'^bill/proccess/fn/annulment$', bill_proccess_fn_annulment, name = 'bill_proccess_fn_annulment'),
	url(r'^bill/proccess/view/annulment$', bill_proccess_view_annulment, name = 'bill_proccess_view_annulment'),
]

urlpatterns = url
