from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from infa_web.apps.m.views import *

url = [

	# Pages
	url(r'^m/dashboard$', mDashboard, name='m_dashboard'),

	url(r'^m/fac$', mFac, name='m_fac'),

	url(r'^m/choose-client$', mFacChooseClient, name='m_choose_client'),
	url(r'^m/search-client$', mFacSearchClient, name='m_search_client'),
	url(r'^m/order$', mFacOrder, name='m_order'),
	url(r'^m/order2$', mFacOrder2, name='m_order2'),
	url(r'^m/choose-article$', mFacChooseArtice, name='m_choose_article'),
	url(r'^m/options-article$', mFacOptionsArticle, name='m_options_article'),
	url(r'^m/pay$', mFacPay, name='m_pay'),
	url(r'^m/third-party/add$', mThirdPartyAdd.as_view(), name='m_third_party_add'),

	# Ajax
	url(r'^m/third-party/list$', mThirtyPartyList, name='m_ajax_third_party_list'),
	url(r'^m/articles/list$', mArticlesList, name='m_ajax_article_list')

]

urlpatterns = url