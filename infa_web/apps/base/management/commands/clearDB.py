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
from infa_web.apps.usuarios.models import *

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
			#Base
			Esdo.objects.using(name_db).all().delete()
			print "Esdo. Registros Borrados con Exito."
			Timo.objects.using(name_db).all().delete()
			print "Timo. Registros Borrados con Exito."
			MediosPago.objects.using(name_db).all().delete()
			print "MediosPago. Registros Borrados con Exito."
			Bode.objects.using(name_db).all().delete()
			print "Bode. Registros Borrados con Exito."
			Modules.objects.using(name_db).all().delete()
			print "Modules. Registros Borrados con Exito."
			Parameters.objects.using(name_db).all().delete()
			print "Parameters. Registros Borrados con Exito."
			Ubica.objects.using(name_db).all().delete()
			print "Ubica. Registros Borrados con Exito."
			Ciudad.objects.using(name_db).all().delete()
			print "Ciudad. Registros Borrados con Exito."
			Departamento.objects.using(name_db).all().delete()
			print "Departamento. Registros Borrados con Exito."
			Iva.objects.using(name_db).all().delete()
			print "Iva. Registros Borrados con Exito."
			Regiva.objects.using(name_db).all().delete()
			print "Regiva. Registros Borrados con Exito."
			Tiide.objects.using(name_db).all().delete()
			print "Tiide. Registros Borrados con Exito."
			Emdor.objects.using(name_db).all().delete()
			print "Emdor. Registros Borrados con Exito."
			Domici.objects.using(name_db).all().delete()
			print "Domici. Registros Borrados con Exito."
			Tifopa.objects.using(name_db).all().delete()
			print "Tifopa. Registros Borrados con Exito."
			Cta.objects.using(name_db).all().delete()
			print "Cta. Registros Borrados con Exito."
			Banfopa.objects.using(name_db).all().delete()
			print "Banfopa. Registros Borrados con Exito."
			Caja.objects.using(name_db).all().delete()
			print "Caja. Registros Borrados con Exito."
			Talo.objects.using(name_db).all().delete()
			print "Talo. Registros Borrados con Exito."
			# Articulos
			Tiarlos.objects.using(name_db).all().delete()
			print "Tiarlos. Registros Borrados con Exito."
			Gpo.objects.using(name_db).all().delete()
			print "Gpo. Registros Borrados con Exito."
			Marca.objects.using(name_db).all().delete()
			print "Marca. Registros Borrados con Exito."
			Unidades.objects.using(name_db).all().delete()
			print "Unidades. Registros Borrados con Exito."
			#Terceros
			Autorre.objects.using(name_db).all().delete()
			print "Autorre. Registros Borrados con Exito."
			Vende.objects.using(name_db).all().delete()
			print "Vende. Registros Borrados con Exito."
			Ruta.objects.using(name_db).all().delete()
			print "Ruta. Registros Borrados con Exito."
			Zona.objects.using(name_db).all().delete()
			print "Zona. Registros Borrados con Exito."
			Tercero.objects.using(name_db).all().delete()
			print "Tercero. Registros Borrados con Exito."
			Personas.objects.using(name_db).all().delete()
			print "Personas. Registros Borrados con Exito."
			Usuario.objects.using(name_db).all().delete()
			print "Usuarios. Registros Borrados con Exito."
		else:
			print "Operación Cancelada."

