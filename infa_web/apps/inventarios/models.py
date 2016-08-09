from __future__ import unicode_literals

from django.db import models

class Invinicab(models.Model):
	cii = models.AutoField(primary_key=True)
	fii = models.DateTimeField()
	fuaii = models.DateTimeField()
	cesdo = models.ForeignKey(Esdos, models.DO_NOTHING, db_column='cesdo')

	class Meta:
		managed = False
		db_table = 'invinicab'

class Invinideta(models.Model):
	cii = models.ForeignKey(Invinicab, models.DO_NOTHING, db_column='cii')
	carlos = models.ForeignKey(Arlos, models.DO_NOTHING, db_column='carlos')
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2)
	vunita = models.DecimalField(max_digits=15, decimal_places=2)
	vtotal = models.DecimalField(max_digits=15, decimal_places=2)
	cancalcu = models.DecimalField(max_digits=15, decimal_places=2)
	ajuent = models.DecimalField(max_digits=15, decimal_places=2)
	ajusal = models.DecimalField(max_digits=15, decimal_places=2)

	class Meta:
		managed = False
		db_table = 'invinideta'
		unique_together = (('carlos', 'cii'),)
