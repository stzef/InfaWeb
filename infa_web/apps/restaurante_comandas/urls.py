from django.conf.urls import include, url
from infa_web.apps.restaurante_comandas.views import *

from django.contrib.auth.decorators import login_required,permission_required

#url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
urlAccounts = [
	url(r'^accounts/save/$', permission_required('facturacion.add_fac')(login_required(SetResuCfac)), name = 'set-cfac')
]
urlOrders = [
	url(r'^orders/$', permission_required('restaurante_comandas.list_coda')(login_required(OrdersList.as_view())), name = 'list-orders'),
	url(r'^orders/take/$', permission_required('restaurante_comandas.add_coda')(login_required(TakeOrder)), name = 'take-order'),

	url(r'^orders/commands/(?P<cmesa>\d+)/$', permission_required('restaurante_comandas.add_coda')(login_required(GetCommandsOrder)), name = 'get-order-commands'),
	url(r'^orders/save/$', permission_required('restaurante_comandas.add_coda')(login_required(SaveCommand)), name = 'save-command'),

	#url(r'^orders/commands/annulment/item/$', AnnulmentItemCoda, name = 'annulment-item-coda'),

	url(r'^orders/join/$', permission_required('restaurante_comandas.add_coda')(login_required(OrdersJoin)), name = 'order-join'),

	url(r'^orders/commands/proccess/fn/annulment/item/$', permission_required('restaurante_comandas')(login_required(AnnulmentItemCommand)), name = 'order-command-proccess-fn-annulment-item'),
	url(r'^orders/commands/proccess/fn/annulment/$', permission_required('rastaurante_comandas')(login_required(AnnulmentCommand)), name = 'order-command-proccess-fn-annulment'),
	url(r'^orders/commands/proccess/view/annulment/$', permission_required('rastaurante_comandas')(login_required(ViewAnnulmentCommand)), name = 'order-command-proccess-view-annulment'),

	url(r'^orders/summary/$', permission_required('rastaurante_comandas')(login_required(OrderSummary)), name = 'order-summary'),
	url(r'^orders/summary/save/$',permission_required('rastaurante_comandas')(login_required(SaveSummary)), name = 'save-summary'),
	url(r'^orders/print/$', permission_required('rastaurante_comandas')(login_required(OrderPrint)), name = 'order-print'),
]

urlComandas = [
	url(r'^commands/print/$', permission_required('rastaurante_comandas')(login_required(CommandPrintRequest)), name = 'command-print'),
	url(r'^commands/printers/$', permission_required('rastaurante_comandas')(login_required(GetPrinters)), name = 'command-print'),
]

urlMesas = [
	url(r'^tables/$', permission_required('restaurante_comandas.list_mesas')(login_required(TablesList.as_view())), name = 'list-tables'),
	url(r'^tables/add/$',permission_required('restaurante_comandas.add_mesas')(login_required(TableCreate.as_view())), name = 'add-table'),
	url(r'^tables/edit/(?P<pk>[0-9]+)/$',permission_required('restaurante_comandas.change_mesas')(login_required(TableUpdate.as_view())), name = 'edit-table'),
	url(r'^tables/info-sumary/(?P<pk>[0-9]+)/$', permission_required('restaurante_comandas')(login_required(InfoSummaryUpdate)), name = 'table-info-summary'),

	url(r'^tables/info-resupedi/(?P<cmesa>[0-9]+)/$',login_required(GetResupediMesa),name="table-info-resupedi"),
	#url(r'^tables/info-resupedi/(?P<cmesa>[0-9]+)/$',login_required(GetResupediMesa),name="table-info-resupedi"),
]
urlReportes = [
	url(r'^orders/reports/fn/accounts$', login_required(report_fn_accounts.as_view()), name = 'report_fn_accounts'),
	url(r'^orders/reports/view/accounts$', login_required(report_view_accounts), name = 'report_view_accounts'),
]

urlpatterns = urlOrders + urlMesas + urlComandas + urlAccounts + urlReportes
