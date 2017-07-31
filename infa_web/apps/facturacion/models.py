from __future__ import unicode_literals

from django.db import models
from django.core import serializers
import json

from infa_web.apps.base.models import *
from infa_web.apps.usuarios.models import *
from infa_web.apps.terceros.models import *
from infa_web.apps.articulos.models import *
from infa_web.apps.movimientos.models import *

class Fac(models.Model):
	class Meta:
		ordering = ["-femi"]
		permissions = (
			("add_fac_pos", "Puede Crear Facturas POS"),
			("print_fac_pos", "Puede Imprimir facturas POS"),
			("list_fac_pos", "Puede Listar Facturas POS"),
			("list_fac", "Puede Listar Facturas"),
			("print_fac", "Puede Imprimir Facturas"),
			("annulment_fac", "Puede Anular Facturas"),
			("report_fac_bill", "Puede Generar Reporte de Ventas"),
			("report_fac_bill_payment", "Puede Generar Reporte de Ventas Por medio de Pago"),
		)
	cfac = models.CharField(max_length=10)
	femi = models.DateTimeField()
	citerce = models.ForeignKey(Tercero,default=DEFAULT_TERCERO)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	fpago = models.DateTimeField()
	ctifopa = models.ForeignKey(Tifopa,default=DEFAULT_FORMA_PAGO)
	descri = models.CharField(max_length=200)
	detaanula = models.CharField(max_length=200,blank=True,null=True)
	vtbase = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)],default=0)
	vtiva = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)],default=0)
	vflete = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)],default=0)
	vdescu = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)],default=0)
	vttotal = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)],default=0)

	vefe = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtar = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vch = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vcred = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])

	#vefe = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	#vtar = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	#doctar = models.CharField(max_length=10)
	#bancotar = models.ForeignKey(Banfopa,related_name="bancotar")
	#vchq = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	#docchq = models.CharField(max_length=10)
	#bancochq = models.ForeignKey(Banfopa,related_name="bancochq")
	ventre = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)],default=0)
	vcambio = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)],default=0)
	#cusu = models.ForeignKey(Usuario)
	ccaja = models.ForeignKey(Caja,default=DEFAULT_CAJA)
	cvende  = models.ForeignKey(Vende,default=DEFAULT_VENDE)
	cdomici  = models.ForeignKey(Domici,default=DEFAULT_DOMICILIARIO)
	tpordes = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
	cemdor  = models.ForeignKey(Emdor,default=DEFAULT_EMPACADOR)
	#ccoti char(10)
	#vncre = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	#doccre = models.CharField(max_length=10)
	brtefte = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)],default=0)
	prtefte = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)],default=0)
	vrtefte = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)],default=0)
	fhasdomi = models.DateTimeField(blank=True,null=True)
	#ccobra char(4)

	def natural_key(self):
		r = {
			"cfac" : self.cfac
		}

		return r

	def __str__(self):
		return self.cfac

	def to_json(self):
		#fac = json.loads(serializers.serialize('json', [self],fields=("vttotal","cfac")))[0]
		fac = json.loads(serializers.serialize('json', [self],fields=("cfac","citerce","cesdo","ctifopa","descri","detaanula","vtbase","vtiva","vflete","vdescu","vttotal","vefe","vtar","vch","vcred","ventre","vcambio","ccaja","cvende","cdomici""tpordes","cemdor","brtefte","prtefte","vrtefte")))[0]
		return fac

	def get_mvsa(self,using,format_json=False):
		query = Mvsa.objects.using(using).get(docrefe = self.cfac)
		if format_json:
			mvsa = json.loads(serializers.serialize('json', [query]))[0]
			mvsa["mvsadeta"] = query.get_mvsadeta(using,format_json)
		else:
			mvsa = query
			mvsa.mvsadeta = query.get_mvsadeta(using)
		return mvsa

	def get_facdeta(self,using,format_json=False):
		query = Facdeta.objects.using(using).filter(cfac = self.pk).order_by('itfac')
		if format_json:
			facdeta = json.loads(serializers.serialize('json', query))
		else:
			facdeta = Facdeta.objects.using(using).filter(cfac = self.pk)
		return facdeta

	def get_related_information(self,using,format_json):
		if format_json:
			data = self.to_json()

			data["mvsa"] = self.get_mvsa(using,format_json)
			data["movis"] = self.get_movi(using,format_json)
			data["facdeta"] = self.get_facdeta(using,format_json)
		else:
			data = self

			data.mvsa = self.get_mvsa(using,format_json)
			data.movis = self.get_movi(using,format_json)
			data.facdeta = self.get_facdeta(using,format_json)

		return data

	def get_movi(self,using,format_json=False):
		query_movideta = Movideta.objects.using(using).filter(docrefe = self.cfac)

		t_movis = list(set(map(lambda x: x.cmovi, query_movideta)))

		movis = []

		for t_movi in t_movis:
			query_movi = Movi.objects.using(using).get(pk=t_movi.pk)

			if format_json:
				movi = json.loads(serializers.serialize('json', [query_movi]))[0]
				movi["movideta"] = query_movi.get_movideta(using,format_json)
				movis.append(movi)
			else:
				movi = query_movi
				movi.movideta = query_movi.get_movideta(using,format_json)
				movis.append(movi)
		return movis

class Facdeta(models.Model):
	cfac = models.ForeignKey(Fac)
	itfac = models.CharField(max_length=4)
	carlos = models.ForeignKey(Arlo)
	nlargo = models.CharField(max_length=100)
	ncorto = models.CharField(max_length=50)
	canti = models.DecimalField(max_digits=16, decimal_places=2,validators=[MinValueValidator(0)],default=1)
	civa = models.ForeignKey(Iva,default=DEFAULT_IVA)
	niva  = models.CharField(max_length=40)
	poriva = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0),MaxValueValidator(100)])
	vunita = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vbase = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	viva = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vtotal = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	pordes = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0),MaxValueValidator(100)],default=0)
	pvtafull = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])
	vcosto = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])

	def __str__(self):
		return str(self.cfac)+' - '+str(self.carlos)

class Facpago(models.Model):
	cfac = models.ForeignKey(Fac)
	it = models.CharField(max_length=4)
	cmpago = models.ForeignKey(MediosPago)
	docmpago = models.CharField(max_length=10,default=0)
	banmpago = models.ForeignKey(Banfopa,default=DEFAULT_BANCO)
	vmpago = models.DecimalField(max_digits=14, decimal_places=2,validators=[MinValueValidator(0)])

	def __str__(self):
		return str(self.cfac)+' - '+self.docmpago
