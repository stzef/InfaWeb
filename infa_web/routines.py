from infa_web.parameters import ManageParameters

from infa_web.apps.articulos.models import Arlo
from infa_web.apps.inventarios.models import *
from infa_web.apps.movimientos.models import *

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

		if is_input:
			nuevo_costo_calculado = calculo_costo(articulo.canti,articulo.vcosto,nueva_cantidad,nuevo_costo,is_input)

			articulo.canti += nueva_cantidad
			articulo.vcosto = nuevo_costo_calculado
		else:
			articulo.canti -= nueva_cantidad

		articulo.save()

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
		print separador
		print articulo
		if Invinideta.objects.filter(cii=invinicab,carlos=articulo).exists():
			invinideta = Invinideta.objects.get(cii=invinicab,carlos=articulo)
		else:
			invinideta = None

		mvendeta = Mvendeta.objects.select_related().order_by('-cmven__fmven').filter(carlos=articulo)
		mvsadeta = Mvsadeta.objects.select_related().order_by('-cmvsa__fmvsa').filter(carlos=articulo)

		#print separador
		#print mvendeta
		#print separador
		#print mvsadeta
		print separador
		mv = list(mvendeta) + list(mvsadeta)
		print separador
		print mv
		print separador
		print invinideta
		##mv = Mven.objects.raw('SELECT movimientos_mven.*, movimientos_mvsa.* FROM movimientos_mven, movimientos_mvsa WHERE movimientos_mven.cmven.carlos_id = %s AND movimientos_mven.cmvsa.carlos_id = %s ORDER BY fmven,fmvsa', [articulo.pk,articulo.pk])
		for x in mv:
			print x
			print type(x)
			if hasattr(x, "cmeven"):
				calcular_costo_articulo(articulo.carlos,x.canti,x.vunita,True)
			else:
				calcular_costo_articulo(articulo.carlos,x.canti,x.vunita,False)
		print mv
	return True



