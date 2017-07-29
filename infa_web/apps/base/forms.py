# -*- coding: utf-8 -*-
from django import forms
from infa_web.apps.base.models import *
from infa_web.apps.articulos.models import *
from infa_web.apps.restaurante_comandas.models import Mesas

class ParametersForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(ParametersForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()

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
		self.fields['cdepar'].queryset = Departamento.objects.using(name_db).all()

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
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()

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
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()

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

class SucursalForm(forms.ModelForm):
	def __init__(self,using='', *args, **kwargs):
		super(SucursalForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()

	class Meta:
		model = Sucursales
		fields = "__all__"
		exclude = ["civa"]
		widgets = {
			'cesdo':forms.Select(attrs={'class':'form-control','required':''}),

			'csucur':forms.TextInput(attrs={'class':'form-control','required':True}),
			'nsucur':forms.TextInput(attrs={'class':'form-control','required':True,'step':'0.01'}),
			'dirsucur':forms.TextInput(attrs={'class':'form-control','required':True}),
			'telsucur':forms.TextInput(attrs={'class':'form-control','required':True}),
			'celsucur':forms.TextInput(attrs={'class':'form-control','required':True}),
		}
		labels = {
			'cesdo':'Estado',
			'csucur':'Código Interno',
			'nsucur':'Nombre',
			'dirsucur':'Direccion',
			'telsucur':'Telefono',
			'celsucur':'Celular',
		}

class CajaForm(forms.ModelForm):
	def __init__(self,using='', *args, **kwargs):
		super(CajaForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()
		self.fields['csucur'].queryset = Sucursales.objects.using(name_db).all()
		self.fields['cbode'].queryset = Bode.objects.using(name_db).all()
		self.fields['ctimocj'].queryset = Timo.objects.using(name_db).all()

	class Meta:
		model = Caja
		fields = "__all__"
		exclude = ["civa"]
		widgets = {
			'cesdo':forms.Select(attrs={'class':'form-control','required':''}),

			'ncaja' :forms.TextInput(attrs={'class':'form-control','required':True}),
			'caseri' :forms.TextInput(attrs={'class':'form-control','required':True}),

			'csucur' :forms.Select(attrs={'class':'form-control','required':''}),
			'ctimocj' :forms.Select(attrs={'class':'form-control','required':''}),
			'cbode' :forms.Select(attrs={'class':'form-control','required':''}),
		}
		labels = {
			'cesdo':'Estado',
			'ncaja':'Nombre',
			'caseri':'Serial Maquina',
			'csucur':'Sucursal',
			'ctimocj':'Movimiento',
			'cbode':'Bodega',
		}

class TaloForm(forms.ModelForm):
	def __init__(self,using='', *args, **kwargs):
		super(TaloForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()
		self.fields['csucur'].queryset = Sucursales.objects.using(name_db).all()
		self.fields['ctifopa'].queryset = Tifopa.objects.using(name_db).all()
		self.fields['ccaja'].queryset = Caja.objects.using(name_db).all()
		self.fields['ctimomvsa'].queryset = Timo.objects.using(name_db).all()

	class Meta:
		model = Talo
		fields = "__all__"
		exclude = []
		widgets = {


			"prefijo" : forms.TextInput(attrs={'class':'form-control','required':True}),
			"resodian" : forms.TextInput(attrs={'class':'form-control','required':True}),
			"nrepo" : forms.TextInput(attrs={'class':'form-control','required':True}),
			"descri" : forms.TextInput(attrs={'class':'form-control','required':True}),
			"prefi_real" : forms.TextInput(attrs={'class':'form-control','required':True}),

			"conse_ini" : forms.NumberInput(attrs={'class':'form-control','required':True}),
			"conse_fin" : forms.NumberInput(attrs={'class':'form-control','required':True}),
			"lar_conse" : forms.NumberInput(attrs={'class':'form-control','required':True}),
			"filas" : forms.NumberInput(attrs={'class':'form-control','required':True}),
			"ncotalo" : forms.NumberInput(attrs={'class':'form-control','required':True}),

			#ifmostrado = models.BooleanField()
			#ifpos = models.BooleanField()

			"csucur" : forms.Select(attrs={'class':'form-control','required':''}),
			"ctifopa" : forms.Select(attrs={'class':'form-control','required':''}),
			"cesdo" : forms.Select(attrs={'class':'form-control','required':''}),
			"ccaja" : forms.Select(attrs={'class':'form-control','required':''}),
			"ctimomvsa" : forms.Select(attrs={'class':'form-control','required':''}),

		}
		labels = {
			"prefijo" : "Prefijo",
			"resodian" : "Resolucion Impuesto",
			"nrepo" : "N Reporte",
			"descri" : "Descripcion",
			"prefi_real" : "Prefijo Real",

			"conse_ini" : "Consecutivo Inicial",
			"conse_fin" : "Consecutivo Final",
			"lar_conse" : "Lar Consecutivo",
			"filas" : "Numero Filas",
			"ncotalo" : "Ncotalo",

			#ifmostrado = models.BooleanField()
			#ifpos = models.BooleanField()

			"csucur" : "Sucursal",
			"ctifopa" : "",
			"cesdo" : "Estado",
			"ccaja" : "Caja",
			"ctimomvsa" : "Tipo Movimiento Salida",
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

	def __init__(self, using='', *args, **kwargs):
		super(IDTypeForm, self).__init__(*args, **kwargs)
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
	def __init__(self,using='', *args, **kwargs):
		super(CommonForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()
		self.fields['mesas'].queryset = Mesas.objects.using(name_db).all()
		self.fields['group'].queryset = Gpo.objects.using(name_db).all()
		self.fields['carlos'].queryset = Arlo.objects.using(name_db).all()
		self.fields['sucursales'].queryset = Sucursales.objects.using(name_db).all()

	cesdo = forms.ModelChoiceField(
		label='Estado',
		widget=forms.Select(attrs={'class':'form-control','required':True,}),
		queryset=Esdo.objects.all()
	)
	mesas = forms.ModelChoiceField(
		label='Mesa',
		widget=forms.Select(attrs={'class':'form-control','required':True,}),
		queryset=Mesas.objects.all()
	)
	sucursales = forms.ModelChoiceField(
		label='Sucursal',
		widget=forms.Select(attrs={'class':'form-control','required':True,}),
		queryset=Sucursales.objects.all()
	)
	group = forms.ModelChoiceField(
		label='Grupo',
		widget=forms.Select(attrs={'class':'form-control'}),
		queryset=Gpo.objects.all()
	)
	carlos = forms.ModelChoiceField(
		label='Articulo',
		widget=forms.NumberInput(attrs={'class':'form-control'}),
		queryset=Arlo.objects.all()
	)

	widgets = {}

