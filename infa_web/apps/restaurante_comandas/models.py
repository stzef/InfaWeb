from __future__ import unicode_literals

from infa_web.apps.base.models import *

from infa_web.apps.base.constantes import *

from django.core.validators import MinValueValidator, MaxValueValidator


from django.db import models

class Mesas(models.Model):
	cmesa = models.IntegerField(primary_key=True)
	nmesa = models.CharField(max_length=50)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	npmax = models.IntegerField()

	def __str__(self):
		return self.nmesa

	def __unicode__(self):
		return self.nmesa

class Meseros(models.Model):
	cmero = models.IntegerField(primary_key=True)
	nmero = models.CharField(max_length=50)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	telmero = models.CharField(max_length=50)
	dirmero = models.CharField(max_length=50)
	foto = models.FileField(upload_to="img/waiters/", blank=True, null=True,default=DEFAULT_IMAGE_WAITERS)

	def __str__(self):
		return self.nmero

	def __unicode__(self):
		return self.nmero

class Coda(models.Model):

	def __str__(self):
		return self.ningre

	def __unicode__(self):
		return self.ningre

class Codadeta(models.Model):
	def __str__(self):
		return self.ningre

	def __unicode__(self):
		return self.ningre

class Talocoda(models.Model):
	ctalocoda = models.IntegerField(primary_key=True)
	ntalocoda = models.CharField(max_length=50)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	nini = models.IntegerField()
	nfin = models.IntegerField()

	def __str__(self):
		return self.ningre

	def __unicode__(self):
		return self.ningre

class Resupedi(models.Model):
	cresupedi = models.IntegerField(primary_key=True)
	fresupedi = models.DateTimeField()
	# cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	vttotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=0.00)
	detaanula = models.CharField(max_length=250)
	ifcortesia = models.BooleanField(default=False)

	def __str__(self):
		return self.ningre

	def __unicode__(self):
		return self.ningre

class Resupedipago(models.Model):
	cresupedi = models.ForeignKey(Resupedi)
	it = models.CharField(max_length=50)
	docmpago = models.CharField(max_length=10,default=0)
	vmpago = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	banmpago = models.ForeignKey(Banfopa,default=DEFAULT_BANCO)
	cmpago = models.ForeignKey(MediosPago)


	def __str__(self):
		return self.ningre

	def __unicode__(self):
		return self.ningre
