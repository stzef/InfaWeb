from django.conf.urls import patterns, include, url
from infa_web.apps.articulos.views import *

from django.contrib.auth.decorators import login_required

urlArticles = [
	url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
	url(r'^articles/get-list/$', login_required(article_list), name = 'articles_list'),
	#url(r'^articles/add/$', ArticleCreate, name = 'add-article'),
	url(r'^articles/add/$', login_required(ArticleCreate.as_view()), name = 'add-article'),
	url(r'^articles/edit/(?P<pk>\d+)/$', login_required(ArticleUpdate.as_view()), name = 'edit-article'),
	url(r'^articles/copy/(?P<pk>\d+)/$', login_required(ArticleCopy.as_view()), name = 'copy-article'),
]

"""urlBreakdownArticles = [
	url(r'^articles/(?P<pk>\d+)/breakdown$', login_required(BreakdownArticle.as_view()), name = 'breakdown-article'),
	url(r'^articles/(?P<pk>\d+)/breakdown/save$', SaveBreakdownArticle, name = 'breakdown-article-save'),
]"""
urlGroups = [
	url(r'^groups/$', login_required(GroupList.as_view()), name = 'list-group'),
	url(r'^groups/add/$', login_required(GroupCreate.as_view()), name = 'add-group'),
	url(r'^groups/edit/(?P<pk>\d+)/$', login_required(GroupUpdate.as_view()), name = 'edit-group'),
]

urlTypesArticles = [
	url(r'^types-articles/$', login_required(TypesArticleList.as_view()), name = 'list-types-articles'),
	url(r'^types-articles/add/$', login_required(TypesArticleCreate.as_view()), name = 'add-type-article'),
	url(r'^types-articles/edit/(?P<pk>\d+)/$', login_required(TypesArticleUpdate.as_view()), name = 'edit-type-article'),
]

urlBrands = [
	url(r'^brands/$', login_required(BrandsList.as_view()), name = 'list-brands'),
	url(r'^brands/add/$', login_required(BrandCreate.as_view()), name = 'add-brand'),
	url(r'^brands/edit/(?P<pk>\d+)/$', login_required(BrandUpdate.as_view()), name = 'edit-brand'),
]

urlAPI = [
	url(r'^api/existis/$', login_required(API_exists), name = 'api-exists'),
	url(r'^api/get-object/$', login_required(API_get_object), name = 'api-get-object'),
]

"""urlpatterns = urlArticles + urlGroups + urlBreakdownArticles + urlBrands + urlAPI + urlTypesArticles"""
urlpatterns = urlArticles + urlGroups + urlBrands + urlAPI + urlTypesArticles
