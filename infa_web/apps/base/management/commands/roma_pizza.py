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


			unidad = Unidades.objects.using(name_db).filter()[0]
			estado = Esdo.objects.using(name_db).get(cesdo=1)

			gplatos_fuerte = GposMenus.objects.using(name_db).create(cgpomenu = 1)
			gentradas = GposMenus.objects.using(name_db).create(cgpomenu = 2)
			gbebidas = GposMenus.objects.using(name_db).create(cgpomenu = 3)
			gplatos_frios = GposMenus.objects.using(name_db).create(cgpomenu = 4)
			gensaladas = GposMenus.objects.using(name_db).create(cgpomenu = 5)
			gcomida_rapida = GposMenus.objects.using(name_db).create(cgpomenu = 6)

			print "Procesando ..."


			menu_1 = Menus.objects.using(name_db).create(cmenu=1000, nmenu="Arroz Seco", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_fuerte, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/menu_1000.jpg")

			menu_2 = Menus.objects.using(name_db).create(cmenu=1001, nmenu="Arroz Con Papa", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_fuerte, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/arroz_papa.jpg")

			menu_3 = Menus.objects.using(name_db).create(cmenu=1002, nmenu="Arroz Con Papa 2", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_fuerte, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/arroz_papa.jpg")

			menu_4 = Menus.objects.using(name_db).create(cmenu=1003, nmenu="Arroz Con Papa 3", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_fuerte, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/arroz_papa.jpg")

			menu_5 = Menus.objects.using(name_db).create(cmenu=1004, nmenu="Arroz Con Papa 4", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_fuerte, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/arroz_papa.jpg")

			menu_6 = Menus.objects.using(name_db).create(cmenu=1005, nmenu="Arroz Con Papa 5", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_fuerte, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/arroz_papa.jpg")

			menu_7 = Menus.objects.using(name_db).create(cmenu=1006, nmenu="Arroz Con Papa 6", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_fuerte, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/arroz_papa.jpg")

			menu_8 = Menus.objects.using(name_db).create(cmenu=1007, nmenu="Arroz Con Papa 7", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_fuerte, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/arroz_papa.jpg")

			menu_9 = Menus.objects.using(name_db).create(cmenu=1008, nmenu="Arroz Con Papa 8", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_fuerte, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/arroz_papa.jpg")

			menu_10 = Menus.objects.using(name_db).create(cmenu=1009, nmenu="Hamburgesa", fcrea="2017-02-02", cesdo=estado, cgpomenu=gcomida_rapida, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/hamburguesa.jpg")

			menu_11 = Menus.objects.using(name_db).create(cmenu=1010, nmenu="Ensalada De Papa", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_frios, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/ensalada_papa.jpg")

			menu_12 = Menus.objects.using(name_db).create(cmenu=1011, nmenu="Pataconas", fcrea="2017-02-02", cesdo=estado, cgpomenu=gentradas, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/pataconas.jpg")

			menu_13 = Menus.objects.using(name_db).create(cmenu=1012, nmenu="Gaseosa", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/gaseosa.jpg")

			menu_14 = Menus.objects.using(name_db).create(cmenu=1013, nmenu="Ensalada Simple", fcrea="2017-02-02", cesdo=estado, cgpomenu=gensaladas, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/ensalada.jpg")

			print "Terminado"

		else:
			print "Operación Cancelada."

