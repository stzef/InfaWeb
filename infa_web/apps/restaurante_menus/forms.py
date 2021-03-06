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
			'canti':'Cantidad',
			'stomin':'Stock Mínimo',
			'stomax':'Stock Máximo',
			'cesdo':'Estado',
			'cunidad':'Unidades',
			'civa':'IVA',
			'foto':'Foto 1',
			'ifcostear': 'Costear',
			'ifedinom': 'Nombre Editable',

		}

	def clean(self):
		if self.cleaned_data["stomin"] > self.cleaned_data["stomax"]:
			self.add_error( "stomin", "El Strock Minimo debe ser menor al Stock Mayor" )

class DishForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(DishForm, self).__init__(*args, **kwargs)

		name_db = using

	class Meta:
		model = Platos
		fields = "__all__"
		exclude = []
		widgets = {
			#'cplato' :
			'nplato' : forms.TextInput(attrs={'class': 'form-control','required':True}),
			#'fcrea' :
			'vttotal' : forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'disabled':True,'step':'0.01','min':0}),
			'foto':forms.FileInput(attrs={'class': 'form-control'}),
			'npax' : forms.TextInput(attrs={'type_input':'text','class': 'form-control ','required':True,'min':0}),


		}
		labels = {
			'cplato':'Código Interno',
			'nplato':'Nombre',
			'fcrea':'Fecha de Creacion',
			'npax' : 'Numero Personas',
			'vttotal':'Vr. Total',
		}

class DishDetailForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(DishDetailForm, self).__init__(*args, **kwargs)

		name_db = using
		#self.fields['cingre'].queryset = Esdo.objects.using(name_db).all()

	class Meta:
		model = Platosdeta
		fields = "__all__"
		#exclude = []
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

"""
class MenuForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(MenuForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()
		self.fields['cgpomenu'].queryset = GposMenus.objects.using(name_db).all()


	class Meta:
		model = Menus
		fields = "__all__"
		exclude = []
		widgets = {
			#'cmenu' :
			'nmenu' : forms.TextInput(attrs={'class': 'form-control','required':True}),
			#'fcrea' :
			'cesdo' : forms.Select(attrs={'class':'form-control','required':True}),
			'cgpomenu' : forms.Select(attrs={'class':'form-control','required':True}),
			'npax' : forms.TextInput(attrs={'type_input':'text','class': 'form-control ','required':True,'min':0}),
			'pvta1' :forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),
			'pvta2' :forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),
			'pvta3' :forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),
			'vttotal' :forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'disabled':True,'step':'0.01','min':0}),
			'foto' : forms.FileInput(attrs={'class': 'form-control'}),
		}
		labels = {
			'cmenu' : 'Codigo',
			'nmenu' : 'Nombre',
			#'fcrea' : '',
			'cesdo' : 'Estado',
			'cgpomenu' : 'Grupo',
			'npax' : 'Numero Personas',
			'pvta1' : 'Precio Venta 1',
			'pvta2' : 'Precio Venta 2',
			'pvta3' : 'Precio Venta 3',
			'vttotal' : 'Vr. Total',
			'foto' : 'Foto',

		}
"""

class MenuDetailForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(MenuDetailForm, self).__init__(*args, **kwargs)

		name_db = using
		#self.fields['cingre'].queryset = Esdo.objects.using(name_db).all()

	class Meta:
		model = Menusdeta
		fields = "__all__"
		exclude = []
		widgets = {
			#'cmenu':
			'it': forms.NumberInput(attrs={'class': 'form-control','required':True,'min':0}),
			#'cplato':
			'canti': forms.NumberInput(attrs={'type_input':'number','class': 'form-control','required':True,'step':'0.01','min':0}),
			'vunita': forms.NumberInput(attrs={'type_input':'number','class': 'form-control','required':True,'step':'0.01','min':0}),
			'vtotal': forms.NumberInput(attrs={'type_input':'number','class': 'form-control','required':True,'step':'0.01','min':0}),
		}
		labels = {
			'cmenu': 'Menu',
			'it': 'Item',
			'cplato': 'Plato',
			'canti': 'Cantidad',
			'vunita': 'V Unitario',
			'vtotal': 'V Total'
		}

"""
class GposMenusForm(forms.ModelForm):

	def __init__(self, using='', *args, **kwargs):
		super(GposMenusForm, self).__init__(*args, **kwargs)
		name_db = using

		lastCgpo = GposMenus.objects.using(name_db).aggregate(Max('cgpomenu'))
		if lastCgpo["cgpomenu__max"]:
			recommendedCgpo = lastCgpo["cgpomenu__max"] + 1
		else:
			recommendedCgpo = 0

		self.fields['cgpomenu'].initial = recommendedCgpo

		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()

	class Meta:
		model = GposMenus
		fields = "__all__"
		widgets = {
			'cesdo' : forms.Select(attrs={'class': 'form-control','required':''}),
			'cgpomenu' : forms.NumberInput(attrs={'class': 'form-control','required': True}),
			'ngpomenu' : forms.TextInput(attrs={'class': 'form-control','required': True}),
			'orden' : forms.NumberInput(attrs={'class': 'form-control','required': True}),
		}
		labels = {
			'cgpomenu' : 'Código Interno',
			'ngpomenu' : 'Nombre',
			'cesdo' : 'Estado',
			'orden' : 'Orden',
		}
"""
