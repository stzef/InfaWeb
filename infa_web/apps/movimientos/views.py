from django.shortcuts import render,render_to_response
from django.views.generic import FormView, CreateView
from django.views.generic.list import ListView
from infa_web.apps.articulos.models import *
import json
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse_lazy 
from infa_web.apps.movimientos.models import *
from infa_web.apps.movimientos.forms import *

class InputMovementList(ListView):
	model = Mven
	template_name = "movimientos/list-input-movements.html"
	form_class = InputMovementForm

	def get_context_data(self,**kwargs):
		context = super(InputMovementList, self).get_context_data(**kwargs)
		context['title'] = "listar Movimiento de Entrada"
		return context

class InputMovementCreate(CreateView):
	model = Mven
	template_name = "movimientos/movement.html"
	form_class = InputMovementForm

	def get_context_data(self,**kwargs):
		context = super(InputMovementCreate, self).get_context_data(**kwargs)
		context['title'] = "Crear Movimiento de Entrada"
		form_movement_detail = InputMovementDetailForm()
		context['form_movement_detail'] = form_movement_detail
		context['current_pk'] = 100

		return context

class OutputMovementCreate(CreateView):
	model = Mvsa 
	template_name = "movimientos/movement.html"
	form_class = OutputMovementForm

	def get_context_data(self,**kwargs):
		context = super(OutputMovementCreate, self).get_context_data(**kwargs)
		context['title'] = "Crear Movimiento de Salida"
		form_movement_detail = OutputMovementDetailForm()
		context['form_movement_detail'] = form_movement_detail
		context['current_pk'] = 100
		return context

def InputMovementUpdate(request,pk):
	context = {
		"title":"Editar Movimiento de Entrada"
	}
	return render_to_response("movimientos/input-movement.html",context)

def InputMovementSave(request):
	data = json.loads(request.body)
	print data
	response = {}
	return HttpResponse(json.dumps(response), "application/json")

def get_info_arlo(request, carlos):
	response = {}
	response['arlo'] = int(Arlo.objects.get(carlos = carlos).vcosto)
	return HttpResponse(json.dumps(response), "application/json")