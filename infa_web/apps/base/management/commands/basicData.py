# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from infa_web.apps.base.constantes import *
from infa_web.apps.base.models import *
from infa_web.apps.articulos.models import *
class Command(BaseCommand):
	def handle(self, *args, **options):
		Esdo.objects.all().delete()
		estadoActivo = Esdo.objects.create(cesdo=CESTADO_ACTIVO,nesdo="ACTIVO",estavali=1,colfon=1)
		estadoInactivo = Esdo.objects.create(cesdo=CESTADO_INACTIVO,nesdo="INACTIVO",estavali=0,colfon=0)
		
		Marca.objects.all().delete()
		Marca.objects.create(cmarca=DEFAULT_MARCAR,nmarca="SIN MARCA",cesdo=estadoActivo)

		Bode.objects.all().delete()
		Bode.objects.create(cbode=DEFAULT_BODEGA,nbode="SIN BODEGA",esbode=1,cesdo=estadoActivo)

		Ubica.objects.all().delete()
		Ubica.objects.create(cubica=DEFAULT_UBICACION,nubica="SIN UBICACION",cesdo=estadoActivo)

		Gpo.objects.all().delete()
		Gpo.objects.create(cgpo=DEFAULT_GRUPO,ngpo="SIN GRUPO",cesdo=estadoActivo)
		
		Departamento.objects.all().delete()
		departamento = Departamento.objects.create(cdepar=9,ndepar="Cundinamarca")

		Ciudad.objects.all().delete()
		Ciudad.objects.create(nciu='Alban',cdepar=departamento)
		Ciudad.objects.create(nciu='Bogotá',cdepar=departamento)
		Ciudad.objects.create(nciu='Bojaca',cdepar=departamento)
		Ciudad.objects.create(nciu='Bosa',cdepar=departamento)
		Ciudad.objects.create(nciu='Briceño',cdepar=departamento)
		Ciudad.objects.create(nciu='Cajicá',cdepar=departamento)
		Ciudad.objects.create(nciu='Chía',cdepar=departamento)
		Ciudad.objects.create(nciu='Chinauta',cdepar=departamento)
		Ciudad.objects.create(nciu='Choconta',cdepar=departamento)
		Ciudad.objects.create(nciu='Cota',cdepar=departamento)
		Ciudad.objects.create(nciu='El Muña',cdepar=departamento)
		Ciudad.objects.create(nciu='El Rosal',cdepar=departamento)
		Ciudad.objects.create(nciu='Engativá',cdepar=departamento)
		Ciudad.objects.create(nciu='Facatativa',cdepar=departamento)
		Ciudad.objects.create(nciu='Fontibón',cdepar=departamento)
		Ciudad.objects.create(nciu='Funza',cdepar=departamento)
		Ciudad.objects.create(nciu='Fusagasuga',cdepar=departamento)
		Ciudad.objects.create(nciu='Gachancipá',cdepar=departamento)
		Ciudad.objects.create(nciu='Girardot',cdepar=departamento)
		Ciudad.objects.create(nciu='Guaduas',cdepar=departamento)
		Ciudad.objects.create(nciu='Guayavetal',cdepar=departamento)
		Ciudad.objects.create(nciu='La Calera',cdepar=departamento)
		Ciudad.objects.create(nciu='La Caro',cdepar=departamento)
		Ciudad.objects.create(nciu='Madrid',cdepar=departamento)
		Ciudad.objects.create(nciu='Mosquera',cdepar=departamento)
		Ciudad.objects.create(nciu='Nemocón',cdepar=departamento)
		Ciudad.objects.create(nciu='Puente Piedra',cdepar=departamento)
		Ciudad.objects.create(nciu='Puente Quetame',cdepar=departamento)
		Ciudad.objects.create(nciu='Puerto Bogotá',cdepar=departamento)
		Ciudad.objects.create(nciu='Puerto Salgar',cdepar=departamento)
		Ciudad.objects.create(nciu='Quetame',cdepar=departamento)
		Ciudad.objects.create(nciu='Sasaima',cdepar=departamento)
		Ciudad.objects.create(nciu='Sesquile',cdepar=departamento)
		Ciudad.objects.create(nciu='Sibaté',cdepar=departamento)
		Ciudad.objects.create(nciu='Silvania',cdepar=departamento)
		Ciudad.objects.create(nciu='Simijaca',cdepar=departamento)
		Ciudad.objects.create(nciu='Soacha',cdepar=departamento)
		Ciudad.objects.create(nciu='Sopo',cdepar=departamento)
		Ciudad.objects.create(nciu='Suba',cdepar=departamento)
		Ciudad.objects.create(nciu='Subachoque',cdepar=departamento)
		Ciudad.objects.create(nciu='Susa',cdepar=departamento)
		Ciudad.objects.create(nciu='Tabio',cdepar=departamento)
		Ciudad.objects.create(nciu='Tenjo',cdepar=departamento)
		Ciudad.objects.create(nciu='Tocancipa',cdepar=departamento)
		Ciudad.objects.create(nciu='Ubaté',cdepar=departamento)
		Ciudad.objects.create(nciu='Usaquén',cdepar=departamento)
		Ciudad.objects.create(nciu='Usme',cdepar=departamento)
		Ciudad.objects.create(nciu='Villapinzón',cdepar=departamento)
		Ciudad.objects.create(nciu='Villeta',cdepar=departamento)
		Ciudad.objects.create(nciu='Zipaquirá',cdepar=departamento)
