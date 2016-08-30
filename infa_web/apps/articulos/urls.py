from django.conf.urls import patterns, include, url
from infa_web.apps.articulos.views import *

urlArticles = [
	url(r'^articles/$', ArticleList.as_view(), name = 'list-articles'),
	#url(r'^articles/add/$', ArticleCreate, name = 'add-article'),
	url(r'^articles/add/$', ArticleCreate.as_view(), name = 'add-article'),
	url(r'^articles/edit/(?P<pk>\d+)/$', ArticleUpdate.as_view(), name = 'edit-article'),
	url(r'^articles/copy/(?P<pk>\d+)/$', ArticleCopy.as_view(), name = 'copy-article'),
]

urlBreakdownArticles = [
	url(r'^articles/(?P<pk>\d+)/breakdown$', BreakdownArticle.as_view(), name = 'breakdown-article'),
	url(r'^articles/(?P<pk>\d+)/breakdown/save$', SaveBreakdownArticle, name = 'breakdown-article-save'),
]
urlGroups = [
	url(r'^groups/$', GroupList.as_view(), name = 'list-group'),
	url(r'^groups/add/$', GroupCreate.as_view(), name = 'add-group'),
	url(r'^groups/edit/(?P<pk>\d+)/$', GroupUpdate.as_view(), name = 'edit-group'),
]

urlTypesArticles = [
	url(r'^types-articles/$', TypesArticleList.as_view(), name = 'list-types-articles'),
	url(r'^types-articles/add/$', TypesArticleCreate.as_view(), name = 'add-type-article'),
	url(r'^types-articles/edit/(?P<pk>\d+)/$', TypesArticleUpdate.as_view(), name = 'edit-type-article'),
]

urlBrands = [
	url(r'^brands/$', BrandsList.as_view(), name = 'list-brands'),
	url(r'^brands/add/$', BrandCreate.as_view(), name = 'add-brand'),
	url(r'^brands/edit/(?P<pk>\d+)/$', BrandUpdate.as_view(), name = 'edit-brand'),
]

urlAPI = [
	url(r'^api/existis/$', API_exists, name = 'api-exists'),
	url(r'^api/get-object/$', API_get_object, name = 'api-get-object'),
]

urlpatterns = urlArticles + urlGroups + urlBreakdownArticles + urlBrands + urlAPI + urlTypesArticles
