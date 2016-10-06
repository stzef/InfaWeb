# -*- coding: utf-8 -*-
from django import forms
from infa_web.apps.base.models import *
from infa_web.apps.articulos.models import *

class ParametersForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(ParametersForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].choices = [(item.pk, unicode(item)) for item in Esdo.objects.using(name_db).all()]

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
	def __init__(self, using='', *args, **kwargs):
		super(CiudadForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cdepar'].choices = [(item.pk, unicode(item)) for item in Departamento.objects.using(name_db).all()]

	class Meta:
		model = Ciudad
		fields = "__all__"
		exclude = ["cciu"]
		widgets = {
			'cdepar':forms.Select(attrs={'class':'form-control','required':''}),
			'nciu':forms.TextInput(attrs={'class':'form-control','required':True}),
		}
		labels = {
			'cciu': 'Código Interno',
			'nciu': 'Nombre',
			'cdepar': 'Departamento'
		}

class MediosPagoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MediosPagoForm, self).__init__(*args, **kwargs)

	class Meta:
		model = MediosPago
		fields = "__all__"
		widgets = {
			'cmpago' : forms.TextInput(attrs={'class':'form-control','required':True}),
			'nmpago' : forms.TextInput(attrs={'class':'form-control','required':True}),
		}
		labels = {
			'cmpago': 'Código Interno',
			'nmpago': 'Nombre',
			'ifdoc': 'Requiere Documento'
		}

class UbicaForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(UbicaForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].choices = [(item.pk, unicode(item)) for item in Esdo.objects.using(name_db).all()]

	class Meta:
		model = Ubica
		fields = "__all__"
		exclude = ["cubica"]
		widgets = {
			'cesdo':forms.Select(attrs={'class':'form-control','required':''}),
			'nubica':forms.TextInput(attrs={'class':'form-control','required':True}),
		}
		labels = {
			'cubica': 'Código Interno',
			'nubica': 'Nombre',
			'cesdo': 'Estado'
		}

class DepartamentoForm(forms.ModelForm):

	def __init__(self, using='', *args, **kwargs):
		super(DepartamentoForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Departamento
		fields = "__all__"
		exclude = ["cdepar"]
		widgets = {
			'ndepar':forms.TextInput(attrs={'class':'form-control','required':True}),
		}
		labels = {
			'cdepar': 'Código Interno',
			'ndepar': 'Nombre'
		}

class StateForm(forms.ModelForm):

	def __init__(self,using='', *args, **kwargs):
		super(StateForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Esdo
		fields = "__all__"
		exclude = []
		widgets = {
			"nesdo":forms.TextInput(attrs={'class':'form-control','required':True}),
			"estavali":forms.TextInput(attrs={'class':'form-control','required':True}),
		}
		labels = {
			'cesdo':'Código Interno',
			'nesdo':'Nombre',
			'estavali':'Estado Valido',
		}

class IvaForm(forms.ModelForm):
	def __init__(self,using='', *args, **kwargs):
		super(IvaForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].choices = [(item.pk, unicode(item)) for item in Esdo.objects.using(name_db).all()]

	class Meta:
		model = Iva
		fields = "__all__"
		exclude = ["civa"]
		widgets = {
			'cesdo':forms.Select(attrs={'class':'form-control','required':''}),
			'niva':forms.TextInput(attrs={'class':'form-control','required':True}),
			'poriva':forms.NumberInput(attrs={'class':'form-control','required':True,'step':'0.01'}),
			'idtira':forms.TextInput(attrs={'class':'form-control','required':True}),
		}
		labels = {
			'civa':'Código Interno',
			'niva':'Nombre',
			'poriva':'Porcentaje',
			'idtira':'Id Tirilla',
			'cesdo':'Estado',
		}

class RegivaForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(RegivaForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Regiva
		fields = "__all__"
		exclude = ["cregiva"]
		widgets = {
			'nregiva':forms.TextInput(attrs={'class':'form-control','required':True}),
		}
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

class CommonForm(forms.Form):
	def __init__(self, using='', *args, **kwargs):
		super(CommonForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].choices = [(item.pk, unicode(item)) for item in Esdo.objects.using(name_db).all()]
		self.fields['group'].choices = [(item.pk, unicode(item)) for item in Gpo.objects.using(name_db).all()]
		self.fields['carlos'].choices = [(item.pk, unicode(item)) for item in Arlo.objects.using(name_db).all()]

	cesdo = forms.ModelChoiceField(queryset=Esdo.objects.all())
	group = forms.ModelChoiceField(
		widget=forms.Select(attrs={'class':'form-control'}),
		queryset=Gpo.objects.all()
	)
	carlos = forms.ModelChoiceField(
		widget=forms.NumberInput(attrs={'class':'form-control'}),
		queryset=Arlo.objects.all()
	)
	
	widgets = {}
