# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

from infa_web.apps.base.constantes import *
from infa_web.apps.base.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.articulos.models import *
class Command(BaseCommand):
	def handle(self, *args, **options):

		if 'APPEMPRESARIAL_USER' in os.environ:
			if not User.objects.filter(username=APPEMPRESARIAL_USER).exists():
				print "Super Usuario Creado Con exito."
				User.objects.create_superuser(APPEMPRESARIAL_USER, APPEMPRESARIAL_EMAIL, APPEMPRESARIAL_PASS)
			else:
				print "El Super Usuario ya Existe."
		else:
			print "No se encontro la variable de entorno APPEMPRESARIAL_USER."

		Tiarlos.objects.all().delete()
		Tiarlos.objects.create(ctiarlos=CTIARLO_ARTICULO,ntiarlos="ARTICULOS")
		Tiarlos.objects.create(ctiarlos=CTIARLO_SERVICIO,ntiarlos="SERVICIOS")
		Tiarlos.objects.create(ctiarlos=CTIARLO_OTRO,ntiarlos="OTROS")
		print "Tiarlos. Registros Creados Correctamente."
		
		
		Esdo.objects.all().delete()
		estadoActivo = Esdo.objects.create(nesdo="ACTIVO",estavali="T",colfon="255,255,255,255")
		Esdo.objects.create(nesdo="EN TRANSICION",estavali="T",colfon="255,255,255,255")
		Esdo.objects.create(nesdo="DESCOTINUADA",estavali="F",colfon="255,255,0,0")
		Esdo.objects.create(nesdo="CONGELADA",estavali="F",colfon="255,255,0,0")
		Esdo.objects.create(nesdo="CERRADA",estavali="T",colfon="255,255,255,255")
		Esdo.objects.create(nesdo="INTEGRIDAD",estavali="F",colfon="255,255,0,0")
		Esdo.objects.create(nesdo="ANULADA",estavali="F",colfon="255,255,0,0")
		print "Esdo. Registros Creados Correctamente."

		Regiva.objects.all().delete()
		Regiva.objects.create(nregiva="REGIMEN COMUN")
		Regiva.objects.create(nregiva="REGIMEN SIMPLIFICADO")
		print "Regiva. Registros Creados Correctamente."

		Tiide.objects.all().delete()
		Tiide.objects.create(ntiide="CEDULA DE CIUDADANIA")
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
		Autorre.objects.create(nautorre="NO AUTORRETENEDOR")
		Autorre.objects.create(nautorre="SI AUTORRETENEDOR")
		print "Autorre. Registros Creados Correctamente."

		Ruta.objects.all().delete()
		Ruta.objects.create(cruta=DEFAULT_RUTA,nruta="SIN RUTA",cesdo=estadoActivo)
		print "Ruta. Registros Creados Correctamente."

		Zona.objects.all().delete()
		Zona.objects.create(czona=DEFAULT_ZONA,nzona="SIN ZONA",cesdo=estadoActivo)
		print "Zona. Registros Creados Correctamente."

		Iva.objects.all().delete()
		Iva.objects.create(niva="SIN IVA",poriva=0,idtira="A",cesdo=estadoActivo)
		Iva.objects.create(niva="08%",poriva=8,idtira="B",cesdo=estadoActivo)
		Iva.objects.create(niva="10%",poriva=10,idtira="C",cesdo=estadoActivo)
		Iva.objects.create(niva="16%",poriva=16,idtira="D",cesdo=estadoActivo)
		Iva.objects.create(niva="EXENTO",poriva=0,idtira="E",cesdo=estadoActivo)
		print "Iva. Registros Creados Correctamente."

		Marca.objects.all().delete()
		Marca.objects.create(cmarca=DEFAULT_MARCAR,nmarca="SIN MARCA",cesdo=estadoActivo)
		print "Marca. Registros Creados Correctamente."

		Bode.objects.all().delete()
		Bode.objects.create(cbode=DEFAULT_BODEGA,nbode="SIN BODEGA",esbode=1,cesdo=estadoActivo)
		print "Bode. Registros Creados Correctamente."

		Ubica.objects.all().delete()
		Ubica.objects.create(cubica=DEFAULT_UBICACION,nubica="SIN UBICACION",cesdo=estadoActivo)
		print "Ubica. Registros Creados Correctamente."

		Gpo.objects.all().delete()
		Gpo.objects.create(cgpo=DEFAULT_GRUPO,ngpo="SIN GRUPO",cesdo=estadoActivo)
		print "Gpo. Registros Creados Correctamente."
		
		Departamento.objects.all().delete()
		departamento = Departamento.objects.create(cdepar=9,ndepar="Cundinamarca")
		print "Departamento. Registros Creados Correctamente."

		Ciudad.objects.all().delete()
		Ciudad.objects.create(nciu='Alban',cdepar=departamento)
		Ciudad.objects.create(nciu='Bogotá',cdepar=departamento)
		Ciudad.objects.create(nciu='Bojaca',cdepar=departamento)
		Ciudad.objects.create(nciu='Bosa',cdepar=departamento)
		Ciudad.objects.create(nciu='Briceño',cdepar=departamento)
		Ciudad.objects.create(nciu='Cajicá',cdepar=departamento)
		Ciudad.objects.create(nciu='Chía',cdepar=departamento)
		Ciudad.objects.create(nciu='Chinauta',cdepar=departamento)
		Ciudad.objects.create(nciu='Choconta',cdepar=departamento)
		Ciudad.objects.create(nciu='Cota',cdepar=departamento)
		Ciudad.objects.create(nciu='El Muña',cdepar=departamento)
		Ciudad.objects.create(nciu='El Rosal',cdepar=departamento)
		Ciudad.objects.create(nciu='Engativá',cdepar=departamento)
		Ciudad.objects.create(nciu='Facatativa',cdepar=departamento)
		Ciudad.objects.create(nciu='Fontibón',cdepar=departamento)
		Ciudad.objects.create(nciu='Funza',cdepar=departamento)
		Ciudad.objects.create(nciu='Fusagasuga',cdepar=departamento)
		Ciudad.objects.create(nciu='Gachancipá',cdepar=departamento)
		Ciudad.objects.create(nciu='Girardot',cdepar=departamento)
		Ciudad.objects.create(nciu='Guaduas',cdepar=departamento)
		Ciudad.objects.create(nciu='Guayavetal',cdepar=departamento)
		Ciudad.objects.create(nciu='La Calera',cdepar=departamento)
		Ciudad.objects.create(nciu='La Caro',cdepar=departamento)
		Ciudad.objects.create(nciu='Madrid',cdepar=departamento)
		Ciudad.objects.create(nciu='Mosquera',cdepar=departamento)
		Ciudad.objects.create(nciu='Nemocón',cdepar=departamento)
		Ciudad.objects.create(nciu='Puente Piedra',cdepar=departamento)
		Ciudad.objects.create(nciu='Puente Quetame',cdepar=departamento)
		Ciudad.objects.create(nciu='Puerto Bogotá',cdepar=departamento)
		Ciudad.objects.create(nciu='Puerto Salgar',cdepar=departamento)
		Ciudad.objects.create(nciu='Quetame',cdepar=departamento)
		Ciudad.objects.create(nciu='Sasaima',cdepar=departamento)
		Ciudad.objects.create(nciu='Sesquile',cdepar=departamento)
		Ciudad.objects.create(nciu='Sibaté',cdepar=departamento)
		Ciudad.objects.create(nciu='Silvania',cdepar=departamento)
		Ciudad.objects.create(nciu='Simijaca',cdepar=departamento)
		Ciudad.objects.create(nciu='Soacha',cdepar=departamento)
		Ciudad.objects.create(nciu='Sopo',cdepar=departamento)
		Ciudad.objects.create(nciu='Suba',cdepar=departamento)
		Ciudad.objects.create(nciu='Subachoque',cdepar=departamento)
		Ciudad.objects.create(nciu='Susa',cdepar=departamento)
		Ciudad.objects.create(nciu='Tabio',cdepar=departamento)
		Ciudad.objects.create(nciu='Tenjo',cdepar=departamento)
		Ciudad.objects.create(nciu='Tocancipa',cdepar=departamento)
		Ciudad.objects.create(nciu='Ubaté',cdepar=departamento)
		Ciudad.objects.create(nciu='Usaquén',cdepar=departamento)
		Ciudad.objects.create(nciu='Usme',cdepar=departamento)
		Ciudad.objects.create(nciu='Villapinzón',cdepar=departamento)
		Ciudad.objects.create(nciu='Villeta',cdepar=departamento)
		Ciudad.objects.create(nciu='Zipaquirá',cdepar=departamento)
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
