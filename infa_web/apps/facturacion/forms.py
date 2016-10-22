# -*- coding: utf-8 -*-
from django import forms

from infa_web.apps.facturacion.models import *
from infa_web.parameters import ManageParameters

class FacForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(FacForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['citerce'].queryset = Tercero.objects.using(name_db).all()
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()
		self.fields['ccaja'].queryset = Caja.objects.using(name_db).all()
		self.fields['cvende'].queryset = Vende.objects.using(name_db).all()
		self.fields['cdomici'].queryset = Domici.objects.using(name_db).all()
		self.fields['cemdor'].queryset = Emdor.objects.using(name_db).all()
		self.fields['ctifopa'].queryset = Tifopa.objects.using(name_db).all()
		
	class Meta:
		model = Fac
		fields = "__all__"
		widgets = {
			'citerce' : forms.Select(attrs={'class':'form-control','required':True,'value':DEFAULT_TERCERO}),
			'cesdo' : forms.Select(attrs={'class':'form-control','required':True}),
			'ccaja' : forms.Select(attrs={'class':'form-control','required':True}),
			'cvende'  : forms.Select(attrs={'class':'form-control','required':True}),
			'cdomici'  : forms.Select(attrs={'class':'form-control','required':True}),
			'cemdor'  : forms.Select(attrs={'class':'form-control','required':True}),
			'ctifopa' : forms.Select(attrs={'class':'form-control','required':True}),

			'cfac' : forms.TextInput(attrs={'class':'app-input-important form-control', 'readonly': True}),
			'detaanula' : forms.TextInput(attrs={'class':'form-control'}),

			'femi' : forms.DateInput(attrs={'class':'form-control date','required':True,'readonly': True}),
			'fpago' : forms.DateInput(attrs={'class':'form-control date','required':True}),
			'fhasdomi' : forms.DateInput(attrs={'class':'form-control date','required':True}),

			'descri' : forms.Textarea(attrs={'class':'form-control'}),
			'vtbase' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0,"readonly":True}),
			'vtiva' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0,"readonly":True}),
			'vflete' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0}),
			'vttotal' : forms.TextInput(attrs={'class': 'input-currency app-input-important form-control','required':True,'readonly':True,'step':'0.01','min':0}),
			'ventre' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0}),
			'vcambio' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'readonly':True,'step':'0.01','min':0}),
			'brtefte' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0}),
			'vrtefte' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0}),
			
			'prtefte' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			
			'vncre' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),#Revisar
			'tpordes' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),#Revisar
			'vdescu' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0}),#Revisar

			#'vefe' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			#'vtar' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			#'doctar' : forms.TextInput(attrs={'class':'form-control'}),
			#'bancotar' : forms.Select(attrs={'class':'form-control','required':True}),
			#'vchq' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			#'docchq' : forms.TextInput(attrs={'class':'form-control'}),
			#'bancochq' : forms.Select(attrs={'class':'form-control','required':True}),
			#cusu char(20)
			#ccoti char(10)
			#'doccre' : forms.TextInput(attrs={'class':'form-control'}),
		}
		labels = {
			'cfac' : 'Codigo Factura',
			'femi' : 'Fecha Emision',
			'citerce' : 'Tercero',
			'cesdo' : 'Estado',
			'fpago' : 'Fecha pago',
			'ctifopa' : 'Forma Pago',
			'descri' : 'Descripcion',
			'detaanula' : 'Deta. Anulacion',
			'vtbase' : 'Base IVA',
			'vtiva' : 'IVA',
			'vflete' : 'V. Flete',
			'vdescu' : 'V. Descto',
			'vttotal' : 'V. Total',
			'vefe' : 'V. Efectivo',
			'vtar' : 'V.Tarjeta',
			'doctar' : 'Doc. Tarjeta',
			'bancotar' : 'Banco',
			'vchq' : 'V. Chque',
			'docchq' : 'Doc. Cheque',
			'bancochq' : 'Banco',
			'ventre' : 'V. Entregado',
			'vcambio' : 'V. Cambio',
			'ccaja' : 'Caja',
			'cvende' : 'Vendedor',
			'cdomici' : 'Domiciliario',
			'tpordes' : '',
			'cemdor' : 'Empacador',
			'vncre' : 'Vr. Nota Credito',
			'doccre' : 'Doc Nota Credito',
			'brtefte' : 'Base Rte Fte',
			'prtefte' : 'Porc Rte Fte',
			'vrtefte' : 'Vr. Rte Fte',
			'fhasdomi' : 'Fecha Domicilio',
			'cusu' : 'Usuario',
			'ccoti' : 'Cotizacion',
		}

class FacdetaForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(FacdetaForm, self).__init__(*args, **kwargs)
		name_db = using
		self.fields['cfac'].queryset = Fac.objects.using(name_db).all()
		self.fields['carlos'].queryset = Arlo.objects.using(name_db).all()
		self.fields['civa'].queryset = Iva.objects.using(name_db).all()

	class Meta:
		model = Facdeta
		fields = "__all__"
		widgets = {
			'cfac' : forms.Select(attrs={'class':'form-control','required':True}),
			'carlos' : forms.Select(attrs={'class':'form-control','required':True}),
			'civa' : forms.Select(attrs={'class':'form-control','required':True,"disabled":True}),
			'itfac' : forms.TextInput(attrs={'class':'form-control'}),
			'nlargo' : forms.TextInput(attrs={'class':'form-control'}),
			'ncorto' : forms.TextInput(attrs={'class':'form-control'}),
			#niva char(40)
			'poriva' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0,"max":100}),
			'canti' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'pordes' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0,"max":100}),
			
			'viva' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vbase' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			
			'vunita' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0}),
			'vtotal' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0, 'readonly':True}),

			'pvtafull' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vcosto' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
		}
		labels = {
			'cfac' : 'Cod. Factura',
			'itfac' : 'Item',
			'carlos' : 'Articulo',
			'nlargo' : 'Nombre Largo',
			'ncorto' : 'Nombre Corto',
			'canti' : 'Cantidad',
			'civa' : 'IVA',
			'niva' : 'Nombre IVA',
			'poriva' : 'Porc IVA',
			'vunita' : 'V. Unitario',
			'vbase' : 'V. Base',
			'viva' : 'V. Iva',
			'vtotal' : 'V. Total',
			'pordes' : 'Porc Descto',
			'pvtafull' : '',
			'vcosto' : 'Costo',
		}

class FacpagoForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(FacpagoForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cmpago'].widget.attrs.update({'required': True, 'class': 'form-control'})
		self.fields['cmpago'].queryset = MediosPago.objects.using(name_db).all()
		self.fields['banmpago'].widget.attrs.update({'required': True, 'class': 'form-control'})
		self.fields['cfac'].queryset = Fac.objects.using(name_db).all()
		self.fields['banmpago'].queryset = Banfopa.objects.using(name_db).all()

	class Meta:
		model = Facpago
		fields = "__all__"
		widgets = {
			'cfac' : forms.Select(attrs={'class':'form-control','required':True}),
			'it' : forms.TextInput(attrs={'class':'form-control','required':True}),
			'docmpago' : forms.TextInput(attrs={'class':'form-control'}),
			'vmpago' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0}),
		}
		labels = {
			'cfac' : 'Codigo Factura',
			'it' : 'Item',
			'cmpago' : 'Medio de Pago',
			'docmpago' : 'Doc. Medio Pago',
			'banmpago' : 'Ban. Medio Pago',
			'vmpago' : 'Valor Medio Pago',
		}

class ReportVentaForm(forms.Form):
	fecha_inicial = forms.CharField(label = 'Fecha Inicial', widget = forms.TextInput(attrs = {'class': 'form-control date', 'required': True}))
	fecha_final = forms.CharField(label = 'Fecha Final', widget = forms.TextInput(attrs = {'class': 'form-control date', 'required': True}))
	cvende = forms.ModelChoiceField(
		widget=forms.Select(attrs={'class':'form-control'}),
		queryset=Vende.objects.all()
	)
	citerce = forms.ModelChoiceField(
		widget=forms.Select(attrs={'class':'form-control'}),
		queryset=Tercero.objects.all()
	)
	ctifopa = forms.ModelChoiceField(
		widget=forms.Select(attrs={'class':'form-control'}),
		queryset=Tifopa.objects.all()
	)
	def __init__(self, using='', *args, **kwargs):
		super(ReportVentaForm, self).__init__(*args, **kwargs)
		name_db = using

		self.fields['cvende'].queryset = Vende.objects.using(name_db).all()
		self.fields['citerce'].queryset = Tercero.objects.using(name_db).all()
		self.fields['ctifopa'].queryset = Tifopa.objects.using(name_db).all()

		manageParameters = ManageParameters(name_db)
