from django.conf.urls import patterns, include, url
from infa_web.apps.m.views import *

url = [
	url(r'^m/dashboard$', mDashboard, name='m_dashboard'),

]

urlpatterns = url
