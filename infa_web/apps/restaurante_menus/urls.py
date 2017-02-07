from django.conf.urls import patterns, include, url
from infa_web.apps.restaurante_menus.views import *

from django.contrib.auth.decorators import login_required

#url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
urlIngredients = [
	url(r'^ingredients/$', IngredientsList.as_view(), name = 'list-ingredients'),
	url(r'^ingredients/get-list/$', Ingredients_list, name = 'ingrediends_list'),
	url(r'^ingredients/add/$', IngredientCreate.as_view(), name = 'add-ingredient'),
	url(r'^ingredients/edit/(?P<pk>\d+)/$', IngredientUpdate.as_view(), name = 'edit-ingredient'),
]

urlDishes = [
	url(r'^dishes/$', DishesList.as_view(), name = 'list-dishes'),
	url(r'^dishes/add/$', DishCreate.as_view(), name = 'add-dish'),
	url(r'^dishes/edit/(?P<pk>\d+)/$', DishUpdate.as_view(), name = 'edit-dish'),

	url(r'^dishes/ingredients/(?P<pk>\d+)/$', GetIngredientsDish, name = 'get-ingredients-dish'),
	url(r'^dishes/ingredients/add/$', DishDetailCreate, name = 'add-ingredient-dish'),
	url(r'^dishes/ingredients/edit/$', DishDetailUpdate, name = 'add-ingredient-dish'),
	url(r'^dishes/ingredients/remove/$', DishDetailRemove, name = 'add-ingredient-dish'),
]

urlMenu = [
	#url(r'^menus/$', MenusList.as_view(), name = 'list-menus'),
	#url(r'^menus/add/$', MenuCreate.as_view(), name = 'add-menu'),
	#url(r'^menus/edit/(?P<pk>\d+)/$', MenuUpdate.as_view(), name = 'edit-menu'),
]

urlGroups = [
	#url(r'^menus/groups/$', GroupsList.as_view(), name = 'list-groups-menus'),
	#url(r'^menus/groups/add/$', GroupCreate.as_view(), name = 'add-group-menu'),
	#url(r'^menus/groups/edit/(?P<pk>\d+)/$', GroupUpdate.as_view(), name = 'edit-group-menu'),
]

urlpatterns = urlIngredients + urlDishes + urlMenu + urlGroups
