from django.conf.urls import patterns, include, url
from infa_web.apps.restaurante_comandas.views import *

from django.contrib.auth.decorators import login_required

#url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
urlOrders = [
	url(r'^orders/$', OrdersList, name = 'list-orders'),
	url(r'^orders/take/$', TakeOrder, name = 'take-order'),

	url(r'^orders/commands/(?P<cmesa>\d+)/$', GetCommandsOrder, name = 'get-order-commands'),
	url(r'^orders/save/$', SaveCommand, name = 'save-command'),

]

urlpatterns = urlOrders
