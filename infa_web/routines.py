from infa_web.parameters import ManageParameters

from infa_web.apps.articulos.models import Arlo

manageParameters = ManageParameters()

def calculo_costo(cantidad_actual,costo_actual,nueva_cantidad,nuevo_costo,is_input):
	if is_input:
		costo = (float(costo_actual)+float(nuevo_costo))/(float(cantidad_actual)+float(nueva_cantidad))
	else:
		costo = (float(costo_actual)+float(nuevo_costo))/(float(cantidad_actual)-float(nueva_cantidad))
	return costo

def calcular_costo_articulo(carlos,nueva_cantidad,nuevo_costo,is_input):
	print "..................................................."
	print "..................................................."
	if(Arlo.objects.filter(carlos=carlos).exists()):
		type_costing_and_stock = manageParameters.get_param_value("type_costing_and_stock")
		if(type_costing_and_stock == "M"):
			return False

		print "Calculo de costo. carlos = " + str(carlos)
		articulo = Arlo.objects.get(carlos=carlos)

		print "..................................................."
		print "Costo Actual = " + str(articulo.vcosto)
		print "Cantidad Actual = " + str(articulo.canti)
		print "..................................................."

		if is_input:
			nuevo_costo_calculado = calculo_costo(articulo.canti,articulo.vcosto,nueva_cantidad,nuevo_costo,is_input)
			articulo.canti += nueva_cantidad
			articulo.vcosto = nuevo_costo_calculado
		else:
			articulo.canti -= nueva_cantidad

		articulo.save()

		print "..................................................."
		print "Costo Enviada = " + str(nueva_cantidad)
		print "Cantidad Enviada = " + str(nuevo_costo)
		print "..................................................."

		print "Nuevo Actual = " + str(articulo.vcosto)
		print "Nueva Cantidad = " + str(articulo.canti)
		print "..................................................."
		print "..................................................."
		return True
	else:
		print "..................................................."
		print "El Articulo no existe. carlos = " + str(carlos)
		print "..................................................."
		return False

