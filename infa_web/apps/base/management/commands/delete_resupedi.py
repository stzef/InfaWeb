# -*- coding: utf-8 -*-
import os
from django.core.management.base import BaseCommand

from infa_web.apps.restaurante_comandas.models import *

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
			for coda in Coda.objects.using(name_db).all():
				coda.cresupedi = None
				coda.save(using=name_db)

			for resupedi in Resupedi.objects.using(name_db).all():
				Resupedipago.objects.using(name_db).filter(cresupedi=resupedi).delete()
				resupedi.delete()

				print "------------------------"
		else:
			print "Operación Cancelada."

