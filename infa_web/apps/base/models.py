from __future__ import unicode_literals
from django.db import models
from infa_web.apps.base.constantes import *
#from infa_web.apps.movimientos.models import *
#from infa_web.apps.articulos.models import *
from django.core.validators import MinValueValidator


class Esdo(models.Model):
	cesdo = models.AutoField(primary_key=True)
	nesdo = models.CharField(max_length=40)
	estavali = models.CharField(max_length=10)

	def __str__(self):
		return self.nesdo

	def natural_key(self):
		return (self.cesdo)

class Timo(models.Model):
	ctimo = models.IntegerField(primary_key=True)
	ntimo = models.CharField(max_length=40)
	prefijo = models.CharField(max_length=4)
	filas = models.IntegerField()
	nrepo = models.CharField(max_length=20)

	def __str__(self):
		return self.ntimo

class Bode(models.Model):
	cbode = models.AutoField(primary_key=True)
	nbode = models.CharField(max_length=80)
	esbode = models.CharField(max_length=2)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nbode

class Modules(models.Model):
	smodule = models.CharField(max_length=5)
	nmodule = models.CharField(max_length=20)
	enabled_enterprise = models.BooleanField()
	enabled = models.BooleanField()
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO) 

	def __str__(self):
		return self.nmodule

	def natural_key(self):
		return (self.smodule)

class Parameters(models.Model):
	cparam = models.CharField(max_length=10)
	module = models.ForeignKey(Modules)
	nparam = models.CharField(max_length=40)

	val_boolean = models.BooleanField(blank=True)
	val_integer = models.IntegerField(blank=True, null=True)
	val_string = models.CharField(max_length=40,blank=True, null=True)
	def __str__(self):
		return self.nparam

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

	def natural_key(self):
		return (self.cdepar)

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
	poriva = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
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

class Emdor(models.Model):
	cemdor = models.AutoField(primary_key=True)
	nemdor = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nemdor

class Domici(models.Model):
	cdomici = models.AutoField(primary_key=True)
	ndomici = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.ndomici

class Tifopa(models.Model):
	ctifopa = models.AutoField(primary_key=True)
	ntifopa = models.CharField(max_length=40)
	ndiasfopa = models.IntegerField()

	def __str__(self):
		return self.ntifopa

class Cta(models.Model):
	ccta = models.CharField(max_length=20, primary_key=True)
	ncta = models.CharField(max_length=80)
	natu = models.IntegerField()
	ifbase = models.BooleanField()
	ifterce = models.BooleanField()
	ifcencos = models.BooleanField()
	ifajus = models.BooleanField()
	ifestas = models.BooleanField()
	ifrtefte = models.BooleanField()
	prf = models.IntegerField()
	nivel = models.IntegerField()
	timaux = models.IntegerField()
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.ncta

class Banfopa(models.Model):
	cbanfopa = models.CharField(max_length=6, primary_key=True)
	nbanfopa = models.CharField(max_length=80)
	porcomi = models.DecimalField(max_digits=5, decimal_places=2,validators=[MinValueValidator(0)])
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nbanfopa

class Caja(models.Model):
	ccaja = models.AutoField(primary_key=True)
	ncaja = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	caseri = models.CharField(max_length=4)
	ctimocj = models.ForeignKey(Timo)
	cbode = models.ForeignKey(Bode)

	def __str__(self):
		return self.ncaja

class Talo(models.Model):
	ctalo = models.AutoField(primary_key=True)
	prefijo = models.CharField(max_length=2)
	conse_ini = models.IntegerField()
	conse_fin = models.IntegerField()
	lar_conse = models.IntegerField()
	resodian = models.CharField(max_length=20)
	nrepo = models.CharField(max_length=10)
	filas = models.IntegerField()
	descri = models.CharField(max_length=40)
	ctifopa = models.ForeignKey(Tifopa)
	ifmostrado = models.BooleanField()
	ifpos = models.BooleanField()
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	prefi_real = models.CharField(max_length=4)
	ncotalo = models.IntegerField()
	ccaja = models.ForeignKey(Caja)
	ctimomvsa = models.ForeignKey(Timo)

	def __str__(self):
		return self.prefijo
