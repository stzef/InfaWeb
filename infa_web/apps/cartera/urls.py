from django.conf.urls import patterns, include, url
from infa_web.apps.cartera.views import *

from django.contrib.auth.decorators import login_required

#url(r'^cartera/payment/$', login_required(PaymentCreate.as_view()), name = 'create-payment'),
url = [
	url(r'^cartera/payment/$', PaymentCreate.as_view(), name = 'create-payment'),
]

urlpatterns = url
