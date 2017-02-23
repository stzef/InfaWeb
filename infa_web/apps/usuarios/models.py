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
	ctalomos = models.ForeignKey(Talo,related_name="ctalomos",null=True,blank=True)#CTALOMOS                         Char(10),
	ctalopos = models.ForeignKey(Talo,related_name="ctalopos",null=True,blank=True)#CTALOPOS                         Char(10),
	#cvende = models.ForeignKey(Vende)

