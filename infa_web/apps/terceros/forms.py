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
			'ape1':forms.TextInput(attrs={'class':'form-control','required':True}),
			'ape2':forms.TextInput(attrs={'class':'form-control','required':True}),
			'nom1':forms.TextInput(attrs={'class':'form-control','required':True}),
			'nom2':forms.TextInput(attrs={'class':'form-control','required':True}),
			'sigla':forms.TextInput(attrs={'class':'form-control','required':True}),
			'nomegre':forms.TextInput(attrs={'class':'form-control','required':True}),
			'replegal':forms.TextInput(attrs={'class':'form-control','required':True}),
			'dirterce':forms.TextInput(attrs={'class':'form-control','required':True}),
			'telterce':forms.NumberInput(attrs={'class':'form-control','required':True}),
			'faxterce':forms.TextInput(attrs={'class':'form-control','required':True}),
			'email':forms.EmailInput(attrs={'class':'form-control','required':True}),
			'contacto':forms.TextInput(attrs={'class':'form-control','required':True}),
			'topcxc':forms.NumberInput(attrs={'class':'form-control','required':True,'step':'0.01'}),
			'ndiacxc':forms.TextInput(attrs={'class':'form-control','required':True}),
			'clipre':forms.TextInput(attrs={'class':'form-control','required':True}),
			'fnaci':forms.DateInput(attrs={'class':'form-control','required':True}),
			'naju':forms.TextInput(attrs={'class':'form-control','required':True}),
			'ordenruta':forms.NumberInput(attrs={'class':'form-control','required':True}),
		}
		labels = {
			'citerce':'Codigo Interno',
			'idterce':'Identificacion',
			'dv':'DV',
			'ctiide':'Tipo Identificaion',
			'rasocial':'Razon Social',
			'nomcomer':'Nombre Comercial',
			'ape1':'Apellido 1',
			'ape2':'Apellido 2',
			'nom1':'Nombre 1',
			'nom2':'Nombre 2',
			'sigla':'Sigla',
			'replegal':'Representante Legal',
			'dirterce':'Dirreccion',
			'telterce':'Telefono',
			'faxterce':'Fax',
			'ciudad':'Ciudad',
			'email':'Correo Electronico',
			'contacto':'COntacto',
			'cregiva':'Regimen de IVA',
			'cautorre':'Autorretenedor',
			'cesdo':'Estado',
			'cvende':'Vendedor',
			'topcxc':'Tope Cartera por Cobrar',
			'czona':'Zona',
			'clipre':'Lista de Precio', # default 1
			'fnaci':'Fecha de Nacimiento',
			'cruta':'Ruta',
			'ordenruta':'Orden Ruta',
			'cpersona':'Tipo de Persona',
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
			'cautorre':'Codigo Interno',
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
			'cruta':'Codigo Interno',
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
			'cruta':'Codigo Interno',
			'nzona':'Nombre',
			'cesdo':'Estado',
		}
