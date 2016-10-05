from django.conf.urls import patterns, include, url
from infa_web.apps.inventarios.views import *

from django.contrib.auth.decorators import login_required
 
urlpatterns = [
	url(r'^inventory/$', login_required(InventoryView.as_view()), name = 'inventory'),
	url(r'^inventory/list/$', login_required(InventoryListView.as_view()), name = 'inventory_list'),
	url(r'^inventory/last/$', login_required(inventory_latest), name = 'inventory_latest'),
	url(r'^inventory/edit/$', login_required(inventory_edit), name = 'inventory_edit'),
	url(r'^inventory/edit/get-list/$', login_required(articles_list_invini), name = 'articles_list_invini'),
	url(r'^inventory/rename/$', login_required(get_name_arlo), name = 'get_name_arlo'),
	url(r'^inventory/save/$', login_required(inventory_save), name = 'inventory_save'),
	url(r'^inventory/save-extra/$', login_required(inventory_save_extra), name = 'inventory_save_extra'),
	url(r'^inventory/report/$', login_required(InventoryReport.as_view()), name = 'inventory_report'),
	url(r'^inventory/pdf/$', login_required(InventoryPDF.as_view()), name = 'inventory_pdf'),
	url(r'^inventory/stocks/report/$', login_required(InventoryReportStocks.as_view()), name = 'inventory_stocks_report'),
	url(r'^inventory/stocks/pdf/$', login_required(InventoryPDFStocks.as_view()), name = 'inventory_stocks_pdf'),
]
