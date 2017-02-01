from __future__ import unicode_literals
from infa_web.apps.articulos.models import *
from infa_web.apps.base.models import *
from infa_web.apps.base.constantes import *
from django.db import models

class Invinicabingre(models.Model):
	cii = models.CharField(max_length=8, primary_key=True)
	"""
	def __str__(self):
		return self.cii

	def __unicode__(self):
		return self.cii
	"""

class Invinidetaingre(models.Model):
	cii = models.ForeignKey(Invinicabingre)

	"""
	def __str__(self):
		return str(self.cii.pk) + '-' + str(self.carlos.pk)

	def __unicode__(self):
		return str(self.cii.pk) + '-' + str(self.carlos.pk)
	"""
