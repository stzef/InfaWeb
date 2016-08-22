from django.conf.urls import patterns, include, url
from infa_web.apps.inventarios.views import *
 
urlpatterns = [
	url(r'^inventory/$', InventoryView.as_view(), name = 'inventory'),
	url(r'^inventory/list/$', InventoryListView.as_view(), name = 'inventory_list'),
	url(r'^inventory/last/$', inventory_latest, name = 'inventory_latest'),
	url(r'^inventory/edit/$', inventory_edit, name = 'inventory_edit'),
	url(r'^inventory/rename/$', get_name_arlo, name = 'get_name_arlo'),
	url(r'^inventory/save/$', inventory_save, name = 'inventory_save'),
]
