from __future__ import unicode_literals

from infa_web.apps.base.models import *
from infa_web.apps.articulos.models import Unidades, Arlo

from infa_web.apps.base.constantes import *

from django.core.validators import MinValueValidator, MaxValueValidator


from django.db import models

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

	def __str__(self):
		return self.ningre

	def __unicode__(self):
		return self.ningre

	class Meta:
		ordering = ['-ningre']

	"""
	def natural_key(self):
		return ({
			"cingre" : self.cingre,
			"ningre" : self.ningre,
			"canti" : self.canti,
			"vcosto" : self.vcosto,
			"ifcostear" : self.ifcostear,
			"stomin" : self.stomin,
			"stomax" : self.stomax,
			"ifedinom" : self.ifedinom,
			"cesdo" : self.cesdo.natural_key(),
			"cunidad" : self.cunidad.natural_key(),
			"civa" : self.civa.natural_key(),
		})
	"""

class Platos(models.Model):
	class Meta:
		permissions = (
			("list_platos", "Puede Listar Platos"),
		)
	cplato = models.IntegerField(primary_key=True)
	nplato = models.CharField(max_length=50)
	fcrea = models.DateTimeField(auto_now_add=True)
	npax = models.IntegerField(default=1)
	vttotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)

	foto = models.FileField(upload_to="img/dishes/", blank=True, null=True,default=DEFAULT_IMAGE_DISHES)

	def __str__(self):
		return self.nplato

	def __unicode__(self):
		return self.nplato

	def natural_key(self):
		return ({
			"cplato" : self.cplato,
			"nplato" : self.nplato,
			#"fcrea" : self.fcrea,
			"npax" : self.npax,
			"vttotal" : self.vttotal,
			"foto" : self.foto.url,
		})

class Platosdeta(models.Model):
	cplato = models.ForeignKey(Platos)
	cingre = models.ForeignKey(Ingredientes)
	it = models.CharField(max_length=50)
	canti = models.DecimalField(max_digits=15, decimal_places=2,default=0.00)
	cunidad = models.ForeignKey(Unidades, default=DEFAULT_UNIDAD)
	vunita = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)
	vtotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)

	def __str__(self):
		return self.it

	def __unicode__(self):
		return self.it

	"""
	def natural_key(self):
		return ({
			"cplato" : self.cplato.natural_key(),
			"cingre" : self.cingre.natural_key(),
			"it" : self.it,
			"canti" : self.canti,
			"cunidad" : self.cunidad.natural_key(),
			"vunita" : self.vunita,
			"vtotal" : self.vtotal,
		})
	"""

class Menusdeta(models.Model):
	cmenu = models.ForeignKey(Arlo)
	it = models.CharField(max_length=50)
	cplato = models.ForeignKey(Platos)
	nplato = models.CharField(max_length=50)
	canti = models.DecimalField(max_digits=15, decimal_places=2,default=0.00)
	#cunidad = models.ForeignKey(Unidades, default=DEFAULT_UNIDAD)
	vunita = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)
	vtotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)

	def __str__(self):
		return self.it

	def __unicode__(self):
		return self.it

	"""
	def natural_key(self):
		return ({
			"cmenu" : self.cmenu.natural_key(),
			"it" : self.it,
			"cplato" : self.cplato.natural_key(),
			"nplato" : self.nplato,
			"canti" : self.canti,
			"vunita" : self.vunita,
			"vtotal" : self.vtotal,
		})
	"""
