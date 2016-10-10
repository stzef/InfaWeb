from django.shortcuts import render

from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView

from django.core.urlresolvers import reverse_lazy

from django import forms

from infa_web.apps.terceros.forms import *
from infa_web.apps.base.views import AjaxableResponseMixin

# thirdParty #
class ThirdPartyCreate(AjaxableResponseMixin,CustomCreateView):
	model = Tercero
	template_name = "terceros/third-party.html"
	form_class = ThirdPartyForm
	success_url=reverse_lazy("add-third-party")
	def get_context_data(self, **kwargs):
		context = super(ThirdPartyCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Tercero'
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-third-party')
		return context
	
class ThirdPartyUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Tercero
	template_name = "terceros/third-party.html"
	success_url=reverse_lazy("add-third-party")
	form_class = ThirdPartyForm
	def get_context_data(self, **kwargs):
		context = super(ThirdPartyUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Tercero'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-third-party',kwargs={'pk': self.kwargs["pk"]},)

		return context

class ThirdPartyList(CustomListView):
	model = Tercero
	template_name = "terceros/list-third-parties.html"
# thirdParty #

# Autorretenedor #
class AutorrtenedorCreate(AjaxableResponseMixin,CustomCreateView):
	model = Autorre
	template_name = "terceros/autorretenedor.html"
	form_class = AutorretenedorForm
	success_url=reverse_lazy("add-autorretenedor")
	def get_context_data(self, **kwargs):
		context = super(AutorrtenedorCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Autorretenedor'
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-autorretenedor')

		return context
	
class AutorrtenedorUpdate(AjaxableResponseMixin,CustomUpdateView):
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

class AutorrtenedorList(CustomListView):
	model = Autorre
	template_name = "terceros/list-autorretenedor.html"
# Autorretenedor #

# zones #
class ZoneCreate(AjaxableResponseMixin,CustomCreateView):
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
	
class ZoneUpdate(AjaxableResponseMixin,CustomUpdateView):
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

class ZonesList(CustomListView):
	model = Zona
	template_name = "terceros/list-zones.html"
# zones #

# Routes #
class RouteCreate(AjaxableResponseMixin,CustomCreateView):
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
	
class RouteUpdate(AjaxableResponseMixin,CustomUpdateView):
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

class RoutesList(CustomListView):
	model = Ruta
	template_name = "terceros/list-routes.html"
# Routes #
