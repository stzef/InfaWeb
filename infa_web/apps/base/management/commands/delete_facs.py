# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os
from datetime import datetime

from infa_web.apps.base.constantes import *
from infa_web.apps.base.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.articulos.models import *
from infa_web.apps.facturacion.models import *
from infa_web.apps.usuarios.models import *

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument(
			'--database',
			action='store',
			dest='database',
			default="default",
			help='DB for connection',
		)
	def handle(self, *args, **options):

		name_db =  options["database"]
		print "DB Actual '%s'" % name_db

		prosiga_bajo_su_responsabilidad = False

		confirmation = raw_input("Seguro? (Si/No) ")
		if(confirmation == "Si"):
			confirmation = raw_input("Completamente Seguro? (Si/No) ")
			if(confirmation == "Si"):
				confirmation = raw_input("Ultima Palabra? (Si/No) ")
				if(confirmation == "Si"):
					prosiga_bajo_su_responsabilidad = True

		if(prosiga_bajo_su_responsabilidad):
			#Base
			for fac in Fac.objects.using(name_db).all():
				print "------------------------"
				Facdeta.objects.using(name_db).filter(cfac=fac.pk).delete()
				print "Factura %s" % fac.cfac
				for mvsa in Mvsa.objects.using(name_db).filter(docrefe=fac.cfac):
					print "Mv Salida %s" % mvsa.cmvsa
					Mvsadeta.objects.using(name_db).filter(cmvsa = mvsa.cmvsa).delete()
					mvsa.delete()

				movideta = Movideta.objects.using(name_db).filter(docrefe=fac.cfac)
				cmovis = list(set(map(lambda x: x.cmovi.cmovi, movideta)))
				for cmovi in cmovis:
					movi = Movi.objects.using(name_db).get(cmovi = cmovi)
					print "Movimiento %s" % movi.cmovi
					Movideta.objects.using(name_db).filter(cmovi = cmovi).delete()
					movi.delete()
				fac.delete()
				print "------------------------"
		else:
			print "Operación Cancelada."

