from django.conf.urls import patterns, include, url
from infa_web.apps.inventarios.views import *
 
urlpatterns = [
	url(r'^inventory/$', InventoryView.as_view(), name = 'inventory'),
	url(r'^inventory/list/$', InventoryListView.as_view(), name = 'inventory_list'),
	url(r'^inventory/last/$', inventory_latest, name = 'inventory_latest'),
	url(r'^inventory/edit/$', inventory_edit, name = 'inventory_edit'),
	url(r'^inventory/edit/get-list/$', articles_list_invini, name = 'articles_list_invini'),
	url(r'^inventory/rename/$', get_name_arlo, name = 'get_name_arlo'),
	url(r'^inventory/save/$', inventory_save, name = 'inventory_save'),
	url(r'^inventory/save-extra/$', inventory_save_extra, name = 'inventory_save_extra'),
	url(r'^inventory/report/$', InventoryReport.as_view(), name = 'inventory_report'),
	url(r'^inventory/pdf/$', InventoryPDF.as_view(), name = 'inventory_pdf'),
	url(r'^inventory/stocks/report/$', InventoryReportStocks.as_view(), name = 'inventory_stocks_report'),
	url(r'^inventory/stocks/pdf/$', InventoryPDFStocks.as_view(), name = 'inventory_stocks_pdf'),
]
