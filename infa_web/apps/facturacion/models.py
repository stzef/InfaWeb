from __future__ import unicode_literals

from django.db import models

from infa_web.apps.base.models import *
from infa_web.apps.terceros.models import *
from infa_web.apps.articulos.models import *

class Fac(models.Model):
	cfac = models.CharField(max_length=10)
	femi = models.DateTimeField()
	citerce = models.ForeignKey(Tercero)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	fpago = models.DateTimeField()
	ctifopa = models.ForeignKey(Tifopa)
	descri = models.CharField(max_length=200)
	detaanula = models.CharField(max_length=200)
	vtbruto = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtbase = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtiva = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vflete = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vdescu = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vttotal = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vefe = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtar = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	doctar = models.CharField(max_length=10)
	bancotar = models.ForeignKey(Banfopa,related_name="bancotar")
	vchq = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	docchq = models.CharField(max_length=10)
	bancochq = models.ForeignKey(Banfopa,related_name="bancochq")
	ventre = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vcambio = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	#cusu char(20)
	ccaja = models.ForeignKey(Caja)
	#ncuo integer, 
	cvende  = models.ForeignKey(Vende)
	cdomici  = models.ForeignKey(Domici)
	tpordes = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
	cemdor  = models.ForeignKey(Emdor)
	#ccoti char(10)
	vncre = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	doccre = models.CharField(max_length=10)
	brtefte = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	prtefte = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
	vrtefte = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	fhasdomi = models.DateTimeField()
	#ccobra char(4)

	def __str__(self):
		return self.cfac

class Facdeta(models.Model):
	cfac = models.ForeignKey(Fac)
	itfac = models.CharField(max_length=4)
	carlos = models.ForeignKey(Arlo)
	nlargo = models.CharField(max_length=100)
	ncorto = models.CharField(max_length=20)
	canti = models.DecimalField(max_digits=16, decimal_places=2,validators=[MinValueValidator(0)])
	#civa char(2)
	#niva char(40)
	poriva = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
	vunita = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vbruto = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vbase = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	viva = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtotal = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	pordes = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
	#crue char(10)
	pvtafull = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vcosto = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	def __str__(self):
		return self.cfac

class Rue(models.Model):
	crue = models.CharField(primary_key=True,max_length=10)
	cfac = models.ForeignKey(Fac)
	deta = models.CharField(max_length=60)
	cbar_rue = models.CharField(max_length=20)
	seri_rue = models.CharField(max_length=20)
	carlos = models.ForeignKey(Arlo)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	cod_rue = models.CharField(max_length=20)
	capaci = models.CharField(max_length=20)
	veloci = models.CharField(max_length=20)
	#CRUE_ORI                         Char(10), 
	citerce = models.ForeignKey(Tercero)
	frue = models.DateTimeField()
	#CUSU                             Char(20), 
	vunita = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	pvta = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	cbode = models.ForeignKey(Bode)
	cemdor  = models.ForeignKey(Emdor)