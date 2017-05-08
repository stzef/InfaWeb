from django.conf.urls import patterns, include, url
from infa_web.apps.POS.views import *

from django.contrib.auth.decorators import login_required

#url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
url = [
	url(r'^pos/$', login_required(BillCreate.as_view()), name = 'create-pos'),
	url(r'^pos/print$', login_required(BillPrint), name = 'pint-pos'),
	url(r'^pos/list/$', login_required(BillList.as_view()), name = 'list-pos-bill'),

]

urlpatterns = url
