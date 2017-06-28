from __future__ import unicode_literals

from infa_web.apps.base.models import *
from infa_web.apps.restaurante_menus.models import *

from infa_web.apps.base.constantes import *

from django.core.validators import MinValueValidator, MaxValueValidator
from infa_web.apps.usuarios.models import Usuario

from django.db import models


class Talocoda(models.Model):
	ctalocoda = models.IntegerField(primary_key=True)
	ntalocoda = models.CharField(max_length=50)
	cesdo = models.ForeignKey(Esdo, default=CESTADO_ACTIVO)
	nini = models.IntegerField()
	nfin = models.IntegerField()
	csucur = models.ForeignKey(Sucursales,default=DEFAULT_SUCURSAL)

	def __str__(self):
		return self.ctalocoda

	def __unicode__(self):
		return unicode("Talonariao " + str(self.ntalocoda))

	def natural_key(self):
		return ({
			"ctalocoda" : self.ctalocoda,
			"ntalocoda" : self.ntalocoda,
			"cesdo" : self.cesdo.natural_key(),
			"nini" : self.nini,
			"nfin" : self.nfin,
			"csucur" : self.csucur.natural_key(),
		})

class Mesas(models.Model):

	class Meta:
		ordering = ["nmesa"]
		permissions = (
			("list_mesas", "Puede Listar Mesas"),
		)
	cmesa = models.AutoField(primary_key=True)
	nmesa = models.CharField(max_length=50)
	cesdo = models.ForeignKey(Esdo, default=CESTADO_ACTIVO)
	npmax = models.IntegerField()

	def __str__(self):
		return self.nmesa

	def __unicode__(self):
		return self.nmesa

	def natural_key(self):
		return ({
			"cmesa" : self.cmesa,
			"nmesa" : self.nmesa,
			"cesdo" : self.cesdo.natural_key(),
			"npmax" : self.npmax,
		})

class Meseros(models.Model):

	class Meta:
		ordering = ["nmero"]

	cmero = models.AutoField(primary_key=True)
	nmero = models.CharField(max_length=50)
	ctalocoda = models.ForeignKey(Talocoda)
	cesdo = models.ForeignKey(Esdo, default=CESTADO_ACTIVO)
	telmero = models.CharField(max_length=50)
	dirmero = models.CharField(max_length=50)
	foto = models.FileField(upload_to="img/waiters/", blank=True, null=True, default=DEFAULT_IMAGE_WAITERS)
	usuario = models.ForeignKey(Usuario)

	def __str__(self):
		return self.nmero

	def __unicode__(self):
		return self.nmero

	def natural_key(self):
		return ({
			"cmero" : self.cmero,
			"nmero" : self.nmero,
			"ctalocoda" : self.ctalocoda.natural_key(),
			"cesdo" : self.cesdo.natural_key(),
			"telmero" : self.telmero,
			"dirmero" : self.dirmero,
			#"foto" : self.foto.url,
			"usuario" : self.usuario.natural_key(),
		})

class Resupedi(models.Model):
	cresupedi = models.IntegerField(primary_key=True)
	fresupedi = models.DateTimeField()
	# cesdo = models.ForeignKey(Esdo, default=CESTADO_ACTIVO)
	vttotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)], default=0.00)
	detaanula = models.CharField(max_length=250)
	ifcortesia = models.BooleanField(default=False)

	def __str__(self):
		return "Resumen de Pedido " + str(self.cresupedi)

	def __unicode__(self):
		return unicode("Resumen de Pedido " + str(self.cresupedi))

	def natural_key(self):
		return ({
			"cresupedi" : self.cresupedi,
			#"fresupedi" : self.fresupedi,
			"vttotal" : self.vttotal,
			"detaanula" : self.detaanula,
			"ifcortesia" : self.ifcortesia,
		})

class Resupedipago(models.Model):
	cresupedi = models.ForeignKey(Resupedi)
	it = models.CharField(max_length=50)
	docmpago = models.CharField(max_length=10, default=0)
	vmpago = models.DecimalField(max_digits=14, decimal_places=2, validators=[MinValueValidator(0)])
	banmpago = models.ForeignKey(Banfopa, default=DEFAULT_BANCO)
	cmpago = models.ForeignKey(MediosPago)


	def __str__(self):
		return "Pago de Resumen de Pedido " + str(self.cresupedi)

	def __unicode__(self):
		return unicode("Pago de Resumen de Pedido " + str(self.cresupedi))


class Coda(models.Model):
	class Meta:
		unique_together = (('ccoda', 'ctalocoda'))
		permissions = (
			("list_coda", "Puede Listar Comandas"),
		)
	ccoda = models.IntegerField()
	ctalocoda = models.ForeignKey(Talocoda)
	fcoda = models.DateTimeField(auto_now_add=True)
	cmesa = models.ForeignKey(Mesas)
	cesdo = models.ForeignKey(Esdo, default=CESTADO_ACTIVO)
	cmero = models.ForeignKey(Meseros)
	cresupedi = models.ForeignKey(Resupedi, blank=True, null=True, default=None)
	detaanula = models.CharField(max_length=250,blank=True, null=True, default="")
	vttotal = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)], default=0.00)
	def __str__(self):
		return "Comanda " + str(self.ccoda)

	def __unicode__(self):
		return unicode("Comanda " + str(self.ccoda))

	def natural_key(self):
		return ({
			"ccoda" : self.ccoda,
			"ctalocoda" : self.ctalocoda.natural_key(),
			"fcoda" : self.fcoda,
			"cmesa" : self.cmesa.natural_key(),
			"cesdo" : self.cesdo.natural_key(),
			"cmero" : self.cmero.natural_key(),
			"cresupedi" : self.cresupedi,
			"detaanula" : self.detaanula,
			"vttotal" : self.vttotal,
		})

class Codadeta(models.Model):
	ccoda = models.ForeignKey(Coda)
	it = models.IntegerField()
	cmenu = models.ForeignKey(Menus)
	nlargo = models.CharField(max_length=50)
	canti = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
	vunita = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)], default=0.00)
	vtotal = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)], default=0.00)
	def __str__(self):
		return "Detalle de Comanda " + str(self.ccoda)

	def __unicode__(self):
		return unicode("Detalle de Comanda " + str(self.ccoda))

	def natural_key(self):
		return ({
			"ccoda" : self.ccoda,
			"it" : self.it,
			#"cmenu" : self.cmenu,
			"nlargo" : self.nlargo,
			"canti" : self.canti,
			"vunita" : self.vunita,
			"vtotal" : self.vtotal,
		})
