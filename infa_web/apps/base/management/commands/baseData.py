# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os
from infa_web.parameters import ManageParameters

from infa_web.apps.base.constantes import *
from infa_web.apps.base.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.articulos.models import *
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
		Unidades.objects.create(pk=1,nunidad="UNIDADES",peso=0)
		Unidades.objects.create(pk=2,nunidad="KILOGRAMOS",peso=0)
		Unidades.objects.create(pk=3,nunidad="METROS",peso=0)
		Unidades.objects.create(pk=4,nunidad="DOCENAS",peso=0)
		Unidades.objects.create(pk=5,nunidad="CAJAS",peso=0)
		Unidades.objects.create(pk=6,nunidad="DISPLAYS",peso=0)
		Unidades.objects.create(pk=7,nunidad="PAQUETE",peso=0)
		Unidades.objects.create(pk=8,nunidad="MILILITROS",peso=0)

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
		Marca.objects.create(cmarca=1, nmarca='ABSOLUT', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=2, nmarca='ADAMS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=3, nmarca='ADAN', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=4, nmarca='AGUA TROPICAL', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=5, nmarca='AGUILA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=6, nmarca='ALASKA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=7, nmarca='ALEJANDRIA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=8, nmarca='ALEXANDER MAC GREGOR', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=9, nmarca='ALPINA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=10, nmarca='AMWAY', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=11, nmarca='ANDRE CELLARS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=12, nmarca='ANTIOQUEÑO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=13, nmarca='ARBOR MIST', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=14, nmarca='AROMO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=15, nmarca='AUSTIN NICHOLS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=16, nmarca='BACARDI', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=17, nmarca='BAILEYS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=18, nmarca='BELLA TAVOLA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=19, nmarca='BIC', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=20, nmarca='BIG COLA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=21, nmarca='BODEGAS AÑEJAS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=22, nmarca='BUDWAISER', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=23, nmarca='CANDIOTA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=24, nmarca='CARIÑOSO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=25, nmarca='CASA CUERVO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=26, nmarca='CASA GRAJALES', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=27, nmarca='CASA TEQUILERA DE ARANDAS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=28, nmarca='CASA VIEJA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=29, nmarca='CASANOVA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=30, nmarca='CASILLERO DEL DIABLO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=31, nmarca='CASTLE HOUSE', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=32, nmarca='CELEBRACION', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=33, nmarca='CHAO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=34, nmarca='CHARLES TANQUERAY', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=35, nmarca='CHIVAS BROTHERS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=36, nmarca='CINZANO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=37, nmarca='CIROC', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=38, nmarca='CLUB COLOMBIA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=39, nmarca='COLANTA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=40, nmarca='COLOMA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=41, nmarca='COLOMBINA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=42, nmarca='COLTABACO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=43, nmarca='CONVIER', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=44, nmarca='CORONA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=45, nmarca='CRISTAL', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=46, nmarca='DE LA SABANA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=47, nmarca='DESECHABLES', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=48, nmarca='DICERMEX', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=49, nmarca='DOM PERIGNON', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=50, nmarca='DON JULIO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=51, nmarca='DROGAS LA REBAJA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=52, nmarca='DUBONNET', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=53, nmarca='EMBOTELLADORA CAPRI LTDA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=54, nmarca='ESTORIL', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=55, nmarca='ETCHART', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=56, nmarca='EXCELSO CREMA DE CAFÉ ', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=57, nmarca='FABRYCAMIL', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=58, nmarca='FEMSA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=59, nmarca='FOSFOROS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=60, nmarca='FREIXENET', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=61, nmarca='FRITO LAY', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=62, nmarca='FRONTERA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=63, nmarca='GATO NEGRO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=64, nmarca='GEORGE BALLANTINE & SON', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=65, nmarca='GLEN MORANGIE', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=66, nmarca='GLEND ORD', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=67, nmarca='GORDONS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=68, nmarca='GRAFIGNA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=69, nmarca='GRAN BRINDIS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=70, nmarca='GRAND OLD PARR', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=71, nmarca='GRAND PRIX', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=72, nmarca='GRISSLY', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=73, nmarca='GROLSCH', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=74, nmarca='GROSSO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=75, nmarca='HALLS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=76, nmarca='HAVANA CLUB', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=77, nmarca='HAWAI', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=78, nmarca='HEINEKEN', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=79, nmarca='HIELO DON GARCIA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=80, nmarca='IMPORTADO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=81, nmarca='IMPORTADORA Y PRODUCTORA DE LICORES', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=82, nmarca='ISABELA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=83, nmarca='ISLEÑA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=84, nmarca='J&B', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=85, nmarca='JACK DANIELS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=86, nmarca='JAMES BUCHANANS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=87, nmarca='JAMES BURROUGH', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=88, nmarca='JAS HENESSY', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=89, nmarca='JHON THOMAS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=90, nmarca='JOHN HAIG', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=91, nmarca='JOHN JAMESON', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=92, nmarca='JOHNNY WALKER', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=93, nmarca='JONH RESTREPO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=94, nmarca='JP', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=95, nmarca='KATICH', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=96, nmarca='KETEL ONE', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=97, nmarca='KOLA SOL', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=98, nmarca='KOOL', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=99, nmarca='KORSAKOF', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=100, nmarca='LA HUERTA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=101, nmarca='LA NACIONAL DE CHOCOLATES', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=102, nmarca='LAZO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=103, nmarca='LOGISTICA AGIL S.A.', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=104, nmarca='MANI LA ESPECIAL', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=105, nmarca='MANISCHEWITZ', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=106, nmarca='MARTELL', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=107, nmarca='MEDELLIN', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=108, nmarca='MILLER', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=109, nmarca='MOET & CHANDON', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=110, nmarca='MONSTER', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=111, nmarca='MOSCATEL DE PASAS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=112, nmarca='MOSCATO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=113, nmarca='MUMM', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=114, nmarca='NAVARRO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=115, nmarca='NAVISCO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=116, nmarca='NECTAR', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=117, nmarca='NESTLE', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=118, nmarca='NOEL', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=119, nmarca='NUTRESA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=120, nmarca='OCHAGAVIA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=121, nmarca='OLMECA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=122, nmarca='PATRON SPIRITS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=123, nmarca='PEDRO DOMECQ', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=124, nmarca='PETERLONGO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=125, nmarca='PIERLANT', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=126, nmarca='POKER', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=127, nmarca='POLMOS ZYRARDOW IN', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=128, nmarca='PONY MALTA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=129, nmarca='POSTOBON', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=130, nmarca='PROTABACO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=131, nmarca='QUALA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=132, nmarca='RAMO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=133, nmarca='RED BULL', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=134, nmarca='REEDS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=135, nmarca='REGINA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=136, nmarca='RITZ', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=137, nmarca='RIVELINO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=138, nmarca='ROMATE', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=139, nmarca='SABAJON APOLO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=140, nmarca='SAGATIBA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=141, nmarca='SAN JULIAN', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=142, nmarca='SANSON', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=143, nmarca='SANTA CAROLINA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=144, nmarca='SANTA CLARA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=145, nmarca='SANTA RITA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=146, nmarca='SANTAFE', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=147, nmarca='SANTERO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=148, nmarca='SELLO DORADO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=149, nmarca='SENDERO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=150, nmarca='SMIRNOFF', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=151, nmarca='SOHO LYCHEE', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=152, nmarca='SOMETHING', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=153, nmarca='SPLENDA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=154, nmarca='SUPER', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=155, nmarca='SUPER RICAS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=156, nmarca='TAMESIS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=157, nmarca='TAPA ROJA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=158, nmarca='THE BOMBAY SPIRITS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=159, nmarca='TIC TAC', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=160, nmarca='TIO PEPE', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=161, nmarca='TRES ESQUINAS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=162, nmarca='UNDURRAGA', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=163, nmarca='VEUVE CLICQUOT', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=164, nmarca='VIEJO DE CALDAS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=165, nmarca='VIÑA MAIPO', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=166, nmarca='WHISKREAM', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=167, nmarca='WILD GRAPE', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=168, nmarca='WILLIAM GRANT & SONS', cesdo=Esdo.objects.get(pk=1))
		Marca.objects.create(cmarca=169, nmarca='ZACAPA', cesdo=Esdo.objects.get(pk=1))

		print "Marca. Registros Creados Correctamente."

		Bode.objects.all().delete()
		oDefaultBodega = Bode.objects.create(nbode="SIN BODEGA",esbode=1,cesdo=estadoActivo)
		print "Bode. Registros Creados Correctamente."

		Ubica.objects.all().delete()
		Ubica.objects.create(pk=1000,nubica="SIN UBICACION",cesdo=estadoActivo)
		print "Ubica. Registros Creados Correctamente."

		Gpo.objects.all().delete()
		oDefaultGroup = Gpo.objects.create(cgpo=DEFAULT_GRUPO,ngpo="SIN GRUPO",cesdo=estadoActivo)
		Gpo.objects.create(cgpo=1,ngpo='AGUARDIENTE',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=2,ngpo='BRANDY',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=3,ngpo='CACHAZA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=4,ngpo='CERVEZA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=5,ngpo='CHAMPAÑA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=6,ngpo='CIGARRILLOS',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=7,ngpo='COCTELERIA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=8,ngpo='COGNAC',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=9,ngpo='CONFITERIA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=10,ngpo='CREMA DE CAFÉ',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=11,ngpo='CREMA DE WHISKY',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=12,ngpo='ENCENDEDORES',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=13,ngpo='ENERGIZANTES',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=14,ngpo='FARMACIA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=15,ngpo='GASEOSA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=16,ngpo='GINEBRA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=17,ngpo='HIDRATANTES',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=18,ngpo='JEREZ',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=19,ngpo='LACTEOS',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=20,ngpo='LYCHHE',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=21,ngpo='MANZANILLA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=22,ngpo='MARTINI',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=23,ngpo='PASABOCAS',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=24,ngpo='PIÑA COLADA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=25,ngpo='PLASTICOS Y DESECHABLES',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=26,ngpo='RON',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=27,ngpo='SABAJON',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=28,ngpo='SALSAMENTARIA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=29,ngpo='SANGRIA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=30,ngpo='TEQUILA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=31,ngpo='TRIPLE SEC',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=32,ngpo='VINO DE MANZANA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=33,ngpo='VINO DULCE',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=34,ngpo='VINO ESPUMOSO',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=35,ngpo='VINO EXTRASECO',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=36,ngpo='VINO MOSCATEL',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=37,ngpo='VINO SECO',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=38,ngpo='VINO SEMISECO',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=39,ngpo='VODKA',  cesdo=Esdo.objects.get(pk=1))
		Gpo.objects.create(cgpo=40,ngpo='WHISKY',  cesdo=Esdo.objects.get(pk=1))

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

		manageParameters = ManageParameters()

		Tercero.objects.all().delete()
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
			fnaci = manageParameters.get_param_value("date_appen"),
			ordenruta = 1,
			ciudad = Ciudad.objects.get(pk=DEFAULT_CIUDAD),
			cesdo = estadoActivo,
			cvende = Vende.objects.get(pk=DEFAULT_VENDE),
			czona = Zona.objects.get(pk=DEFAULT_ZONA),
			cruta = Ruta.objects.get(pk=DEFAULT_RUTA),
			cpersona = Personas.objects.get(pk=DEFAULT_PERSONA),
			cautorre = Autorre.objects.get(pk=CESTADO_AUTORRETENEDOR),
			cregiva = Regiva.objects.get(pk=DEFAULT_REGIMEN_IVA),
			ctiide = Tiide.objects.get(pk=DEFAULT_TIIDE),
		)

