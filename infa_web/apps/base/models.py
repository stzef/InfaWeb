from __future__ import unicode_literals
from django.db import models
from infa_web.apps.base.constantes import *
from django.core.validators import MinValueValidator


class Esdo(models.Model):
	cesdo = models.AutoField(primary_key=True)
	nesdo = models.CharField(max_length=40)
	estavali = models.CharField(max_length=10)
	colfon = models.CharField(max_length=20)

	def __str__(self):
		return self.nesdo

	def natural_key(self):
		return (self.cesdo)

class Modules(models.Model):
	smodule = models.CharField(max_length=5)
	nmodule = models.CharField(max_length=20)
	enabled_enterprise = models.BooleanField()
	enabled = models.BooleanField()
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO) 

	def __str__(self):
		return self.nmodule

	def natural_key(self):
		return (self.smodule)

class Parameters(models.Model):
	cparam = models.CharField(max_length=10)
	module = models.ForeignKey(Modules)
	nparam = models.CharField(max_length=40)

	val_boolean = models.BooleanField(blank=True)
	val_integer = models.IntegerField(blank=True, null=True)
	val_string = models.CharField(max_length=40,blank=True, null=True)
	def __str__(self):
		return self.nparam

class Ubica(models.Model):
	cubica = models.AutoField(primary_key=True)
	nubica = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO) 

	def __str__(self):
		return self.nubica

class Departamento(models.Model):
	cdepar = models.AutoField(primary_key=True)
	ndepar = models.CharField(max_length=45)

	def __str__(self):
		return self.ndepar

	def natural_key(self):
		return (self.cdepar)

class Ciudad(models.Model):
	cciu = models.AutoField(primary_key=True)
	nciu = models.CharField(max_length=40)
	cdepar = models.ForeignKey(Departamento)
	def __str__(self):
		return self.nciu
	def __unicode__(self):
		return self.nciu

class Iva(models.Model):
	civa = models.AutoField(primary_key=True)
	niva = models.CharField(max_length=40)
	poriva = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
	idtira = models.CharField(max_length=1)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.niva

class Regiva(models.Model):
	cregiva = models.AutoField(primary_key=True)
	nregiva = models.CharField(max_length=40)

	def __str__(self):
		return self.nregiva

class Tiide(models.Model):
	idtiide = models.AutoField(primary_key=True)
	ntiide = models.CharField(max_length=40)

	def __str__(self):
		return self.ntiide

