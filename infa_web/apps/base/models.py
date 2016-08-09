from __future__ import unicode_literals
from django.db import models

class Esdo(models.Model):
	cesdo = models.AutoField(primary_key=True)
	nesdo = models.CharField(max_length=40)
	estavali = models.CharField(max_length=10)
	colfon = models.CharField(max_length=20)

	def __str__(self):
		return self.nesdo

	def __init__(self):
		return self.nesdo

class Ubica(models.Model):
	cubica = models.AutoField(primary_key=True)
	nubica = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo)

	def __str__(self):
		return self.nubica

	def __init__(self):
		return self.nubica

class Departamento(models.Model):
	cdepar = models.AutoField(primary_key=True)
	ndepar = models.CharField(max_length=45)

	def __str__(self):
		return self.ndepar

	def __init__(self):
		return self.ndepar

class Ciudad(models.Model):
	cciu = models.AutoField(primary_key=True)
	nciu = models.CharField(max_length=40)
	cdepar = models.ForeignKey(Departamento)

	def __str__(self):
		return self.nciu

	def __init__(self):
		return self.nciu

class Iva(models.Model):
	civa = models.AutoField(primary_key=True)
	niva = models.CharField(max_length=40)
	poriva = models.DecimalField(max_digits=6, decimal_places=2)
	idtira = models.CharField(max_length=1)
	cesdo = models.ForeignKey(Esdo)

	def __str__(self):
		return self.niva

	def __init__(self):
		return self.niva

class Regiva(models.Model):
	cregiva = models.AutoField(primary_key=True)
	nregiva = models.CharField(max_length=40)

	def __str__(self):
		return self.nregiva

	def __init__(self):
		return self.nregiva

class Tiide(models.Model):
	idtiide = models.AutoField(primary_key=True)
	ntiide = models.CharField(max_length=40)

	def __str__(self):
		return self.ntiide

	def __init__(self):
		return self.ntiide