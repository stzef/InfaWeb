# -*- coding: utf-8 -*-
from django import forms
from infa_web.apps.movimientos.models import *
from infa_web.parameters import ManageParameters

class InputMovementForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(InputMovementForm, self).__init__(*args, **kwargs)

		manageParameters = ManageParameters()
		minCodeArlos = manageParameters.get_param_value("default_movement_for_input_bills")
		self.fields['ctimo'].initial = minCodeArlos
		
	class Meta:
		model = Mven
		fields = "__all__"
		widgets = {
			'cesdo':forms.Select(attrs={'class':'form-control','required':True}),
			'citerce' : forms.Select(attrs={'class':'form-control','required':True}),
			'ctimo' : forms.Select(attrs={'class':'form-control','required':True}),
			'cbode0' : forms.Select(attrs={'class':'form-control','required':True}),
			'cbode1' : forms.Select(attrs={'class':'form-control','required':True}),
			'docrefe' : forms.TextInput(attrs={'class':'form-control','max_length':10}),
			'descri' : forms.TextInput(attrs={'class':'form-control','max_length':250}),
			'detaanula' : forms.TextInput(attrs={'class':'form-control','max_length':250}),
			'vttotal' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'1','min':0}),
			'cmven' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'1','min':0}),
			'fmven':forms.DateInput(attrs={'class':'form-control date','required':True}),
		}
		labels = {
			'cesdo':'Estado',
			'citerce':'Tercero',
			'ctimo':'Movimiento',
			'cbode0':'Bodega',
			'cbode1':'Bodega',
			'docrefe':'Doc Refe',
			'descri':'Descripcion',
			'detaanula':'',
			'vttotal':'Valor Total',
			'cmven':'Códgio Interno',
			'fmven':'Fecha',
		}

class InputMovementDetailForm(forms.ModelForm):
	class Meta:
		model = Mvendeta
		fields = "__all__"
		widgets = {
			'cmven':forms.Select(attrs={'class':'form-control','required':True}),
			'it':forms.NumberInput(attrs={'class': 'form-control','required':True,'min':0}),
			'carlos':forms.Select(attrs={'class':'form-control','required':True}),
			'nlargo':forms.TextInput(attrs={'class':'form-control'}),
			'canti':forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'1','min':0}),
			'vunita':forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'1','min':0}),
			'vtotal':forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'1','min':0}),
		}
		labels = {
			'cmven':'Codigo M Entrada',
			'it':'Item',
			'carlos':'Articulo',
			'nlargo':'Nombre Largo',
			'canti':'Cantidad',
			'vunita':'V Unitario',
			'vtotal':'V Total',
		}
