# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from infa_web.apps.restaurante_menus.models import Ingredientes, GposMenus
from infa_web.apps.restaurante_comandas.models import Platos, Platosdeta, Menus, Menusdeta
from infa_web.apps.articulos.models import Unidades
from infa_web.apps.base.models import Esdo
from infa_web.apps.base.constantes import DEFAULT_IMAGE_DISHES, DEFAULT_IMAGE_MENUS

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument(
			'--database',
			action='store',
			dest='database',
			default="default",
			help='DB for connection',
		)
	def gvting(self,ing):
		valores = [i.vcosto for i in ing]
		return sum(valores)
	def gvtpla(self,pla):
		valores = [p.vttotal for p in pla]
		return sum(valores)
	def handle(self, *args, **options):

		name_db =  options["database"]
		print "DB Actual '%s'" % name_db
		confirmation = raw_input("Seguro? (Si/No) ")

		if(confirmation == "Si"):
			Ingredientes.objects.using(name_db).all().delete()
			Platos.objects.using(name_db).all().delete()
			Platosdeta.objects.using(name_db).all().delete()
			Menus.objects.using(name_db).all().delete()
			Menusdeta.objects.using(name_db).all().delete()
			GposMenus.objects.using(name_db).all().delete()
			print "Ingredientes, Platos, Platosdeta, Menus, GposMenus y Menusdeta Borrados"


			unidad = Unidades.objects.using(name_db).get(cunidad=1)
			estado = Esdo.objects.using(name_db).get(cesdo=1)

			gpizza_tradicional = GposMenus.objects.using(name_db).create(cgpomenu = 4,ngpomenu='Tradicional')
			gpizza_premium = GposMenus.objects.using(name_db).create(cgpomenu = 5,ngpomenu='Premium')
			gpizza_familiar = GposMenus.objects.using(name_db).create(cgpomenu = 7,ngpomenu='Pizza Familiar')
			glasana = GposMenus.objects.using(name_db).create(cgpomenu = 8,ngpomenu='Lasaña')
			ghamburguesas = GposMenus.objects.using(name_db).create(cgpomenu = 6,ngpomenu='Roma Burguer')
			gperros_calientes = GposMenus.objects.using(name_db).create(cgpomenu = 10,ngpomenu='Perros Calientes')
			gsalchipapa = GposMenus.objects.using(name_db).create(cgpomenu = 9,ngpomenu='Salchipapa')
			gsandwich = GposMenus.objects.using(name_db).create(cgpomenu = 11,ngpomenu='Sandwiches')
			gpatacones = GposMenus.objects.using(name_db).create(cgpomenu = 12,ngpomenu='Patacones')
			gburritos = GposMenus.objects.using(name_db).create(cgpomenu = 13,ngpomenu='Burritos')
			gadicionales = GposMenus.objects.using(name_db).create(cgpomenu = 14,ngpomenu='Adicionales')
			gbebidas = GposMenus.objects.using(name_db).create(cgpomenu = 15,ngpomenu='Bebidas')
			ghelado = GposMenus.objects.using(name_db).create(cgpomenu = 16,ngpomenu='Helados')
			gensalada_frutas = GposMenus.objects.using(name_db).create(cgpomenu = 17,ngpomenu='Ensalada de frutas')

			print "Procesando ..."

			#PIZZA TRADICIONAL
			menu_1 = Menus.objects.using(name_db).create(cmenu=1000, nmenu="PIZZA DE LA CASA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_tradicional, npax=1, pvta1=6000, pvta2=6000, pvta3=6000, vttotal=6000, foto="img/menus/menu_1000.jpg")
			menu_2 = Menus.objects.using(name_db).create(cmenu=1001, nmenu="PIZZA DE CARNE", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_tradicional,	npax=1, pvta1=6000, pvta2=6000, pvta3=6000, vttotal=6000, foto="img/menus/menu_1001.jpg")
			menu_3 = Menus.objects.using(name_db).create(cmenu=1002, nmenu="PIZZA DE POLLO CON CHAMPIÑONES", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_tradicional,	npax=1, pvta1=6000, pvta2=6000, pvta3=6000, vttotal=6000, foto="img/menus/menu_1002.jpg")
			menu_4 = Menus.objects.using(name_db).create(cmenu=1003, nmenu="PIZZA DE POLLO CON MAIZ TIERNO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_tradicional, npax=1, pvta1=6000, pvta2=6000, pvta3=6000, vttotal=6000, foto="img/menus/menu_1003.jpg")
			menu_5 = Menus.objects.using(name_db).create(cmenu=1004, nmenu="PIZZA POLLO CON JAMON ", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_tradicional, npax=1, pvta1=6000, pvta2=6000, pvta3=6000, vttotal=6000, foto="img/menus/menu_1004.jpg")
			menu_6 = Menus.objects.using(name_db).create(cmenu=1005, nmenu="PIZZA HAWAIANA ", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_tradicional, npax=1, pvta1=6000, pvta2=6000, pvta3=6000, vttotal=6000, foto="img/menus/menu_1005.jpg")
			menu_7 = Menus.objects.using(name_db).create(cmenu=1006, nmenu="PIZZA NAPOLITANA ", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_tradicional, npax=1, pvta1=6000, pvta2=6000, pvta3=6000, vttotal=6000, foto="img/menus/menu_1006.jpg")
			menu_8 = Menus.objects.using(name_db).create(cmenu=1007, nmenu="PIZZA MEXICANA ", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_tradicional, npax=1, pvta1=6000, pvta2=6000, pvta3=6000, vttotal=6000, foto="img/menus/menu_1007.jpg")
			#PIZZA PREMIUM
			menu_9 = Menus.objects.using(name_db).create(cmenu=1008, nmenu="PIZZA RANCH POLLO Y TOCINETA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=8000, pvta2=8000, pvta3=8000, vttotal=8000, foto="img/menus/menu_1008.jpg")
			menu_10 = Menus.objects.using(name_db).create(cmenu=1009, nmenu="PIZZA NORTEÑA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=9000, pvta2=9000, pvta3=9000, vttotal=9000, foto="img/menus/menu_1009.jpg")
			menu_11 = Menus.objects.using(name_db).create(cmenu=1010, nmenu="PIZZA HOT", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=9000, pvta2=9000, pvta3=9000, vttotal=9000, foto="img/menus/menu_1010.jpg")
			menu_12 = Menus.objects.using(name_db).create(cmenu=1011, nmenu="PIZZA CRIOLLA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium,	npax=1, pvta1=8800, pvta2=8800, pvta3=8800, vttotal=8800, foto="img/menus/menu_1011.jpg")
			menu_13 = Menus.objects.using(name_db).create(cmenu=1012, nmenu="PIZZA HAWAIANA-POLLO-BBQ", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=9000, pvta2=9000, pvta3=9000, vttotal=9000, foto="img/menus/menu_1012.jpg")
			menu_14 = Menus.objects.using(name_db).create(cmenu=1013, nmenu="PIZZA PEPPERONI", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=9800, pvta2=9800, pvta3=9800, vttotal=9800, foto="img/menus/menu_1013.jpg")
			menu_15 = Menus.objects.using(name_db).create(cmenu=1014, nmenu="PIZZA POMODORO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=6500, pvta2=6500, pvta3=6500, vttotal=6500, foto="img/menus/menu_1014.jpg")
			menu_16 = Menus.objects.using(name_db).create(cmenu=1015, nmenu="PIZZA RANCH", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=7500, pvta2=7500, pvta3=7500, vttotal=7500, foto="img/menus/menu_1015.jpg")
			menu_17 = Menus.objects.using(name_db).create(cmenu=1016, nmenu="PIZZA ITALIANA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=9500, pvta2=9500, pvta3=9500, vttotal=9500, foto="img/menus/menu_1016.jpg")
			menu_18 = Menus.objects.using(name_db).create(cmenu=1017, nmenu="PIZZA CAMPESINA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=9000, pvta2=9000, pvta3=9000, vttotal=9000, foto="img/menus/menu_1017.jpg")
			menu_19 = Menus.objects.using(name_db).create(cmenu=1018, nmenu="PIZZA MEGA CARNE", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=11000, pvta2=11000, pvta3=11000, vttotal=11000, foto="img/menus/menu_1018.jpg")
			menu_20 = Menus.objects.using(name_db).create(cmenu=1019, nmenu="ROMA PIZZA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=11000, pvta2=11000, pvta3=11000, vttotal=11000, foto="img/menus/menu_1019.jpg")
			menu_21 = Menus.objects.using(name_db).create(cmenu=1020, nmenu="PIZZA FRUTOS ROJOS", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=9000, pvta2=9000, pvta3=9000, vttotal=9000, foto="img/menus/menu_1020.jpg")
			menu_22 = Menus.objects.using(name_db).create(cmenu=1021, nmenu="PIZZA FANTASIA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_premium, npax=1, pvta1=9000, pvta2=9000, pvta3=9000, vttotal=9000, foto="img/menus/menu_1021.jpg")
			#ROMA BURGUER
			menu_23 = Menus.objects.using(name_db).create(cmenu=1022, nmenu="ROMA", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghamburguesas, npax=1, pvta1=13000, pvta2=13000, pvta3=13000, vttotal=13000, foto="img/menus/menu_1022.jpg")
			menu_24 = Menus.objects.using(name_db).create(cmenu=1023, nmenu="RANCHERA", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghamburguesas, npax=1, pvta1=12600, pvta2=12600, pvta3=12600, vttotal=12600, foto="img/menus/menu_1023.jpg")
			menu_25 = Menus.objects.using(name_db).create(cmenu=1024, nmenu="MAMA", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghamburguesas, npax=1, pvta1=11500, pvta2=11500, pvta3=11500, vttotal=11500, foto="img/menus/menu_1024.jpg")
			menu_26 = Menus.objects.using(name_db).create(cmenu=1025, nmenu="POLLO", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghamburguesas, npax=1, pvta1=9900, pvta2=9900, pvta3=9900, vttotal=9900, foto="img/menus/menu_1025.jpg")	
			menu_27 = Menus.objects.using(name_db).create(cmenu=1026, nmenu="DOBLE", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghamburguesas, npax=1, pvta1=12400, pvta2=12400, pvta3=12400, vttotal=12400, foto="img/menus/menu_1026.jpg")
			menu_28 = Menus.objects.using(name_db).create(cmenu=1027, nmenu="ESPECIAL", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghamburguesas, npax=1, pvta1=11000, pvta2=11000, pvta3=11000, vttotal=11000, foto="img/menus/menu_1027.jpg")
			menu_29 = Menus.objects.using(name_db).create(cmenu=1028, nmenu="SENCILLA", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghamburguesas, npax=1, pvta1=9200, pvta2=9200, pvta3=9200, vttotal=9200, foto="img/menus/menu_1028.jpg")	
			menu_30 = Menus.objects.using(name_db).create(cmenu=1029, nmenu="MEDITERRANEA", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghamburguesas, npax=1, pvta1=12600, pvta2=12600, pvta3=12600, vttotal=12600, foto="img/menus/menu_1029.jpg")
			#PIZZA FAMILIAR				
			menu_31 = Menus.objects.using(name_db).create(cmenu=1030, nmenu="PIZZA FAMILIAR SABOR TRADICIONAL", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_familiar, npax=1, pvta1=38000, pvta2=38000, pvta3=38000, vttotal=38000, foto="img/menus/menu_1030.jpg")
			menu_32 = Menus.objects.using(name_db).create(cmenu=1031, nmenu="PIZZA FAMILIAR PREMIUM - 1 SABOR", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_familiar, npax=1, pvta1=48600, pvta2=48600, pvta3=48600, vttotal=48600, foto="img/menus/menu_1031.jpg")
			menu_33 = Menus.objects.using(name_db).create(cmenu=1032, nmenu="PIZZA FAMILIAR PREMIUM - 2 SABOR", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_familiar, npax=1, pvta1=52600, pvta2=52600, pvta3=52600, vttotal=52600, foto="img/menus/menu_1032.jpg")
			menu_34 = Menus.objects.using(name_db).create(cmenu=1033, nmenu="PIZZA MIXTA TRADICIONAL", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_familiar, npax=1, pvta1=6000, pvta2=6000, pvta3=6000, vttotal=6000, foto="img/menus/menu_1033.jpg")
			menu_35 = Menus.objects.using(name_db).create(cmenu=1034, nmenu="PIZZA MIXTA PREMIUM ", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_familiar, npax=1, pvta1=11000, pvta2=11000, pvta3=11000, vttotal=11000, foto="img/menus/menu_1034.jpg")
			menu_36 = Menus.objects.using(name_db).create(cmenu=1035, nmenu="EMPAQUE PARA LLEVAR", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpizza_familiar, npax=1, pvta1=2000, pvta2=2000, pvta3=2000, vttotal=2000, foto="img/menus/menu_1035.jpg")
			#LASAÑA
			menu_37 = Menus.objects.using(name_db).create(cmenu=1036, nmenu="POLLO CON CHAMPIÑONES", fcrea="2017-02-02", cesdo=estado, cgpomenu=glasana, npax=1, pvta1=11000, pvta2=11000, pvta3=11000, vttotal=11000, foto="img/menus/menu_1036.jpg")			
			menu_38 = Menus.objects.using(name_db).create(cmenu=1037, nmenu="NAPOLITANA", fcrea="2017-02-02", cesdo=estado, cgpomenu=glasana, npax=1, pvta1=9500, pvta2=9500, pvta3=9500, vttotal=9500, foto="img/menus/menu_1037.jpg")			
			menu_39 = Menus.objects.using(name_db).create(cmenu=1038, nmenu="RANCHERA", fcrea="2017-02-02", cesdo=estado, cgpomenu=glasana, npax=1, pvta1=13000, pvta2=13000, pvta3=13000, vttotal=13000, foto="img/menus/menu_1038.jpg")			
			menu_40 = Menus.objects.using(name_db).create(cmenu=1039, nmenu="BOLOÑESA", fcrea="2017-02-02", cesdo=estado, cgpomenu=glasana, npax=1, pvta1=12000, pvta2=12000, pvta3=12000, vttotal=12000, foto="img/menus/menu_1039.jpg")			
			menu_41 = Menus.objects.using(name_db).create(cmenu=1040, nmenu="LASAÑA MIXTA", fcrea="2017-02-02", cesdo=estado, cgpomenu=glasana, npax=1, pvta1=14500, pvta2=14500, pvta3=14500, vttotal=14500, foto="img/menus/menu_1040.jpg")			
			#SALCHIPAPA
			menu_42 = Menus.objects.using(name_db).create(cmenu=1041, nmenu="SALCHIPAPA ROMA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gsalchipapa, npax=1, pvta1=11000, pvta2=11000, pvta3=11000, vttotal=11000, foto="img/menus/menu_1041.jpg")			
			menu_43 = Menus.objects.using(name_db).create(cmenu=1042, nmenu="SALCHIPAPA TAXCO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gsalchipapa, npax=1, pvta1=12000, pvta2=12000, pvta3=12000, vttotal=12000, foto="img/menus/menu_1042.jpg")
			menu_44 = Menus.objects.using(name_db).create(cmenu=1043, nmenu="SALCHIPAPA AMERICANA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gsalchipapa, npax=1, pvta1=6000, pvta2=6000, pvta3=6000, vttotal=6000, foto="img/menus/menu_1043.jpg")
			menu_45 = Menus.objects.using(name_db).create(cmenu=1044, nmenu="SALCHIPAPA TRADICIONAL", fcrea="2017-02-02", cesdo=estado, cgpomenu=gsalchipapa, npax=1, pvta1=5000, pvta2=5000, pvta3=5000, vttotal=5000, foto="img/menus/menu_1044.jpg")
			#SANDWICHES
			menu_46 = Menus.objects.using(name_db).create(cmenu=1045, nmenu="SANDWICHES", fcrea="2017-02-02", cesdo=estado, cgpomenu=gsandwich, npax=1, pvta1=7500, pvta2=7500, pvta3=7500, vttotal=7500, foto="img/menus/menu_1045.jpg")
			menu_47 = Menus.objects.using(name_db).create(cmenu=1046, nmenu="SANDWICH DE ATUN", fcrea="2017-02-02", cesdo=estado, cgpomenu=gsandwich, npax=1, pvta1=10000, pvta2=10000, pvta3=10000, vttotal=10000, foto="img/menus/menu_1046.jpg")
			menu_48 = Menus.objects.using(name_db).create(cmenu=1047, nmenu="SANDWICH POLLO AL GRATIN", fcrea="2017-02-02", cesdo=estado, cgpomenu=gsandwich, npax=1, pvta1=13000, pvta2=13000, pvta3=13000, vttotal=13000, foto="img/menus/menu_1047.jpg")
			menu_49 = Menus.objects.using(name_db).create(cmenu=1048, nmenu="SANDWICH CLUB", fcrea="2017-02-02", cesdo=estado, cgpomenu=gsandwich, npax=1, pvta1=14000, pvta2=14000, pvta3=14000, vttotal=14000, foto="img/menus/menu_1048.jpg")
			menu_50 = Menus.objects.using(name_db).create(cmenu=1049, nmenu="SANDWICH WOW", fcrea="2017-02-02", cesdo=estado, cgpomenu=gsandwich, npax=1, pvta1=14000, pvta2=14000, pvta3=14000, vttotal=14000, foto="img/menus/menu_1049.jpg")
			#PATACONES
			menu_51 = Menus.objects.using(name_db).create(cmenu=1050, nmenu="PATACON RES", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpatacones, npax=1, pvta1=11500, pvta2=11500, pvta3=11500, vttotal=11500, foto="img/menus/menu_1050.jpg")			
			menu_52 = Menus.objects.using(name_db).create(cmenu=1051, nmenu="PATACON CON POLLO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpatacones, npax=1, pvta1=11500, pvta2=11500, pvta3=11500, vttotal=11500, foto="img/menus/menu_1051.jpg")
			menu_53 = Menus.objects.using(name_db).create(cmenu=1052, nmenu="PATACON MIXTO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gpatacones, npax=1, pvta1=11500, pvta2=11500, pvta3=11500, vttotal=11500, foto="img/menus/menu_1052.jpg")
			#BURRITOS
			menu_54 = Menus.objects.using(name_db).create(cmenu=1053, nmenu="BURRITO DE CARNE", fcrea="2017-02-02", cesdo=estado, cgpomenu=gburritos, npax=1, pvta1=12000, pvta2=12000, pvta3=12000, vttotal=12000, foto="img/menus/menu_1053.jpg")
			menu_55 = Menus.objects.using(name_db).create(cmenu=1054, nmenu="BURRITO DE POLLO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gburritos, npax=1, pvta1=12000, pvta2=12000, pvta3=12000, vttotal=12000, foto="img/menus/menu_1054.jpg")
			menu_56 = Menus.objects.using(name_db).create(cmenu=1055, nmenu="BURRITO MIXTO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gburritos, npax=1, pvta1=12000, pvta2=12000, pvta3=12000, vttotal=12000, foto="img/menus/menu_1055.jpg")
			#ADICIONALES
			menu_57 = Menus.objects.using(name_db).create(cmenu=1056, nmenu="QUESO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=3500, pvta2=3500, pvta3=3500, vttotal=3500, foto="img/menus/menu_1056.jpg")
			menu_58 = Menus.objects.using(name_db).create(cmenu=1057, nmenu="TOCINETA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=2800, pvta2=2800, pvta3=2800, vttotal=2800, foto="img/menus/menu_1057.jpg")
			menu_59 = Menus.objects.using(name_db).create(cmenu=1058, nmenu="JAMON", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=1700, pvta2=1700, pvta3=1700, vttotal=1700, foto="img/menus/menu_1058.jpg")
			menu_60 = Menus.objects.using(name_db).create(cmenu=1059, nmenu="SALCHICHA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=1700, pvta2=1700, pvta3=1700, vttotal=1700, foto="img/menus/menu_1059.jpg")
			menu_61 = Menus.objects.using(name_db).create(cmenu=1060, nmenu="SALAMI", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=1700, pvta2=1700, pvta3=1700, vttotal=1700, foto="img/menus/menu_1060.jpg")
			menu_62 = Menus.objects.using(name_db).create(cmenu=1061, nmenu="PIÑA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=1700, pvta2=1700, pvta3=1700, vttotal=1700, foto="img/menus/menu_1061.jpg")
			menu_63 = Menus.objects.using(name_db).create(cmenu=1062, nmenu="PEPERONNI", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=4900, pvta2=4900, pvta3=4900, vttotal=4900, foto="img/menus/menu_1062.jpg")
			menu_64 = Menus.objects.using(name_db).create(cmenu=1063, nmenu="BASE PIZZA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=2700, pvta2=2700, pvta3=2700, vttotal=2700, foto="img/menus/menu_1063.jpg")
			menu_65 = Menus.objects.using(name_db).create(cmenu=1064, nmenu="CIRUELAS", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=2000, pvta2=2000, pvta3=2000, vttotal=2000, foto="img/menus/menu_1064.jpg")
			menu_66 = Menus.objects.using(name_db).create(cmenu=1065, nmenu="MAIZ TIERNO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=1800, pvta2=1800, pvta3=1800, vttotal=1800, foto="img/menus/menu_1065.jpg")
			menu_67 = Menus.objects.using(name_db).create(cmenu=1066, nmenu="CHAMPIÑONES", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=1800, pvta2=1800, pvta3=1800, vttotal=1800, foto="img/menus/menu_1066.jpg")
			menu_68 = Menus.objects.using(name_db).create(cmenu=1067, nmenu="POLLO APANADO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=4500, pvta2=4500, pvta3=4500, vttotal=4500, foto="img/menus/menu_1067.jpg")
			menu_69 = Menus.objects.using(name_db).create(cmenu=1068, nmenu="EMPAQUE PARA LLEVAR", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=700, pvta2=700, pvta3=700, vttotal=700, foto="img/menus/menu_1068.jpg")
			menu_70 = Menus.objects.using(name_db).create(cmenu=1069, nmenu="ACEITUNAS NEGRAS", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=3500, pvta2=3500, pvta3=3500, vttotal=3500, foto="img/menus/menu_1069.jpg")
			menu_71 = Menus.objects.using(name_db).create(cmenu=1070, nmenu="PAPA A LA FRANCESA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=5000, pvta2=5000, pvta3=5000, vttotal=5000, foto="img/menus/menu_1070.jpg")
			menu_72 = Menus.objects.using(name_db).create(cmenu=1071, nmenu="CARNE HAMBURGUESA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=4500, pvta2=4500, pvta3=4500, vttotal=4500, foto="img/menus/menu_1071.jpg")
			menu_73 = Menus.objects.using(name_db).create(cmenu=1072, nmenu="SALCHICHA AMERICANA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=4000, pvta2=4000, pvta3=4000, vttotal=4000, foto="img/menus/menu_1072.jpg")
			menu_74 = Menus.objects.using(name_db).create(cmenu=1073, nmenu="POLLO DESMENUZADO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=2800, pvta2=2800, pvta3=2800, vttotal=2800, foto="img/menus/menu_1073.jpg")
			menu_75 = Menus.objects.using(name_db).create(cmenu=1074, nmenu="JALAPEÑOS", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=2800, pvta2=2800, pvta3=2800, vttotal=2800, foto="img/menus/menu_1074.jpg")
			menu_76 = Menus.objects.using(name_db).create(cmenu=1075, nmenu="ANCHOAS", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=7800, pvta2=7800, pvta3=7800, vttotal=7800, foto="img/menus/menu_1075.jpg")
			menu_77 = Menus.objects.using(name_db).create(cmenu=1076, nmenu="MELOCOTONES", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=2500, pvta2=2500, pvta3=2500, vttotal=2500, foto="img/menus/menu_1076.jpg")
			menu_78 = Menus.objects.using(name_db).create(cmenu=1077, nmenu="CABANO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=1800, pvta2=1800, pvta3=1800, vttotal=1800, foto="img/menus/menu_1077.jpg")
			menu_79 = Menus.objects.using(name_db).create(cmenu=1078, nmenu="CEREZAS", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=1800, pvta2=1800, pvta3=1800, vttotal=1800, foto="img/menus/menu_1078.jpg")
			menu_80 = Menus.objects.using(name_db).create(cmenu=1079, nmenu="CHORIZO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=4000, pvta2=4000, pvta3=4000, vttotal=4000, foto="img/menus/menu_1079.jpg")
			menu_81 = Menus.objects.using(name_db).create(cmenu=1080, nmenu="PORCION DE PAN", fcrea="2017-02-02", cesdo=estado, cgpomenu=gadicionales, npax=1, pvta1=2300, pvta2=2300, pvta3=2300, vttotal=2300, foto="img/menus/menu_1080.jpg")
			#BEBIDAS
			menu_82 = Menus.objects.using(name_db).create(cmenu=1081, nmenu="GASEOSA PERSONAL", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=2500, pvta2=2500, pvta3=2500, vttotal=2500, foto="img/menus/menu_1081.jpg")
			menu_83 = Menus.objects.using(name_db).create(cmenu=1082, nmenu="GASEOSA 1 1/2 L", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=4500, pvta2=4500, pvta3=4500, vttotal=4500, foto="img/menus/menu_1082.jpg")
			menu_84 = Menus.objects.using(name_db).create(cmenu=1083, nmenu="GASEOSA 2L", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=5300, pvta2=5300, pvta3=5300, vttotal=5300, foto="img/menus/menu_1083.jpg")
			menu_85 = Menus.objects.using(name_db).create(cmenu=1084, nmenu="GASEOSA 3L", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=7500, pvta2=7500, pvta3=7500, vttotal=7500, foto="img/menus/menu_1084.jpg")
			menu_86 = Menus.objects.using(name_db).create(cmenu=1085, nmenu="AGUA EN BOTELLA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas,	npax=1, pvta1=2500, pvta2=2500, pvta3=2500, vttotal=2500, foto="img/menus/menu_1085.jpg")
			menu_87 = Menus.objects.using(name_db).create(cmenu=1086, nmenu="AGUA CON GAS", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=2500, pvta2=2500, pvta3=2500, vttotal=2500, foto="img/menus/menu_1086.jpg")
			menu_88 = Menus.objects.using(name_db).create(cmenu=1087, nmenu="CERVEZA NACIONAL", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=2800, pvta2=2800, pvta3=2800, vttotal=2800, foto="img/menus/menu_1087.jpg")
			menu_89 = Menus.objects.using(name_db).create(cmenu=1088, nmenu="CERVEZA IMPORTADA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=7000, pvta2=7000, pvta3=7000, vttotal=7000, foto="img/menus/menu_1088.jpg")
			menu_90 = Menus.objects.using(name_db).create(cmenu=1089, nmenu="JUGOS NATURALES/AGUA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=4500, pvta2=4500, pvta3=4500, vttotal=4500, foto="img/menus/menu_1089.jpg")
			menu_91 = Menus.objects.using(name_db).create(cmenu=1090, nmenu="JUGOS NATURALES/LECHE", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=5000, pvta2=5000, pvta3=5000, vttotal=5000, foto="img/menus/menu_1090.jpg")
			menu_92 = Menus.objects.using(name_db).create(cmenu=1091, nmenu="LIMONADA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=4000, pvta2=4000, pvta3=4000, vttotal=4000, foto="img/menus/menu_1091.jpg")
			menu_93 = Menus.objects.using(name_db).create(cmenu=1092, nmenu="JARRA LIMONADA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=9000, pvta2=9000, pvta3=9000, vttotal=9000, foto="img/menus/menu_1092.jpg")
			menu_94 = Menus.objects.using(name_db).create(cmenu=1093, nmenu="JARRA JUGO/AGUA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=9000, pvta2=9000, pvta3=9000, vttotal=9000, foto="img/menus/menu_1093.jpg")
			menu_95 = Menus.objects.using(name_db).create(cmenu=1094, nmenu="JARRA JUGO/LECHE", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=10500, pvta2=10500, pvta3=10500, vttotal=10500, foto="img/menus/menu_1094.jpg")
			menu_96 = Menus.objects.using(name_db).create(cmenu=1095, nmenu="GASEOSA LATA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=2500, pvta2=2500, pvta3=2500, vttotal=2500, foto="img/menus/menu_1095.jpg")
			menu_97 = Menus.objects.using(name_db).create(cmenu=1096, nmenu="TE PERSONAL", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas,	npax=1, pvta1=2500, pvta2=2500, pvta3=2500, vttotal=2500, foto="img/menus/menu_1096.jpg")
			menu_98 = Menus.objects.using(name_db).create(cmenu=1097, nmenu="MALTA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=2500, pvta2=2500, pvta3=2500, vttotal=2500, foto="img/menus/menu_1097.jpg")
			menu_99 = Menus.objects.using(name_db).create(cmenu=1098, nmenu="JUGOS HIT", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=2000, pvta2=2000, pvta3=2000, vttotal=2000, foto="img/menus/menu_1098.jpg")
			#HELADOS
			menu_100 = Menus.objects.using(name_db).create(cmenu=1099, nmenu="CONO DE UNA BOLA", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghelado, npax=1, pvta1=3500, pvta2=3500, pvta3=3500, vttotal=3500, foto="img/menus/menu_1099.jpg")
			menu_101 = Menus.objects.using(name_db).create(cmenu=1100, nmenu="CONO CON DOS BOLAS", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghelado, npax=1, pvta1=4500, pvta2=4500, pvta3=4500, vttotal=4500, foto="img/menus/menu_1100.jpg")
			menu_102 = Menus.objects.using(name_db).create(cmenu=1101, nmenu="MALTEADAS 12 ONZAS", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghelado, npax=1, pvta1=7500, pvta2=7500, pvta3=7500, vttotal=7500, foto="img/menus/menu_1101.jpg")
			menu_103= Menus.objects.using(name_db).create(cmenu=1102, nmenu="GRANIZADOS 12 ONZAS", fcrea="2017-02-02", cesdo=estado, cgpomenu=ghelado, npax=1, pvta1=6900, pvta2=6900, pvta3=6900, vttotal=6900, foto="img/menus/menu_1102.jpg")
			#ENSALADA DE FRUTAS
			menu_104= Menus.objects.using(name_db).create(cmenu=1103, nmenu="ENSALADA FRUTAS JUNIOR", fcrea="2017-02-02", cesdo=estado, cgpomenu=gensalada_frutas, npax=1, pvta1=6500, pvta2=6500, pvta3=6500, vttotal=6500, foto="img/menus/menu_1103.jpg")
			menu_105= Menus.objects.using(name_db).create(cmenu=1104, nmenu="ENSALADA FRUTAS NORMAL SIN HELADO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gensalada_frutas, npax=1, pvta1=7500, pvta2=7500, pvta3=7500, vttotal=7500, foto="img/menus/menu_1104.jpg")
			menu_106= Menus.objects.using(name_db).create(cmenu=1105, nmenu="ENSALADA FRUTAS NROMAL CON HELADO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gensalada_frutas, npax=1, pvta1=8800, pvta2=8800, pvta3=8800, vttotal=8800, foto="img/menus/menu_1105.jpg")
			#PERROS CALIENTES
		 	menu_106= Menus.objects.using(name_db).create(cmenu=1106, nmenu="PERRO ROMA", fcrea="2017-02-02", cesdo=estado, cgpomenu=gperros_calientes, npax=1, pvta1=10500, pvta2=10500, pvta3=10500, vttotal=10500, foto="img/menus/menu_1106.jpg")
		 	menu_107= Menus.objects.using(name_db).create(cmenu=1107, nmenu="PERRO AMERICANO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gperros_calientes, npax=1, pvta1=6000, pvta2=6000, pvta3=6000, vttotal=6000, foto="img/menus/menu_1107.jpg")
		 	menu_108= Menus.objects.using(name_db).create(cmenu=1108, nmenu="PERRO TRADICIONAL", fcrea="2017-02-02", cesdo=estado, cgpomenu=gperros_calientes, npax=1, pvta1=5000, pvta2=5000, pvta3=5000, vttotal=5000, foto="img/menus/menu_1108.jpg")
		 	menu_109= Menus.objects.using(name_db).create(cmenu=1109, nmenu="PERRO HAWAIANO", fcrea="2017-02-02", cesdo=estado, cgpomenu=gperros_calientes, npax=1, pvta1=9000, pvta2=9000, pvta3=9000, vttotal=9000, foto="img/menus/menu_1109.jpg")

			
			print "Terminado"

		else:
			print "Operación Cancelada."

