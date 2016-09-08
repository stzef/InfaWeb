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

import decimal


def calcular_costo_articulo(carlos,nueva_cantidad,nuevo_costo,is_input,if_save=True):

	nueva_cantidad = decimal.Decimal(nueva_cantidad)
	nuevo_costo = decimal.Decimal(nuevo_costo)

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

def costing_and_stock(date_range=False,if_save=True,query_arlo={}):
	
	query_arlo["cesdo"] = CESTADO_ACTIVO

	print query_arlo

	articulos = Arlo.objects.order_by('carlos').filter(**query_arlo)[:20]

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

		query_mvendeta = {"carlos":articulo}
		query_mvsadeta = {"carlos":articulo}

		#if date_range:
			#query_mvendeta = {"cmven__fmven__gte":date_range["start_date"],"cmven__fmven__lte":date_range["end_date"]}
			#query_mvsadeta = {"cmvsa__fmvsa__gte":date_range["start_date"],"cmvsa__fmvsa__lte":date_range["end_date"]}

		mvendeta = Mvendeta.objects.select_related().order_by('-cmven__fmven').filter(**query_mvendeta)
		mvsadeta = Mvsadeta.objects.select_related().order_by('-cmvsa__fmvsa').filter(**query_mvsadeta)

		mvsdeta = list(mvendeta) + list(mvsadeta)

		for temp_mvdeta in mvsdeta:
			if hasattr(temp_mvdeta, "cmven"):
				temp_mvdeta.fmv = temp_mvdeta.cmven.fmven
			else:
				temp_mvdeta.fmv = temp_mvdeta.cmvsa.fmvsa

		#mvsdeta.sort(key=lambda x: x.fmv, reverse=True)
		mvsdeta.sort(key=lambda x: x.fmv)

		print "---------------------"
		print "---------------------"
		print "---------------------"
		print "---------------------"
		print (mvsdeta)
		print "---------------------"
		print "---------------------"
		print "---------------------"
		print "---------------------"

		if invinideta:
			articulo.canti = invinideta.canti
			articulo.vtotal = invinideta.vunita
		else:
			articulo.canti = 0
			articulo.vtotal = 0

		if if_save:
			articulo.save()

		if not len(mvsdeta):
			#print "Sin mv"
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
			print mvdeta.fmv
			data_operation = {
				"carlos" : articulo.carlos,
				"ncorto" : articulo.ncorto,
				"change" : True
			}
			#print mvdeta
			if hasattr(mvdeta, "cmven"):
#				print mvdeta.cmven.fmven
				is_input = True
			else:
				#print mvdeta.cmvsa.fmvsa
				is_input = False
			response = calcular_costo_articulo(articulo.carlos,mvdeta.canti,mvdeta.vtotal,is_input,if_save)
			data_operation["data"] = response
		all_data.append(data_operation)
		##print(all_data)
		print("%s / %s" % (index,len(articulos)))
	return all_data



