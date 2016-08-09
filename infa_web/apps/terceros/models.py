from __future__ import unicode_literals

from django.db import models

class Terceros(models.Model):
	citerce = models.AutoField(primary_key=True)
	idterce = models.CharField(max_length=20)
	dv = models.CharField(max_length=1)
	ctiide = models.ForeignKey('Tiide', models.DO_NOTHING, db_column='ctiide')
	rasocial = models.CharField(max_length=200)
	nomcomer = models.CharField(max_length=200)
	ape1 = models.CharField(max_length=40)
	ape2 = models.CharField(max_length=40)
	nom1 = models.CharField(max_length=40)
	nom2 = models.CharField(max_length=40)
	sigla = models.CharField(max_length=100)
	nomegre = models.CharField(max_length=100)
	replegal = models.CharField(max_length=100)
	dirterce = models.CharField(max_length=80)
	telterce = models.CharField(max_length=20)
	faxterce = models.CharField(max_length=20)
	cciu = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='cciu')
	email = models.CharField(max_length=40)
	contacto = models.CharField(max_length=20)
	cregiva = models.ForeignKey(Regiva, models.DO_NOTHING, db_column='cregiva')
	cautorre = models.ForeignKey(Autorre, models.DO_NOTHING, db_column='cautorre')
	cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')
	cvende = models.ForeignKey('Vende', models.DO_NOTHING, db_column='cvende')
	topcxc = models.DecimalField(max_digits=15, decimal_places=2)
	ndiacxc = models.IntegerField()
	czona = models.ForeignKey('Zonas', models.DO_NOTHING, db_column='czona')
	clipre = models.IntegerField()
	fnaci = models.DateField()
	naju = models.IntegerField()
	cruta = models.ForeignKey(Rutas, models.DO_NOTHING, db_column='cruta')
	ordenruta = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'terceros'

class Autorre(models.Model):
	cautorre = models.AutoField(primary_key=True)
	nautorre = models.CharField(max_length=40)

	class Meta:
		managed = False
		db_table = 'autorre'

class Rutas(models.Model):
	cruta = models.AutoField(primary_key=True)
	nruta = models.CharField(max_length=45)
	cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')

	class Meta:
		managed = False
		db_table = 'rutas'

class Vende(models.Model):
	cvende = models.AutoField(primary_key=True)
	nvende = models.CharField(max_length=80)
	porventa = models.DecimalField(max_digits=7, decimal_places=4)
	cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')

	class Meta:
		managed = False
		db_table = 'vende'

class Zonas(models.Model):
	czona = models.AutoField(primary_key=True)
	nzona = models.CharField(max_length=40)
	activo = models.CharField(max_length=1)

	class Meta:
		managed = False
		db_table = 'zonas'
