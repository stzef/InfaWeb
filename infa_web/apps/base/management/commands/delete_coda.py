# -*- coding: utf-8 -*-
import os
from django.core.management.base import BaseCommand

from infa_web.apps.restaurante_comandas.models import *

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
			for coda in Coda.objects.using(name_db).all():
				for codadeta in Codadeta.objects.using(name_db).filter(ccoda=coda):
					print "Codadeta %s Borrado " % codadeta.pk
					codadeta.delete()
				coda.delete()
				print "Coda %s Borrado " % coda.ccoda

				print "------------------------"
		else:
			print "Operación Cancelada."

