from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from infa_web.apps.m.views import *

url = [
	url(r'^m/dashboard$', mDashboard, name='m_dashboard'),

]

urlpatterns = url
