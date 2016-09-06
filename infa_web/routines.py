from infa_web.parameters import ManageParameters

from infa_web.apps.articulos.models import Arlo
from infa_web.apps.inventarios.models import *
from infa_web.apps.movimientos.models import *
import operator

manageParameters = ManageParameters()

def calculo_costo(cantidad_actual,costo_actual,nueva_cantidad,nuevo_costo,is_input):
	if is_input:
		costo = (float(costo_actual)+float(nuevo_costo))/(float(cantidad_actual)+float(nueva_cantidad))
	else:
		costo = (float(costo_actual)+float(nuevo_costo))/(float(cantidad_actual)-float(nueva_cantidad))
	return costo

def calcular_costo_articulo(carlos,nueva_cantidad,nuevo_costo,is_input):
	response = {}
	response["status"] = False
	if(Arlo.objects.filter(carlos=carlos).exists()):
		type_costing_and_stock = manageParameters.get_param_value("type_costing_and_stock")
		if(type_costing_and_stock == "M"):
			return response
		articulo = Arlo.objects.get(carlos=carlos)

		response["current_vcosto"] = str(articulo.vcosto)
		response["current_canti"] = str(articulo.canti)

		if is_input:
			nuevo_costo_calculado = calculo_costo(articulo.canti,(articulo.canti*articulo.vcosto),nueva_cantidad,nuevo_costo,is_input)

			articulo.canti += nueva_cantidad
			articulo.vcosto = nuevo_costo_calculado
		else:
			articulo.canti -= nueva_cantidad

		articulo.save()
		response["new_vcosto"] = str(articulo.vcosto)
		response["new_canti"] = str(articulo.canti)
		response["status"] = True
		return response
	else:
		return response

def costing_and_stock():
	separador = "------------------------------------------------"
	#articulos = Arlo.objects.filter(esdo=01)
	articulos = Arlo.objects.all()

	initial_note = manageParameters.get_param_value("initial_note")
	invinicab = Invinicab.objects.get(cii=initial_note)

	for articulo in articulos:
		if Invinideta.objects.filter(cii=invinicab,carlos=articulo).exists():
			invinideta = Invinideta.objects.get(cii=invinicab,carlos=articulo)
		else:
			invinideta = None

		mvendeta = Mvendeta.objects.select_related().order_by('-cmven__fmven').filter(carlos=articulo)
		mvsadeta = Mvsadeta.objects.select_related().order_by('-cmvsa__fmvsa').filter(carlos=articulo)

		mvsdeta = list(mvendeta) + list(mvsadeta)

		if invinideta:
			articulo.canti = invinideta.canti
			articulo.vtotal = invinideta.vunita
		else:
			articulo.canti = 0
			articulo.vtotal = 0

		articulo.save()

		all_data = []

		for mvdeta in mvsdeta:
			data_operation = {
				"arlo" : invinideta.carlos.carlos,
				"data" : []
			}
			print mvdeta
			if hasattr(mvdeta, "cmven"):
				print mvdeta.cmven.fmven
				is_input = True
			else:
				print mvdeta.cmvsa.fmvsa
				is_input = False
			response = calcular_costo_articulo(invinideta.carlos.carlos,mvdeta.canti,mvdeta.vtotal,is_input)
			data_operation["data"].append(response)
		all_data.append(data_operation)
		print(all_data)
	return all_data



