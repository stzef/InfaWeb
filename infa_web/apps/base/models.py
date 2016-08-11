from __future__ import unicode_literals
from django.db import models
from infa_web.apps.base.constantes import *

class Esdo(models.Model):
	cesdo = models.AutoField(primary_key=True)
	nesdo = models.CharField(max_length=40)
	estavali = models.CharField(max_length=10)
	colfon = models.CharField(max_length=20)

	def __str__(self):
		return self.nesdo

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
	poriva = models.DecimalField(max_digits=6, decimal_places=2)
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

