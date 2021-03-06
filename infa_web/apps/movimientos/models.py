from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator

from infa_web.apps.base.constantes import *
from django.core import serializers

from infa_web.apps.articulos.models import *
from infa_web.apps.terceros.models import *
from infa_web.apps.base.models import *

import json

class Mven(models.Model):
	class Meta:
		unique_together = (('cmven', 'ctimo'))

	cmven = models.IntegerField(primary_key=True)
	fmven = models.DateTimeField()
	docrefe = models.CharField(max_length=10)
	citerce = models.ForeignKey(Tercero,default=DEFAULT_TERCERO)
	ctimo = models.ForeignKey(Timo)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	vttotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	descri = models.CharField(max_length=250)
	detaanula = models.CharField(max_length=250)
	cbode0 = models.ForeignKey(Bode, related_name='cbode0',default=DEFAULT_BODEGA)
	cbode1 = models.ForeignKey(Bode, related_name='cbode1',null=True,blank=True)

	def __str__(self):
		return "M. Entrada - D.Ref: %s - Cod: %s - TMovi: %s " % (self.docrefe,self.cmven,self.ctimo)

	def get_mvendeta(self,using):
		mvendeta = Mvendeta.objects.using(using).filter(cmven = self.cmven)
		return mvendeta

class Mvendeta(models.Model):
	class Meta:
		unique_together = (('cmven', 'ctimo','it'))

	cmven = models.ForeignKey(Mven,on_delete=models.CASCADE)
	it = models.CharField(max_length=4)
	ctimo = models.ForeignKey(Timo)
	carlos = models.ForeignKey(Arlo)
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=1)
	vunita = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	vtotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	def __str__(self):
		return "M. D. Entrada - D.Ref: %s - It: %s - Cod: %s - TMovi: %s - Fecha: %s " % (self.cmven.docrefe,self.it,self.cmven.cmven,self.ctimo,self.cmven.fmven)

class Mvsa(models.Model):
	class Meta:
		unique_together = (('cmvsa', 'ctimo'))

	cmvsa = models.AutoField(primary_key=True)
	fmvsa = models.DateTimeField()
	docrefe = models.CharField(max_length=10)
	citerce = models.ForeignKey(Tercero,default=DEFAULT_TERCERO)
	ctimo = models.ForeignKey(Timo)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	vttotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	descri = models.CharField(max_length=250)
	detaanula = models.CharField(max_length=250,default='-')
	cbode0 = models.ForeignKey(Bode, related_name = 'cbode_0',default=DEFAULT_BODEGA)
	cbode1 = models.ForeignKey(Bode, related_name = 'cbode_1',null=True,blank=True)

	def get_mvsadeta(self,using,format_json=False):
		query = Mvsadeta.objects.using(using).filter(cmvsa = self.cmvsa).order_by('it')
		if format_json:
			mvsadeta = json.loads(serializers.serialize('json', query))
		else:
			mvsadeta = query
		return mvsadeta

	def __str__(self):
		return "M. Salida - D.Ref: %s - Cod: %s - TMovi: %s " % (self.docrefe,self.cmvsa,self.ctimo)

class Mvsadeta(models.Model):
	cmvsa = models.ForeignKey(Mvsa,on_delete=models.CASCADE)
	it = models.CharField(max_length=4)
	carlos = models.ForeignKey(Arlo)
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)],default=1)
	vunita = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	vtotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	def __str__(self):
		return "M. D. Salida - D.Ref: %s - It: %s - Cod: %s - Fecha: %s " % (self.cmvsa.docrefe,self.it,self.cmvsa.cmvsa,self.cmvsa.fmvsa)

class Movi(models.Model):
	cmovi = models.CharField(max_length=10, primary_key=True)
	ctimo = models.ForeignKey(Timo,default=DEFAULT_TERCERO)
	citerce = models.ForeignKey(Tercero,default=DEFAULT_TERCERO)
	fmovi = models.DateTimeField()
	descrimovi = models.CharField(max_length=80)
	vttotal = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	vefe = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtar = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vch = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vcred = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])

	ventre = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vcambio = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	ccaja = models.ForeignKey(Caja,default=DEFAULT_CAJA)

	#civa = models.ForeignKey(Iva)

	baseiva = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtiva = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtsuma = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtdescu = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	detaanula = models.CharField(max_length=80,blank=True, null=True)

	def to_json(self,using):
		query = Movi.objects.using(using).get(cmovi = self.cmovi)
		movi = json.loads(serializers.serialize('json', [query]))[0]
		return movi

	def get_movideta(self,using,format_json=False):
		query = Movideta.objects.using(using).filter(cmovi = self.cmovi).order_by('itmovi')
		if format_json:
			movideta = json.loads(serializers.serialize('json', query))
		else:
			movideta = query
		return movideta

	def get_movipago(self,using,format_json=False):
		query = Movipago.objects.using(using).filter(cmovi = self.cmovi).order_by('it')
		if format_json:
			movipago = json.loads(serializers.serialize('json', query))
		else:
			movipago = query
		return movipago

	def get_related_information(self,using,format_json):
		if format_json:
			data = self.to_json(using)

			data["movideta"] = self.get_movideta(using,format_json)
			data["movipago"] = self.get_movipago(using,format_json)
		else:
			data = self
			data.mvsa = self.get_movideta(using,format_json)
			data.movis = self.get_movipago(using,format_json)
		return data

	def __str__(self):
		return str(self.cmovi)

class Movideta(models.Model):
	cmovi = models.ForeignKey(Movi,on_delete=models.CASCADE)
	itmovi = models.CharField(max_length=4)
	docrefe = models.CharField(max_length=10)
	detalle = models.CharField(max_length=60)
	vmovi = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])

	def __str__(self):
		return str(self.cmovi)+' - '+self.docrefe+' - '+str(self.vmovi)

class Movipago(models.Model):
	cmovi = models.ForeignKey(Movi,on_delete=models.CASCADE)
	it = models.CharField(max_length=4,blank=True, null=True)
	cmpago = models.ForeignKey(MediosPago,blank=True, null=True)
	docmpago = models.CharField(max_length=10,default=0,blank=True, null=True)
	banmpago = models.ForeignKey(Banfopa,blank=True, null=True)
	vmpago = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)],blank=True, null=True)

	def __str__(self):
		return str(self.cmovi)+' - '+self.docmpago
