from django.shortcuts import render,render_to_response

from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView

from infa_web.apps.articulos.models import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy 
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt

from dateutil import parser
import datetime
import json

from infa_web.apps.base.forms import *
from infa_web.apps.movimientos.forms import *
from infa_web.apps.movimientos.models import *
from infa_web.routines import calcular_costo_articulo,costing_and_stock

class InputMovementList(CustomListView):
	model = Mven
	template_name = "movimientos/list-movements.html"
	form_class = InputMovementForm

	def get_context_data(self,**kwargs):
		context = super(InputMovementList, self).get_context_data(**kwargs)
		context['title'] = "Listar Movimiento de Entrada"
		context['is_input_movement'] = True
		context['is_output_movement'] = False
		return context

class OutputMovementList(CustomListView):
	model = Mvsa
	template_name = "movimientos/list-movements.html"
	form_class = OutputMovementForm

	def get_context_data(self,**kwargs):
		context = super(OutputMovementList, self).get_context_data(**kwargs)
		context['title'] = "Listar Movimiento de Salida"
		context['is_input_movement'] = False
		context['is_output_movement'] = True
		return context

class InputMovementCreate(CustomCreateView):
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

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('save-movement')

		return context

class OutputMovementCreate(CustomCreateView):
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

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('save-movement')
		return context

class InputMovementUpdate(CustomUpdateView):
	model = Mven
	template_name = "movimientos/movement.html"
	form_class = InputMovementForm

	def get_context_data(self,**kwargs):
		context = super(InputMovementUpdate, self).get_context_data(**kwargs)

		context['title'] = "Editar Movimiento de Entrada"
		form_movement_detail = InputMovementDetailForm()
		context['form_movement_detail'] = form_movement_detail
		context['is_input_movement'] = True
		context['is_output_movement'] = False

		context['mvdeta'] = list(Mvendeta.objects.using(self.request.db).filter(cmven=self.kwargs["pk"]))
		context['mvdeta_json'] = serializers.serialize("json", list(Mvendeta.objects.using(self.request.db).filter(cmven=self.kwargs["pk"])),use_natural_foreign_keys=True, use_natural_primary_keys=True)

		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-movement',kwargs={'pk': self.kwargs["pk"]},)

		return context

class OutputMovementUpdate(CustomUpdateView):
	model = Mvsa 
	template_name = "movimientos/movement.html"
	form_class = OutputMovementForm

	def get_context_data(self,**kwargs):
		context = super(OutputMovementUpdate, self).get_context_data(**kwargs)

		context['title'] = "Editar Movimiento de Salida"
		form_movement_detail = OutputMovementDetailForm()
		context['form_movement_detail'] = form_movement_detail
		context['is_input_movement'] = False
		context['is_output_movement'] = True
		
		context['mvdeta'] = list(Mvsadeta.objects.using(self.request.db).filter(cmvsa=self.kwargs["pk"]))
		context['mvdeta_json'] = context['mvdeta_json'] = serializers.serialize("json", list(Mvsadeta.objects.using(self.request.db).filter(cmvsa=self.kwargs["pk"])),use_natural_foreign_keys=True, use_natural_primary_keys=True)

		context['mode_view'] = 'edit'
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit-movement',kwargs={'pk': self.kwargs["pk"]},)

		return context

def proccess_view_annulment(request):
	form = CommonForm()
	return render(request,"movimientos/procesos/annulment.html",{"form":form})

@csrf_exempt
def proccess_fn_annulment(request,pk):
	data = json.loads(request.body)

	if data["timo"] == "I":
		movement = Mven.objects.using(request.db).get(cmven=data["cmv"])
	else:
		movement = Mvsa.objects.using(request.db).get(cmvsa=data["cmv"])

	current_datetime = str(datetime.datetime.now())
	user = "Usuario Estatico"

	movement.detaanula = data["detaanula"] + " " + current_datetime + " " + user
	movement.cesdo = Esdo.objects.using(request.db).get(pk=data["cesdo"])

	print data["detaanula"] + " - " + current_datetime + " - " + user

	movement.save(using=request.db)

	return HttpResponse(json.dumps({"message":"Se realizo exitosamente el cambio"}), content_type="application/json",status=200)

