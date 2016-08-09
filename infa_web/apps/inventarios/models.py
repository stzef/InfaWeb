from __future__ import unicode_literals
from infa_web.apps.articulos.models import *
from infa_web.apps.base.models import *
from django.db import models

class Invinicab(models.Model):
	cii = models.AutoField(primary_key=True)
	fii = models.DateTimeField()
	fuaii = models.DateTimeField()
	cesdo = models.ForeignKey(Esdo)

	def __str__(self):
		return str(self.cii)

	def __init__(self):
		return str(self.cii)

class Invinideta(models.Model):
	cii = models.ForeignKey(Invinicab)
	carlos = models.ForeignKey(Arlo)
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

	def __str__(self):
		return str(self.cii)

	def __init__(self):
		return str(self.cii)
