from django.conf.urls import include, url
from infa_web.apps.articulos.views import *

from django.contrib.auth.decorators import login_required,permission_required

#url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
urlArticles = [
	url(r'^articles/$', permission_required('articulos.list_arlo')(login_required(ArticleList.as_view())), name = 'list-articles'),
	url(r'^articles/get-list/$', permission_required('')(login_required(article_list)), name = 'articles_list'),
	#url(r'^articles/add/$', ArticleCreate, name = 'add-article'),
	url(r'^articles/add/$', permission_required('articulos.add_arlo')(login_required(ArticleCreate.as_view())), name = 'add-article'),
	url(r'^articles/edit/(?P<pk>\d+)/$', permission_required('articulos.change_arlo')(login_required(ArticleUpdate.as_view())), name = 'edit-article'),
	url(r'^articles/copy/(?P<pk>\d+)/$', permission_required('articulos.add_arlo')(login_required(ArticleCopy.as_view())), name = 'copy-article'),
]

"""urlBreakdownArticles = [
	url(r'^articles/(?P<pk>\d+)/breakdown$', login_required(BreakdownArticle.as_view()), name = 'breakdown-article'),
	url(r'^articles/(?P<pk>\d+)/breakdown/save$', SaveBreakdownArticle, name = 'breakdown-article-save'),
]"""
urlGroups = [
	url(r'^groups/$', permission_required('articulos.list_gpo')(login_required(GroupList.as_view())), name = 'list-group'),
	url(r'^groups/add/$', permission_required('articulos.add_gpo')(login_required(GroupCreate.as_view())), name = 'add-group'),
	url(r'^groups/edit/(?P<pk>\d+)/$', permission_required('articulos.change_gpo')(login_required(GroupUpdate.as_view())), name = 'edit-group'),
]

urlTypesArticles = [
	url(r'^types-articles/$', permission_required('articulos.list_tiarlos')(login_required(TypesArticleList.as_view())), name = 'list-types-articles'),
	url(r'^types-articles/add/$', permission_required('articulos.add_tiarlos')(login_required(TypesArticleCreate.as_view())), name = 'add-type-article'),
	url(r'^types-articles/edit/(?P<pk>\d+)/$', permission_required('articulos.change_tiarlos')(login_required(TypesArticleUpdate.as_view())), name = 'edit-type-article'),
]

urlBrands = [
	url(r'^brands/$', permission_required('sucursales.list_marcas')(login_required(BrandsList.as_view())), name = 'list-brands'),
	url(r'^brands/add/$', permission_required('sucursales.add_marcas')(login_required(BrandCreate.as_view())), name = 'add-brand'),
	url(r'^brands/edit/(?P<pk>\d+)/$', permission_required('sucursales.change_marcas')(login_required(BrandUpdate.as_view())), name = 'edit-brand'),
]

urlUnits = [
	url(r'^units/$', permission_required('articulos.list_unidades')(login_required(UnitsList.as_view())), name = 'list-units'),
	url(r'^units/add/$', permission_required('articulos.add_unidades')(login_required(UnitCreate.as_view())), name = 'add-unit'),
	url(r'^units/edit/(?P<pk>\d+)/$', permission_required('articulos.change_unidades')(login_required(UnitUpdate.as_view())), name = 'edit-unit'),
]

urlAPI = [
	url(r'^api/existis/$', permission_required('')(login_required(API_exists)), name = 'api-exists'),
	url(r'^api/get-object/$', permission_required('')(login_required(API_get_object)), name = 'api-get-object'),
]

"""urlpatterns = urlArticles + urlGroups + urlBreakdownArticles + urlBrands + urlAPI + urlTypesArticles"""
urlpatterns = urlArticles + urlGroups + urlBrands + urlAPI + urlTypesArticles + urlUnits
