from django.conf.urls import include, url
from infa_web.apps.restaurante_menus.views import *

from django.contrib.auth.decorators import login_required,permission_required

#url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
urlIngredients = [
	url(r'^ingredients/$', permission_required('restaurante_inventarios.add_invinicabingre')(login_required(IngredientsList.as_view())), name = 'list-ingredients'),
	url(r'^ingredients/get-list/$', login_required(Ingredients_list), name = 'ingrediends_list'),
	url(r'^ingredients/add/$', permission_required('restaurante_inventarios.add_invinicabingre')(login_required(IngredientCreate.as_view())), name = 'add-ingredient'),
	url(r'^ingredients/edit/(?P<pk>\d+)/$', permission_required('restaurante_inventarios.change_invinicabingre')(login_required(IngredientUpdate.as_view())), name = 'edit-ingredient'),
]

urlDishes = [
	url(r'^dishes/$', permission_required('restaurante_menus.list_platos')(login_required(DishesList.as_view())), name = 'list-dishes'),
	url(r'^dishes/add/$', permission_required('restaurante_menus.add_platos')(login_required(DishCreate.as_view())), name = 'add-dish'),
	url(r'^dishes/edit/(?P<pk>\d+)/$', permission_required('restaurante_menus.change_platos')(login_required(DishUpdate.as_view())), name = 'edit-dish'),

	url(r'^dishes/ingredients/(?P<pk>\d+)/$', GetDishDetail, name = 'get-ingredients-dish'),
	url(r'^dishes/ingredients/$', DishDetailCRUD, name = 'crud-ingredient-dish'),
]

urlMenu = [
	url(r'^menus/$', permission_required('restaurante_menus.list_menus')(login_required(MenusList.as_view())), name = 'list-menus'),
	url(r'^menus/add/$', permission_required('restaurante_menus.add_menus')(login_required(MenuCreate.as_view())), name = 'add-menu'),
	url(r'^menus/edit/(?P<pk>\d+)/$', permission_required('restaurante_menus.change_menus')(login_required(MenuUpdate.as_view())), name = 'edit-menu'),

	url(r'^menus/dishes/(?P<pk>\d+)/$', permission_required('restaurante_menuss')(login_required(GetMenuDetail)), name = 'get-platos-menu'),
	url(r'^menus/dishes/$', permission_required('restaurante_menus')(login_required(MenuDetailCRUD)), name = 'crud-platos-menu'),
]


urlGroups = [
	#url(r'^menus/groups/$', login_required(GroupsList.as_view()), name = 'list-groups-menus'),
	#url(r'^menus/groups/add/$', login_required(GroupCreate.as_view()), name = 'add-group-menu'),
	#url(r'^menus/groups/edit/(?P<pk>\d+)/$', login_required(GroupUpdate.as_view()), name = 'edit-group-menu'),
]

"""
urlGroups = [
	url(r'^menu-groups/$', permission_required('restaurante_menus')(login_required(GroupList.as_view())), name = 'list-menu-groups'),
	url(r'^menu-groups/add/$', permission_required('restaurante_menus')(login_required(GroupCreate.as_view())), name = 'add-menu-group'),
	url(r'^menu-groups/edit/(?P<pk>\d+)/$', permission_required('restaurante_menus')(login_required(GroupUpdate.as_view())), name = 'edit-menu-group'),
]
"""

urlpatterns = urlIngredients + urlDishes + urlMenu + urlGroups
