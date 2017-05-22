from django.conf.urls import include, url
from infa_web.apps.facturacion.views import *

from django.contrib.auth.decorators import login_required

#url(r'^bill/billing/$', login_required(BillCreate.as_view()), name = 'create-bill'),
url = [
	url(r'^bill/billing/$', login_required(BillCreate.as_view()), name = 'create-bill'),
	url(r'^bill/billing/(?P<pk>\d+)/$', login_required(BillEdit.as_view()), name = 'edit-bill'),

	url(r'^bill/list/$', login_required(BillList.as_view()), name = 'list-bill'),

	url(r'^bill/save/$', login_required(BillSave), name = 'save-bill'),
	url(r'^bill/save/(?P<pk>\d+)/$', login_required(BillUpdate), name = 'update-bill'),

	url(r'^bill/print/$', login_required(BillPrint.as_view()), name = 'print-bill'),

	url(r'^bill/proccess/fn/annulment$', login_required(bill_proccess_fn_annulment), name = 'bill_proccess_fn_annulment'),
	url(r'^bill/proccess/view/annulment$', login_required(bill_proccess_view_annulment), name = 'bill_proccess_view_annulment'),

	url(r'^bill/reports/fn/ventas$', login_required(report_fn_bill.as_view()), name = 'report_fn_bill'),
	url(r'^bill/reports/view/ventas$', login_required(report_view_bill), name = 'report_view_bill'),

	url(r'^bill/reports/fn/ventas_formas_pago$', login_required(report_fn_bill_payment_methods.as_view()), name = 'report_fn_bill_payment_methods'),
	url(r'^bill/reports/view/ventas_formas_pago$', login_required(report_view_bill_payment_methods), name = 'report_view_bill_payment_methods'),
]

urlpatterns = url
