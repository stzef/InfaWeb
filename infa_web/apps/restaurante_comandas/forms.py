# -*- coding: utf-8 -*-
from django import forms
from infa_web.apps.restaurante_comandas.models import *
from django.core.exceptions import ValidationError
from django.db.models import Max

class TableForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(TableForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()

	class Meta:
		model = Mesas
		fields = "__all__"
		exclude = []
		widgets = {
			#'cmesa':forms.TextInput(attrs={'class': 'form-control','required':True}),
			'nmesa':forms.TextInput(attrs={'class': 'form-control','required':True}),
			'cesdo': forms.Select(attrs={'class':'form-control','required':True}),
			'npmax': forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
		}
		labels = {
			'nmesa':'Nombre',
			'cesdo':'Estado',
			'npmax':'# Personas',
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
			'npax' : forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),
			'pvta1' :forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),
			'pvta2' :forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),
			'pvta3' :forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),
			'vttotal' :forms.TextInput(attrs={'type_input':'text','class': 'form-control input-currency','required':True,'step':'0.01','min':0}),
			'foto' : forms.FileInput(attrs={'class': 'form-control'}),
		}
		labels = {
			'nmenu' : 'Nombre',
			#'fcrea' : '',
			'cesdo' : 'Estado',
			'cgpomenu' : 'Grupo',
			'npax' : 'Numero Personas',
			'pvta1' : 'Precio Venta 1',
			'pvta2' : 'Precio Venta 2',
			'pvta3' : 'Precio Venta 3',
			'vttotal' : 'V Total',
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


class ResupedipagoForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(ResupedipagoForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cmpago'].widget.attrs.update({'required': True, 'class': 'form-control'})
		self.fields['cmpago'].queryset = MediosPago.objects.using(name_db).all()
		self.fields['banmpago'].widget.attrs.update({'required': True, 'class': 'form-control'})
		self.fields['banmpago'].queryset = Banfopa.objects.using(name_db).all()

	class Meta:
		model = Resupedipago
		fields = "__all__"
		exclude = []
		widgets = {
			#'cresupedi':
			'it': forms.NumberInput(attrs={'class': 'form-control','required':True,'min':0}),
			'docmpago': forms.TextInput(attrs={'class':'form-control'}),
			'vmpago': forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0}),
			#'banmpago': forms.NumberInput(attrs={'type_input':'number','class': 'form-control','required':True,'step':'0.01','min':0}),
			#'cmpago': forms.NumberInput(attrs={'type_input':'number','class': 'form-control','required':True,'step':'0.01','min':0}),
		}
		labels = {
			'cresupedi': 'Resumen',
			'it': 'Item',
			'docmpago': 'Plato',
			'vmpago': 'Cantidad',
			'banmpago': 'V Unitario',
			'cmpago': 'V Total'
		}

