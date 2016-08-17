from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy


from infa_web.apps.articulos.models import *
from infa_web.apps.articulos.forms import *
from infa_web.apps.base.forms import *

from django.core import serializers

from django.http import JsonResponse

class AjaxableResponseMixin(object):
	"""
	Mixin to add AJAX support to a form.
	Must be used with an object-based FormView (e.g. CreateView)
	"""
	def form_invalid(self, form):
		response = super(AjaxableResponseMixin, self).form_invalid(form)
		if self.request.is_ajax():
			data = {
				'error':True,
				'message':'El proceso se realizo Con Exito',
				'errors':form.errors,
			}
			return JsonResponse(data, status=400)
		else:
			return response

	def form_valid(self, form):
		# We make sure to call the parent's form_valid() method because
		# it might do some processing (in the case of CreateView, it will
		# call form.save() for example).
		response = super(AjaxableResponseMixin, self).form_valid(form)
		if self.request.is_ajax():
			data = {
				'message':'El proceso se realizo Con Exito',
				'pk': self.object.pk,
				'object': serializers.serialize("json", [self.object],use_natural_foreign_keys=True, use_natural_primary_keys=True)
			}
			return JsonResponse(data)
		else:
			return response

# Parameters #
class ParametersList(ListView):
	model = Parameters
	template_name = "parametros/parameters.html"

	def get_context_data(self, **kwargs):
		context = super(ParametersList, self).get_context_data(**kwargs)
		context['title'] = 'Parametros'
		context['modules'] = {}
		for module in Modules.objects.all():
			if not module.pk in context['modules'].keys():
				context['modules'][module.pk] = []
			
			for parameter in Parameters.objects.all():
				print parameter.module.pk
				context['modules'][parameter.module.pk].append(parameter)
		print context['modules']
		return context

def ParameterCreate(request):
	data = json.loads(request.body)
	return HttpResponse(json.dumps(data), "application/json")
	
	Parameters.objects.create()

def ParameterUpdate(request,pk):
	parameter = Parameters.objects.get(cparam=pk)
	return HttpResponse(json.dumps(parameter), "application/json")

# Parameters #

