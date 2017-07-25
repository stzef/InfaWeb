# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from infa_web.apps.terceros.models import *
from infa_web.apps.base.models import *
from infa_web.apps.base.constantes import *

from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

class Tiarlos(models.Model):
	class Meta:
		ordering = ["ntiarlos"]

	ctiarlos = models.AutoField(primary_key=True)
	ntiarlos = models.CharField(max_length=40)

	def __str__(self):
		return self.ntiarlos

class Gpo(models.Model):

	class Meta:
		ordering = ["ngpo"]

	cgpo = models.IntegerField(primary_key=True,validators=[MinValueValidator(0)])
	ngpo = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	orden = models.IntegerField(default=0,validators=[MinValueValidator(0)])
	impresora = models.CharField(max_length=100,default="")

	def __str__(self):
		return self.ngpo

	def __unicode__(self):
		return self.ngpo

class Marca(models.Model):

	class Meta:
		ordering = ["nmarca"]

	cmarca = models.AutoField(primary_key=True)
	nmarca = models.CharField(max_length=60)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nmarca

	def __unicode__(self):
		return self.nmarca

	class Meta:
		ordering = ['nmarca']

class Unidades(models.Model):

	class Meta:
		ordering = ["nunidad"]

	cunidad = models.AutoField(primary_key=True)
	nunidad = models.CharField(max_length=60)
	peso = models.IntegerField(validators=[MinValueValidator(0)])

	def __str__(self):
		return self.nunidad

	def __unicode__(self):
		return self.nunidad

	def natural_key(self):
		return ({
			"cunidad" : self.cunidad,
			"nunidad" : self.nunidad,
			"peso" : self.peso,
		})

class Arlo(models.Model):
	carlos = models.IntegerField(primary_key=True)
	cbarras = models.CharField(max_length=50,blank=True,null=True)
	cgpo = models.ForeignKey(Gpo,default=DEFAULT_GRUPO)
	ncorto = models.CharField(max_length=50)
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2,default=0.00)
	vcosto = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)
	ifcostear = models.BooleanField(default=True)
	ifpvfijo = models.BooleanField()
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	ctiarlo = models.ForeignKey(Tiarlos,default=CTIARLO_ARTICULO)
	cunidad = models.ForeignKey(Unidades, default=DEFAULT_UNIDAD)
	ivas_civa = models.ForeignKey(Iva,default=DEFAULT_IVA)
	stomin = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=1)
	stomax = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=100)
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
	refe = models.CharField(max_length=100,blank=True,null=True)
	cmarca = models.ForeignKey(Marca,default=DEFAULT_MARCA)
	ifdesglo = models.BooleanField()
	mesesgara = models.IntegerField(blank=True,null=True,validators=[MinValueValidator(0)],default=0)
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

	npax = models.IntegerField(default=0)
	fcrea = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.nlargo

	def __unicode__(self):
		return self.nlargo

	def natural_key(self):
		return ({
			"carlos" : self.carlos,
			"cbarras" : self.cbarras,
			#"cgpo" : self.cgpo,
			"ncorto" : self.ncorto,
			"nlargo" : self.nlargo,
			"canti" : self.canti,
			"vcosto" : self.vcosto,
			"ifcostear" : self.ifcostear,
			"ifpvfijo" : self.ifpvfijo,
			#"cesdo" : self.cesdo,
			#"ctiarlo" : self.ctiarlo,
			#"cunidad" : self.cunidad,
			#"ivas_civa" : self.ivas_civa,
			"stomin" : self.stomin,
			"stomax" : self.stomax,
			"pvta1" : self.pvta1,
			"pvta2" : self.pvta2,
			"pvta3" : self.pvta3,
			"pvta4" : self.pvta4,
			"pvta5" : self.pvta5,
			"pvta6" : self.pvta6,
			"ifedinom" : self.ifedinom,
			"refe" : self.refe,
			#"cmarca" : self.cmarca,
			"ifdesglo" : self.ifdesglo,
			"mesesgara" : self.mesesgara,
			#"cubica" : self.cubica,
			"porult1" : self.porult1,
			"porult2" : self.porult2,
			"porult3" : self.porult3,
			"porult4" : self.porult4,
			"porult5" : self.porult5,
			"porult6" : self.porult6,
			"foto1" : self.foto1.url,
			"foto2" : self.foto2.url,
			"foto3" : self.foto3.url,
		})

	class Meta:
		ordering = ['-nlargo']
		permissions = (
			("list_arlo", "Puede Listar Articulos"),
			("list_gpo", "Puede Listar Grupos"),
			("list_tiarlos", "Puede Listar Tipo de Articulos"),
		)


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
