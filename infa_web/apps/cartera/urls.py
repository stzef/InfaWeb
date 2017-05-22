from django.conf.urls import include, url
from infa_web.apps.cartera.views import *

from django.contrib.auth.decorators import login_required

#url(r'^cartera/payment/$', login_required(PaymentCreate.as_view()), name = 'create-payment'),
url = [
	url(r'^cartera/payment/$', login_required(PaymentCreate.as_view()), name = 'view-create-payment'),
	url(r'^cartera/payment/(?P<pk>\d+)/$', login_required(PaymentEdit.as_view()), name = 'view-update-payment'),
	url(r'^cartera/payment/save/$', login_required(PaymentSave), name = 'save-payment'),
	url(r'^cartera/payment/save/(?P<pk>\d+)/$', login_required(PaymentUpdate), name = 'update-payment'),

	url(r'^cartera/get_cartera/(?P<citerce>\d+)/$', login_required(get_cartera_tercero), name = 'get-cartera-tercero'),
]

urlpatterns = url
