# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response, redirect

from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required


import json

from infa_web.parameters import ManageParameters
from infa_web.apps.articulos.models import *
from infa_web.apps.articulos.forms import *
from infa_web.apps.base.forms import *
from infa_web.settings import BASE_DIR


def dashboard(request):
	return render(request, 'home/dashboard.html', {'title': 'Dashboard'})

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
	Must be used with an object-based FormView (e.g. CustomCreateView)
	"""
	def form_invalid(self, form):
		response = super(AjaxableResponseMixin, self).form_invalid(form)
		if self.request.is_ajax():
			data = {
				'error':True,
				'message':'Ocurrio un Error al realizar el Proceso.',
				'errors':form.errors,
			}
			return JsonResponse(data, status=400)
		else:
			return response

	def form_valid(self, form):
		# We make sure to call the parent's form_valid() method because
		# it might do some processing (in the case of CustomCreateView, it will
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
def ParametersList(request):
	context = {}
	context['title'] = 'Parametros'

	manageParameters = ManageParameters(request.db)
	context['modules'] = Modules.objects.using(request.db).all()


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

			for object_db in model.objects.using(request.db).filter(**query):
				value = getattr(object_db, parameter["field"]["value"])
				text = getattr(object_db, parameter["field"]["text"])

				selected = False
				if(str(value) == str(parameter["value"])):
					selected = True

				parameter["field"]["options"].append({"value": value,"text": text,"selected":selected})

			if(len(parameter["field"]["options"]) == 0):
				parameter["field"]["options"].append({"value": "@","text": "No se encontraron Valores" ,"selected":True})

	context['parameters'] = parameters

	return render_to_response("parametros/parameters.html",context)

@csrf_exempt
def ParametersSave(request):
	data = json.loads(request.body)
	response = {}
	manageParameters = ManageParameters(request.db)

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
class StateCreate(AjaxableResponseMixin,CustomCreateView):
	model = Esdo
	template_name = "base/state.html"
	form_class = StateForm
	success_url=reverse_lazy("add-state")

	def get_context_data(self, **kwargs):
		context = super(StateCreate, self).get_context_data(**kwargs)

		context_request = RequestContext(self.request)
		#context['context_request'] = context_request
		self.context_instance = RequestContext(self.request)


		context['title'] = 'Crear Estado'
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-state')
		return context

class StateUpdate(AjaxableResponseMixin,CustomUpdateView):
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

class StatesList(CustomListView):
	model = Esdo
	template_name = "base/list-states.html"
# States #

# Cities #
class CityCreate(AjaxableResponseMixin,CustomCreateView):
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

class CityUpdate(AjaxableResponseMixin,CustomUpdateView):
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

class CitiesList(CustomListView):
	model = Ciudad
	template_name = "base/list-cities.html"
# Cities #

# Departaments #
class DepartamentCreate(AjaxableResponseMixin,CustomCreateView):
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

class DepartamentUpdate(AjaxableResponseMixin,CustomUpdateView):
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

class DepartamentsList(CustomListView):
	model = Departamento
	template_name = "base/list-departaments.html"
# Departaments #

# Locations #
class LocationCreate(AjaxableResponseMixin,CustomCreateView):
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

class LocationUpdate(AjaxableResponseMixin,CustomUpdateView):
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

class LocationsList(CustomListView):
	model = Ubica
	template_name = "base/list-locations.html"
# Locations #

# IVA #
class IvaCreate(AjaxableResponseMixin,CustomCreateView):
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

class IvaUpdate(AjaxableResponseMixin,CustomUpdateView):
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

class IvaList(CustomListView):
	model = Iva
	template_name = "base/list-iva.html"
# IVA #

# RegIva #
class RegIvaCreate(AjaxableResponseMixin,CustomCreateView):
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

class RegIvaUpdate(AjaxableResponseMixin,CustomUpdateView):
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

class RegIvasList(CustomListView):
	model = Regiva
	template_name = "base/list-reg-iva.html"
# RegIva #

# Tiide #
class IDTypeCreate(AjaxableResponseMixin,CustomCreateView):
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

class IDTypeUpdate(AjaxableResponseMixin,CustomUpdateView):
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

class IDTypesList(CustomListView):
	model = Tiide
	template_name = "base/list-id-types.html"
# Tiide #

# Sucursales #

class BanchCreate(AjaxableResponseMixin,CustomCreateView):
	model = Sucursales
	form_class = SucursalForm
	template_name = "base/sucursal.html"
	success_url=reverse_lazy("add-branch")

	def get_context_data(self, **kwargs):
		context = super(BanchCreate, self).get_context_data(**kwargs)
		context['title'] = 'Crear Sucursal'
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-branch')

		return context

class BanchUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Sucursales
	form_class = SucursalForm
	template_name = "base/sucursal.html"
	success_url=reverse_lazy("add-branch")

	def get_context_data(self, **kwargs):
		context = super(BanchUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Sucursal'
		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-branch',kwargs={'pk': self.kwargs["pk"]},)

		return context

class BanchsList(CustomListView):
	model = Sucursales
	template_name = "base/list-sucursales.html"
# Sucursales #


# Models find #
import json
import django.apps
def clear_filter_dic(query):
	for key,value in query.iteritems():
		if value == "__NULL__":
			nkey = key + "__isnull"
			del query[key]
			query[nkey] = True
	print query
	return query

@csrf_exempt
def ModelFind(request):
	data = json.loads(request.body)
	models = [ {"app":model._meta.app_label,"model":model._meta.object_name} for model in django.apps.apps.get_models() ]
	model = filter(lambda x: x["model"] == data["model"], models)

	if len(model) != 1:
		return JsonResponse({"objs":None},status=400)
	else:
		model = model[0]

	model = apps.get_model(app_label=model["app"],model_name=model["model"])

	filter_dict = clear_filter_dic(data["query"])


	if model.objects.using(request.db).filter(**filter_dict).exists():
		object_db = serializers.serialize("json", model.objects.using(request.db).filter(**filter_dict),use_natural_foreign_keys=True)
		object_db = json.loads(object_db)
		return JsonResponse({"objs":object_db})
	else:
		return JsonResponse({"objs":None})

@csrf_exempt
def ModelFindOne(request):
	data = json.loads(request.body)
	models = [ {"app":model._meta.app_label,"model":model._meta.object_name} for model in django.apps.apps.get_models() ]
	model = filter(lambda x: x["model"] == data["model"], models)

	if len(model) != 1:
		return JsonResponse({"obj":None},status=400)
	else:
		model = model[0]

	model = apps.get_model(app_label=model["app"],model_name=model["model"])

	filter_dict = clear_filter_dic(data["query"])

	if model.objects.using(request.db).filter(**filter_dict).exists():
		objects = serializers.serialize("json", [model.objects.using(request.db).get(**filter_dict)],use_natural_foreign_keys=True)
		objects = json.loads(objects)[0]
		return JsonResponse({"obj":objects})
	else:
		return JsonResponse({"obj":None})

# Models find #

# Generales #
from infa_web.apps.base.utils import get_current_user
def defaults(request):



	data = {
		"tercero" : Tercero.objects.using(request.db).filter(citerce=DEFAULT_TERCERO),
		"domiciliario" : Domici.objects.using(request.db).filter(cdomici=DEFAULT_DOMICILIARIO),
		"empacador" : Emdor.objects.using(request.db).filter(cemdor=DEFAULT_EMPACADOR),
		"banco" : Banfopa.objects.using(request.db).filter(cbanfopa=DEFAULT_BANCO),
		"caja" : Caja.objects.using(request.db).filter(ccaja=DEFAULT_CAJA),
		"talonario" : Talo.objects.using(request.db).filter(ctalo=DEFAULT_TALONARIO),
		"medio_pago" : MediosPago.objects.using(request.db).filter(cmpago=DEFAULT_FORMA_PAGO),
		"marca" : Marca.objects.using(request.db).filter(cmarca=DEFAULT_MARCA),
		"bodega" : Bode.objects.using(request.db).filter(cbode=DEFAULT_BODEGA),
		"ubicacion" : Ubica.objects.using(request.db).filter(cubica=DEFAULT_UBICACION),
		"grupo" : Gpo.objects.using(request.db).filter(cgpo=DEFAULT_GRUPO),
		"zona" : Zona.objects.using(request.db).filter(czona=DEFAULT_ZONA),
		"ruta" : Ruta.objects.using(request.db).filter(cruta=DEFAULT_RUTA),
		"unidad" : Unidades.objects.using(request.db).filter(cunidad=DEFAULT_UNIDAD),
		"persona" : Personas.objects.using(request.db).filter(cpersona=DEFAULT_PERSONA),
		#DEFAULT_LISTA_PRECIOS = 1
		#DEFAULT_AUTORRETENEDOR = 1
		"iva" : Iva.objects.using(request.db).filter(civa=DEFAULT_IVA),
		"regimen_iva" : Regiva.objects.using(request.db).filter(cregiva=DEFAULT_REGIMEN_IVA),
		"vendedor" : Vende.objects.using(request.db).filter(cvende=DEFAULT_VENDE),
		"tipo_identificacion" : Tiide.objects.using(request.db).filter(idtiide=DEFAULT_TIIDE),
		"ciudad" : Ciudad.objects.using(request.db).filter(cciu=DEFAULT_CIUDAD),
		"estado" : Esdo.objects.using(request.db).filter(cesdo=DEFAULT_ACTIVO),
		"tipo_articulo" : Tiarlos.objects.using(request.db).filter(ctiarlos=DEFAULT_CTIARLO),
		"forma_pago" : Tifopa.objects.using(request.db).filter(ctifopa=DEFAULT_MEDIO_PAGO),
	}

	data["tercero"] = json.loads(serializers.serialize("json", data["tercero"],use_natural_foreign_keys=True))[0]
	data["domiciliario"] = json.loads(serializers.serialize("json", data["domiciliario"],use_natural_foreign_keys=True))[0]
	data["empacador"] = json.loads(serializers.serialize("json", data["empacador"],use_natural_foreign_keys=True))[0]
	data["banco"] = json.loads(serializers.serialize("json", data["banco"],use_natural_foreign_keys=True))[0]
	data["caja"] = json.loads(serializers.serialize("json", data["caja"],use_natural_foreign_keys=True))[0]
	data["talonario"] = json.loads(serializers.serialize("json", data["talonario"],use_natural_foreign_keys=True))[0]
	data["medio_pago"] = json.loads(serializers.serialize("json", data["medio_pago"],use_natural_foreign_keys=True))[0]
	data["marca"] = json.loads(serializers.serialize("json", data["marca"],use_natural_foreign_keys=True))[0]
	data["bodega"] = json.loads(serializers.serialize("json", data["bodega"],use_natural_foreign_keys=True))[0]
	data["ubicacion"] = json.loads(serializers.serialize("json", data["ubicacion"],use_natural_foreign_keys=True))[0]
	data["grupo"] = json.loads(serializers.serialize("json", data["grupo"],use_natural_foreign_keys=True))[0]
	data["zona"] = json.loads(serializers.serialize("json", data["zona"],use_natural_foreign_keys=True))[0]
	data["ruta"] = json.loads(serializers.serialize("json", data["ruta"],use_natural_foreign_keys=True))[0]
	data["unidad"] = json.loads(serializers.serialize("json", data["unidad"],use_natural_foreign_keys=True))[0]
	data["persona"] = json.loads(serializers.serialize("json", data["persona"],use_natural_foreign_keys=True))[0]
	data["iva"] = json.loads(serializers.serialize("json", data["iva"],use_natural_foreign_keys=True))[0]
	data["regimen_iva"] = json.loads(serializers.serialize("json", data["regimen_iva"],use_natural_foreign_keys=True))[0]
	data["vendedor"] = json.loads(serializers.serialize("json", data["vendedor"],use_natural_foreign_keys=True))[0]
	data["tipo_identificacion"] = json.loads(serializers.serialize("json", data["tipo_identificacion"],use_natural_foreign_keys=True))[0]
	data["ciudad"] = json.loads(serializers.serialize("json", data["ciudad"],use_natural_foreign_keys=True))[0]
	data["estado"] = json.loads(serializers.serialize("json", data["estado"],use_natural_foreign_keys=True))[0]
	data["tipo_articulo"] = json.loads(serializers.serialize("json", data["tipo_articulo"],use_natural_foreign_keys=True))[0]
	data["forma_pago"] = json.loads(serializers.serialize("json", data["forma_pago"],use_natural_foreign_keys=True))[0]

	user_django = get_current_user(request.db,request.user,user_django=True)
	if user_django is not None:
		data["current_user_django"] = json.loads(serializers.serialize("json", [user_django],use_natural_foreign_keys=True))[0]
		del data["current_user_django"]["fields"]["password"]
	user_appem = get_current_user(request.db,request.user,user_appem=True)
	if user_appem is not None:
		data["current_user_appem"] = json.loads(serializers.serialize("json", [user_appem],use_natural_foreign_keys=True))[0]
	mesero = get_current_user(request.db,request.user,mesero=True)
	if mesero is not None:
		data["current_mesero"] = json.loads(serializers.serialize("json", [mesero],use_natural_foreign_keys=True))[0]
	vendedor = get_current_user(request.db,request.user,vendedor=True)
	if vendedor is not None:
		data["current_vendedor"] = json.loads(serializers.serialize("json", [vendedor],use_natural_foreign_keys=True))[0]
	return JsonResponse(data)

# Generales #