def proccess_view_costing_and_stock(request):
	form = ProccessCostingAndStock()
	form_common = CommonForm()
	return render(request,"movimientos/procesos/costing_and_stock.html",{"form":form,"form_common":form_common})

@csrf_exempt
def proccess_fn_costing_and_stock(request):
	data = json.loads(request.body)
	query = {}
	if data["type"] == "All":
		query = {}
	elif data["type"] == "Group":
		query = {"cgpo":Gpo.objects.using(request.db).get(cgpo=data["group"])}
	elif data["type"] == "Arlo":
		query = {"carlos":data["carlos"]}
	
	#all
	#forGroup
	#forArticle
	data["date_range"]["start_date"] = parser.parse(data["date_range"]["start_date"])
	data["date_range"]["end_date"] = parser.parse(data["date_range"]["end_date"])
	response = {
		"data":costing_and_stock(data["date_range"],data["if_save"],query)
	}
	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def UpdateMovement(request,pk):
	data = json.loads(request.body)
	cmven = pk
	response = {}
	response["error"] = False
	response["message"] = "Movimiento Editado con Exito"

	timo = ctimo=Timo.objects.using(request.db).get(pk=data["ctimo"])

	if data['is_input_movement']:

		input_movement = Mven.objects.using(request.db).get(ctimo=timo,cmven=cmven)

		input_movement.cbode0 = Bode.objects.using(request.db).get(pk=data["cbode0"])
		input_movement.cesdo = Esdo.objects.using(request.db).get(pk=data["cesdo"])
		input_movement.citerce = Tercero.objects.using(request.db).get(pk=data["citerce"])
		input_movement.ctimo = timo
		input_movement.descri = data["descri"]
		input_movement.docrefe = data["docrefe"]
		input_movement.fmven = data["fmven"]
		input_movement.vttotal = data["vttotal"]

		input_movement.save(using=request.db)

		Mvendeta.objects.using(request.db).filter(ctimo=timo,cmven=input_movement).delete()
		for deta_movement in data["mvdeta"]:
			articulo = Arlo.objects.using(request.db).get(pk=deta_movement["carlos"])

			Mvendeta.objects.using(request.db).create(
				canti=deta_movement["canti"],
				carlos=articulo,
				it=deta_movement["it"],
				vtotal=deta_movement["vtotal"],
				vunita=deta_movement["vunita"],
				cmven=input_movement,
				ctimo=Timo.objects.using(request.db).get(pk=data["ctimo"]),
				nlargo=articulo.nlargo,
			)

			costing_and_stock(False,True,{"carlos":articulo.carlos})
			#calcular_costo_articulo(deta_movement["carlos"],deta_movement["canti"],deta_movement["vtotal"],data['is_input_movement'])

	else:

		output_movement = Mvsa.objects.using(request.db).get(ctimo=timo,cmvsa=cmven)

		output_movement.cbode0 = Bode.objects.using(request.db).get(pk=data["cbode0"])
		output_movement.cesdo = Esdo.objects.using(request.db).get(pk=data["cesdo"])
		output_movement.citerce = Tercero.objects.using(request.db).get(pk=data["citerce"])
		output_movement.ctimo = timo
		output_movement.descri = data["descri"]
		output_movement.docrefe = data["docrefe"]
		output_movement.fmvsa = data["fmvsa"]
		output_movement.vttotal = data["vttotal"]

		output_movement.save(using=request.db)

		Mvsadeta.objects.using(request.db).filter(cmvsa=output_movement).delete()
		for deta_movement in data["mvdeta"]:
			articulo = Arlo.objects.using(request.db).get(pk=deta_movement["carlos"])

			Mvsadeta.objects.using(request.db).create(
				canti=deta_movement["canti"],
				carlos=articulo,
				it=deta_movement["it"],
				vtotal=deta_movement["vtotal"],
				vunita=deta_movement["vunita"],
				cmvsa=output_movement,
				nlargo=articulo.nlargo,
			)

			costing_and_stock(False,True,{"carlos":articulo.carlos})
			#calcular_costo_articulo(deta_movement["carlos"],deta_movement["canti"],deta_movement["vtotal"],data['is_input_movement'])


	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def SaveMovement(request):
	data = json.loads(request.body)
	response = {}
	response["error"] = False
	response["message"] = "Movimiento Guardado con Exito"

	#print json.dumps(data, indent=4)

	if data['is_input_movement']:

		maxCmven = Mven.objects.using(request.db).aggregate(Max('cmven'))
		if maxCmven["cmven__max"]:
			cmven = maxCmven["cmven__max"] + 1
		else:
			cmven = 1
			
		response["cmv"] = cmven

		if not  Mven.objects.using(request.db).filter(ctimo=Timo.objects.using(request.db).get(pk=data["ctimo"]),cmven=cmven).exists():
			movement = Mven.objects.using(request.db).create(
				cbode0= Bode.objects.using(request.db).get(pk=data["cbode0"]),
				cesdo= Esdo.objects.using(request.db).get(pk=data["cesdo"]),
				citerce= Tercero.objects.using(request.db).get(pk=data["citerce"]),
				ctimo=Timo.objects.using(request.db).get(pk=data["ctimo"]),
				descri=data["descri"],
				docrefe=data["docrefe"],
				vttotal=data["vttotal"],
				fmven=data["fmven"],
				cmven=cmven,
			)
			for deta_movement in data["mvdeta"]:
				articulo = Arlo.objects.using(request.db).get(pk=deta_movement["carlos"])
				Mvendeta.objects.using(request.db).create(
					canti=deta_movement["canti"],
					carlos=articulo,
					it=deta_movement["it"],
					vtotal=deta_movement["vtotal"],
					vunita=deta_movement["vunita"],
					cmven=movement,
					ctimo=Timo.objects.using(request.db).get(pk=data["ctimo"]),
					#ctimo=Timo.objects.using(request.db).get(pk=movement.ctimo),
					nlargo=articulo.nlargo,
				)
				calcular_costo_articulo(deta_movement["carlos"],deta_movement["canti"],deta_movement["vtotal"],data['is_input_movement'])
		else:
			response["error"] = True
			response["message"] = "Este movimiento ya existe"
			response["cmv"] = None

	else:
		maxCmvsa = Mvsa.objects.using(request.db).aggregate(Max('cmvsa'))
		if maxCmvsa["cmvsa__max"]:
			cmvsa = maxCmvsa["cmvsa__max"] + 1
		else:
			cmvsa = 1

		response["cmv"] = cmvsa

		if not Mvsa.objects.using(request.db).filter(ctimo=Timo.objects.using(request.db).get(pk=data["ctimo"]),cmvsa=cmvsa).exists():
			movement = Mvsa.objects.using(request.db).create(
				cbode0= Bode.objects.using(request.db).get(pk=data["cbode0"]),
				cesdo= Esdo.objects.using(request.db).get(pk=data["cesdo"]),
				citerce= Tercero.objects.using(request.db).get(pk=data["citerce"]),
				ctimo=Timo.objects.using(request.db).get(pk=data["ctimo"]),
				descri=data["descri"],
				docrefe=data["docrefe"],
				vttotal=data["vttotal"],
				fmvsa=data["fmvsa"],
				cmvsa=cmvsa,
			)
			for deta_movement in data["mvdeta"]:
				articulo = Arlo.objects.using(request.db).get(pk=deta_movement["carlos"])
				Mvsadeta.objects.using(request.db).create(
					canti=deta_movement["canti"],
					carlos=articulo,
					it=deta_movement["it"],
					vtotal=deta_movement["vtotal"],
					vunita=deta_movement["vunita"],
					cmvsa=movement,
					nlargo=articulo.nlargo,
				)
				calcular_costo_articulo(deta_movement["carlos"],deta_movement["canti"],deta_movement["vtotal"],data['is_input_movement'])
		else:
			response["error"] = True
			response["message"] = "Este movimiento ya existe"
			response["cmv"] = None

	return HttpResponse(json.dumps(response), "application/json")
