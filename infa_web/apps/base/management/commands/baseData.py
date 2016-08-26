# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os
from infa_web.parameters import ManageParameters
from datetime import datetime

from infa_web.apps.base.constantes import *
from infa_web.apps.base.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.articulos.models import *
class Command(BaseCommand):
	def handle(self, *args, **options):
		Esdo.objects.all().delete()
		Tiarlos.objects.all().delete()
		Personas.objects.all().delete()
		Vende.objects.all().delete()
		Unidades.objects.all().delete()
		Regiva.objects.all().delete()
		Tiide.objects.all().delete()
		Modules.objects.all().delete()
		Autorre.objects.all().delete()
		Ruta.objects.all().delete()
		Zona.objects.all().delete()
		Iva.objects.all().delete()
		Marca.objects.all().delete()
		Bode.objects.all().delete()
		Ubica.objects.all().delete()
		Gpo.objects.all().delete()
		Departamento.objects.all().delete()
		Ciudad.objects.all().delete()
		Timo.objects.all().delete()
		Tercero.objects.all().delete()


		estadoActivo = Esdo.objects.create(nesdo="ACTIVO",estavali="T")
		Esdo.objects.create(nesdo="EN TRANSICION",estavali="T")
		Esdo.objects.create(nesdo="DESCOTINUADA",estavali="F")
		Esdo.objects.create(nesdo="CONGELADA",estavali="F")
		Esdo.objects.create(nesdo="CERRADA",estavali="T")
		Esdo.objects.create(nesdo="INTEGRIDAD",estavali="F")
		Esdo.objects.create(nesdo="ANULADA",estavali="F")
		print "Esdo. Registros Creados Correctamente."

		if 'APPEMPRESARIAL_USER' in os.environ:
			if not User.objects.filter(username=APPEMPRESARIAL_USER).exists():
				print "Super Usuario Creado Con exito."
				User.objects.create_superuser(APPEMPRESARIAL_USER, APPEMPRESARIAL_EMAIL, APPEMPRESARIAL_PASS)
			else:
				print "El Super Usuario ya Existe."
		else:
			print "No se encontro la variable de entorno APPEMPRESARIAL_USER."

		Tiarlos.objects.create(ctiarlos=CTIARLO_ARTICULO,ntiarlos="ARTICULOS")
		Tiarlos.objects.create(ctiarlos=CTIARLO_SERVICIO,ntiarlos="SERVICIOS")
		Tiarlos.objects.create(ctiarlos=CTIARLO_OTRO,ntiarlos="OTROS")
		print "Tiarlos. Registros Creados Correctamente."

		Personas.objects.create(cpersona="PN",npersona="PERSONA NATURAL")
		Personas.objects.create(cpersona="PJ",npersona="PERSONA JURIDICA")
		print "Personas. Registros Creados Correctamente."

		Vende.objects.create(nvende="SIN VENDEDOR",porventa=0,cesdo=estadoActivo)
		print "Vende. Registros Creados Correctamente."

		Unidades.objects.create(nunidad="UNIDADES",peso=0)
		Unidades.objects.create(nunidad="KILOGRAMOS",peso=0)
		Unidades.objects.create(nunidad="METROS",peso=0)
		Unidades.objects.create(nunidad="DOCENAS",peso=0)
		Unidades.objects.create(nunidad="CAJAS",peso=0)
		Unidades.objects.create(nunidad="DISPLAYS",peso=0)
		Unidades.objects.create(nunidad="PAQUETE",peso=0)
		Unidades.objects.create(nunidad="MILILITROS",peso=0)

		print "Unidades. Registros Creados Correctamente."


		Regiva.objects.create(nregiva="REGIMEN COMUN")
		Regiva.objects.create(nregiva="REGIMEN SIMPLIFICADO")
		print "Regiva. Registros Creados Correctamente."

		Tiide.objects.create(ntiide="CEDULA DE CIUDADANIA")
		Tiide.objects.create(ntiide="NIT")
		Tiide.objects.create(ntiide="NUMERO UNICO DE IDENTIFICACION")
		print "Tiide. Registros Creados Correctamente."

		Modules.objects.create(smodule="I",nmodule="Inventarios",cesdo=estadoActivo,enabled_enterprise=True,enabled=True)
		Modules.objects.create(smodule="F",nmodule="Facturacion",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="P",nmodule="POS",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="CAR",nmodule="Cartera",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="CAJ",nmodule="Caja",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="CON",nmodule="Contabilidad",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="A",nmodule="Administracion",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		Modules.objects.create(smodule="F",nmodule="Financiero",cesdo=estadoActivo,enabled_enterprise=True,enabled=False)
		print "Modules. Registros Creados Correctamente."

		Autorre.objects.create(nautorre="NO AUTORRETENEDOR")
		Autorre.objects.create(nautorre="SI AUTORRETENEDOR")
		print "Autorre. Registros Creados Correctamente."

		Ruta.objects.create(nruta="SIN RUTA",cesdo=estadoActivo)
		print "Ruta. Registros Creados Correctamente."

		Zona.objects.create(nzona="SIN ZONA",cesdo=estadoActivo)
		print "Zona. Registros Creados Correctamente."

		Iva.objects.create(niva="SIN IVA",poriva=0,idtira="A",cesdo=estadoActivo)
		Iva.objects.create(niva="08%",poriva=8,idtira="B",cesdo=estadoActivo)
		Iva.objects.create(niva="10%",poriva=10,idtira="C",cesdo=estadoActivo)
		Iva.objects.create(niva="16%",poriva=16,idtira="D",cesdo=estadoActivo)
		Iva.objects.create(niva="EXENTO",poriva=0,idtira="E",cesdo=estadoActivo)
		print "Iva. Registros Creados Correctamente."

		Marca.objects.create(nmarca="SIN MARCA",cesdo=estadoActivo)
		print "Marca. Registros Creados Correctamente."

		Bode.objects.create(nbode="SIN BODEGA",esbode=1,cesdo=estadoActivo)
		print "Bode. Registros Creados Correctamente."

		Ubica.objects.create(nubica="SIN UBICACION",cesdo=estadoActivo)
		print "Ubica. Registros Creados Correctamente."

		Gpo.objects.create(cgpo=DEFAULT_GRUPO,ngpo="SIN GRUPO",cesdo=estadoActivo)
		print "Gpo. Registros Creados Correctamente."
		
		oDefaultDepartament = Departamento.objects.create(cdepar=9,ndepar="Cundinamarca")
		print "Departamento. Registros Creados Correctamente."

		Ciudad.objects.create(nciu='Alban',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Bogotá',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Bojaca',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Bosa',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Briceño',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Cajicá',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Chía',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Chinauta',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Choconta',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Cota',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='El Muña',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='El Rosal',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Engativá',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Facatativa',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Fontibón',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Funza',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Fusagasuga',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Gachancipá',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Girardot',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Guaduas',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Guayavetal',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='La Calera',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='La Caro',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Madrid',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Mosquera',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Nemocón',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Puente Piedra',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Puente Quetame',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Puerto Bogotá',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Puerto Salgar',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Quetame',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Sasaima',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Sesquile',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Sibaté',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Silvania',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Simijaca',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Soacha',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Sopo',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Suba',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Subachoque',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Susa',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Tabio',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Tenjo',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Tocancipa',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Ubaté',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Usaquén',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Usme',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Villapinzón',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Villeta',cdepar=oDefaultDepartament)
		Ciudad.objects.create(nciu='Zipaquirá',cdepar=oDefaultDepartament)
		print "Cuidad. Registros Creados Correctamente."

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

		manageParameters = ManageParameters()
		
		Tercero.objects.create(
			citerce = 0,
			idterce = 0,
			dv = 0,
			rasocial = "MOSTRADOR",
			nomcomer = "MOSTRADOR",
			ape1 = "MOSTRADOR",
			ape2 = "MOSTRADOR",
			nom1 = "MOSTRADOR",
			nom2 = "MOSTRADOR",
			sigla = "M",
			replegal = "MOSTRADOR",
			dirterce = "Direccion",
			telterce = 00000000,
			faxterce = 000000,
			email = "no_email@gmail.com",
			contacto = "xxxxxxxxxxxx",
			topcxc = 2,
			clipre = DEFAULT_LISTA_PRECIOS,
			fnaci = datetime.strptime(manageParameters.get_param_value("date_appen"),'%Y/%m/%d %H:%M:%S'),
			ordenruta = 1,
			ciudad = Ciudad.objects.get(pk=DEFAULT_CIUDAD),
			cesdo = estadoActivo,
			cvende = Vende.objects.get(pk=DEFAULT_VENDE),
			czona = Zona.objects.get(pk=DEFAULT_ZONA),
			cruta = Ruta.objects.get(pk=DEFAULT_RUTA),
			cpersona = Personas.objects.get(pk=DEFAULT_PERSONA),
			cautorre = Autorre.objects.get(pk=DEFAULT_AUTORRETENEDOR),
			cregiva = Regiva.objects.get(pk=DEFAULT_REGIMEN_IVA),
			ctiide = Tiide.objects.get(pk=DEFAULT_TIIDE),
		)
		

