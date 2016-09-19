from __future__ import unicode_literals

from django.db import models

from infa_web.apps.base.models import *
from infa_web.apps.usuarios.models import *
from infa_web.apps.terceros.models import *
from infa_web.apps.articulos.models import *

class Fac(models.Model):
	cfac = models.CharField(max_length=10)
	femi = models.DateTimeField()
	citerce = models.ForeignKey(Tercero,default=DEFAULT_TERCERO)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	fpago = models.DateTimeField()
	ctifopa = models.ForeignKey(Tifopa,default=DEFAULT_FORMA_PAGO)
	descri = models.CharField(max_length=200)
	detaanula = models.CharField(max_length=200,blank=True,null=True)
	vtbase = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtiva = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vflete = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vdescu = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vttotal = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	#vefe = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	#vtar = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	#doctar = models.CharField(max_length=10)
	#bancotar = models.ForeignKey(Banfopa,related_name="bancotar")
	#vchq = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	#docchq = models.CharField(max_length=10)
	#bancochq = models.ForeignKey(Banfopa,related_name="bancochq")
	ventre = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vcambio = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	#cusu = models.ForeignKey(Usuario)
	ccaja = models.ForeignKey(Caja,default=DEFAULT_CAJA)
	cvende  = models.ForeignKey(Vende,default=DEFAULT_VENDE)
	cdomici  = models.ForeignKey(Domici,default=DEFAULT_DOMICILIARIO)
	tpordes = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
	cemdor  = models.ForeignKey(Emdor,default=DEFAULT_EMPACADOR)
	#ccoti char(10)
	#vncre = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	#doccre = models.CharField(max_length=10)
	brtefte = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	prtefte = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
	vrtefte = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	fhasdomi = models.DateTimeField(blank=True,null=True)
	#ccobra char(4)

	def __str__(self):
		return self.cfac

class Facdeta(models.Model):
	cfac = models.ForeignKey(Fac)
	itfac = models.CharField(max_length=4)
	carlos = models.ForeignKey(Arlo)
	nlargo = models.CharField(max_length=100)
	ncorto = models.CharField(max_length=20)
	canti = models.DecimalField(max_digits=16, decimal_places=2,validators=[MinValueValidator(0)],default=1)
	civa = models.ForeignKey(Iva,default=DEFAULT_IVA)
	niva  = models.CharField(max_length=40)
	poriva = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
	vunita = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vbase = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	viva = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtotal = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	pordes = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)],default=0)
	pvtafull = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vcosto = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	def __str__(self):
		return self.cfac

class Facpago(models.Model):
	cfac = models.ForeignKey(Fac)
	it = models.CharField(max_length=4)
	cmpago = models.ForeignKey(MediosPago)
	docmpago = models.CharField(max_length=10)
	banmpago = models.ForeignKey(Banfopa)
	vmpago = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	
	def __str__(self):
		return self.cfac
