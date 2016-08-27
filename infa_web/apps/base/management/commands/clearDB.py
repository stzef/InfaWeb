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
class Command(BaseCommand):
	def handle(self, *args, **options):
		Esdo.objects.all().delete()
		print "clear Esdo"
		Tiarlos.objects.all().delete()
		print "clear Tiarlos"
		Personas.objects.all().delete()
		print "clear Personas"
		Vende.objects.all().delete()
		print "clear Vende"
		Unidades.objects.all().delete()
		print "clear Unidades"
		Regiva.objects.all().delete()
		print "clear Regiva"
		Tiide.objects.all().delete()
		print "clear Tiide"
		Modules.objects.all().delete()
		print "clear Modules"
		Autorre.objects.all().delete()
		print "clear Autorre"
		Ruta.objects.all().delete()
		print "clear Ruta"
		Zona.objects.all().delete()
		print "clear Zona"
		Iva.objects.all().delete()
		print "clear Iva"
		Marca.objects.all().delete()
		print "clear Marca"
		Bode.objects.all().delete()
		print "clear Bode"
		Ubica.objects.all().delete()
		print "clear Ubica"
		Gpo.objects.all().delete()
		print "clear Gpo"
		Departamento.objects.all().delete()
		print "clear Departamento"
		Ciudad.objects.all().delete()
		print "clear Ciudad"
		Timo.objects.all().delete()
		print "clear Timo"
		Tercero.objects.all().delete()
		print "clear Tercero"
