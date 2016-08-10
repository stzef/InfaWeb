from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('infa_web.apps.inventarios.views',
	url(r'^inventory/$', InventoryView.as_view(), name = 'inventory'),
	url(r'^inventory-last/$', 'inventory_latest', name = 'inventory_latest'),
)