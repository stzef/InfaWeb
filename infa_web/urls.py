from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url('', include('infa_web.apps.base.urls')),
	url('', include('infa_web.apps.inventarios.urls')),
	url('', include('infa_web.apps.articulos.urls'))
]
