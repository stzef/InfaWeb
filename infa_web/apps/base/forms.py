# -*- coding: utf-8 -*-
from django import forms
from infa_web.apps.base.models import *

class ParametersForm(forms.ModelForm):
	class Meta:
		model = Parameters
		fields = "__all__"
		widgets = {
			'cesdo':forms.Select(attrs={'class':'form-control','required':''}),
		}
		labels = {
			"smodule":"Sigla",
			"nmodule":"Nombre",
			"enabled_enterprise":"Estado General",
			"enabled":"Estado Empresa",
			"cesdo":"Estado",
		}

class CiudadForm(forms.ModelForm):
	class Meta:
		model = Ciudad
		fields = "__all__"
		exclude = ["cciu"]
		widgets = {
			'cdepar':forms.Select(attrs={'class':'form-control','required':''}),
		}
		labels = {
			'cciu': 'Código Interno',
			'nciu': 'Nombre',
			'cdepar': 'Departamento'
		}

class UbicaForm(forms.ModelForm):
	class Meta:
		model = Ubica
		fields = "__all__"
		exclude = ["cubica"]
		widgets = {
			'cesdo':forms.Select(attrs={'class':'form-control','required':''}),
		}
		labels = {
			'cubica': 'Código Interno',
			'nubica': 'Nombre',
			'cesdo': 'Estado'
		}

class DepartamentoForm(forms.ModelForm):
	class Meta:
		model = Departamento
		fields = "__all__"
		exclude = ["cdepar"]
		widgets = {}
		labels = {
			'cdepar': 'Código Interno',
			'ndepar': 'Nombre'
		}

class StateForm(forms.ModelForm):
	class Meta:
		model = Esdo
		fields = "__all__"
		exclude = []
		widgets = {}
		labels = {
			'cesdo':'Código Interno',
			'nesdo':'Nombre',
			'estavali':'Estado Valido',
		}

class IvaForm(forms.ModelForm):
	class Meta:
		model = Iva
		fields = "__all__"
		exclude = ["civa"]
		widgets = {
			'cesdo':forms.Select(attrs={'class':'form-control','required':''}),
		}
		labels = {
			'civa':'Código Interno',
			'niva':'Nombre',
			'poriva':'Porcentaje',
			'idtira':'Id Tirilla',
			'cesdo':'Estado',
		}

class RegivaForm(forms.ModelForm):
	class Meta:
		model = Regiva
		fields = "__all__"
		exclude = ["cregiva"]
		widgets = {}
		labels = {
			'cregiva':'Código Interno',
			'nregiva':'Nombre',
		}

class IDTypeForm(forms.ModelForm):
	class Meta:
		model = Tiide
		fields = "__all__"
		exclude = ["idtiide"]
		widgets = {
			'ntiide' : forms.TextInput(attrs={'class': 'form-control','required':True}),
		}
		labels = {
			'idtiide':'Código Interno',
			'ntiide':'Nombre',
		}

