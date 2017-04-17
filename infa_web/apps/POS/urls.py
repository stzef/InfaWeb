from django.conf.urls import patterns, include, url
from infa_web.apps.POS.views import *

from django.contrib.auth.decorators import login_required

#url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
url = [
	url(r'^pos/$', login_required(BillCreate.as_view()), name = 'pos'),
	url(r'^some_view/$', login_required(some_view), name = 'some_view'),
]

urlpatterns = url
