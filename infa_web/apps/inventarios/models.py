from __future__ import unicode_literals
from infa_web.apps.articulos.models import *
from infa_web.apps.base.models import *
from infa_web.apps.base.constantes import *
from django.db import models

class Invinicab(models.Model):
	cii = models.CharField(max_length=8, primary_key=True)
	fii = models.DateTimeField(auto_now = True)
	fuaii = models.DateTimeField(null=True, blank=True)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)

	def __str__(self):
		return self.cii

	def __unicode__(self):
		return self.cii

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
