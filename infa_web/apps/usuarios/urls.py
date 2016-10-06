from django.contrib.auth.decorators import user_passes_test
from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from infa_web.apps.usuarios.views import *

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/')

url = [
	#url(r'^login$', login, name = 'login'),
	url(r'^login$', login_forbidden(auth_views.login), {'template_name': 'usuarios/login.html', 'extra_context': {'title': 'Acceso', 'type': 'login'}}, name = 'login'),
	url(r'^logout$', auth_views.logout, {'next_page': '/login'}, name = 'logout')
]

urlpatterns = url
