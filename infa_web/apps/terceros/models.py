from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

from infa_web.apps.base.constantes import *
from infa_web.apps.base.models import *
from infa_web.apps.usuarios.models import Usuario

class Autorre(models.Model):

	class Meta:
		ordering = ["nautorre"]

	cautorre = models.AutoField(primary_key=True)
	nautorre = models.CharField(max_length=40)

	def __str__(self):
		return self.nautorre

class Vende(models.Model):

	class Meta:
		ordering = ["nvende"]

	cvende = models.AutoField(primary_key=True)
	nvende = models.CharField(max_length=80)
	porventa = models.DecimalField(max_digits=7, decimal_places=4,validators=[MinValueValidator(0)])
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	usuario = models.ForeignKey(Usuario)

	def __str__(self):
		return self.nvende

class Cobra(models.Model):

	class Meta:
		ordering = ["ncobra"]

	ccobra = models.AutoField(primary_key=True)
	ncobra = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.ncobra

class Ruta(models.Model):

	class Meta:
		ordering = ["nruta"]

	cruta = models.AutoField(primary_key=True)
	nruta = models.CharField(max_length=45)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nruta

class Personas(models.Model):

	class Meta:
		ordering = ["npersona"]

	cpersona = models.CharField(primary_key=True,max_length=5)
	npersona = models.CharField(max_length=45)

	def __str__(self):
		return self.npersona

class Zona(models.Model):

	class Meta:
		ordering = ["nzona"]

	czona = models.AutoField(primary_key=True)
	nzona = models.CharField(max_length=40)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nzona

class Tercero(models.Model):
	citerce = models.AutoField(primary_key=True)
	idterce = models.CharField(max_length=20)
	dv = models.CharField(max_length=1)
	ctiide = models.ForeignKey(Tiide,default=DEFAULT_TIIDE)
	rasocial = models.CharField(max_length=200)
	nomcomer = models.CharField(max_length=200)
	ape1 = models.CharField(max_length=40,blank=True, null=True)
	ape2 = models.CharField(max_length=40,blank=True, null=True)
	nom1 = models.CharField(max_length=40,blank=True, null=True)
	nom2 = models.CharField(max_length=40,blank=True, null=True)
	sigla = models.CharField(max_length=100,blank=True, null=True)
	replegal = models.CharField(max_length=100,blank=True, null=True)
	dirterce = models.CharField(max_length=80)
	telterce = models.CharField(max_length=20)
	faxterce = models.CharField(max_length=20,blank=True, null=True)
	ciudad = models.ForeignKey(Ciudad)
	email = models.CharField(max_length=40,blank=True, null=True)
	contacto = models.CharField(max_length=20,blank=True, null=True)
	cregiva = models.ForeignKey(Regiva,default=DEFAULT_REGIMEN_IVA)
	cautorre = models.ForeignKey(Autorre,default=DEFAULT_AUTORRETENEDOR)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	cvende = models.ForeignKey(Vende,default=DEFAULT_VENDE)
	topcxc = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True,default=1000000)
	czona = models.ForeignKey(Zona,default=DEFAULT_ZONA)
	clipre = models.IntegerField(default=DEFAULT_LISTA_PRECIOS)
	fnaci = models.DateField(default=timezone.now)
	cruta = models.ForeignKey(Ruta,default=DEFAULT_RUTA)
	ordenruta = models.IntegerField(blank=True, null=True)
	cpersona = models.ForeignKey(Personas,default=DEFAULT_PERSONA)

	def nameFull(self):
		return self.nom1 + " " + self.nom2 + " " + self.ape1 + " " + self.ape2

	def __str__(self):
		return self.rasocial

class Coti(models.Model):
	ccoti = models.CharField(primary_key=True, max_length=10)
	fcoti = models.DateTimeField()
	citerce = models.ForeignKey(Tercero)
	descri = models.CharField(max_length=300)
	osberini = models.CharField(max_length=250)
	autoriza = models.CharField(max_length=100)
	obserfin = models.CharField(max_length=250)
	#HCOTI                            Char(8),
	ffin = models.DateTimeField()
	#HFIN                             Char(8),
	fentre = models.DateTimeField()
	#HENTRE                           Char(8),
	ctiservi = models.ForeignKey(Tiservi)
	cvende = models.ForeignKey(Vende)
	#CVENDETEC                        Char(4),
	ifareglad = models.BooleanField()
	ctimo = models.ForeignKey(Timo)
	docuref = models.CharField(max_length=10)
	fhcoti = models.DateTimeField()
	detaanula = models.CharField(max_length=300)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

