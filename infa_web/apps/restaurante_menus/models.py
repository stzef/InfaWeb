from __future__ import unicode_literals

from infa_web.apps.base.models import *
from infa_web.apps.articulos.models import Unidades

from infa_web.apps.base.constantes import *

from django.core.validators import MinValueValidator, MaxValueValidator


from django.db import models

class GposMenus(models.Model):
	cgpomenu = models.IntegerField(primary_key=True)
	ngpomenu = models.CharField(max_length=50)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	def __str__(self):
		return self.ningre

	def __unicode__(self):
		return self.ningre

class Ingredientes(models.Model):
	cingre = models.IntegerField(primary_key=True)
	ningre = models.CharField(max_length=50)
	canti = models.DecimalField(max_digits=15, decimal_places=2,default=0.00)
	vcosto = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)
	ifcostear = models.BooleanField(default=True)
	stomin = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=1)
	stomax = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=100)
	ifedinom = models.BooleanField(max_length=1)

	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	cunidad = models.ForeignKey(Unidades, default=DEFAULT_UNIDAD)
	civa = models.ForeignKey(Iva,default=DEFAULT_IVA)


	foto = models.FileField(upload_to="img/ingredients/", blank=True, null=True,default=DEFAULT_IMAGE_INGREDIENTS)

	def __str__(self):
		return self.ningre

	def __unicode__(self):
		return self.ningre

	class Meta:
		ordering = ['-ningre']

class Platos(models.Model):
	cplato = models.IntegerField(primary_key=True)
	nplato = models.CharField(max_length=50)
	fcrea = models.DateTimeField()
	vttotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)

	foto = models.FileField(upload_to="img/dishes/", blank=True, null=True,default=DEFAULT_IMAGE_DISHES)

	def __str__(self):
		return self.nplato

	def __unicode__(self):
		return self.nplato

class Platosdeta(models.Model):
	cplato = models.ForeignKey(Platos)
	cingre = models.ForeignKey(Ingredientes)
	it = models.CharField(max_length=50)
	canti = models.DecimalField(max_digits=15, decimal_places=2,default=0.00)
	vunita = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)
	vtotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)

	def __str__(self):
		return self.cplato

	def __unicode__(self):
		return self.cplato

class Menus(models.Model):
	cmenu = models.IntegerField(primary_key=True)
	nmenu = models.CharField(max_length=50)
	fcrea = models.DateTimeField()
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	cgpomenu = models.ForeignKey(GposMenus,default=CESTADO_ACTIVO)
	npax = models.IntegerField()
	pvta1 = models.DecimalField(max_digits=15, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	pvta2 = models.DecimalField(max_digits=15, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])
	pvta3 = models.DecimalField(max_digits=15, decimal_places=2,default=0,blank=True, null=True,validators=[MinValueValidator(0)])

	vttotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)

	foto = models.FileField(upload_to="img/dishes/", blank=True, null=True,default=DEFAULT_IMAGE_DISHES)

	def __str__(self):
		return self.nplato

	def __unicode__(self):
		return self.nplato

class Menusdeta(models.Model):
	cmenu = models.ForeignKey(Menus)
	it = models.CharField(max_length=50)
	cplato = models.ForeignKey(Platos)
	canti = models.DecimalField(max_digits=15, decimal_places=2,default=0.00)
	vunita = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)
	vtotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)

	def __str__(self):
		return self.cplato

	def __unicode__(self):
		return self.cplato
