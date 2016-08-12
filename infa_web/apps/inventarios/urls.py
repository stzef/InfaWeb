from django.conf.urls import patterns, include, url
from infa_web.apps.inventarios.views import *
 
urlpatterns = [
	url(r'^inventory/$', InventoryView.as_view(), name = 'inventory'),
	url(r'^inventory-last/$', inventory_latest, name = 'inventory_latest'),
	url(r'^inventory-save/$', inventory_save, name = 'inventory_save'),
]
