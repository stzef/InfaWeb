from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url('', include('infa_web.apps.base.urls')),
	url('', include('infa_web.apps.terceros.urls')),
	url('', include('infa_web.apps.movimientos.urls')),
	url('', include('infa_web.apps.articulos.urls')),
	url('', include('infa_web.apps.inventarios.urls')),
	url('', include('infa_web.apps.facturacion.urls')),
	url('', include('infa_web.apps.cartera.urls')),
	url('', include('infa_web.apps.usuarios.urls')),
	url('', include('infa_web.apps.m.urls')),

	# Restaurante
	url('', include('infa_web.apps.restaurante_comandas.urls')),
	url('', include('infa_web.apps.restaurante_inventarios.urls')),
	url('', include('infa_web.apps.restaurante_menus.urls')),
	url('', include('infa_web.apps.restaurante_movimientos.urls')),
	url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
