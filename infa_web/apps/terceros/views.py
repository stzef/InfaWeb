from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

from django import forms

from infa_web.apps.terceros.forms import *
from infa_web.apps.base.views import AjaxableResponseMixin


# thirdParty #
class ThirdPartyCreate(AjaxableResponseMixin,CreateView):
	model = Tercero
	template_name = "terceros/third-party.html"
	form_class = ThirdPartyForm
	success_url=reverse_lazy("add-third-party")
	
class ThirdPartyUpdate(AjaxableResponseMixin,UpdateView):
	model = Tercero
	template_name = "terceros/third-party.html"
	success_url=reverse_lazy("add-third-party")
	form_class = ThirdPartyForm

class ThirdPartyList(ListView):
	model = Tercero
	template_name = "terceros/list-third-parties.html"
# thirdParty #

# Autorretenedor #
class AutorrtenedorCreate(AjaxableResponseMixin,CreateView):
	model = Autorre
	template_name = "terceros/autorretenedor.html"
	form_class = AutorretenedorForm
	success_url=reverse_lazy("add-autorretenedor")
	def get_context_data(self, **kwargs):
		context = super(AutorrtenedorCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Autorretenedor'
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-autorretenedor',kwargs={'pk': self.kwargs["pk"]},)

		return context
	
class AutorrtenedorUpdate(AjaxableResponseMixin,UpdateView):
	model = Autorre
	template_name = "terceros/autorretenedor.html"
	success_url=reverse_lazy("add-autorretenedor")
	form_class = AutorretenedorForm
	def get_context_data(self, **kwargs):
		context = super(AutorrtenedorUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Autorretenedor'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-autorretenedor',kwargs={'pk': self.kwargs["pk"]},)

		return context

class AutorrtenedorList(ListView):
	model = Autorre
	template_name = "terceros/list-autorretenedor.html"
# Autorretenedor #

# zones #
class ZoneCreate(AjaxableResponseMixin,CreateView):
	model = Zona
	template_name = "terceros/zone.html"
	form_class = ZoneForm
	success_url=reverse_lazy("add-zone")
	def get_context_data(self, **kwargs):
		context = super(ZoneCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Zona'
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-zone')

		return context
	
class ZoneUpdate(AjaxableResponseMixin,UpdateView):
	model = Zona
	template_name = "terceros/zone.html"
	success_url=reverse_lazy("add-zone")
	form_class = ZoneForm
	def get_context_data(self, **kwargs):
		context = super(ZoneUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Zona'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-zone',kwargs={'pk': self.kwargs["pk"]},)

		return context

class ZonesList(ListView):
	model = Zona
	template_name = "terceros/list-zones.html"
# zones #

# Routes #
class RouteCreate(AjaxableResponseMixin,CreateView):
	model = Ruta
	template_name = "terceros/route.html"
	form_class = RouteForm
	success_url=reverse_lazy("add-route")
	def get_context_data(self, **kwargs):
		context = super(RouteCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Ruta'
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-route')

		return context
	
class RouteUpdate(AjaxableResponseMixin,UpdateView):
	model = Ruta
	template_name = "terceros/route.html"
	success_url=reverse_lazy("add-route")
	form_class = RouteForm
	def get_context_data(self, **kwargs):
		context = super(RouteUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Ruta'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-route',kwargs={'pk': self.kwargs["pk"]},)

		return context

class RoutesList(ListView):
	model = Ruta
	template_name = "terceros/list-routes.html"
# Routes #
