from __future__ import unicode_literals

from django.db import models

class Mven(models.Model):
	cmven = models.AutoField(primary_key=True)
	fmven = models.DateTimeField()
	docrefe = models.CharField(max_length=10)
	citerce = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='citerce')
	ctimo = models.ForeignKey('Timo', models.DO_NOTHING, db_column='ctimo')
	cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')
	vttotal = models.DecimalField(max_digits=15, decimal_places=2)
	descri = models.CharField(max_length=250)
	detaanula = models.CharField(max_length=250)
	cbode0 = models.ForeignKey(Bode, models.DO_NOTHING, db_column='cbode0')
	cbode1 = models.ForeignKey(Bode, models.DO_NOTHING, db_column='cbode1')

	class Meta:
		managed = False
		db_table = 'mven'

class Mvendeta(models.Model):
	cmven = models.ForeignKey(Mven, models.DO_NOTHING, db_column='cmven')
	it = models.CharField(max_length=4)
	carlos = models.ForeignKey(Arlos, models.DO_NOTHING, db_column='carlos')
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2)
	vunita = models.DecimalField(max_digits=15, decimal_places=2)
	vtotal = models.DecimalField(max_digits=15, decimal_places=2)

	class Meta:
		managed = False
		db_table = 'mvendeta'
		unique_together = (('cmven', 'it'),)

class Mvsa(models.Model):
	cmvsa = models.AutoField(primary_key=True)
	fmvsa = models.DateTimeField()
	docrefe = models.CharField(max_length=10)
	citerce = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='citerce')
	ctimo = models.ForeignKey('Timo', models.DO_NOTHING, db_column='ctimo')
	cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')
	vttotal = models.DecimalField(max_digits=15, decimal_places=2)
	descri = models.CharField(max_length=250)
	detaanula = models.CharField(max_length=250)
	cbode0 = models.ForeignKey(Bode, models.DO_NOTHING, db_column='cbode0')
	cbode1 = models.ForeignKey(Bode, models.DO_NOTHING, db_column='cbode1')

	class Meta:
		managed = False
		db_table = 'mvsa'

class Mvsadeta(models.Model):
	cmvsa = models.ForeignKey(Mvsa, models.DO_NOTHING, db_column='cmvsa')
	it = models.CharField(max_length=4)
	citerce = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='citerce')
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2)
	vunita = models.DecimalField(max_digits=15, decimal_places=2)
	vtotal = models.DecimalField(max_digits=15, decimal_places=2)

	class Meta:
		managed = False
		db_table = 'mvsadeta'
		unique_together = (('cmvsa', 'it'),)

