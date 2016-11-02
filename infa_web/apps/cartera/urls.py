from django.conf.urls import patterns, include, url
from infa_web.apps.cartera.views import *

from django.contrib.auth.decorators import login_required

#url(r'^cartera/payment/$', login_required(PaymentCreate.as_view()), name = 'create-payment'),
url = [
	url(r'^cartera/payment/$', PaymentCreate.as_view(), name = 'view-create-payment'),
	url(r'^cartera/payment/(?P<pk>\d+)/$', PaymentEdit.as_view(), name = 'view-update-payment'),
	url(r'^cartera/payment/save/$', PaymentSave, name = 'save-payment'),
	url(r'^cartera/payment/save/(?P<pk>\d+)/$', PaymentUpdate, name = 'update-payment'),
	
	url(r'^cartera/get_cartera/(?P<citerce>\d+)/$', get_cartera_tercero, name = 'get-cartera-tercero'),
]

urlpatterns = url
