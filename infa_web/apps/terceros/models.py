from __future__ import unicode_literals
from infa_web.apps.base.models import *
from django.db import models
from infa_web.apps.base.constantes import *
from django.core.validators import MinValueValidator
from django.utils import timezone

class Autorre(models.Model):
	cautorre = models.AutoField(primary_key=True)
	nautorre = models.CharField(max_length=40)

	def __str__(self):
		return self.nautorre

class Vende(models.Model):
	cvende = models.AutoField(primary_key=True)
	nvende = models.CharField(max_length=80)
	porventa = models.DecimalField(max_digits=7, decimal_places=4,validators=[MinValueValidator(0)])
	cesdo = models.ForeignKey(Esdo)

	def __str__(self):
		return self.nvende

class Ruta(models.Model):
	cruta = models.AutoField(primary_key=True)
	nruta = models.CharField(max_length=45)
	cesdo = models.ForeignKey(Esdo)

	def __str__(self):
		return self.nruta

class Personas(models.Model):
	cpersona = models.CharField(primary_key=True,max_length=5)
	npersona = models.CharField(max_length=45)

	def __str__(self):
		return self.npersona

class Zona(models.Model):
	czona = models.AutoField(primary_key=True)
	nzona = models.CharField(max_length=40)
	cesdo = models.ForeignKey(Esdo)

	def __str__(self):
		return self.nzona
		
class Tercero(models.Model):
	citerce = models.AutoField(primary_key=True)
	idterce = models.CharField(max_length=20)
	dv = models.CharField(max_length=1)
	ctiide = models.ForeignKey(Tiide)
	rasocial = models.CharField(max_length=200)
	nomcomer = models.CharField(max_length=200)
	ape1 = models.CharField(max_length=40)
	ape2 = models.CharField(max_length=40)
	nom1 = models.CharField(max_length=40)
	nom2 = models.CharField(max_length=40)
	sigla = models.CharField(max_length=100)
	replegal = models.CharField(max_length=100)
	dirterce = models.CharField(max_length=80)
	telterce = models.CharField(max_length=20)
	faxterce = models.CharField(max_length=20,blank=True, null=True)
	ciudad = models.ForeignKey(Ciudad)
	email = models.CharField(max_length=40,blank=True, null=True)
	contacto = models.CharField(max_length=20,blank=True, null=True)
	cregiva = models.ForeignKey(Regiva,default=DEFAULT_REGIMEN_IVA)
	cautorre = models.ForeignKey(Autorre,default=CESTADO_AUTORRETENEDOR)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	cvende = models.ForeignKey(Vende,default=DEFAULT_VENDE)
	topcxc = models.DecimalField(max_digits=15, decimal_places=2)
	czona = models.ForeignKey(Zona,default=DEFAULT_ZONA)
	clipre = models.IntegerField(default=DEFAULT_LISTA_PRECIOS)
	fnaci = models.DateField(default=timezone.now)
	cruta = models.ForeignKey(Ruta,default=DEFAULT_RUTA)
	ordenruta = models.IntegerField()
	cpersona = models.ForeignKey(Personas,default=DEFAULT_PERSONA)

	def nameFull(self):
		return self.nom1 + " " + self.nom2 + " " + self.ape1 + " " + self.ape2

	def __str__(self):
		return self.rasocial

