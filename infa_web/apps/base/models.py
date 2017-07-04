from __future__ import unicode_literals
from django.db import models
from infa_web.apps.base.constantes import *
#from infa_web.apps.movimientos.models import *
#from infa_web.apps.articulos.models import *
from django.core.validators import MinValueValidator

from django.contrib.auth.models import Permission

class Esdo(models.Model):

	class Meta:
		ordering = ["nesdo"]
		permissions = (
			("list_esdo", "Puede Listar Estados"),
			("list_parameters", "Puede Listar Parametros"),
			("save_parameters", "Puede Crear Parametros"),
		)

	cesdo = models.AutoField(primary_key=True)
	nesdo = models.CharField(max_length=40)
	estavali = models.CharField(max_length=10)

	def __str__(self):
		return self.nesdo

	def natural_key(self):
		return (self.cesdo)

class Sucursales(models.Model):

	class Meta:
		ordering = ["csucur"]
		permissions = (
			("list_sucursales", "Puede Listar Sucursales"),
		)
	csucur = models.AutoField(primary_key=True)
	nsucur = models.CharField(max_length=40)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	dirsucur = models.CharField(max_length=255)
	telsucur = models.CharField(max_length=255)
	celsucur = models.CharField(max_length=255)

	def __str__(self):
		return self.nsucur

	def natural_key(self):
		return {
			"csucur" : self.csucur,
			"nsucur" : self.nsucur,
			"cesdo" : self.cesdo.natural_key(),
			"dirsucur" : self.dirsucur,
			"telsucur" : self.telsucur,
			"celsucur" : self.celsucur,
		}

class MediosPago(models.Model):

	class Meta:
		ordering = ["nmpago"]

	cmpago = models.AutoField(primary_key=True)
	nmpago = models.CharField(max_length=40)
	ifdoc = models.BooleanField()

	def __str__(self):
		return self.nmpago

class Timo(models.Model):

	class Meta:
		ordering = ["ctimo"]

	ctimo = models.IntegerField(primary_key=True)
	ntimo = models.CharField(max_length=40)
	prefijo = models.CharField(max_length=4)
	filas = models.IntegerField()
	nrepo = models.CharField(max_length=20)

	def __str__(self):
		return self.ntimo

class Bode(models.Model):

	class Meta:
		ordering = ["cbode"]
		permissions = (
			("list_caja", "Puede Listar Bodejas"),
		)

	cbode = models.AutoField(primary_key=True)
	nbode = models.CharField(max_length=80)
	esbode = models.CharField(max_length=2)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nbode

class Modules(models.Model):

	class Meta:
		ordering = ["nmodule"]

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

	class Meta:
		ordering = ["nubica"]

	cubica = models.AutoField(primary_key=True)
	nubica = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nubica

class Departamento(models.Model):

	class Meta:
		ordering = ["ndepar"]
		permissions = (
			("list_esdo", "Puede Listar Departamentos"),
		)

	cdepar = models.AutoField(primary_key=True)
	ndepar = models.CharField(max_length=45)

	def __str__(self):
		return self.ndepar
	def __unicode__(self):
		return self.ndepar

	def natural_key(self):
		return (self.cdepar)

class Ciudad(models.Model):

	class Meta:
		ordering = ["cciu","nciu"]
		permissions = (
			("list_esdo", "Puede Listar Ciudades"),
		)

	cciu = models.AutoField(primary_key=True)
	nciu = models.CharField(max_length=40)
	cdepar = models.ForeignKey(Departamento)
	def __str__(self):
		return self.nciu
	def __unicode__(self):
		return self.nciu

class Iva(models.Model):

	class Meta:
		ordering = ["niva"]

	civa = models.AutoField(primary_key=True)
	niva = models.CharField(max_length=40)
	poriva = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
	idtira = models.CharField(max_length=1)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.niva

class Regiva(models.Model):

	class Meta:
		ordering = ["nregiva"]

	cregiva = models.AutoField(primary_key=True)
	nregiva = models.CharField(max_length=40)

	def __str__(self):
		return self.nregiva

class Tiide(models.Model):

	class Meta:
		ordering = ["ntiide"]

	idtiide = models.AutoField(primary_key=True)
	ntiide = models.CharField(max_length=40)

	def __str__(self):
		return self.ntiide

