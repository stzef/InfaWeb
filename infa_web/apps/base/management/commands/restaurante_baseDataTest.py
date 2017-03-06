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
	def gvting(self,ing):
		valores = [i.vcosto for i in ing]
		return sum(valores)
	def gvtpla(self,pla):
		valores = [p.vttotal for p in pla]
		return sum(valores)
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

			gplatos_fuerte = GposMenus.objects.using(name_db).get(cgpomenu = 1)
			gentradas = GposMenus.objects.using(name_db).get(cgpomenu = 2)
			gbebidas = GposMenus.objects.using(name_db).get(cgpomenu = 3)
			gplatos_frios = GposMenus.objects.using(name_db).get(cgpomenu = 4)
			gensaladas = GposMenus.objects.using(name_db).get(cgpomenu = 5)
			gcomida_rapida = GposMenus.objects.using(name_db).get(cgpomenu = 6)

			arroz = Ingredientes.objects.using(name_db).create(cingre =1000, ningre ="Arroz", canti =100, vcosto =1000, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			papa = Ingredientes.objects.using(name_db).create(cingre =1001, ningre ="Papa", canti =100, vcosto =500, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			sal = Ingredientes.objects.using(name_db).create(cingre =1002, ningre ="Sal", canti =100, vcosto =200, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			agua = Ingredientes.objects.using(name_db).create(cingre =1003, ningre ="Agua", canti =100, vcosto =500, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			cebolla = Ingredientes.objects.using(name_db).create(cingre =1004, ningre ="Cebolla", canti =100, vcosto =300, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			salsa = Ingredientes.objects.using(name_db).create(cingre =1005, ningre ="Salsa", canti =100, vcosto =300, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			pan = Ingredientes.objects.using(name_db).create(cingre =1006, ningre ="Pan", canti =100, vcosto =300, ifcostear = 1, stomin =1, stomax = 500, ifedinom = 1)
			mandarina = Ingredientes.objects.using(name_db).create(cingre =1007, ningre ="Mandarina", canti =100, vcosto =300, ifcostear=1, stomin =1, stomax=500, ifedinom = 1)
			azucar = Ingredientes.objects.using(name_db).create(cingre =1008, ningre ="Azucar", canti =100, vcosto =300, ifcostear = 1, stomin =1, stomax = 500, ifedinom = 1)
			carne = Ingredientes.objects.using(name_db).create(cingre =1009, ningre ="Carne", canti =100, vcosto =300, ifcostear = 1, stomin =1, stomax = 500, ifedinom = 1)
			platano = Ingredientes.objects.using(name_db).create(cingre =1010, ningre ="Platano", canti =100, vcosto =500, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			aceite = Ingredientes.objects.using(name_db).create(cingre =1011, ningre ="Aceite", canti =100, vcosto =500, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			gaseosa = Ingredientes.objects.using(name_db).create(cingre =1012, ningre ="Gaseosa", canti =100, vcosto =500, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			tomate = Ingredientes.objects.using(name_db).create(cingre =1013, ningre ="Tomate", canti =100, vcosto =500, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			ajo = Ingredientes.objects.using(name_db).create(cingre =1014, ningre ="Ajo", canti =100, vcosto =500, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)
			limon = Ingredientes.objects.using(name_db).create(cingre =1015, ningre ="Limon", canti =100, vcosto =500, ifcostear = 1, stomin =1, stomax = 100, ifedinom = 1)


			ing = [arroz,sal,agua,cebolla]
			palto_arroz_seco = Platos.objects.using(name_db).create(cplato= 1000, nplato= "Arroz Seco", fcrea= "2017-02-02", npax= 1, vttotal= self.gvting(ing), foto="img/dishes/arroz.jpg")
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_seco, cingre=arroz, it=1, canti=1, cunidad=unidad, vunita=arroz.vcosto, vtotal=(arroz.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_seco, cingre=sal, it=2, canti=1, cunidad=unidad, vunita=sal.vcosto, vtotal=(sal.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_seco, cingre=agua, it=3, canti=1, cunidad=unidad, vunita=agua.vcosto, vtotal=(agua.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_seco, cingre=cebolla, it=4, canti=1, cunidad=unidad, vunita=cebolla.vcosto, vtotal=(cebolla.vcosto*1))

			ing = [arroz,papa,sal,agua,cebolla]
			palto_arroz_papa = Platos.objects.using(name_db).create(cplato= 1001, nplato= "Arroz Con Papa", fcrea= "2017-02-02", npax= 1, vttotal= self.gvting(ing), foto="img/dishes/arroz_papa.jpg")
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_papa, cingre=arroz, it=1, canti=1, cunidad=unidad, vunita=arroz.vcosto, vtotal=(arroz.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_papa, cingre=papa, it=2, canti=1, cunidad=unidad, vunita=papa.vcosto, vtotal=(papa.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_papa, cingre=sal, it=3, canti=1, cunidad=unidad, vunita=sal.vcosto, vtotal=(sal.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_papa, cingre=agua, it=4, canti=1, cunidad=unidad, vunita=agua.vcosto, vtotal=(agua.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=palto_arroz_papa, cingre=cebolla, it=5, canti=1, cunidad=unidad, vunita=cebolla.vcosto, vtotal=(cebolla.vcosto*1))

			ing = [cebolla,pan,carne,salsa,papa]
			hamburgesa = Platos.objects.using(name_db).create(cplato= 1002, nplato= "Arroz Seco", fcrea= "2017-02-02", npax= 1, vttotal= self.gvting(ing), foto="img/dishes/hamburguesa.jpg")
			Platosdeta.objects.using(name_db).create(cplato=hamburgesa, cingre=cebolla, it=1, canti=1, cunidad=unidad, vunita=cebolla.vcosto, vtotal=(cebolla.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=hamburgesa, cingre=pan, it=2, canti=1, cunidad=unidad, vunita=pan.vcosto, vtotal=(pan.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=hamburgesa, cingre=carne, it=3, canti=1, cunidad=unidad, vunita=carne.vcosto, vtotal=(carne.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=hamburgesa, cingre=salsa, it=4, canti=1, cunidad=unidad, vunita=salsa.vcosto, vtotal=(salsa.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=hamburgesa, cingre=papa, it=5, canti=1, cunidad=unidad, vunita=papa.vcosto, vtotal=(papa.vcosto*1))


			ing = [cebolla,salsa,papa]
			ensalada_papa = Platos.objects.using(name_db).create(cplato= 1003, nplato= "Arroz Seco", fcrea= "2017-02-02", npax= 1, vttotal= self.gvting(ing), foto="img/dishes/ensalada_papa.jpg")
			Platosdeta.objects.using(name_db).create(cplato=ensalada_papa, cingre=cebolla, it=1, canti=1, cunidad=unidad, vunita=cebolla.vcosto, vtotal=(cebolla.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=ensalada_papa, cingre=salsa, it=4, canti=1, cunidad=unidad, vunita=salsa.vcosto, vtotal=(salsa.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=ensalada_papa, cingre=papa, it=5, canti=1, cunidad=unidad, vunita=papa.vcosto, vtotal=(papa.vcosto*1))

			ing = [platano,aceite]
			pataconas = Platos.objects.using(name_db).create(cplato= 1004, nplato= "Arroz Seco", fcrea= "2017-02-02", npax= 1, vttotal= self.gvting(ing), foto="img/dishes/pataconas.jpg")
			Platosdeta.objects.using(name_db).create(cplato=pataconas, cingre=platano, it=1, canti=1, cunidad=unidad, vunita=platano.vcosto, vtotal=(platano.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=pataconas, cingre=aceite, it=4, canti=1, cunidad=unidad, vunita=aceite.vcosto, vtotal=(aceite.vcosto*1))

			ing = [gaseosa]
			bebida_gaseosa = Platos.objects.using(name_db).create(cplato= 1005, nplato= "Gaseosa", fcrea= "2017-02-02", npax= 1, vttotal= self.gvting(ing), foto="img/dishes/gaseosa.jpg")
			Platosdeta.objects.using(name_db).create(cplato=bebida_gaseosa, cingre=gaseosa, it=1, canti=1, cunidad=unidad, vunita=gaseosa.vcosto, vtotal=(gaseosa.vcosto*1))

			ing = [cebolla,tomate,ajo,limon]
			ensalada_simple = Platos.objects.using(name_db).create(cplato= 1006, nplato= "Ensalada", fcrea= "2017-02-02", npax= 1, vttotal= self.gvting(ing), foto="img/dishes/ensalada.jpg")
			Platosdeta.objects.using(name_db).create(cplato=ensalada_simple, cingre=cebolla, it=1, canti=1, cunidad=unidad, vunita=cebolla.vcosto, vtotal=(cebolla.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=ensalada_simple, cingre=tomate, it=2, canti=1, cunidad=unidad, vunita=tomate.vcosto, vtotal=(tomate.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=ensalada_simple, cingre=ajo, it=3, canti=1, cunidad=unidad, vunita=ajo.vcosto, vtotal=(ajo.vcosto*1))
			Platosdeta.objects.using(name_db).create(cplato=ensalada_simple, cingre=limon, it=4, canti=1, cunidad=unidad, vunita=limon.vcosto, vtotal=(limon.vcosto*1))

			pla = [palto_arroz_seco]
			menu_1 = Menus.objects.using(name_db).create(cmenu=1000, nmenu="Arroz Seco", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_fuerte, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/arroz.jpg")
			Menusdeta.objects.using(name_db).create(cmenu=menu_1, it=1, cplato=palto_arroz_seco, nplato=palto_arroz_seco.nplato, canti=1, vunita=palto_arroz_seco.vttotal, vtotal=(palto_arroz_seco.vttotal*1))

			pla = [palto_arroz_papa]
			menu_2 = Menus.objects.using(name_db).create(cmenu=1001, nmenu="Arroz Con Papa", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_fuerte, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/arroz_papa.jpg")
			Menusdeta.objects.using(name_db).create(cmenu=menu_2, it=1, cplato=palto_arroz_papa, nplato=palto_arroz_papa.nplato, canti=1, vunita=palto_arroz_papa.vttotal, vtotal=(palto_arroz_papa.vttotal*1))

			pla = [hamburgesa]
			menu_3 = Menus.objects.using(name_db).create(cmenu=1002, nmenu="Hamburgesa", fcrea="2017-02-02", cesdo=estado, cgpomenu=gcomida_rapida, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/hamburguesa.jpg")
			Menusdeta.objects.using(name_db).create(cmenu=menu_3, it=1, cplato=hamburgesa, nplato=hamburgesa.nplato, canti=1, vunita=hamburgesa.vttotal, vtotal=(hamburgesa.vttotal*1))

			pla = [ensalada_papa]
			menu_4 = Menus.objects.using(name_db).create(cmenu=1003, nmenu="Ensalada De Papa", fcrea="2017-02-02", cesdo=estado, cgpomenu=gplatos_frios, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/ensalada_papa.jpg")
			Menusdeta.objects.using(name_db).create(cmenu=menu_4, it=1, cplato=ensalada_papa, nplato=ensalada_papa.nplato, canti=1, vunita=ensalada_papa.vttotal, vtotal=(ensalada_papa.vttotal*1))

			pla = [pataconas]
			menu_5 = Menus.objects.using(name_db).create(cmenu=1004, nmenu="Pataconas", fcrea="2017-02-02", cesdo=estado, cgpomenu=gentradas, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/pataconas.jpg")
			Menusdeta.objects.using(name_db).create(cmenu=menu_5, it=1, cplato=pataconas, nplato=pataconas.nplato, canti=1, vunita=pataconas.vttotal, vtotal=(pataconas.vttotal*1))

			pla = [bebida_gaseosa]
			menu_5 = Menus.objects.using(name_db).create(cmenu=1005, nmenu="Gaseosa", fcrea="2017-02-02", cesdo=estado, cgpomenu=gbebidas, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/gaseosa.jpg")
			Menusdeta.objects.using(name_db).create(cmenu=menu_5, it=1, cplato=bebida_gaseosa, nplato=bebida_gaseosa.nplato, canti=1, vunita=bebida_gaseosa.vttotal, vtotal=(bebida_gaseosa.vttotal*1))

			pla = [ensalada_simple]
			menu_6 = Menus.objects.using(name_db).create(cmenu=1006, nmenu="Ensalada Simple", fcrea="2017-02-02", cesdo=estado, cgpomenu=gensaladas, npax=1, pvta1=1000, pvta2=1200, pvta3=1400, vttotal=self.gvtpla(pla), foto="img/menus/ensalada.jpg")
			Menusdeta.objects.using(name_db).create(cmenu=menu_6, it=1, cplato=ensalada_simple, nplato=ensalada_simple.nplato, canti=1, vunita=ensalada_simple.vttotal, vtotal=(ensalada_simple.vttotal*1))



		else:
			print "Operación Cancelada."

