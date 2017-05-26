from django.conf.urls import include, url
from infa_web.apps.POS.views import *

from django.contrib.auth.decorators import login_required,permission_required

#url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
url = [
	url(r'^pos/$', permission_required ( 'facturacion.add_fac_pos',raise_exception=True )(login_required(BillCreate.as_view())), name = 'create-pos'),
	url(r'^pos/print$', permission_required('facturacion.print_fac_pos')(login_required(BillPrint)), name = 'pint-pos'),
	url(r'^pos/list/$', permission_required('facturacion.list_fac_pos')(login_required(BillList.as_view())), name = 'list-pos-bill'),
 
]

urlpatterns = url
