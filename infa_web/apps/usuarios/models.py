from __future__ import unicode_literals

from django.db import models
from infa_web.apps.base.models import *
from infa_web.apps.terceros.models import *
from django.contrib.auth.models import User

class Usuario(models.Model):
	user = models.OneToOneField(User, primary_key = True)
	#ENCRI                            Char(21), 
	finusu = models.DateTimeField()
	fveusu = models.DateTimeField()
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	foto = models.ImageField(upload_to="usuarios/")
	ifprises = models.BooleanField()
	ccaja = models.ForeignKey(Caja)
	#CTALOMOS                         Char(10), 
	#CTALOPOS                         Char(10), 
	cvende = models.ForeignKey(Vende)