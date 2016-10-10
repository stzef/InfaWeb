from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from infa_web.apps.m.views import *

url = [
	url(r'^m/dashboard$', mDashboard, name='m_dashboard'),
	url(r'^m/choose-client$', mFacChooseClient, name='m_choose_client'),
	url(r'^m/search-client$', mFacSearchClient, name='m_search_client'),
	url(r'^m/order$', mFacOrder, name='m_order'),
	url(r'^m/order2$', mFacOrder2, name='m_order2'),
	url(r'^m/choose-article$', mFacChooseArtice, name='m_choose_article'),
	url(r'^m/pay$', mFacPay, name='m_pay'),
]

urlpatterns = url
