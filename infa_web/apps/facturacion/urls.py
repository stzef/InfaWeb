from django.conf.urls import patterns, include, url
from infa_web.apps.facturacion.views import *

from django.contrib.auth.decorators import login_required

url = [
	url(r'^bill/billing/$', login_required(BillCreate.as_view()), name = 'create-bill'),
	url(r'^bill/billing/(?P<pk>\d+)/$', login_required(BillEdit.as_view()), name = 'edit-bill'),

	url(r'^bill/list/$', login_required(BillList.as_view()), name = 'list-bill'),

	url(r'^bill/save/$', login_required(BillSave), name = 'save-bill'),
	url(r'^bill/save/(?P<pk>\d+)/$', login_required(BillUpdate), name = 'update-bill'),
	
	url(r'^bill/print/$', login_required(BillPrint.as_view()), name = 'print-bill'),

	url(r'^bill/proccess/fn/annulment$', login_required(bill_proccess_fn_annulment), name = 'bill_proccess_fn_annulment'),
	url(r'^bill/proccess/view/annulment$', login_required(bill_proccess_view_annulment), name = 'bill_proccess_view_annulment'),
]

urlpatterns = url
