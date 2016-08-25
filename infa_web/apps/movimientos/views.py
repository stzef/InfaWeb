from django.shortcuts import render,render_to_response
from django.views.generic import FormView, CreateView
from django.views.generic.list import ListView
from infa_web.apps.articulos.models import *
import json
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse_lazy 
from infa_web.apps.movimientos.models import *
from infa_web.apps.movimientos.forms import *
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def SaveMovement(request):
	data = json.loads(request.body)
	print data
	if data["cmven"]:
		movement = Mven.objects.create(
			cbode0= Bode.objects.get(pk=data["cbode0"]),
			cesdo= Esdo.objects.get(pk=data["cesdo"]),
			citerce= Tercero.objects.get(pk=data["citerce"]),
			ctimo=Timo.objects.get(pk=data["ctimo"]),
			descri=data["descri"],
			docrefe=data["docrefe"],
			vttotal=data["vttotal"],
			fmven=data["fmven"],
			cmven=data["cmven"],
		)
		print "------------------------"
		print movement.ctimo
		print "------------------------"
		for deta_movement in data["mvendeta"]:
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

	else:
		movement = Mvsa.objects.create(
			cbode0= Bode.objects.get(pk=data["cbode0"]),
			cesdo= Esdo.objects.get(pk=data["cesdo"]),
			citerce= Tercero.objects.get(pk=data["citerce"]),
			ctimo=Timo.objects.get(pk=data["ctimo"]),
			descri=data["descri"],
			docrefe=data["docrefe"],
			vttotal=data["vttotal"],
			fmvsa=data["fmven"],
			cmvsa=data["cmven"],
		)
		for deta_movement in data["mvendeta"]:
			articulo = Arlo.objects.get(pk=deta_movement["carlos"])
			Mvsadeta.objects.create(
				canti=deta_movement["canti"],
				carlos=articulo,
				it=deta_movement["it"],
				vtotal=deta_movement["vtotal"],
				vunita=deta_movement["vunita"],
				cmvsa=movement,
				ctimo=Timo.objects.get(pk=data["ctimo"]),
				#ctimo=Timo.objects.get(pk=movement.ctimo),
				nlargo=articulo.nlargo,
			)
	response = {}
	return HttpResponse(json.dumps(response), "application/json")