# States #
class StateCreate(AjaxableResponseMixin,CreateView):
	model = Esdo
	template_name = "base/state.html"
	form_class = StateForm
	success_url=reverse_lazy("add-state")

	def get_context_data(self, **kwargs):
		context = super(StateCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Estado'
		context['mode_view'] = 'create'
		return context

class StateUpdate(AjaxableResponseMixin,UpdateView):
	model = Esdo
	template_name = "base/state.html"
	form_class = StateForm
	success_url=reverse_lazy("add-state")

	def get_context_data(self, **kwargs):
		context = super(StateUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Estado'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		return context

class StatesList(ListView):
	model = Esdo
	template_name = "articulos/list-states.html"
# States #

# Cities #
class CityCreate(AjaxableResponseMixin,CreateView):
	model = Ciudad
	template_name = "base/city.html"
	form_class = CiudadForm
	success_url=reverse_lazy("add-city")

	def get_context_data(self, **kwargs):
		context = super(CityCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Ciudad'
		context['mode_view'] = 'create'
		return context

class CityUpdate(AjaxableResponseMixin,UpdateView):
	model = Ciudad
	template_name = "base/city.html"
	form_class = CiudadForm
	success_url=reverse_lazy("add-city")

	def get_context_data(self, **kwargs):
		context = super(CityUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Ciudad'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		return context

class CitiesList(ListView):
	model = Ciudad
	template_name = "articulos/list-cities.html"
# Cities #

# Departaments #
class DepartamentCreate(AjaxableResponseMixin,CreateView):
	model = Departamento
	template_name = "base/departament.html"
	form_class = DepartamentoForm
	success_url=reverse_lazy("add-departament")

	def get_context_data(self, **kwargs):
		context = super(DepartamentCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Departamento'
		context['mode_view'] = 'create'
		return context

class DepartamentUpdate(AjaxableResponseMixin,UpdateView):
	model = Departamento
	template_name = "base/departament.html"
	form_class = DepartamentoForm
	success_url=reverse_lazy("add-departament")

	def get_context_data(self, **kwargs):
		context = super(DepartamentUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Departamento'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		return context

class DepartamentsList(ListView):
	model = Departamento
	template_name = "articulos/list-departaments.html"
# Departaments #

# Locations #
class LocationCreate(AjaxableResponseMixin,CreateView):
	model = Ubica
	template_name = "base/location.html"
	form_class = UbicaForm
	success_url=reverse_lazy("add-location")

	def get_context_data(self, **kwargs):
		context = super(LocationCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Departamento'
		context['mode_view'] = 'create'
		return context

class LocationUpdate(AjaxableResponseMixin,UpdateView):
	model = Ubica
	template_name = "base/location.html"
	form_class = UbicaForm
	success_url=reverse_lazy("add-location")

	def get_context_data(self, **kwargs):
		context = super(LocationUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Departamento'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		return context

class LocationsList(ListView):
	model = Ubica
	template_name = "articulos/list-locations.html"
# Locations #

# Brands #
class BrandCreate(AjaxableResponseMixin,CreateView):
	model = Marca
	form_class = BrandForm
	template_name = "base/brand.html"
	success_url=reverse_lazy("add-brand")

	def get_context_data(self, **kwargs):
		context = super(BrandCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Marca'
		context['mode_view'] = 'create'
		return context

class BrandUpdate(AjaxableResponseMixin,UpdateView):
	model = Marca
	form_class = BrandForm
	template_name = "base/brand.html"
	success_url=reverse_lazy("add-brand")

	def get_context_data(self, **kwargs):
		context = super(BrandUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Marca'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		return context

class BrandsList(ListView):
	model = Marca
	template_name = "base/list-brands.html"
# Brands #

# IVA #
class IvaCreate(AjaxableResponseMixin,CreateView):
	model = Iva
	form_class = IvaForm
	template_name = "base/iva.html"
	success_url=reverse_lazy("add-iva")

	def get_context_data(self, **kwargs):
		context = super(IvaCreate, self).get_context_data(**kwargs)
		context['title'] = 'Editar IVA'
		context['mode_view'] = 'create'
		return context

class IvaUpdate(AjaxableResponseMixin,UpdateView):
	model = Iva
	form_class = IvaForm
	template_name = "base/iva.html"
	success_url=reverse_lazy("add-iva")

	def get_context_data(self, **kwargs):
		context = super(IvaUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar IVA'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		return context

class IvaList(ListView):
	model = Iva
	template_name = "base/list-iva.html"
# IVA #

# RegIva #
class RegIvaCreate(AjaxableResponseMixin,CreateView):
	model = Regiva
	form_class = RegivaForm
	template_name = "base/reg-iva.html"
	success_url=reverse_lazy("add-reg-iva")

	def get_context_data(self, **kwargs):
		context = super(RegIvaCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Regimen de IVA'
		context['mode_view'] = 'create'
		return context

class RegIvaUpdate(AjaxableResponseMixin,UpdateView):
	model = Regiva
	form_class = RegivaForm
	template_name = "base/reg-iva.html"
	success_url=reverse_lazy("add-reg-iva")

	def get_context_data(self, **kwargs):
		context = super(RegIvaUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Regimen de IVA'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		return context

class RegIvasList(ListView):
	model = Regiva
	template_name = "base/list-reg-iva.html"
# RegIva #

# Tiide #
class IDTypeCreate(AjaxableResponseMixin,CreateView):
	model = Tiide
	form_class = IDTypeForm
	template_name = "base/id-types.html"
	success_url=reverse_lazy("add-id-type")

	def get_context_data(self, **kwargs):
		context = super(IDTypeCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Tipo de Identificacion'
		context['mode_view'] = 'create'
		return context

class IDTypeUpdate(AjaxableResponseMixin,UpdateView):
	model = Tiide
	form_class = IDTypeForm
	template_name = "base/id-types.html"
	success_url=reverse_lazy("add-id-type")

	def get_context_data(self, **kwargs):
		context = super(IDTypeUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Tipo de Identificacion'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		return context

class IDTypesList(ListView):
	model = Tiide
	template_name = "base/list-id-types.html"
# Tiide #
