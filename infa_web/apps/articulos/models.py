# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from infa_web.apps.terceros.models import *
from infa_web.apps.base.models import *
from infa_web.apps.base.constantes import *

from django.core.validators import MinValueValidator
 
from django.db import models

class Tiarlos(models.Model):
	ctiarlos = models.AutoField(primary_key=True)
	ntiarlos = models.CharField(max_length=40)
	
	def __str__(self):
		return self.ntiarlos

class Gpo(models.Model):
	cgpo = models.IntegerField(primary_key=True,validators=[MinValueValidator(0)])
	ngpo = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.ngpo

	def __unicode__(self):
		return self.ngpo

class Marca(models.Model):
	cmarca = models.AutoField(primary_key=True)
	nmarca = models.CharField(max_length=60)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nmarca

	def __unicode__(self):
		return self.nmarca

class Unidades(models.Model):
	cunidad = models.AutoField(primary_key=True)
	nunidad = models.CharField(max_length=60,default=DEFAULT_UNIDAD)
	peso = models.IntegerField(validators=[MinValueValidator(0)])

	def __str__(self):
		return self.nunidad

	def __unicode__(self):
		return self.nunidad

class Arlo(models.Model):
	carlos = models.IntegerField(primary_key=True)
	cbarras = models.CharField(max_length=50)
	cgpo = models.ForeignKey(Gpo,default=DEFAULT_GRUPO)
	ncorto = models.CharField(max_length=50)
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	vcosto = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	ifcostear = models.BooleanField(default=True)
	ifpvfijo = models.BooleanField()
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	ctiarlo = models.ForeignKey(Tiarlos,default=CTIARLO_ARTICULO)
	cunidad = models.ForeignKey(Unidades)
	ivas_civa = models.ForeignKey(Iva,default=DEFAULT_IVA)
	stomin = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	stomax = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	pvta1 = models.DecimalField(max_digits=15, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	pvta2 = models.DecimalField(max_digits=15, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	pvta3 = models.DecimalField(max_digits=15, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	pvta4 = models.DecimalField(max_digits=15, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	pvta5 = models.DecimalField(max_digits=15, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	pvta6 = models.DecimalField(max_digits=15, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	citerce1 = models.ForeignKey(Tercero, related_name='citerce1', blank=True, null=True)
	vcosto1 = models.DecimalField(max_digits=15, decimal_places=2,default=0,null=True,blank=True,validators=[MinValueValidator(0)])
	fcosto1 = models.DateField(blank=True,null=True)
	citerce2 = models.ForeignKey(Tercero, related_name='citerce2', blank=True, null=True)
	vcosto2 = models.DecimalField(max_digits=15, decimal_places=2,default=0,null=True,blank=True,validators=[MinValueValidator(0)])
	fcosto2 = models.DateField(blank=True,null=True)
	citerce3 = models.ForeignKey(Tercero, related_name='citerce3', blank=True, null=True)
	vcosto3 = models.DecimalField(max_digits=15, decimal_places=2,default=0,null=True,blank=True,validators=[MinValueValidator(0)])
	fcosto3 = models.DateField(blank=True,null=True)
	ifedinom = models.BooleanField(max_length=1)
	refe = models.CharField(max_length=20)
	cmarca = models.ForeignKey(Marca,default=DEFAULT_MARCA)
	ifdesglo = models.BooleanField()
	mesesgara = models.IntegerField()
	cubica = models.ForeignKey(Ubica,default=DEFAULT_UBICACION)
	porult1 = models.DecimalField(max_digits=6, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	porult2 = models.DecimalField(max_digits=6, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	porult3 = models.DecimalField(max_digits=6, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	porult4 = models.DecimalField(max_digits=6, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	porult5 = models.DecimalField(max_digits=6, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	porult6 = models.DecimalField(max_digits=6, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	foto1 = models.FileField(upload_to="img/articles/", blank=True, null=True,default=DEFAULT_IMAGE_ARTICLE)
	foto2 = models.FileField(upload_to="img/articles/", blank=True, null=True,default=DEFAULT_IMAGE_ARTICLE)
	foto3 = models.FileField(upload_to="img/articles/", blank=True, null=True,default=DEFAULT_IMAGE_ARTICLE)

	def __str__(self):
		return self.nlargo

class Arlosdesglo(models.Model):
	carlosp = models.ForeignKey(Arlo, related_name='carlosp')
	itglo = models.CharField(max_length=4,validators=[MinValueValidator(0)])
	carlosglo = models.ForeignKey(Arlo, related_name='carlosglo')
	cantiglo = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	costoglo = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	vtoglo = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return str(self.carlosp)+' - '+str(self.itglo)

	def __unicode__(self):
		return str(self.carlosp)+' - '+str(self.itglo)

class Bode(models.Model):
	cbode = models.AutoField(primary_key=True)
	nbode = models.CharField(max_length=80)
	esbode = models.CharField(max_length=2)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nbode