class Emdor(models.Model):

	class Meta:
		ordering = ["nemdor"]

	cemdor = models.AutoField(primary_key=True)
	nemdor = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nemdor

class Domici(models.Model):

	class Meta:
		ordering = ["ndomici"]

	cdomici = models.AutoField(primary_key=True)
	ndomici = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.ndomici

class Tifopa(models.Model):

	class Meta:
		ordering = ["ntifopa"]

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

	class Meta:
		ordering = ["nbanfopa"]
		permissions = (
			("list_esdo", "Puede Listar Bancos"),
		)

	cbanfopa = models.CharField(max_length=6, primary_key=True)
	nbanfopa = models.CharField(max_length=80)
	porcomi = models.DecimalField(max_digits=5, decimal_places=2,validators=[MinValueValidator(0)])
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.nbanfopa

class Caja(models.Model):
	class Meta:
		ordering = ["ncaja"]
		permissions = (
			("list_caja", "Puede Listar Cajas"),
		)

	ccaja = models.AutoField(primary_key=True)
	ncaja = models.CharField(max_length=80)
	csucur = models.ForeignKey(Sucursales,default=DEFAULT_SUCURSAL)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	caseri = models.CharField(max_length=4)
	ctimocj = models.ForeignKey(Timo)
	cbode = models.ForeignKey(Bode)

	def __str__(self):
		return self.ncaja

	def natural_key(self):
		return ({
			"ccaja" : self.ccaja,
			"ncaja" : self.ncaja,
			"csucur" : self.csucur.natural_key(),
			"cesdo" : self.cesdo.natural_key(),
			"caseri" : self.caseri,
			#"ctimocj" : self.ctimocj,
			#"cbode" : self.cbode,
		})


class Talo(models.Model):
	ctalo = models.AutoField(primary_key=True)
	csucur = models.ForeignKey(Sucursales,default=DEFAULT_SUCURSAL)
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
		return "%s - %s" % (self.prefijo,self.descri)

	def natural_key(self):
		return ({
			"ctalo" : self.ctalo,
			"csucur" : self.csucur.natural_key(),
			"prefijo" : self.prefijo,
			"conse_ini" : self.conse_ini,
			"conse_fin" : self.conse_fin,
			"lar_conse" : self.lar_conse,
			"resodian" : self.resodian,
			"nrepo" : self.nrepo,
			"filas" : self.filas,
			"descri" : self.descri,
			#"ctifopa" : self.ctifopa,
			"ifmostrado" : self.ifmostrado,
			"ifpos" : self.ifpos,
			"cesdo" : self.cesdo.natural_key(),
			"prefi_real" : self.prefi_real,
			"ncotalo" : self.ncotalo,
			"ccaja" : self.ccaja.natural_key(),
			#"ctimomvsa" : self.ctimomvsa,
		})

class Tiservi(models.Model):

	class Meta:
		ordering = ["ntiservi"]

	ctiservi = models.AutoField(primary_key=True)
	ntiservi = models.CharField(max_length=40)

	def __str__(self):
		return self.ntiservi

class NavMenus(models.Model):

	class Meta:
		ordering = ["name"]

	name = models.TextField(max_length=255)
	icon = models.TextField(max_length=255)
	main = models.BooleanField(default=False)
	enabled = models.BooleanField(default=True)
	anchor = models.BooleanField() # Link Ancla
	url = models.TextField(max_length=255,null=True, blank=True)
	permission = models.TextField(max_length=1000,null=True, blank=True)
	module = models.ForeignKey(Modules,null=True, blank=True)
	general = models.BooleanField(default=False)
	orden = models.IntegerField(default=0)
	father = models.ForeignKey('NavMenus',null=True, blank=True)
	quick_access = models.BooleanField(default=False)

	def __str__(self):
		return "%s - %s (%s)" % (self.id,self.name,self.father)

	def __unicode__(self):
		return "%s - %s (%s)" % (self.id,self.name,self.father)

	def natural_key(self):
		return ({
			name : self.name,
			icon : self.icon,
			main : self.main,
			enabled : self.enabled,
			anchor : self.anchor,
			url : self.url,
			permission : self.permission,
			#module : self.module,
			general : self.general,
			#father : self.father,
			orden : self.orden,
		})
