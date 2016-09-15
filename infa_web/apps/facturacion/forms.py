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
			'citerce' : forms.Select(attrs={'class':'form-control','required':True,'value':DEFAULT_TERCERO}),
			'cesdo' : forms.Select(attrs={'class':'form-control','required':True}),
			'fpago' : forms.DateInput(attrs={'class':'form-control date','required':True}),
			'ctifopa' : forms.Select(attrs={'class':'form-control','required':True}),
			'descri' : forms.TextInput(attrs={'class':'form-control'}),
			'detaanula' : forms.TextInput(attrs={'class':'form-control'}),
			'vtbase' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vtiva' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vflete' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vdescu' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vttotal' : forms.NumberInput(attrs={'class': 'app-input-important form-control','required':True,'step':'0.01','min':0}),
			'vefe' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vtar' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'doctar' : forms.TextInput(attrs={'class':'form-control'}),
			'bancotar' : forms.Select(attrs={'class':'form-control','required':True}),
			'vchq' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'docchq' : forms.TextInput(attrs={'class':'form-control'}),
			'bancochq' : forms.Select(attrs={'class':'form-control','required':True}),
			'ventre' : forms.NumberInput(attrs={'class': 'app-input-important form-control','required':True,'step':'0.01','min':0}),
			'vcambio' : forms.NumberInput(attrs={'class': 'app-input-important form-control','required':True,'step':'0.01','min':0}),
			#cusu char(20)
			'ccaja' : forms.Select(attrs={'class':'form-control','required':True}),
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
			'cfac' : 'Codigo Interno',
			'femi' : 'Fecha Emision',
			'citerce' : 'Tercero',
			'cesdo' : 'Estado',
			'fpago' : 'Fecha pago',
			'ctifopa' : 'Forma Pago',
			'descri' : 'Descripcion',
			'detaanula' : 'Deta. Anulacion',
			'vtbase' : 'V.Tot Base',
			'vtiva' : 'V.Tot IVA',
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
			'vncre' : 'V Nota Credito',
			'doccre' : 'Doc Nota Credito',
			'brtefte' : 'Base Rte Fte',
			'prtefte' : 'Porc Rte Fte',
			'vrtefte' : 'V Rte Fte',
			'fhasdomi' : 'Fecha Domicilio',
			'cusu' : 'Usuario',
			'ccoti' : 'Cotizacion',
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
			'civa' : forms.Select(attrs={'class':'form-control','required':True}),
			#niva char(40)
			'poriva' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vunita' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vbase' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'viva' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'vtotal' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
			'pordes' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0}),
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
