from infa_web.parameters import ManageParameters

from infa_web.apps.articulos.models import Arlo

manageParameters = ManageParameters()

def calculo_costo(cantidad_actual,costo_actual,nueva_cantidad,nuevo_costo):
	costo = (costo_actual+nuevo_costo)/(cantidad_actual+nueva_cantidad)
	return costo

def calcular_costo_articulo(carlos,nueva_cantidad,nuevo_costo):
	print "..................................................."
	print "..................................................."
	if(Arlo.objects.filter(carlos=carlos).exists()):
		print "Calculo de costo. carlos = " + str(carlos)
		articulo = Arlo.objects.get(carlos=carlos)

		manageParameters.get_param_value("min_code_arlos")

		print "..................................................."
		print "Costo Actual = " + str(articulo.vcosto)
		print "Cantidad Actual = " + str(articulo.canti)
		print "..................................................."
		nuevo_costo_calculado = calculo_costo(articulo.canti,articulo.vcosto,nueva_cantidad,nuevo_costo)
		articulo.vcosto = nuevo_costo_calculado
		s = articulo.save()

		print "..................................................."
		print "Costo Enviada = " + str(nueva_cantidad)
		print "Cantidad Enviada = " + str(nuevo_costo)
		print "..................................................."

		print "Nuevo Actual = " + str(articulo.vcosto)
		print "..................................................."
		print "..................................................."
		return True
	else:
		print "..................................................."
		print "El Articulo no existe. carlos = " + str(carlos)
		print "..................................................."
		return False

