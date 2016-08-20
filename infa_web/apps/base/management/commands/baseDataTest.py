# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

from infa_web.apps.base.constantes import *
from infa_web.apps.base.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.articulos.models import *
from django.db.models import Max
from infa_web.parameters import ManageParameters
import random


class Command(BaseCommand):
	def handle(self, *args, **options):

		Esdo.objects.all().delete()
		estadoActivo = Esdo.objects.create(pk='1',nesdo="ACTIVO",estavali="T")
		Esdo.objects.create(pk='2',nesdo="EN TRANSICION",estavali="T")
		Esdo.objects.create(pk='3',nesdo="DESCOTINUADA",estavali="F")
		Esdo.objects.create(pk='4',nesdo="CONGELADA",estavali="F")
		Esdo.objects.create(pk='5',nesdo="CERRADA",estavali="T")
		Esdo.objects.create(pk='6',nesdo="INTEGRIDAD",estavali="F")
		Esdo.objects.create(pk='7',nesdo="ANULADA",estavali="F")
		print "Esdo. Registros Creados Correctamente."

		if 'APPEMPRESARIAL_USER' in os.environ:
			if not User.objects.filter(username=APPEMPRESARIAL_USER).exists():
				print "Super Usuario Creado Con exito."
				User.objects.create_superuser(APPEMPRESARIAL_USER, APPEMPRESARIAL_EMAIL, APPEMPRESARIAL_PASS)
			else:
				print "El Super Usuario ya Existe."
		else:
			print "No se encontro la variable de entorno APPEMPRESARIAL_USER."

		Tiarlos.objects.all().delete()
		oDefaultTypeArticle = Tiarlos.objects.create(ctiarlos=CTIARLO_ARTICULO,ntiarlos="ARTICULOS")
		Tiarlos.objects.create(ctiarlos=CTIARLO_SERVICIO,ntiarlos="SERVICIOS")
		Tiarlos.objects.create(ctiarlos=CTIARLO_OTRO,ntiarlos="OTROS")
		print "Tiarlos. Registros Creados Correctamente."

		Personas.objects.all().delete()
		oDefaultPersona = Personas.objects.create(cpersona="PN",npersona="PERSONA NATURAL")
		Personas.objects.create(cpersona="PJ",npersona="PERSONA JURIDICA")
		print "Personas. Registros Creados Correctamente."

		Vende.objects.all().delete()
		oDefaultVende = Vende.objects.create(nvende="SIN VENDEDOR",porventa=0,cesdo=estadoActivo)
		print "Vende. Registros Creados Correctamente."

		Unidades.objects.all().delete()
		oDefaultUnidades = Unidades.objects.create(nunidad="UNIDADES",peso=0)
		Unidades.objects.create(nunidad="KILOGRAMOS",peso=0)
		Unidades.objects.create(nunidad="METROS",peso=0)
		Unidades.objects.create(nunidad="DOCENAS",peso=0)
		Unidades.objects.create(nunidad="CAJAS",peso=0)
		Unidades.objects.create(nunidad="DISPLAYS",peso=0)
		Unidades.objects.create(nunidad="PAQUETE",peso=0)
		Unidades.objects.create(nunidad="MILILITROS",peso=0)
		print "Unidades. Registros Creados Correctamente."


		Regiva.objects.all().delete()
		oDefaultRegIva = Regiva.objects.create(nregiva="REGIMEN COMUN")
		Regiva.objects.create(nregiva="REGIMEN SIMPLIFICADO")
		print "Regiva. Registros Creados Correctamente."

		Tiide.objects.all().delete()
		oDefaultType = Tiide.objects.create(ntiide="CEDULA DE CIUDADANIA")
		Tiide.objects.create(ntiide="NIT")
		Tiide.objects.create(ntiide="NUMERO UNICO DE IDENTIFICACION")
		print "Tiide. Registros Creados Correctamente."

		Modules.objects.all().delete()
		Modules.objects.create(smodule="I",nmodule="Inventarios",cesdo=estadoActivo,enabled_enterprise=True,enabled=True)
		Modules.objects.create(smodule="F",nmodule="Facturacion",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="P",nmodule="POS",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="CAR",nmodule="Cartera",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="CAJ",nmodule="Caja",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="CON",nmodule="Contabilidad",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="A",nmodule="Administracion",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="F",nmodule="Financiero",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		print "Modules. Registros Creados Correctamente."

		Autorre.objects.all().delete()
		oDefaultAutorretenedor = Autorre.objects.create(nautorre="NO AUTORRETENEDOR")
		Autorre.objects.create(nautorre="SI AUTORRETENEDOR")
		print "Autorre. Registros Creados Correctamente."

		Ruta.objects.all().delete()
		oDefaultRuta = Ruta.objects.create(nruta="SIN RUTA",cesdo=estadoActivo)
		print "Ruta. Registros Creados Correctamente."

		Zona.objects.all().delete()
		oDefaultZona= Zona.objects.create(nzona="SIN ZONA",cesdo=estadoActivo)
		print "Zona. Registros Creados Correctamente."

		Iva.objects.all().delete()
		oDefaultIva = Iva.objects.create(pk=1,niva="SIN IVA",poriva=0,idtira="A",cesdo=estadoActivo)
		Iva.objects.create(pk=2,niva="08%",poriva=8,idtira="B",cesdo=estadoActivo)
		Iva.objects.create(pk=3,niva="10%",poriva=10,idtira="C",cesdo=estadoActivo)
		Iva.objects.create(pk=4,niva="16%",poriva=16,idtira="D",cesdo=estadoActivo)
		Iva.objects.create(pk=5,niva="EXENTO",poriva=0,idtira="E",cesdo=estadoActivo)
		print "Iva. Registros Creados Correctamente."

		Marca.objects.all().delete()
		oDefaultMarca = Marca.objects.create(cmarca=DEFAULT_MARCA,nmarca="SIN MARCA",cesdo=estadoActivo)
		print "Marca. Registros Creados Correctamente."

		Bode.objects.all().delete()
		oDefaultBodega = Bode.objects.create(nbode="SIN BODEGA",esbode=1,cesdo=estadoActivo)
		print "Bode. Registros Creados Correctamente."

		Ubica.objects.all().delete()
		oDefaultLocation = Ubica.objects.create(nubica="SIN UBICACION",cesdo=estadoActivo)
		print "Ubica. Registros Creados Correctamente."

		Gpo.objects.all().delete()
		oDefaultGroup = Gpo.objects.create(cgpo=DEFAULT_GRUPO,ngpo="SIN GRUPO",cesdo=estadoActivo)
		print "Gpo. Registros Creados Correctamente."
		
		Departamento.objects.all().delete()
		oDefaultDepartament = Departamento.objects.create(cdepar=9,ndepar="Cundinamarca")
		print "Departamento. Registros Creados Correctamente."

		Ciudad.objects.all().delete()
		Ciudad.objects.create(pk=1,nciu='Alban',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=2,nciu='Bogotá',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=3,nciu='Bojaca',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=4,nciu='Bosa',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=5,nciu='Briceño',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=6,nciu='Cajicá',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=7,nciu='Chía',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=8,nciu='Chinauta',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=9,nciu='Choconta',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=10,nciu='Cota',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=11,nciu='El Muña',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=12,nciu='El Rosal',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=13,nciu='Engativá',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=14,nciu='Facatativa',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=15,nciu='Fontibón',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=16,nciu='Funza',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=17,nciu='Fusagasuga',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=18,nciu='Gachancipá',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=69,nciu='Girardot',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=19,nciu='Guaduas',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=20,nciu='Guayavetal',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=21,nciu='La Calera',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=22,nciu='La Caro',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=23,nciu='Madrid',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=24,nciu='Mosquera',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=25,nciu='Nemocón',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=26,nciu='Puente Piedra',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=27,nciu='Puente Quetame',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=28,nciu='Puerto Bogotá',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=29,nciu='Puerto Salgar',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=30,nciu='Quetame',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=31,nciu='Sasaima',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=32,nciu='Sesquile',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=33,nciu='Sibaté',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=34,nciu='Silvania',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=35,nciu='Simijaca',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=36,nciu='Soacha',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=37,nciu='Sopo',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=38,nciu='Suba',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=39,nciu='Subachoque',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=40,nciu='Susa',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=41,nciu='Tabio',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=42,nciu='Tenjo',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=43,nciu='Tocancipa',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=44,nciu='Ubaté',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=45,nciu='Usaquén',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=46,nciu='Usme',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=47,nciu='Villapinzón',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=48,nciu='Villeta',cdepar=oDefaultDepartament)
		Ciudad.objects.create(pk=49,nciu='Zipaquirá',cdepar=oDefaultDepartament)
		print "Cuidad. Registros Creados Correctamente."

		Timo.objects.all().delete()
		Timo.objects.create(ctimo=1000,ntimo="*** ENTRADA INVENTARIOS ***",prefijo="",filas=50,nrepo="")
		Timo.objects.create(ctimo=1001,ntimo="COMPRA MERCANCIA",prefijo="EA",filas=10,nrepo="R00504TXT")
		Timo.objects.create(ctimo=1002,ntimo="DEVOLUCIONES COMPRAS",prefijo="EB",filas=10,nrepo="R00504TXT")
		Timo.objects.create(ctimo=1003,ntimo="AJUSTE ENTRADA",prefijo="EC",filas=45,nrepo="R00504TXT")
		Timo.objects.create(ctimo=1004,ntimo="OTRAS ENTRADAS",prefijo="EC",filas=10,nrepo="R00504TXT")
		Timo.objects.create(ctimo=2000,ntimo="*** SALIDA INVENTARIOS ***",prefijo="",filas=0,nrepo="")
		Timo.objects.create(ctimo=2001,ntimo="SALIDAS MERCANCIA",prefijo="SA",filas=10,nrepo="R00604TXT")
		Timo.objects.create(ctimo=2002,ntimo="DEVOLUCIONES SALIDAS",prefijo="SB",filas=10,nrepo="R00604TXT")
		Timo.objects.create(ctimo=2003,ntimo="BAJAS MERCANCIA",prefijo="SC",filas=10,nrepo="R00604TXT")
		Timo.objects.create(ctimo=2004,ntimo="SALIDAS FACTURACION",prefijo="SD",filas=10,nrepo="R00604TXT")
		Timo.objects.create(ctimo=2005,ntimo="GASTOS ALMACEN",prefijo="SE",filas=10,nrepo="R00604TXT")
		Timo.objects.create(ctimo=2006,ntimo="AJUSTE SALIDA",prefijo="SF",filas=10,nrepo="R00604TXT")
		Timo.objects.create(ctimo=3000,ntimo="*** INGRESOS CAJA ***",prefijo="",filas=0,nrepo="")
		Timo.objects.create(ctimo=3001,ntimo="RECIBOS CAJA ABONOS FACTURAS",prefijo="IA",filas=10,nrepo="R01702WIN")
		Timo.objects.create(ctimo=3002,ntimo="RECIBO ABONOS EMPLEADOS",prefijo="IB",filas=1,nrepo="R01702WIN")
		Timo.objects.create(ctimo=3003,ntimo="PRESTAMOS TERCEROS",prefijo="IC",filas=10,nrepo="R01702WIN")
		Timo.objects.create(ctimo=3008,ntimo="INGRESOS VARIOS",prefijo="IH",filas=10,nrepo="R01702WIN")
		Timo.objects.create(ctimo=3100,ntimo="**** EGRESOS CAJA ****",prefijo="",filas=0,nrepo="")
		Timo.objects.create(ctimo=3101,ntimo="PAGO PROVEEDORES",prefijo="GA",filas=10,nrepo="R02102TXT")
		Timo.objects.create(ctimo=3102,ntimo="PRESTAMOS EMPLEADOS",prefijo="GB",filas=10,nrepo="R02102TXT")
		Timo.objects.create(ctimo=3103,ntimo="LABORES MENSUALES",prefijo="GC",filas=10,nrepo="R02102TXT")
		Timo.objects.create(ctimo=3104,ntimo="SERVICIOS PUBLICOS",prefijo="GD",filas=10,nrepo="R02102TXT")
		Timo.objects.create(ctimo=3105,ntimo="GASTOS ARRIENDO",prefijo="GE",filas=10,nrepo="R02102TXT")
		Timo.objects.create(ctimo=3106,ntimo="GASTO VEHICULO",prefijo="GF",filas=10,nrepo="R02102TXT")
		Timo.objects.create(ctimo=3107,ntimo="COMISIONES",prefijo="GH",filas=10,nrepo="R02102TXT")
		Timo.objects.create(ctimo=3108,ntimo="DOTACION",prefijo="GI",filas=10,nrepo="R02102TXT")
		Timo.objects.create(ctimo=3109,ntimo="PAGO PRESTAMOS TERCEROS",prefijo="GJ",filas=10,nrepo="R02102TXT")
		Timo.objects.create(ctimo=3110,ntimo="EGRESOS VARIOS",prefijo="GJ",filas=10,nrepo="R02102TXT")
		Timo.objects.create(ctimo=4000,ntimo="*** CARGOS CARTERA COBRAR ***",prefijo="",filas=0,nrepo="")
		Timo.objects.create(ctimo=4001,ntimo="SALDO CXC",prefijo="CA",filas=1,nrepo="R01701WIN")
		Timo.objects.create(ctimo=4002,ntimo="CARGOS CXC",prefijo="CB",filas=10,nrepo="R01701WIN")
		Timo.objects.create(ctimo=4003,ntimo="OTROS CARGOS CXC",prefijo="CC",filas=10,nrepo="R01701WIN")
		Timo.objects.create(ctimo=4100,ntimo="*** ABONOS CARTERA COBRAR ***",prefijo="",filas=0,nrepo="")
		Timo.objects.create(ctimo=4101,ntimo="ABONOS CXC",prefijo="OA",filas=5,nrepo="R01701WIN")
		Timo.objects.create(ctimo=4102,ntimo="OTROS ABONOS CXC",prefijo="OB",filas=5,nrepo="R01701WIN")
		Timo.objects.create(ctimo=4200,ntimo="*** CARGOS CARTERA PAGAR ***",prefijo="",filas=0,nrepo="")
		Timo.objects.create(ctimo=4201,ntimo="SALDO CXP",prefijo="RA",filas=1,nrepo="R01701WIN")
		Timo.objects.create(ctimo=4202,ntimo="CARGOS CXP",prefijo="RB",filas=1,nrepo="R01701WIN")
		Timo.objects.create(ctimo=4203,ntimo="OTROS CARGOS CXP",prefijo="RC",filas=1,nrepo="R01701WIN")
		Timo.objects.create(ctimo=4300,ntimo="*** ABONOS CARTERA PAGAR ***",prefijo="",filas=0,nrepo="")
		Timo.objects.create(ctimo=4301,ntimo="ABONOS CXP",prefijo="PA",filas=1,nrepo="R01701WIN")
		Timo.objects.create(ctimo=4302,ntimo="OTROS ABONOS CXP",prefijo="PB",filas=1,nrepo="R01701WIN")
		Timo.objects.create(ctimo=4400,ntimo="***Servicios Tecnicos***",prefijo="",filas=0,nrepo="")
		Timo.objects.create(ctimo=4401,ntimo="SERVICIOS",prefijo="TA",filas=0,nrepo="r141_win")
		print "Timo. Registros Creados Correctamente."
		
		Arlo.objects.all().delete()
		numberOfArlos = 100
		for index in xrange(1,numberOfArlos):
			print "Arlo. Registros Creados Correctamente. Registro " + str(index) + "/" + str(numberOfArlos)

			maxCarlos = Arlo.objects.aggregate(Max('carlos'))

			manageParameters = ManageParameters()
			minCodeArlos = manageParameters.get_param_value("min_code_arlos")

			if maxCarlos["carlos__max"]:
				carlos = maxCarlos["carlos__max"] + 1
			else:
				carlos = minCodeArlos

			canti = random.randrange(1,10)
			costo = random.random()*50000

			stomin = random.randrange(1,5)
			stomax = random.randrange(5,10)
			Arlo.objects.create(
				carlos=carlos,
				cbarras="Codigo de Barras " + str(index),
				cgpo=oDefaultGroup,
				ncorto="Nombre Corto " + str(index),
				nlargo="Nombre Largo Descripcion " + str(index),
				canti=canti,
				vcosto=costo,
				ifcostear=True,
				ifpvfijo=False,
				cesdo=estadoActivo,
				ctiarlo=oDefaultTypeArticle,
				cunidad=oDefaultUnidades,
				ivas_civa=oDefaultIva,
				stomin=stomin,
				stomax=stomax,
				pvta1=5000,
				pvta2=0,
				pvta3=0,
				pvta4=0,
				pvta5=0,
				pvta6=0,
				#citerce1="",
				#vcosto1="",
				#fcosto1="",
				#citerce2="",
				#vcosto2="",
				#fcosto2="",
				#citerce3="",
				#vcosto3="",
				#fcosto3="",
				ifedinom=False,
				refe="Referencia " + str(index),
				cmarca=oDefaultMarca,
				ifdesglo=False,
				mesesgara=10,
				cubica=oDefaultLocation,
				porult1=10,
				porult2=0,
				porult3=0,
				porult4=0,
				porult5=0,
				porult6=0,
				foto1=DEFAULT_IMAGE_ARTICLE,
				foto2=DEFAULT_IMAGE_ARTICLE,
				foto3=DEFAULT_IMAGE_ARTICLE,
			)
