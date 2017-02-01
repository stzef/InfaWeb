# -*- coding: utf-8 -*-
from django import forms
from infa_web.apps.restaurante_menus.models import *
from django.core.exceptions import ValidationError
from django.db.models import Max

class IngredientForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(IngredientForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()
		self.fields['cunidad'].queryset = Unidades.objects.using(name_db).all()
		self.fields['civa'].queryset = Iva.objects.using(name_db).all()

	class Meta:
		model = Ingredientes
		fields = "__all__"
		exclude = []
		widgets = {
			#'cingre':
			'ningre':forms.TextInput(attrs={'class': 'form-control','required':True}),
			'canti':forms.NumberInput(attrs={'type_input':'number','class': 'form-control','required':True,'step':'0.01','min':0}),
			'vcosto':forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),
			#'ifcostear':
			'stomin': forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'stomax': forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			#'ifedinom':
			'cesdo': forms.Select(attrs={'class':'form-control','required':True}),
			'cunidad': forms.Select(attrs={'class':'form-control','required':True}),
			'civa': forms.Select(attrs={'class':'form-control','required':True}),

			'foto':forms.FileInput(attrs={'class': 'form-control'}),
		}
		labels = {
			'cingre':'Código Interno',
			'ningre':'Nombre',
			'vcosto':'Costo',
			'stomin':'Stock Mínimo',
			'stomax':'Stock Máximo',
			'cesdo':'Estado',
			'cunidad':'Unidades',
			'civa':'IVA',
			'foto':'Foto 1',
		}

	def clean(self):
		if self.cleaned_data["stomin"] > self.cleaned_data["stomax"]:
			self.add_error( "stomin", "El Strock Minimo debe ser menor al Stock Mayor" )

class DishForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(IngredientForm, self).__init__(*args, **kwargs)

		name_db = using

	class Meta:
		model = Ingredientes
		fields = "__all__"
		exclude = []
		widgets = {
			#'cplato' :
			'nplato' : forms.TextInput(attrs={'class': 'form-control','required':True}),
			#'fcrea' :
			'vttotal' : forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),


		}
		labels = {
			'cplato':'Código Interno',
			'nplato':'Nombre',
			'fcrea':'fECHA cREACION',
			'vttotal':'Valor Total',
		}


class DishDetail(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(IngredientForm, self).__init__(*args, **kwargs)

		name_db = using
		#self.fields['cingre'].queryset = Esdo.objects.using(name_db).all()

	class Meta:
		model = Ingredientes
		fields = "__all__"
		exclude = []
		widgets = {
			#'cplato' :
			'cingre' : forms.Select(attrs={'class':'form-control','required':True}),
			'it' : forms.NumberInput(attrs={'class': 'form-control','required':True,'min':0}),
			'canti' : forms.NumberInput(attrs={'type_input':'number','class': 'form-control','required':True,'step':'0.01','min':0}),
			'vunita' : forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),
			'vtotal' : forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),
		}
		labels = {
			'cplato':'Código Plato',
			'cingre':'Ingrediente',
			'it':'Item',
			'canti':'Cantidad',
			'vunita':'V Unitario',
			'vtotal':'Valor Total',
		}

