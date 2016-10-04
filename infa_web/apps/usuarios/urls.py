from django.conf.urls import patterns, include, url
from infa_web.apps.usuarios.views import *

url = [
	url(r'^login$', login, name = 'login'),
]

urlpatterns = url
