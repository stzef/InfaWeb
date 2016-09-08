# -*- coding: utf-8 -*-
from django import forms
from infa_web.apps.terceros.models import *

class ThirdPartyForm(forms.ModelForm):
	class Meta:
		model = Tercero
		fields = "__all__"
		exclude = ["citerce"]
		widgets = {
			'ctiide':forms.Select(attrs={'class':'form-control','required':''}),
			'ciudad':forms.Select(attrs={'class':'form-control','required':''}),
			'cregiva':forms.Select(attrs={'class':'form-control','required':''}),
			'cautorre':forms.Select(attrs={'class':'form-control','required':''}),
			'cesdo':forms.Select(attrs={'class':'form-control','required':''}),
			'cvende':forms.Select(attrs={'class':'form-control','required':''}),
			'czona':forms.Select(attrs={'class':'form-control','required':''}),
			'cruta':forms.Select(attrs={'class':'form-control','required':''}),
			'cpersona':forms.Select(attrs={'class':'form-control','required':''}),

			'idterce':forms.NumberInput(attrs={'class':'form-control','required':True}),
			'dv':forms.TextInput(attrs={'class':'form-control','required':True}),
			'rasocial':forms.TextInput(attrs={'class':'form-control','required':True}),
			'nomcomer':forms.TextInput(attrs={'class':'form-control','required':True}),
			'ape1':forms.TextInput(attrs={'class':'form-control'}),
			'ape2':forms.TextInput(attrs={'class':'form-control'}),
			'nom1':forms.TextInput(attrs={'class':'form-control'}),
			'nom2':forms.TextInput(attrs={'class':'form-control'}),
			'sigla':forms.TextInput(attrs={'class':'form-control'}),
			'nomegre':forms.TextInput(attrs={'class':'form-control','required':True}),
			'replegal':forms.TextInput(attrs={'class':'form-control'}),
			'dirterce':forms.TextInput(attrs={'class':'form-control','required':True}),
			'telterce':forms.NumberInput(attrs={'class':'form-control','required':True}),
			'faxterce':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'contacto':forms.TextInput(attrs={'class':'form-control'}),
			'topcxc':forms.NumberInput(attrs={'class':'form-control','step':'0.01'}),
			'ndiacxc':forms.TextInput(attrs={'class':'form-control','required':True}),
			'clipre':forms.TextInput(attrs={'class':'form-control','required':True}),
			'fnaci':forms.DateInput(attrs={'class':'form-control date','required':True}),
			'naju':forms.TextInput(attrs={'class':'form-control','required':True}),
			'ordenruta':forms.NumberInput(attrs={'class':'form-control'}),
		}
		labels = {
			'citerce':'Código Interno',
			'idterce':'Identificación',
			'dv':'DV',
			'ctiide':'Tipo Identificación',
			'rasocial':'Razón Social',
			'nomcomer':'Nombre Comercial',
			'ape1':'Apellido 1',
			'ape2':'Apellido 2',
			'nom1':'Nombre 1',
			'nom2':'Nombre 2',
			'sigla':'Sigla',
			'replegal':'Representante Legal',
			'dirterce':'Dirección',
			'telterce':'Teléfono',
			'faxterce':'Fax',
			'ciudad':'Ciudad',
			'email':'Correo Electrónico',
			'contacto':'Contacto',
			'cregiva':'Régimen de IVA',
			'cautorre':'Autorretenedor',
			'cesdo':'Estado',
			'cvende':'Vendedor',
			'topcxc':'Tope Cartera por Cobrar',
			'czona':'Zona',
			'clipre':'Lista de Precio',
			'fnaci':'Fecha de Nacimiento',
			'cruta':'Ruta',
			'ordenruta':'Orden Ruta',
			'cpersona':'Tipo de Tercero',
		}

class AutorretenedorForm(forms.ModelForm):
	class Meta:
		model = Autorre
		fields = "__all__"
		exclude = ["cautorre"]
		widgets = {
			'nautorre' : forms.TextInput(attrs={'class': 'form-control','required':True}),
		}
		labels = {
			'cautorre':'Código Interno',
			'nautorre':'Nombre',
		}

class RouteForm(forms.ModelForm):
	class Meta:
		model = Ruta
		fields = "__all__"
		exclude = ["cruta"]
		widgets = {
			'nruta' : forms.TextInput(attrs={'class': 'form-control','required':True}),
			'cesdo':forms.Select(attrs={'class':'form-control','required':''}),
		}
		labels = {
			'cruta':'Código Interno',
			'nruta':'Nombre',
			'cesdo':'Estado',
		}

class ZoneForm(forms.ModelForm):
	class Meta:
		model = Zona
		fields = "__all__"
		exclude = ["czona"]
		widgets = {
			'nzona' : forms.TextInput(attrs={'class': 'form-control','required':True}),
			'cesdo':forms.Select(attrs={'class':'form-control','required':''}),
		}
		labels = {
			'cruta':'Código Interno',
			'nzona':'Nombre',
			'cesdo':'Estado',
		}
