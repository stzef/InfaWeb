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
	def handle(self, *args, **options):
		#Base
		Esdo.objects.all().delete()
		print "Esdo. Registros Borrados con Exito."
		Timo.objects.all().delete()
		print "Timo. Registros Borrados con Exito."
		MediosPago.objects.all().delete()
		print "MediosPago. Registros Borrados con Exito."
		Bode.objects.all().delete()
		print "Bode. Registros Borrados con Exito."
		Modules.objects.all().delete()
		print "Modules. Registros Borrados con Exito."
		Parameters.objects.all().delete()
		print "Parameters. Registros Borrados con Exito."
		Ubica.objects.all().delete()
		print "Ubica. Registros Borrados con Exito."
		Ciudad.objects.all().delete()
		print "Ciudad. Registros Borrados con Exito."
		Departamento.objects.all().delete()
		print "Departamento. Registros Borrados con Exito."
		Iva.objects.all().delete()
		print "Iva. Registros Borrados con Exito."
		Regiva.objects.all().delete()
		print "Regiva. Registros Borrados con Exito."
		Tiide.objects.all().delete()
		print "Tiide. Registros Borrados con Exito."
		Emdor.objects.all().delete()
		print "Emdor. Registros Borrados con Exito."
		Domici.objects.all().delete()
		print "Domici. Registros Borrados con Exito."
		Tifopa.objects.all().delete()
		print "Tifopa. Registros Borrados con Exito."
		Cta.objects.all().delete()
		print "Cta. Registros Borrados con Exito."
		Banfopa.objects.all().delete()
		print "Banfopa. Registros Borrados con Exito."
		Caja.objects.all().delete()
		print "Caja. Registros Borrados con Exito."
		Talo.objects.all().delete()
		print "Talo. Registros Borrados con Exito."
		# Articulos
		Tiarlos.objects.all().delete()
		print "Tiarlos. Registros Borrados con Exito."
		Gpo.objects.all().delete()
		print "Gpo. Registros Borrados con Exito."
		Marca.objects.all().delete()
		print "Marca. Registros Borrados con Exito."
		Unidades.objects.all().delete()
		print "Unidades. Registros Borrados con Exito."
		#Terceros
		Autorre.objects.all().delete()
		print "Autorre. Registros Borrados con Exito."
		Vende.objects.all().delete()
		print "Vende. Registros Borrados con Exito."
		Ruta.objects.all().delete()
		print "Ruta. Registros Borrados con Exito."
		Zona.objects.all().delete()
		print "Zona. Registros Borrados con Exito."
		Tercero.objects.all().delete()
		print "Tercero. Registros Borrados con Exito."
		Personas.objects.all().delete()
		print "Personas. Registros Borrados con Exito."
		Usuario.objects.all().delete()
		print "Usuarios. Registros Borrados con Exito."
