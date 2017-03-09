from django.conf.urls import patterns, include, url
from infa_web.apps.restaurante_comandas.views import *

from django.contrib.auth.decorators import login_required

#url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
urlOrders = [
	url(r'^orders/$', OrdersList.as_view(), name = 'list-orders'),
	url(r'^orders/take/$', TakeOrder, name = 'take-order'),

	url(r'^orders/commands/(?P<cmesa>\d+)/$', GetCommandsOrder, name = 'get-order-commands'),
	url(r'^orders/save/$', SaveCommand, name = 'save-command'),

	#url(r'^orders/commands/annulment/item/$', AnnulmentItemCoda, name = 'annulment-item-coda'),

	url(r'^orders/join/$', OrdersJoin, name = 'order-join'),

	url(r'^orders/commands/proccess/fn/annulment/item/$', AnnulmentItemCommand, name = 'order-command-proccess-fn-annulment-item'),
	url(r'^orders/commands/proccess/fn/annulment/$', AnnulmentCommand, name = 'order-command-proccess-fn-annulment'),
	url(r'^orders/commands/proccess/view/annulment/$', ViewAnnulmentCommand, name = 'order-command-proccess-view-annulment'),

	url(r'^orders/summary/$', OrderSummary, name = 'order-summary'),
	url(r'^orders/summary/save/$', SaveSummary, name = 'save-summary'),
	url(r'^orders/print/$', OrderPrint.as_view(), name = 'order-print'),

]

urlpatterns = urlOrders
