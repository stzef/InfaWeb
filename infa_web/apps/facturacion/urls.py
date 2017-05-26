from django.conf.urls import patterns, include, url
from infa_web.apps.facturacion.views import *

from django.contrib.auth.decorators import login_required,permission_required

#url(r'^bill/billing/$', login_required(BillCreate.as_view()), name = 'create-bill'),
url = [
	url(r'^bill/billing/$', permission_required('facturacion.add_fac')(login_required(BillCreate.as_view())), name = 'create-bill'),
	url(r'^bill/billing/(?P<pk>\d+)/$', permission_required('facturacion.change_fac')(login_required(BillEdit.as_view())), name = 'edit-bill'),

	url(r'^bill/list/$', permission_required('facturacion.list_fac')(login_required(BillList.as_view())), name = 'list-bill'),

	url(r'^bill/save/$', permission_required('facturacion.add_fac')(login_required(BillSave)), name = 'save-bill'),
	url(r'^bill/save/(?P<pk>\d+)/$', permission_required('facturacion.change_fac')(login_required(BillUpdate)), name = 'update-bill'),

	url(r'^bill/print/$', permission_required('facturacion.print_fac')(login_required(BillPrint.as_view())), name = 'print-bill'),

	url(r'^bill/proccess/fn/annulment$', permission_required('facturacion.change_fac')(login_required(bill_proccess_fn_annulment)), name = 'bill_proccess_fn_annulment'),
	url(r'^bill/proccess/view/annulment$', permission_required('facturacion.change_fac')(login_required(bill_proccess_view_annulment)), name = 'bill_proccess_view_annulment'),

	url(r'^bill/reports/fn/ventas$', permission_required('facturacion.add_fac')(login_required(report_fn_bill.as_view())), name = 'report_fn_bill'),
	url(r'^bill/reports/view/ventas$', permission_required('facturacion.add_fac')(login_required(report_view_bill)), name = 'report_view_bill'),
	url(r'^bill/send/$',login_required(send_email), name="send_email"),
	url(r'^bill/reports/fn/ventas_formas_pago$', permission_required('facturacion.add_fac')(login_required(report_fn_bill_payment_methods.as_view())), name = 'report_fn_bill_payment_methods'),
	url(r'^bill/reports/view/ventas_formas_pago$', permission_required('facturacion.add_fac')(login_required(report_view_bill_payment_methods)), name = 'report_view_bill_payment_methods'),
]

urlpatterns = url
