from __future__ import unicode_literals
from infa_web.apps.terceros.models import *
from infa_web.apps.base.models import *
from django.db import models

class Gpo(models.Model):
	cgpo = models.IntegerField(primary_key=True)
	ngpo = models.CharField(max_length=80)
	cesdo = models.ForeignKey(Esdo)

	def __str__(self):
		return self.ngpo

class Marca(models.Model):
	cmarca = models.AutoField(primary_key=True)
	nmarca = models.CharField(max_length=60)
	cesdo = models.ForeignKey(Esdo)

	def __str__(self):
		return self.nmarca

class Arlo(models.Model):
	carlos = models.IntegerField(primary_key=True)
	cbarras = models.CharField(max_length=50)
	cgpo = models.ForeignKey(Gpo)
	ncorto = models.CharField(max_length=20)
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2)
	vcosto = models.DecimalField(max_digits=15, decimal_places=2)
	ifcostear = models.BooleanField()
	ifpvfijo = models.BooleanField()
	cesdo = models.ForeignKey(Esdo)
	ciudad = models.ForeignKey(Ciudad)
	ivas_civa = models.ForeignKey(Iva)
	stomin = models.DecimalField(max_digits=15, decimal_places=2)
	stomax = models.DecimalField(max_digits=15, decimal_places=2)
	pvta1 = models.DecimalField(max_digits=15, decimal_places=2)
	pvta2 = models.DecimalField(max_digits=15, decimal_places=2)
	pvta3 = models.DecimalField(max_digits=15, decimal_places=2)
	pvta4 = models.DecimalField(max_digits=15, decimal_places=2)
	pvta5 = models.DecimalField(max_digits=15, decimal_places=2)
	pvta6 = models.DecimalField(max_digits=15, decimal_places=2)
	citerce1 = models.ForeignKey(Tercero, related_name='citerce1', blank=True, null=True)
	vcosto1 = models.DecimalField(max_digits=15, decimal_places=2,default=0,null=True,blank=True)
	fcosto1 = models.DateField(blank=True,null=True)
	citerce2 = models.ForeignKey(Tercero, related_name='citerce2', blank=True, null=True)
	vcosto2 = models.DecimalField(max_digits=15, decimal_places=2,default=0,null=True,blank=True)
	fcosto2 = models.DateField(blank=True,null=True)
	citerce3 = models.ForeignKey(Tercero, related_name='citerce3', blank=True, null=True)
	vcosto3 = models.DecimalField(max_digits=15, decimal_places=2,default=0,null=True,blank=True)
	fcosto3 = models.DateField(blank=True,null=True)
	ifedinom = models.BooleanField(max_length=1)
	refe = models.CharField(max_length=20)
	cmarca = models.ForeignKey(Marca)
	ifdesglo = models.BooleanField()
	mesesgara = models.IntegerField()
	cubica = models.ForeignKey(Ubica)
	porult1 = models.DecimalField(max_digits=6, decimal_places=2)
	porult2 = models.DecimalField(max_digits=6, decimal_places=2)
	porult3 = models.DecimalField(max_digits=6, decimal_places=2)
	porult4 = models.DecimalField(max_digits=6, decimal_places=2)
	porult5 = models.DecimalField(max_digits=6, decimal_places=2)
	porult6 = models.DecimalField(max_digits=6, decimal_places=2)
	foto1 = models.CharField(max_length=250, blank=True, null=True)
	foto2 = models.CharField(max_length=250, blank=True, null=True)
	foto3 = models.CharField(max_length=250, blank=True, null=True)

	def __str__(self):
		return self.nlargo

class Arlosdesglo(models.Model):
	carlosp = models.ForeignKey(Arlo, related_name='carlosp')
	itglo = models.CharField(max_length=4)
	carlosglo = models.ForeignKey(Arlo, related_name='carlosglo')
	cantiglo = models.DecimalField(max_digits=15, decimal_places=2)
	costoglo = models.DecimalField(max_digits=15, decimal_places=2)
	vtoglo = models.DecimalField(max_digits=15, decimal_places=2)
	cesdo = models.ForeignKey(Esdo)

	class Meta:
		managed = False
		unique_together = (('carlosp', 'itglo'),)

	def __str__(self):
		return str(self.carlosp)+' - '+str(self.itglo)

class Bode(models.Model):
	cbode = models.AutoField(primary_key=True)
	nbode = models.CharField(max_length=80)
	esbode = models.CharField(max_length=2)

	def __str__(self):
		return self.nbode
