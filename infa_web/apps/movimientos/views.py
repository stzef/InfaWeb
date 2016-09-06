from django.shortcuts import render,render_to_response
from django.views.generic import FormView, CreateView
from django.views.generic.list import ListView
from infa_web.apps.articulos.models import *
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse_lazy 
from infa_web.apps.movimientos.models import *
from infa_web.apps.movimientos.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max

import json

from infa_web.routines import calcular_costo_articulo,costing_and_stock

class InputMovementList(ListView):
	model = Mven
	template_name = "movimientos/list-movements.html"
	form_class = InputMovementForm

	def get_context_data(self,**kwargs):
		context = super(InputMovementList, self).get_context_data(**kwargs)
		context['title'] = "Listar Movimiento de Entrada"
		context['is_input_movement'] = True
		context['is_output_movement'] = False
		return context

class OutputMovementList(ListView):
	model = Mvsa
	template_name = "movimientos/list-movements.html"
	form_class = OutputMovementForm

	def get_context_data(self,**kwargs):
		context = super(OutputMovementList, self).get_context_data(**kwargs)
		context['title'] = "Listar Movimiento de Salida"
		context['is_input_movement'] = False
		context['is_output_movement'] = True
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
		context['is_input_movement'] = True
		context['is_output_movement'] = False

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
		context['is_input_movement'] = False
		context['is_output_movement'] = True
		return context

def proccess_view_costing_and_stock(request):
	form = ProccessCostingAndStock()
	return render(request,"movimientos/procesos/costing_and_stock.html",{"form":form})
@csrf_exempt
def proccess_fn_costing_and_stock(request):
	response = {
		"status":costing_and_stock()
	}
	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def SaveMovement(request):
	data = json.loads(request.body)
	response = {}
	response["error"] = False
	response["message"] = "Movimiento Guardado con Exito"

	print json.dumps(data, indent=4)

	if data['is_input_movement']:

		maxCmven = Mven.objects.aggregate(Max('cmven'))
		if maxCmven["cmven__max"]:
			cmven = maxCmven["cmven__max"] + 1
		else:
			cmven = 1
			
		response["cmv"] = cmven

		if not  Mven.objects.filter(ctimo=Timo.objects.get(pk=data["ctimo"]),cmven=cmven).exists():
			movement = Mven.objects.create(
				cbode0= Bode.objects.get(pk=data["cbode0"]),
				cesdo= Esdo.objects.get(pk=data["cesdo"]),
				citerce= Tercero.objects.get(pk=data["citerce"]),
				ctimo=Timo.objects.get(pk=data["ctimo"]),
				descri=data["descri"],
				docrefe=data["docrefe"],
				vttotal=data["vttotal"],
				fmven=data["fmven"],
				cmven=cmven,
			)
			for deta_movement in data["mvdeta"]:
				articulo = Arlo.objects.get(pk=deta_movement["carlos"])
				Mvendeta.objects.create(
					canti=deta_movement["canti"],
					carlos=articulo,
					it=deta_movement["it"],
					vtotal=deta_movement["vtotal"],
					vunita=deta_movement["vunita"],
					cmven=movement,
					ctimo=Timo.objects.get(pk=data["ctimo"]),
					#ctimo=Timo.objects.get(pk=movement.ctimo),
					nlargo=articulo.nlargo,
				)
				calcular_costo_articulo(deta_movement["carlos"],deta_movement["canti"],deta_movement["vtotal"],data['is_input_movement'])
		else:
			response["error"] = True
			response["message"] = "Este movimiento ya existe"
			response["cmv"] = None

	else:
		maxCmvsa = Mvsa.objects.aggregate(Max('cmvsa'))
		if maxCmvsa["cmvsa__max"]:
			cmvsa = maxCmvsa["cmvsa__max"] + 1
		else:
			cmvsa = 1

		response["cmv"] = cmvsa

		if not Mvsa.objects.filter(ctimo=Timo.objects.get(pk=data["ctimo"]),cmvsa=cmvsa).exists():
			movement = Mvsa.objects.create(
				cbode0= Bode.objects.get(pk=data["cbode0"]),
				cesdo= Esdo.objects.get(pk=data["cesdo"]),
				citerce= Tercero.objects.get(pk=data["citerce"]),
				ctimo=Timo.objects.get(pk=data["ctimo"]),
				descri=data["descri"],
				docrefe=data["docrefe"],
				vttotal=data["vttotal"],
				fmvsa=data["fmvsa"],
				cmvsa=cmvsa,
			)
			for deta_movement in data["mvdeta"]:
				articulo = Arlo.objects.get(pk=deta_movement["carlos"])
				Mvsadeta.objects.create(
					canti=deta_movement["canti"],
					carlos=articulo,
					it=deta_movement["it"],
					vtotal=deta_movement["vtotal"],
					vunita=deta_movement["vunita"],
					cmvsa=movement,
					ctimo=Timo.objects.get(pk=data["ctimo"]),
					nlargo=articulo.nlargo,
				)
				calcular_costo_articulo(deta_movement["carlos"],deta_movement["canti"],deta_movement["vtotal"],data['is_input_movement'])
		else:
			response["error"] = True
			response["message"] = "Este movimiento ya existe"
			response["cmv"] = None

	return HttpResponse(json.dumps(response), "application/json")
