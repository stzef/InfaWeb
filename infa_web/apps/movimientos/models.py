from __future__ import unicode_literals
from infa_web.apps.articulos.models import *
from infa_web.apps.terceros.models import *
from infa_web.apps.base.models import *
from django.db import models
from infa_web.apps.base.constantes import *
from django.core.validators import MinValueValidator

class Timo(models.Model):
	ctimo = models.IntegerField(primary_key=True)
	ntimo = models.CharField(max_length=40)
	prefijo = models.CharField(max_length=4)
	filas = models.IntegerField()
	nrepo = models.CharField(max_length=20)

	def __str__(self):
		return self.ntimo

class Mven(models.Model):
	class Meta:
		unique_together = (('cmven', 'ctimo'))

	cmven = models.IntegerField(primary_key=True)
	fmven = models.DateTimeField()
	docrefe = models.CharField(max_length=10)
	citerce = models.ForeignKey(Tercero)
	ctimo = models.ForeignKey(Timo)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	vttotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	descri = models.CharField(max_length=250)
	detaanula = models.CharField(max_length=250)
	cbode0 = models.ForeignKey(Bode, related_name='cbode0',default=DEFAULT_BODEGA)
	cbode1 = models.ForeignKey(Bode, related_name='cbode1',null=True,blank=True)
	#cbode1 = models.ForeignKey(Bode, related_name='cbode1',default=DEFAULT_BODEGA,null=True,blank=True)

	def __str__(self):
		return str(self.cmven)

class Mvendeta(models.Model):
	class Meta:
		unique_together = (('cmven', 'ctimo','it'))

	cmven = models.ForeignKey(Mven)
	it = models.CharField(max_length=4)
	ctimo = models.ForeignKey(Timo)
	carlos = models.ForeignKey(Arlo)
	#citerce = models.ForeignKey(Tercero)
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	vunita = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	vtotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	def __str__(self):
		return str(self.cmven)
		
class Mvsa(models.Model):
	class Meta:
		unique_together = (('cmvsa', 'ctimo'))

	cmvsa = models.IntegerField(primary_key=True)
	fmvsa = models.DateTimeField()
	docrefe = models.CharField(max_length=10)
	citerce = models.ForeignKey(Tercero)
	ctimo = models.ForeignKey(Timo)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	vttotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	descri = models.CharField(max_length=250)
	detaanula = models.CharField(max_length=250)
	cbode0 = models.ForeignKey(Bode, related_name = 'cbode_0',default=DEFAULT_BODEGA)
	cbode1 = models.ForeignKey(Bode, related_name = 'cbode_1',default=DEFAULT_BODEGA)

	def __str__(self):
		return str(self.cmvsa)

class Mvsadeta(models.Model):
	class Meta:
		unique_together = (('cmvsa', 'ctimo','it'))
	cmvsa = models.ForeignKey(Mvsa)
	it = models.CharField(max_length=4)
	ctimo = models.ForeignKey(Timo)
	carlos = models.ForeignKey(Arlo)
	#citerce = models.ForeignKey(Tercero)
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	vunita = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	vtotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	def __str__(self):
		return str(self.cmvsa)
