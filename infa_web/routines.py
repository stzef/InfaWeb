from infa_web.parameters import ManageParameters

from infa_web.apps.articulos.models import Arlo
from infa_web.apps.inventarios.models import *
from infa_web.apps.movimientos.models import *
import decimal
import operator

# Solo se usa en este archivo
def costing(cantidad_actual,costo_actual,nueva_cantidad,nuevo_costo,is_input):
	if is_input:
		costo = (float(costo_actual)+float(nuevo_costo))/(float(cantidad_actual)+float(nueva_cantidad))
	else:
		costo = (float(costo_actual)+float(nuevo_costo))/(float(cantidad_actual)-float(nueva_cantidad))
	return costo

# Se usa en este archivo y en movimientos/views.py
def calcular_costo_articulo(carlos,nueva_cantidad,nuevo_costo,is_input,if_save=True,db_name='default'):
	manageParameters = ManageParameters(db_name)

	nueva_cantidad = decimal.Decimal(nueva_cantidad)
	nuevo_costo = decimal.Decimal(nuevo_costo)

	response = {}
	response["status"] = False
	if(Arlo.objects.using(db_name).filter(carlos=carlos).exists()):
		type_costing_and_stock = manageParameters.get_param_value("type_costing_and_stock")
		if(type_costing_and_stock == "M"):
			return response
		articulo = Arlo.objects.using(db_name).get(carlos=carlos)

		response["current_vcosto"] = str(articulo.vcosto)
		response["current_canti"] = str(articulo.canti)

		if is_input:
			nuevo_costo_calculado = costing(articulo.canti,(articulo.canti*articulo.vcosto),nueva_cantidad,nuevo_costo,is_input)

			articulo.canti += nueva_cantidad
			articulo.vcosto = nuevo_costo_calculado
			response["new_vcosto"] = str(nuevo_costo_calculado)
		else:
			response["new_vcosto"] = str(articulo.vcosto)
			articulo.canti -= nueva_cantidad
		response["new_canti"] = str(articulo.canti)
		

		#if if_save:
		articulo.save(using=db_name)
			
		response["status"] = True
		return response
	else:
		return response

# Se usa en este archivo, en inventarios/views.py y movimientos/views.py
# Falta inventarios/views.py
def costing_and_stock(date_range=False,if_save=True,query_arlo={},db_name='default'):
	manageParameters = ManageParameters(db_name)
	query_arlo["cesdo"] = CESTADO_ACTIVO

	articulos = Arlo.objects.using(db_name).order_by('carlos').filter(**query_arlo)
	print articulos

	"""
	No validar costos en 0
	"""

	initial_note = manageParameters.get_param_value("initial_note")
	
	try:
		invinicab = Invinicab.objects.using(db_name).get(cii=initial_note)
	except Invinicab.DoesNotExist, e:
		invinicab = None

	all_data = []
	for articulo in articulos:
		try:
			invinideta = Invinideta.objects.using(db_name).get(cii=invinicab,carlos=articulo)
		except Invinideta.DoesNotExist, e:
			invinideta = None

		query_mvendeta = {
			"carlos":articulo,
			"cmven__cesdo__in":list(Esdo.objects.using(db_name).exclude(**{"cesdo":CESDO_ANULADO}))
			}
		query_mvsadeta = {
			"carlos":articulo,
			"cmvsa__cesdo__in":list(Esdo.objects.using(db_name).exclude(**{"cesdo":CESDO_ANULADO}))
			}

		if date_range:
			query_mvendeta["cmven__fmven__gte"] = date_range["start_date"].replace(hour=0, minute=0, second=0, microsecond=0)
			query_mvendeta["cmven__fmven__lte"] = date_range["end_date"].replace(hour=0, minute=0, second=0, microsecond=0)

			query_mvsadeta["cmvsa__fmvsa__gte"] = date_range["start_date"].replace(hour=0, minute=0, second=0, microsecond=0)
			query_mvsadeta["cmvsa__fmvsa__lte"] = date_range["end_date"].replace(hour=0, minute=0, second=0, microsecond=0)

		mvendeta = Mvendeta.objects.using(db_name).select_related().order_by('-cmven__fmven').filter(**query_mvendeta)
		mvsadeta = Mvsadeta.objects.using(db_name).select_related().order_by('-cmvsa__fmvsa').filter(**query_mvsadeta)

		mvsdeta = list(mvendeta) + list(mvsadeta)

		for temp_mvdeta in mvsdeta:
			if hasattr(temp_mvdeta, "cmven"):
				temp_mvdeta.fmv = temp_mvdeta.cmven.fmven
			else:
				temp_mvdeta.fmv = temp_mvdeta.cmvsa.fmvsa
		mvsdeta.sort(key=lambda x: x.fmv)

		if invinideta:
			articulo.canti = invinideta.canti
			articulo.vcosto = invinideta.vunita
		else:
			articulo.canti = 0
			articulo.vcosto = 0

		#if if_save:
		articulo.save(using=db_name)

		if not len(mvsdeta):
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
		else:

			for mvdeta in mvsdeta:
				data_operation = {
					"carlos" : articulo.carlos,
					"ncorto" : articulo.ncorto,
					"change" : True
				}
				if hasattr(mvdeta, "cmven"):
					is_input = True
				else:
					is_input = False
				response = calcular_costo_articulo(articulo.carlos,mvdeta.canti,mvdeta.vtotal,is_input,if_save,db_name)
				data_operation["data"] = response

		all_data.append(data_operation)
	return all_data
