from __future__ import unicode_literals
from infa_web.apps.base.models import *
from django.db import models

class Autorre(models.Model):
	cautorre = models.AutoField(primary_key=True)
	nautorre = models.CharField(max_length=40)

	def __str__(self):
		return self.nautorre

	def __init__(self):
		return self.nautorre

class Vende(models.Model):
	cvende = models.AutoField(primary_key=True)
	nvende = models.CharField(max_length=80)
	porventa = models.DecimalField(max_digits=7, decimal_places=4)
	cesdo = models.ForeignKey(Esdo)

	def __str__(self):
		return self.nvende

	def __init__(self):
		return self.nvende

class Ruta(models.Model):
	cruta = models.AutoField(primary_key=True)
	nruta = models.CharField(max_length=45)
	cesdo = models.ForeignKey(Esdo)

	def __str__(self):
		return self.nruta

	def __init__(self):
		return self.nruta

class Zona(models.Model):
	czona = models.AutoField(primary_key=True)
	nzona = models.CharField(max_length=40)
	activo = models.CharField(max_length=1)

	def __str__(self):
		return self.nzona

	def __init__(self):
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
	nomegre = models.CharField(max_length=100)
	replegal = models.CharField(max_length=100)
	dirterce = models.CharField(max_length=80)
	telterce = models.CharField(max_length=20)
	faxterce = models.CharField(max_length=20)
	cciu = models.ForeignKey(Ciudad)
	email = models.CharField(max_length=40)
	contacto = models.CharField(max_length=20)
	cregiva = models.ForeignKey(Regiva)
	cautorre = models.ForeignKey(Autorre)
	cesdo = models.ForeignKey(Esdo)
	cvende = models.ForeignKey(Vende)
	topcxc = models.DecimalField(max_digits=15, decimal_places=2)
	ndiacxc = models.IntegerField()
	czona = models.ForeignKey(Zona)
	clipre = models.IntegerField()
	fnaci = models.DateField()
	naju = models.IntegerField()
	cruta = models.ForeignKey(Ruta)
	ordenruta = models.IntegerField()

	def __str__(self):
		return self.nomcomer

	def __init__(self):
		return self.nomcomer