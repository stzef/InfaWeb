from django.contrib.auth.decorators import user_passes_test
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from infa_web.apps.usuarios.views import *
from django.contrib.auth.decorators import login_required


url = [
	url(r'^login$', loginView.as_view(), name = 'login'),
	#url(r'^login$', login_forbidden(auth_views.login), {'template_name': 'usuarios/login.html', 'extra_context': {'title': 'Acceso', 'type': 'login'}}, name = 'login'),
	url(r'^logout$', auth_views.logout, {'next_page': '/login'}, name = 'logout'),
	url(r'^users/registar/$', login_required(RegistarUsuario), name = 'registrar-usuario'),
	url(r'^users/administrar/$', login_required(AdministrarUsuario), name = 'administrar-usuarios'),
]

urlpatterns = url
