import math
from infa_web.apps.articulos.models import *
from infa_web.apps.base.models import *

cient_por_ciento = float(100)

def calcular_valor_cambio(ventre,vttotal):
	ventre = float(ventre)
	vttotal = float(vttotal)
	"""
		ventre: Valor entregado
		vttotal: Valor Total de la factura

		Validaciones
		Verifica que el ventre tenga valor
		Verifica que el vttotal tenga valor

		Calcula el valor de cambio de la factura
		Operacion = ventre - vttotal
	"""
	if ventre >= vttotal:
		v_cambio = ventre - vttotal
	else:
		v_cambio = float(0)
	return v_cambio

def calcular_valor_unitario(carlos,list_price,descuento,pvta,name_db):
	"""
		pordes: Porcentaje de descuento del articulo
		vunita: Valor Unitario del articulo
		precio_venta: precio de venta que aplica para el tercero seleccionado(clipre: lista de precios)

		Validaciones
		Valida que se haya seleccionado un articulo en #form_deta_movement

		Calcula el valor unitario de un articulo
		Operacion = precio_venta - ( precio_venta * ( pordes / 100 ) )
	"""
	article = Arlo.objects.using(name_db).get(carlos=carlos)

	#name_list_price = "pvta" + str(list_price)
	#price_venta = float(getattr(article, name_list_price))
	price_venta = float(pvta)


	descuento = float(descuento)

	vunita = price_venta - ( price_venta * ( descuento / cient_por_ciento ) )

	return vunita

def calcular_total_flete(brtefte,prtefte):
	"""
		brtefte: Valor base del flete
		prtefte: Porcentaje de descuento del flete
		vrtefte: valor total del flete

		Recalcula el valor total del flete de la factura
		Operacion = brtefte - ( brtefte * ( prtefte / 100 ) )
	"""
	brtefte = float(brtefte)
	prtefte = float(prtefte)

	vrtefte = brtefte - ( brtefte * ( prtefte / cient_por_ciento ) )
	return vrtefte

def calcular_vtbase_vtiva(data_array,name_db="default"):
	"""
		canti: cantidad a vender del articulo
		vunita: Valor unitario del articulo
		pordes: Porcentaje de descuento del articulo
		civa: IVA para el articulo

		vtbase: valor total de la base
		vtiva: valor total del iva

		Calcula el valor total de la base y el valor total del iva
		Operaciones
			vbase = precio_total / ( 1 + ( porcentaje_iva / 100 ) )
			viva = vbase * ( porcentaje_iva / 100 )

			vtbase += vbase
			vtiva += viva
	"""

	vtbase = float(0)
	vtiva = float(0)

	print "vbase " + str(data_array)
	for data in data_array:
		cantidad = float(data["canti"])
		precio = float(data["vunita"])
		porcentaje_descuento = float(data["pordes"])

		codigo_iva = int(data["civa"])
		porcentaje_iva = float(Iva.objects.using(name_db).get(civa = codigo_iva).poriva)

		#precio_total_sin_descuento = cantidad * precio
		#precio_total = precio_total_sin_descuento - ( precio_total_sin_descuento * ( porcentaje_descuento / cient_por_ciento ) )
		"""
			No se Aplica el Descuento pues en el valor unitario ya se calculo
		"""
		precio_total = cantidad * precio

		vbase = precio_total / ( float(1) + ( porcentaje_iva / cient_por_ciento ) )
		viva = vbase * ( porcentaje_iva / cient_por_ciento )

		vtbase += custom_round(vbase)
		#vtbase += vbase
		vtiva += custom_round(viva)
		#vtiva += viva

	print {"vtbase": vtbase,"vtiva": vtiva}

	return {"vtbase": vtbase,"vtiva": vtiva}

def custom_round(x):
	decimal = math.modf(x)[0]
	integer = math.modf(x)[1]

	if(decimal > 0.5):
		return math.ceil(x)
	else:
		return math.floor(x)

def calcular_total(data_array,vflete,vdescu):
	"""
		Calcula el valor Total de la Factura

		Recorre todos los times de la factura calculando el valor individual y sumandolos para luego operarlos con el descuento y los valores del flete
	"""
	vttotal_items = float(0)
	vttotal_local = float(0)
	
	for data in data_array:
		temp_vunita = float(data["vunita"])
		temp_canti = float(data["canti"])
		descuento = float(data["pordes"])
		
		#vtotal_temp_sin_descuento = temp_vunita * temp_canti
		#vtotal_temp = vtotal_temp_sin_descuento - ( vtotal_temp_sin_descuento * ( descuento / cient_por_ciento ) )
		"""
			No se Aplica el Descuento pues en el valor unitario ya se calculo
		"""
		vtotal_temp = temp_vunita * temp_canti

		vttotal_items += vtotal_temp

	vflete = float(vflete)
	porcentaje_descuento = float(vdescu)

	vttotal_local_sin_descuento = vflete + vttotal_items
	vttotal_local = vttotal_local_sin_descuento - ( vttotal_local_sin_descuento * ( porcentaje_descuento / cient_por_ciento ) )

	return vttotal_local
