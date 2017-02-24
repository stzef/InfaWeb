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
			'--db',
			action='store',
			dest='db',
			default="default",
			help='DB for connection',
		)
	def handle(self, *args, **options):

		name_db =  options["db"]
		print "DB Actual '%s'" % name_db
		confirmation = raw_input("Seguro? (Si/No) ")

		if(confirmation == "Si"):
			Ingredientes.objects.using(name_db).all().delete()
			Platos.objects.using(name_db).all().delete()
			Platosdeta.objects.using(name_db).all().delete()
			Menus.objects.using(name_db).all().delete()
			Menusdeta.objects.using(name_db).all().delete()

			unidad = Unidades.objects.using(name_db).filter()[0]
			estado = Esdo.objects.using(name_db).get(cesdo=1)
			grupo = GposMenus.objects.using(name_db).get(cgpomenu=1)

			arroz = Ingredientes.objects.using(name_db).create(cingre =1000, ningre ="Arroz", canti =100, vcosto =1000, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			papa = Ingredientes.objects.using(name_db).create(cingre =1001, ningre ="Papa", canti =100, vcosto =500, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			sal = Ingredientes.objects.using(name_db).create(cingre =1002, ningre ="Sal", canti =100, vcosto =200, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			agua = Ingredientes.objects.using(name_db).create(cingre =1003, ningre ="Agua", canti =100, vcosto =500, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			cebolla = Ingredientes.objects.using(name_db).create(cingre =1004, ningre ="Cebolla", canti =100, vcosto =300, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)

			palto_arroz_seco = Platos.objects.using(name_db).create(cplato= 1000, nplato= "Arroz Seco", fcrea= "2017-02-02", npax= 1, vttotal= 0, foto=DEFAULT_IMAGE_DISHES)

			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_seco, cingre=arroz, it=1, canti=1, cunidad=unidad, vunita=arroz.vcosto, vtotal=(arroz.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_seco, cingre=sal, it=2, canti=1, cunidad=unidad, vunita=sal.vcosto, vtotal=(sal.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_seco, cingre=agua, it=3, canti=1, cunidad=unidad, vunita=agua.vcosto, vtotal=(agua.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_seco, cingre=cebolla, it=4, canti=1, cunidad=unidad, vunita=cebolla.vcosto, vtotal=(cebolla.vcosto*1))



			palto_arroz_papa = Platos.objects.using(name_db).create(cplato= 1001, nplato= "Arroz Seco", fcrea= "2017-02-02", npax= 1, vttotal= 0, foto=DEFAULT_IMAGE_DISHES)

			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_papa, cingre=arroz, it=1, canti=1, cunidad=unidad, vunita=arroz.vcosto, vtotal=(arroz.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_papa, cingre=papa, it=2, canti=1, cunidad=unidad, vunita=papa.vcosto, vtotal=(papa.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_papa, cingre=sal, it=3, canti=1, cunidad=unidad, vunita=sal.vcosto, vtotal=(sal.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_papa, cingre=agua, it=4, canti=1, cunidad=unidad, vunita=agua.vcosto, vtotal=(agua.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_papa, cingre=cebolla, it=5, canti=1, cunidad=unidad, vunita=cebolla.vcosto, vtotal=(cebolla.vcosto*1))



			menu_1 = Menus.objects.using(name_db).create(cmenu=1000, nmenu="Menu 1", fcrea="2017-02-02", cesdo=estado, cgpomenu=grupo, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=0, foto=DEFAULT_IMAGE_MENUS)

			Menusdeta.objects.using(name_db).create(cmenu=menu_1, it=1, cplato=palto_arroz_seco, nplato=palto_arroz_seco.nplato, canti=1, vunita=palto_arroz_seco.vttotal, vtotal=(palto_arroz_seco.vttotal*1))



			menu_2 = Menus.objects.using(name_db).create(cmenu=1001, nmenu="Menu 2", fcrea="2017-02-02", cesdo=estado, cgpomenu=grupo, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=0, foto=DEFAULT_IMAGE_MENUS)

			Menusdeta.objects.using(name_db).create(cmenu=menu_2, it=1, cplato=palto_arroz_papa, nplato=palto_arroz_papa.nplato, canti=1, vunita=palto_arroz_papa.vttotal, vtotal=(palto_arroz_papa.vttotal*1))



		else:
			print "Operación Cancelada."

