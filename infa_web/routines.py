from infa_web.parameters import ManageParameters

from infa_web.apps.articulos.models import Arlo
from infa_web.apps.inventarios.models import *
from infa_web.apps.movimientos.models import *
import operator

manageParameters = ManageParameters()

def costing(cantidad_actual,costo_actual,nueva_cantidad,nuevo_costo,is_input):
	if is_input:
		costo = (float(costo_actual)+float(nuevo_costo))/(float(cantidad_actual)+float(nueva_cantidad))
	else:
		costo = (float(costo_actual)+float(nuevo_costo))/(float(cantidad_actual)-float(nueva_cantidad))
	return costo

def calcular_costo_articulo(carlos,nueva_cantidad,nuevo_costo,is_input,if_save=True):
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
			nuevo_costo_calculado = costing(articulo.canti,(articulo.canti*articulo.vcosto),nueva_cantidad,nuevo_costo,is_input)

			articulo.canti += nueva_cantidad
			articulo.vcosto = nuevo_costo_calculado
		else:
			articulo.canti -= nueva_cantidad
		
		if if_save:
			articulo.save()

		response["new_vcosto"] = str(articulo.vcosto)
		response["new_canti"] = str(articulo.canti)
		response["status"] = True
		return response
	else:
		return response


def costing_and_stock(date_range,if_save):
	articulos = Arlo.objects.order_by('carlos').filter(cesdo=CESTADO_ACTIVO)

	"""
	No validar costos en 0
	"""

	initial_note = manageParameters.get_param_value("initial_note")
	
	try:
		invinicab = Invinicab.objects.get(cii=initial_note)
	except Invinicab.DoesNotExist, e:
		invinicab = None

	all_data = []
	for index,articulo in enumerate(articulos):
		try:
			invinideta = Invinideta.objects.get(cii=invinicab,carlos=articulo)
		except Invinideta.DoesNotExist, e:
			invinideta = None

		#mvendeta = Mvendeta.objects.select_related().order_by('-cmven__fmven').filter(carlos=articulo,cmven__fmven__range=(date_range["start_date"], date_range["end_date"]))
		mvendeta = Mvendeta.objects.select_related().order_by('-cmven__fmven').filter(carlos=articulo)
		#mvsadeta = Mvsadeta.objects.select_related().order_by('-cmvsa__fmvsa').filter(carlos=articulo,cmvsa__fmvsa__range=(date_range["start_date"], date_range["end_date"]))
		mvsadeta = Mvsadeta.objects.select_related().order_by('-cmvsa__fmvsa').filter(carlos=articulo)

		mvsdeta = list(mvendeta) + list(mvsadeta)

		if invinideta:
			articulo.canti = invinideta.canti
			articulo.vtotal = invinideta.vunita
		else:
			articulo.canti = 0
			articulo.vtotal = 0

		if if_save:
			articulo.save()

		if not len(mvsdeta):
			print "Sin mv"
			data_operation = {
				"carlos" : articulo.carlos,
				"ncorto" : articulo.ncorto,
				"change" : False
			}

			response = {}

			response["current_vcosto"] = str(articulo.vcosto)
			response["current_canti"] = str(articulo.canti)
			response["new_vcosto"] = str(articulo.vcosto)
			response["new_canti"] = str(articulo.canti)

			data_operation["data"] = response

			all_data.append(data_operation)

		for mvdeta in mvsdeta:
			data_operation = {
				"carlos" : articulo.carlos,
				"ncorto" : articulo.ncorto,
				"change" : True
			}
			print mvdeta
			if hasattr(mvdeta, "cmven"):
				print mvdeta.cmven.fmven
				is_input = True
			else:
				print mvdeta.cmvsa.fmvsa
				is_input = False
			response = calcular_costo_articulo(articulo.carlos,mvdeta.canti,mvdeta.vtotal,is_input,if_save)
			data_operation["data"] = response
			all_data.append(data_operation)
		##print(all_data)
		print("%s / %s" % (articulo.carlos,articulo.canti))
	return all_data