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
	if(Arlo.objects.filter(carlos=carlos).exists()):
		type_costing_and_stock = manageParameters.get_param_value("type_costing_and_stock")
		if(type_costing_and_stock == "M"):
			return False
		articulo = Arlo.objects.get(carlos=carlos)

		print "-------------------------"
		print "%s -> %s" % (articulo.canti,articulo.vcosto)

		if is_input:
			nuevo_costo_calculado = calculo_costo(articulo.canti,articulo.vcosto,nueva_cantidad,nuevo_costo,is_input)

			articulo.canti += nueva_cantidad
			articulo.vcosto = nuevo_costo_calculado
		else:
			articulo.canti -= nueva_cantidad

		articulo.save()
		print "%s -> %s" % (articulo.canti,articulo.vcosto)
		print "-------------------------"

		return True
	else:
		return False

def calculo_cantidad_costo():
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

		mv = list(mvendeta) + list(mvsadeta)
		if invinideta:
			for x in mv:
				if hasattr(x, "cmven"):
					calcular_costo_articulo(invinideta.carlos.carlos,x.canti,x.vtotal,True)
				else:
					calcular_costo_articulo(invinideta.carlos.carlos,x.canti,x.vtotal,False)
		else:
			print "El articulo no se encuentra en el inventario"
	return True



