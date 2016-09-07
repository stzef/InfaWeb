# -*- coding: utf-8 -*-
from django import forms
from infa_web.apps.movimientos.models import *
from infa_web.apps.inventarios.models import *
from infa_web.parameters import ManageParameters

class InputMovementForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(InputMovementForm, self).__init__(*args, **kwargs)

		manageParameters = ManageParameters()
		default_movement = manageParameters.get_param_value("default_movement_for_input_bills")
		self.fields['ctimo'].choices = [(timo.pk, unicode(timo)) for timo in Timo.objects.filter(ctimo__startswith=PREFIJO_MOVIMIENTOS_ENTRADA)]
		self.fields['ctimo'].initial = default_movement

	class Meta:
		model = Mven
		fields = "__all__"
		widgets = { 
			'cesdo':forms.Select(attrs={'class':'form-control','required':True}),
			'citerce' : forms.Select(attrs={'class':'form-control','required':True,'value':DEFAULT_TERCERO}),
			'ctimo' : forms.Select(attrs={'class':'form-control','required':True}),
			'cbode0' : forms.Select(attrs={'class':'form-control','required':True}),
			'cbode1' : forms.Select(attrs={'class':'form-control','required':True}),
			'docrefe' : forms.TextInput(attrs={'class':'form-control','max_length':10,'required':True}),
			'descri' : forms.TextInput(attrs={'class':'form-control','max_length':250}),
			'detaanula' : forms.TextInput(attrs={'class':'form-control','max_length':250}),
			'vttotal' : forms.NumberInput(attrs={'class': 'form-control app-input-important','required':True,'step':'1','min':0}),
			'cmven' : forms.NumberInput(attrs={'class': 'form-control'}),
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
			'cmven':'Código Interno',
			'fmven':'Fecha',
		}

class OutputMovementForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(OutputMovementForm, self).__init__(*args, **kwargs)

		manageParameters = ManageParameters()
		default_movement = manageParameters.get_param_value("default_movement_for_output_bills")
		self.fields['ctimo'].choices = [(timo.pk, unicode(timo)) for timo in Timo.objects.filter(ctimo__startswith=PREFIJO_MOVIMIENTOS_SALIDA)]
		self.fields['ctimo'].initial = default_movement
		
	class Meta:
		model = Mvsa
		fields = "__all__"
		widgets = {
			'cesdo':forms.Select(attrs={'class':'form-control','required':True}),
			'citerce' : forms.Select(attrs={'class':'form-control','required':True,'value':DEFAULT_TERCERO}),
			'ctimo' : forms.Select(attrs={'class':'form-control','required':True}),
			'cbode0' : forms.Select(attrs={'class':'form-control','required':True}),
			'cbode1' : forms.Select(attrs={'class':'form-control','required':True}),
			'docrefe' : forms.TextInput(attrs={'class':'form-control','max_length':10,'required':True}),
			'descri' : forms.TextInput(attrs={'class':'form-control','max_length':250}),
			'detaanula' : forms.TextInput(attrs={'class':'form-control','max_length':250}),
			'vttotal' : forms.NumberInput(attrs={'class': 'form-control app-input-important','required':True,'step':'1','min':0}),
			'cmvsa' : forms.NumberInput(attrs={'class': 'form-control'}),
			'fmvsa':forms.DateInput(attrs={'class':'form-control date','required':True}),
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
			'cmvsa':'Código Interno',
			'fmvsa':'Fecha',
		}

class InputMovementDetailForm(forms.ModelForm):
	class Meta:
		model = Mvendeta
		fields = "__all__"
		widgets = {
			'cmven':forms.Select(attrs={'class':'form-control'}),
			'it':forms.NumberInput(attrs={'class': 'form-control','required':True,'min':0}),
			'carlos':forms.Select(attrs={'class':'form-control','required':True}),
			#'citerce':forms.Select(attrs={'class':'form-control','required':True}),
			'nlargo':forms.TextInput(attrs={'class':'form-control'}),
			'canti':forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'1','min':0}),
			'vunita':forms.NumberInput(attrs={'class': 'form-control','required':True,'min':0,'step':'0.01',}),
			'vtotal':forms.NumberInput(attrs={'class': 'form-control','required':True,'min':0,'step':'0.01',}),
		}
		labels = {
			'cmven':'Codigo M Entrada',
			'it':'Item',
			'carlos':'Articulo',
			#'citerce':'Tercero',
			'nlargo':'Nombre Largo',
			'canti':'Cantidad',
			'vunita':'V Unitario',
			'vtotal':'V Total',
		}

class OutputMovementDetailForm(forms.ModelForm):
	class Meta:
		model = Mvsadeta
		fields = "__all__"
		widgets = {
			'cmvsa':forms.Select(attrs={'class':'form-control'}),
			'it':forms.NumberInput(attrs={'class': 'form-control','required':True,'min':0}),
			'carlos':forms.Select(attrs={'class':'form-control','required':True}),
			#'citerce':forms.Select(attrs={'class':'form-control','required':True}),
			'nlargo':forms.TextInput(attrs={'class':'form-control'}),
			'canti':forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'1','min':0}),
			'vunita':forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vtotal':forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
		}
		labels = {
			'cmvsa':'Codigo M Entrada',
			'it':'Item',
			'carlos':'Articulo',
			#'citerce':'Tercero',
			'nlargo':'Nombre Largo',
			'canti':'Cantidad',
			'vunita':'V Unitario',
			'vtotal':'V Total',
		}

class ProccessCostingAndStock(forms.Form):
	nota_inicial = forms.CharField(label = 'Nota Inicial', widget = forms.TextInput(attrs = {'class': 'form-control', 'readonly': True}))
	fecha_nota_inicial = forms.CharField(label = 'Fecha Nota Inicial', widget = forms.TextInput(attrs = {'class': 'form-control', 'readonly': True}))
	fecha_final = forms.CharField(label = 'Fecha Final', widget = forms.TextInput(attrs = {'class': 'form-control date', 'required': True}))

	def __init__(self, *args, **kwargs):
		super(ProccessCostingAndStock, self).__init__(*args, **kwargs)
		manageParameters = ManageParameters()
		try:
			invini = Invinicab.objects.get(pk = manageParameters.get_param_value("initial_note"))
			self.fields['nota_inicial'].initial = invini.cii
			self.fields['fecha_nota_inicial'].initial = invini.fii
		except Invinicab.DoesNotExist:
			self.fields['nota_inicial'].initial = ''
			self.fields['fecha_nota_inicial'].initial = ''
