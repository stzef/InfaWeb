from django.conf.urls import patterns, include, url
from infa_web.apps.inventarios.views import *

from django.contrib.auth.decorators import login_required,permission_required

#url(r'^inventory/$', login_required(InventoryView.as_view()), name = 'inventory'),
urlpatterns = [
	url(r'^inventory/$', permission_required('inventarios.add_invinicab')(login_required(InventoryView.as_view())), name = 'inventory'),
	url(r'^inventory/list/$', permission_required('inventarios.list_invinicab')(login_required(InventoryListView.as_view())), name = 'inventory_list'),
	url(r'^inventory/last/$', permission_required('inventarios.add_invinicab')(login_required(inventory_latest)), name = 'inventory_latest'),
	url(r'^inventory/edit/$', permission_required('inventarios.change_invinicab')(login_required(inventory_edit)), name = 'inventory_edit'),
	url(r'^inventory/arlo/$', permission_required('inventarios.add_invinicab')(login_required(find_arlo)), name = 'find_arlo'),
	url(r'^inventory/edit/get-list/$', permission_required('inventarios.add_invinicab')(login_required(articles_list_invini)), name = 'articles_list_invini'),
	url(r'^inventory/rename/$', permission_required('inventarios.add_invinicab')(login_required(get_name_arlo)), name = 'get_name_arlo'),
	url(r'^inventory/save/$', permission_required('inventarios.add_invinicab')(login_required(inventory_save)), name = 'inventory_save'),
	url(r'^inventory/save-extra/$', permission_required('inventarios.add_invinicab')(login_required(inventory_save_extra)), name = 'inventory_save_extra'),
	url(r'^inventory/report/$',permission_required('inventarios.add_invinicab')(login_required(InventoryReport.as_view())), name = 'inventory_report'),
	url(r'^inventory/pdf/$', permission_required('inventarios.add_invinicab')(login_required(InventoryPDF.as_view())), name = 'inventory_pdf'),
	url(r'^inventory/stocks/report/$', permission_required('inventarios.add_invinicab')(login_required(InventoryReportStocks.as_view())), name = 'inventory_stocks_report'),
	url(r'^inventory/stocks/pdf/$', permission_required('inventarios.add_invinicab')(login_required(InventoryPDFStocks.as_view())), name = 'inventory_stocks_pdf'),
]
