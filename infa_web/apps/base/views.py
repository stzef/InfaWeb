from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

from infa_web.apps.articulos.models import *
from infa_web.apps.articulos.forms import *
from infa_web.apps.base.forms import *

# States #
class StateCreate(CreateView):
	model = Esdo
	template_name = "base/state.html"
	form_class = StateForm
	success_url=reverse_lazy("add-state")

class StateUpdate(UpdateView):
	model = Esdo
	template_name = "base/state.html"
	form_class = StateForm

class StatesList(ListView):
	model = Esdo
	template_name = "articulos/list-states.html"
# States #

# Cities #
class CityCreate(CreateView):
	model = Ciudad
	template_name = "base/city.html"
	form_class = CiudadForm
	success_url=reverse_lazy("add-city")

class CityUpdate(UpdateView):
	model = Ciudad
	template_name = "base/city.html"
	form_class = CiudadForm

class CitiesList(ListView):
	model = Ciudad
	template_name = "articulos/list-cities.html"
# Cities #

# Departaments #
class DepartamentCreate(CreateView):
	model = Departamento
	template_name = "base/departament.html"
	form_class = DepartamentoForm
	success_url=reverse_lazy("add-departament")

class DepartamentUpdate(UpdateView):
	model = Departamento
	template_name = "base/departament.html"
	form_class = DepartamentoForm

class DepartamentsList(ListView):
	model = Departamento
	template_name = "articulos/list-departaments.html"
# Departaments #

# Locations #
class LocationCreate(CreateView):
	model = Ubica
	template_name = "base/location.html"
	form_class = UbicaForm
	success_url=reverse_lazy("add-location")

class LocationUpdate(UpdateView):
	model = Ubica
	template_name = "base/location.html"
	form_class = UbicaForm

class LocationsList(ListView):
	model = Ubica
	template_name = "articulos/list-locations.html"
# Locations #

# Brands #
class BrandCreate(CreateView):
	model = Marca
	form_class = BrandForm
	template_name = "base/brand.html"
	success_url=reverse_lazy("add-brand")

class BrandUpdate(UpdateView):
	model = Marca
	form_class = BrandForm
	template_name = "base/brand.html"

class BrandsList(ListView):
	model = Marca
	template_name = "base/list-brands.html"
# Brands #

# IVA #
class IvaCreate(CreateView):
	model = Iva
	form_class = IvaForm
	template_name = "base/iva.html"
	success_url=reverse_lazy("add-iva")

class IvaUpdate(UpdateView):
	model = Iva
	form_class = IvaForm
	template_name = "base/iva.html"

class IvaList(ListView):
	model = Iva
	template_name = "base/list-iva.html"
# IVA #

# RegIva #
class RegIvaCreate(CreateView):
	model = Regiva
	form_class = RegivaForm
	template_name = "base/reg-iva.html"
	success_url=reverse_lazy("add-reg-iva")

class RegIvaUpdate(UpdateView):
	model = Regiva
	form_class = RegivaForm
	template_name = "base/reg-iva.html"

class RegIvasList(ListView):
	model = Regiva
	template_name = "base/list-reg-iva.html"
# RegIva #
