# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.views.generic import CreateView, UpdateView,DeleteView,FormView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, JsonResponse

from django.template import RequestContext

from django.apps import apps

import json

from infa_web.parameters import ManageParameters

from infa_web.apps.articulos.models import *
from infa_web.apps.articulos.forms import *
from infa_web.apps.base.forms import *
from django.views.decorators.csrf import csrf_exempt


from infa_web.settings import BASE_DIR

from django.core import serializers

from django.http import JsonResponse

def get_custom_message_response(instance,object):
	message = "El proceso se realizo con Exito."

	if isinstance(instance,Gpo): message = "El Grupo <strong>%s</strong> se guardo Correctamente. Codigo: %s" % (object.ngpo,object.pk)
	if isinstance(instance,Tiarlos): message = "El Tipo de articulo <strong>%s</strong> se guardo Correctamente. Codigo: %s" % (object.ntiarlo,object.pk)
	if isinstance(instance,Marca): message = "La Marca <strong>%s</strong> se guardo Correctamente. Codigo: %s" % (object.nmarca,object.pk)
	if isinstance(instance,Unidades): message = "La medidad de Unidad <strong>%s</strong> se guardo Correctamente. Codigo: %s" % (object.nunidad,object.pk)
	if isinstance(instance,Bode): message = "La Bodega <strong>%s</strong> se guardo Correctamente. Codigo: %s" % (object.nbode,object.pk)
	if isinstance(instance,Modules): message = "El Modulo <strong>%s</strong> se guardo Correctamente. Codigo: %s" % (object.nmodulo,object.pk)

	if isinstance(instance,Parameters): message = "El Parametro <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Ubica): message = "La Ubicacion <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Departamento): message = "El Departamento <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Ciudad): message = "La Ciudad <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Iva): message = "El Valor de IVA <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Regiva): message = "El Regimen de IVA <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Tiide): message = "El Tipo de Identificación <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Timo): message = "El Tipo de Movimiento <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Autorre): message = "El Autorretenedor <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Vende): message = "El Vendedor <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Ruta): message = "La Ruta <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Personas): message = "El Tipo de Persona <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)
	if isinstance(instance,Zona): message = "La Zona <strong>%s</strong> se guardo Correctamente. Codigo: %s" % ("",object.pk)

	if isinstance(instance,Esdo): message = "El Estado <strong>%s</strong> se guardo Correctamente. Codigo: %s" % (object.nesdo,object.pk)
	if isinstance(instance,Arlo): message = "El Articulo <strong>%s</strong> se guardo Correctamente. Codigo: %s" % (object.ncorto,object.pk)
	if isinstance(instance,Tercero): message = "El Tercero <strong>%s</strong> se guardo Correctamente. Codigo: %s" % (object.rasocial,object.pk)
	return message

class JSONResponseMixin(object):
	"""
	A mixin that can be used to render a JSON response.
	"""
	def render_to_json_response(self, context, **response_kwargs):
		"""
		Returns a JSON response, transforming 'context' to make the payload.
		"""
		return JsonResponse(
			self.get_data(context),
			**response_kwargs
		)

	def get_data(self, context):
		"""
		Returns an object that will be serialized as JSON by json.dumps().
		"""
		# Note: This is *EXTREMELY* naive; in reality, you'll need
		# to do much more complex handling to ensure that arbitrary
		# objects -- such as Django model instances or querysets
		# -- can be serialized as JSON.
		return context

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
			message = get_custom_message_response(form.instance,self.object)
			data = {
				'message':message,
				'pk': self.object.pk,
				'object': serializers.serialize("json", [self.object],use_natural_foreign_keys=True, use_natural_primary_keys=True)
			}
			return JsonResponse(data)
		else:
			return response

