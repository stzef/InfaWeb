from django.conf.urls import patterns, include, url
from infa_web.apps.restaurante_comandas.views import *

from django.contrib.auth.decorators import login_required

#url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
urlOrders = [
	url(r'^orders/$', login_required(OrdersList.as_view()), name = 'list-orders'),
	url(r'^orders/take/$', login_required(TakeOrder), name = 'take-order'),

	url(r'^orders/commands/(?P<cmesa>\d+)/$', login_required(GetCommandsOrder), name = 'get-order-commands'),
	url(r'^orders/save/$', login_required(SaveCommand), name = 'save-command'),

	#url(r'^orders/commands/annulment/item/$', AnnulmentItemCoda, name = 'annulment-item-coda'),

	url(r'^orders/join/$', login_required(OrdersJoin), name = 'order-join'),

	url(r'^orders/commands/proccess/fn/annulment/item/$', login_required(AnnulmentItemCommand), name = 'order-command-proccess-fn-annulment-item'),
	url(r'^orders/commands/proccess/fn/annulment/$', login_required(AnnulmentCommand), name = 'order-command-proccess-fn-annulment'),
	url(r'^orders/commands/proccess/view/annulment/$', login_required(ViewAnnulmentCommand), name = 'order-command-proccess-view-annulment'),

	url(r'^orders/summary/$', login_required(OrderSummary), name = 'order-summary'),
	url(r'^orders/summary/save/$', login_required(SaveSummary), name = 'save-summary'),
	url(r'^orders/print/$', login_required(OrderPrint.as_view()), name = 'order-print'),

]

urlpatterns = urlOrders
