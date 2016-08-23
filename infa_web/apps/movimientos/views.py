from django.shortcuts import render,render_to_response
from django.views.generic import FormView, CreateView
from django.views.generic.list import ListView
import json
from django.http import JsonResponse
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
	template_name = "movimientos/input-movement.html"
	form_class = InputMovementForm

	def get_context_data(self,**kwargs):
		context = super(InputMovementCreate, self).get_context_data(**kwargs)
		context['title'] = "Crear Movimiento de Entrada"

		form_input_movement_detail = InputMovementDetailForm()
		context['form_input_movement_detail'] = form_input_movement_detail

		return context

def InputMovementUpdate(request,pk):
	context = {
		"title":"Editar Movimiento de Entrada"
	}
	return render_to_response("movimientos/input-movement.html",context)

def InputMovementSave(request):
	data = json.loads(request.body)
	response = {}
	return HttpResponse(json.dumps(response), "application/json")


