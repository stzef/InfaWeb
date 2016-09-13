# -*- coding: utf-8 -*-
from django import forms

from infa_web.apps.facturacion.models import *

class FacForm(forms.ModelForm):
	class Meta:
		model = Fac
		fields = "__all__"
		widgets = {
			'cfac' : forms.TextInput(attrs={'class':'form-control'}),
			'femi' : forms.DateInput(attrs={'class':'form-control date','required':True}),
			'citerce' : forms.Select(attrs={'class':'form-control','required':True}),
			'cesdo' : forms.Select(attrs={'class':'form-control','required':True}),
			'fpago' : forms.DateInput(attrs={'class':'form-control date','required':True}),
			'ctifopa' : forms.Select(attrs={'class':'form-control','required':True}),
			'descri' : forms.TextInput(attrs={'class':'form-control'}),
			'detaanula' : forms.TextInput(attrs={'class':'form-control'}),
			'vtbruto' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vtbase' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vtiva' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vflete' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vdescu' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vttotal' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vefe' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vtar' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'doctar' : forms.TextInput(attrs={'class':'form-control'}),
			'bancotar' : forms.Select(attrs={'class':'form-control','required':True}),
			'vchq' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'docchq' : forms.TextInput(attrs={'class':'form-control'}),
			'bancochq' : forms.Select(attrs={'class':'form-control','required':True}),
			'ventre' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vcambio' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			#cusu char(20)
			'ccaja' : forms.Select(attrs={'class':'form-control','required':True}),
			#ncuo integer, 
			'cvende'  : forms.Select(attrs={'class':'form-control','required':True}),
			'cdomici'  : forms.Select(attrs={'class':'form-control','required':True}),
			'tpordes' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'cemdor'  : forms.Select(attrs={'class':'form-control','required':True}),
			#ccoti char(10)
			'vncre' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'doccre' : forms.TextInput(attrs={'class':'form-control'}),
			'brtefte' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'prtefte' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vrtefte' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'fhasdomi' : forms.DateInput(attrs={'class':'form-control date','required':True}),
		}
		labels = {
		}

class FacdetaForm(forms.ModelForm):
	class Meta:
		model = Facdeta
		fields = "__all__"
		widgets = {
			'cfac' : forms.Select(attrs={'class':'form-control','required':True}),
			'itfac' : forms.TextInput(attrs={'class':'form-control'}),
			'carlos' : forms.Select(attrs={'class':'form-control','required':True}),
			'nlargo' : forms.TextInput(attrs={'class':'form-control'}),
			'ncorto' : forms.TextInput(attrs={'class':'form-control'}),
			'canti' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			#civa char(2)
			#niva char(40)
			'poriva' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vunita' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vbruto' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vbase' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'viva' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vtotal' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'pordes' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			#crue char(10)
			'pvtafull' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vcosto' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
		}
		labels = {
		}
