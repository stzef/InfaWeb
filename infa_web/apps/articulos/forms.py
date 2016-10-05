# -*- coding: utf-8 -*-
from django import forms
from infa_web.apps.articulos.models import *
from django.core.exceptions import ValidationError
from django.db.models import Max

class ArticleForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ArticleForm, self).__init__(*args, **kwargs)

		name_db = "db_1"
		self.fields['cesdo'].choices = [(item.pk, unicode(item)) for item in Esdo.objects.using(name_db).all()]
		self.fields['cgpo'].choices = [(item.pk, unicode(item)) for item in Gpo.objects.using(name_db).all()]
		self.fields['cunidad'].choices = [(item.pk, unicode(item)) for item in Unidades.objects.using(name_db).all()]
		self.fields['ivas_civa'].choices = [(item.pk, unicode(item)) for item in Iva.objects.using(name_db).all()]
		#self.fields['citerce1'].choices = [(item.pk, unicode(item)) for item in Tercero.objects.using(name_db).all()]
		#self.fields['citerce2'].choices = [(item.pk, unicode(item)) for item in Tercero.objects.using(name_db).all()]
		#self.fields['citerce3'].choices = [(item.pk, unicode(item)) for item in Tercero.objects.using(name_db).all()]
		self.fields['cmarca'].choices = [(item.pk, unicode(item)) for item in Marca.objects.using(name_db).all()]
		self.fields['cubica'].choices = [(item.pk, unicode(item)) for item in Ubica.objects.using(name_db).all()]
		self.fields['ctiarlo'].choices = [(item.pk, unicode(item)) for item in Tiarlos.objects.using(name_db).all()]

	class Meta:
		model = Arlo
		fields = "__all__"
		exclude = ["citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3"]
		widgets = {
			'cgpo':forms.Select(attrs={'class':'form-control','required':True}),
			'cesdo' : forms.Select(attrs={'class': 'form-control','required':True}),
			'cunidad' : forms.Select(attrs={'class': 'form-control','required':True}),
			'ivas_civa' : forms.Select(attrs={'class': 'form-control','required':True}),
			'citerce1' : forms.Select(attrs={'class': 'form-control'}),
			'citerce2' : forms.Select(attrs={'class': 'form-control'}),
			'citerce3' : forms.Select(attrs={'class': 'form-control'}),
			'cmarca' : forms.Select(attrs={'class': 'form-control','required':True}),
			'cubica' : forms.Select(attrs={'class': 'form-control','required':True}),
			'ctiarlo' : forms.Select(attrs={'class': 'form-control','required':True}),

			'ncorto' : forms.TextInput(attrs={'class': 'form-control','required':True}),
			'nlargo' : forms.TextInput(attrs={'class': 'form-control','required':True}),
			'refe' : forms.TextInput(attrs={'class': 'form-control'}),

			'cbarras' : forms.NumberInput(attrs={'class': 'form-control','step':'1'}),
			'mesesgara' : forms.NumberInput(attrs={'class': 'form-control','step':'1','min':0}),
			'stomin' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'stomax' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			#'canti' : forms.NumberInput(attrs={'type_input':'number','class': 'form-control','required':True,'step':'0.01','min':0}),
			'canti' : forms.NumberInput(attrs={'type_input':'number','class': 'form-control','required':True,'step':'0.01','min':0}),
			'vcosto' : forms.NumberInput(attrs={'type_input':'number','class': 'form-control','required':True,'step':'0.01','min':0}),
			'porult1':forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'porult2':forms.NumberInput(attrs={'class': 'form-control','step':'0.01','min':0}),
			'porult3':forms.NumberInput(attrs={'class': 'form-control','step':'0.01','min':0}),
			'porult4':forms.NumberInput(attrs={'class': 'form-control','step':'0.01','min':0}),
			'porult5':forms.NumberInput(attrs={'class': 'form-control','step':'0.01','min':0}),
			'porult6':forms.NumberInput(attrs={'class': 'form-control','step':'0.01','min':0}),
			'pvta1': forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'pvta2': forms.NumberInput(attrs={'class': 'form-control','step':'0.01','min':0}),
			'pvta3': forms.NumberInput(attrs={'class': 'form-control','step':'0.01','min':0}),
			'pvta4': forms.NumberInput(attrs={'class': 'form-control','step':'0.01','min':0}),
			'pvta5': forms.NumberInput(attrs={'class': 'form-control','step':'0.01','min':0}),
			'pvta6': forms.NumberInput(attrs={'class': 'form-control','step':'0.01','min':0}),

			'foto1':forms.FileInput(attrs={'class': 'form-control'}),
			'foto2':forms.FileInput(attrs={'class': 'form-control'}),
			'foto3':forms.FileInput(attrs={'class': 'form-control'})
		}
		labels = {
			'carlos':'Código Interno',
			'cbarras':'Código de Barras',
			'cgpo':'Grupo',
			'ncorto':'Nombre Corto',
			'nlargo':'Descripción',
			'canti':'Cantidad',
			'vcosto':'Costo',
			'ifcostear':'Costear',
			'ifpvfijo':'Precio Venta Fijo',
			'cesdo':'Estado',
			'cunidad':'Unidades',
			'ctiarlo':'Tipo de Artículo',
			'ivas_civa':'IVA',
			'stomin':'Stock Mínimo',
			'stomax':'Stock Máximo',
			'pvta1':'Precio Venta 1',
			'pvta2':'Precio Venta 2',
			'pvta3':'Precio Venta 3',
			'pvta4':'Precio Venta 4',
			'pvta5':'Precio Venta 5',
			'pvta6':'Precio Venta 6',
			'citerce1':'',
			'vcosto1':'',
			'fcosto1':'',
			'citerce2':'',
			'vcosto2':'',
			'fcosto2':'',
			'citerce3':'',
			'vcosto3':'',
			'fcosto3':'',
			'ifedinom':'Nombre Editable',
			'refe':'Referencia',
			'cmarca':'Marca',
			'ifdesglo':'Desglosado',
			'mesesgara':'Garantía(Meses)',
			'cubica':'Ubicación',
			'porult1':'Porcentaje 1',
			'porult2':'Porcentaje 2',
			'porult3':'Porcentaje 3',
			'porult4':'Porcentaje 4',
			'porult5':'Porcentaje 5',
			'porult6':'Porcentaje 6',
			'foto1':'Foto 1',
			'foto2':'Foto 2',
			'foto3':'Foto 3'
		}

	def clean(self):
		if self.cleaned_data["stomin"] > self.cleaned_data["stomax"]:
			self.add_error( "stomin", "El Strock Minimo debe ser menor al Stock Mayor" )

class GpoForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(GpoForm, self).__init__(*args, **kwargs)
		name_db = "db_1"

		lastCgpo = Gpo.objects.using(name_db).aggregate(Max('cgpo'))
		if lastCgpo["cgpo__max"]:
			recommendedCgpo = lastCgpo["cgpo__max"] + 1
		else:
			recommendedCgpo = 0

		self.fields['cgpo'].initial = recommendedCgpo

		self.fields['cesdo'].choices = [(item.pk, unicode(item)) for item in Esdo.objects.using(name_db).all()]

	class Meta:
		model = Gpo
		fields = "__all__"
		widgets = {
			'cesdo' : forms.Select(attrs={'class': 'form-control','required':''}),
			'cgpo' : forms.NumberInput(attrs={'class': 'form-control','required': True}),
			'ngpo' : forms.TextInput(attrs={'class': 'form-control','required': True}),
		}
		labels = {
			'cgpo' : 'Código Interno',
			'ngpo' : 'Nombre',
			'cesdo' : 'Estado'
		}

class BreakdownArticleForm(forms.ModelForm):
	class Meta:
		model = Arlosdesglo
		fields = "__all__"
		exclude = ["arlosp"]
		widgets = {
			'cesdo' : forms.Select(attrs={'class': 'form-control','required': True}),
			'carlosglo' : forms.Select(attrs={'class': 'form-control','required': True}),
		}
		labels = {
			"carlosp":"",
			"itglo":"",
			"carlosglo":"",
			"cantiglo":"",
			"costoglo":"",
			"vtoglo":"",
			"cesdo":"",
		}

class BrandForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(BrandForm, self).__init__(*args, **kwargs)

		name_db = "db_1"
		self.fields['cesdo'].choices = [(item.pk, unicode(item)) for item in Esdo.objects.using(name_db).all()]

	class Meta:
		model = Marca
		fields = "__all__"
		exclude = ["cmarca"]
		widgets = {
			'cesdo' : forms.Select(attrs={'class': 'form-control','required':''}),
			'nmarca' : forms.TextInput(attrs={'class': 'form-control','required': True}),
		}
		labels = {
			'cmarca' : 'Código Interno',
			'nmarca' : 'Nombre',
			'cesdo' : 'Estado'
		}
		
class TiarlosForm(forms.ModelForm):
	class Meta:
		model = Tiarlos
		fields = "__all__"
		exclude = ["ctiarlos"]
		widgets = {
			'ntiarlos' : forms.TextInput(attrs={'class': 'form-control','required': True}),
		}
		labels = {
			'ctiarlos' : 'Código Interno',
			'ntiarlos' : 'Nombre',
		}