# Parameters #
def ParametersList(FormView):
	context = {}
	context['title'] = 'Parametros'

	manageParameters = ManageParameters()
	context['modules'] = Modules.objects.using(self.request.db).all()


	if(manageParameters.get_all() == None):
		context['parameters'] = []
		return render_to_response("parametros/parameters.html",context)

	parameters = manageParameters.get_all()
	for parameter in parameters:
		if parameter["type"] == "Model":
			modelString = parameter["model"]
			appString = parameter["app"]
			model = apps.get_model(app_label=appString,model_name=modelString)

			query = {}
			if("query" in parameter.keys()):
				query = parameter["query"]

				for key,value in query.iteritems():
					if(value[0:2] == "::" and value[-2:] == "::"):
						query[key] = eval(value[2:-2])

			for object_db in model.objects.using(self.request.db).filter(**query):
				value = getattr(object_db, parameter["field"]["value"])
				text = getattr(object_db, parameter["field"]["text"])

				selected = False
				if(str(value) == str(parameter["value"])):
					selected = True

				parameter["field"]["options"].append({"value": value,"text": text,"selected":selected})

			if(len(parameter["field"]["options"]) == 0):
				parameter["field"]["options"].append({"value": "@","text": "No se encontraron Valores" ,"selected":True})

	print json.dumps(parameters, indent=4)
	context['parameters'] = parameters

	return render_to_response("parametros/parameters.html",context)

@csrf_exempt
def ParametersSave(request):
	data = json.loads(request.body)
	response = {}
	manageParameters = ManageParameters()
	
	parameters = manageParameters.get_all()
	
	for dparameter in data:
		for parameter in parameters:
			if(parameter["cparam"] == dparameter["cparam"]):
				parameter["value"] = dparameter["value"]
				parameter["field"]["selected"] = dparameter["value"]
				if parameter["field"]["select"]:
					for option in parameter["field"]["options"]:
						if option["value"] == dparameter["value"]:
							option["selected"] = True
				break

	if manageParameters.save(parameters):
		response["message"] = "Parametros Guardados con Exito."
		return JsonResponse(response, status=200)
	else:
		response["message"] = "Error al guardar los Parametros."
		return JsonResponse(response, status=400)
# Parameters #

# States #
class StateCreate(AjaxableResponseMixin,CreateView):
	model = Esdo
	template_name = "base/state.html"
	form_class = StateForm
	success_url=reverse_lazy("add-state")

	def get_context_data(self, **kwargs):
		context = super(StateCreate, self).get_context_data(**kwargs)

		context_request = RequestContext(self.request)
		#context['context_request'] = context_request
		self.context_instance = RequestContext(self.request)

		#print context_request

		context['title'] = 'Crear Estado'
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-state')
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
		context['url'] = reverse_lazy('edit-state',kwargs={'pk': self.kwargs["pk"]},)
		context['current_pk'] = self.kwargs["pk"]
		return context

class StatesList(ListView):
	model = Esdo
	template_name = "base/list-states.html"
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
		context['url'] = reverse_lazy('add-city')

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
		context['url'] = reverse_lazy('edit-city',kwargs={'pk': self.kwargs["pk"]})

		return context

class CitiesList(ListView):
	model = Ciudad
	template_name = "base/list-cities.html"
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
		context['url'] = reverse_lazy('add-departament')

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
		context['url'] = reverse_lazy('edit-departament',kwargs={'pk': self.kwargs["pk"]},)

		return context

class DepartamentsList(ListView):
	model = Departamento
	template_name = "base/list-departaments.html"
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
		context['url'] = reverse_lazy('add-location')

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
		context['url'] = reverse_lazy('edit-location',kwargs={'pk': self.kwargs["pk"]},)

		return context

class LocationsList(ListView):
	model = Ubica
	template_name = "base/list-locations.html"
# Locations #

# IVA #
class IvaCreate(AjaxableResponseMixin,CreateView):
	model = Iva
	form_class = IvaForm
	template_name = "base/iva.html"
	success_url=reverse_lazy("add-iva")

	def get_context_data(self, **kwargs):
		context = super(IvaCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear IVA'
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-iva')

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
		context['url'] = reverse_lazy('edit-iva',kwargs={'pk': self.kwargs["pk"]},)

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
		context['url'] = reverse_lazy('add-reg-iva')

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
		context['url'] = reverse_lazy('edit-reg-iva',kwargs={'pk': self.kwargs["pk"]},)

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
		context['url'] = reverse_lazy('add-id-type')

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
		context['url'] = reverse_lazy('edit-id-type',kwargs={'pk': self.kwargs["pk"]},)

		return context

class IDTypesList(ListView):
	model = Tiide
	template_name = "base/list-id-types.html"
# Tiide #
