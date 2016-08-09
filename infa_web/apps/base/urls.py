from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('infa_web.apps.base.views',
	url(r'^$', TemplateView.as_view(template_name = 'home/dashboard.html'), {'title': 'Inicio'}, name = 'dashboard'),
)