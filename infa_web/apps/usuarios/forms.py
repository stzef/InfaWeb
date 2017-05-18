# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from infa_web.apps.base.models import Esdo, Caja,Sucursales, Talo
from django.contrib.auth.models import Group

class loginForm(forms.Form):
	username = forms.CharField(error_messages={'required': 'Ingresa tu Usuario, '},widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'nombre de usuario','autofocus':''}))
	password = forms.CharField(error_messages={'required': 'Ingresa tu Contraseña'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}))

	def auth_user(self, request_bd):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username = username, password = password, request_bd = request_bd)
		return user

class ManageUsers(forms.Form):
	def __init__(self,using='', *args, **kwargs):
		super(ManageUsers, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()
		self.fields['csucur'].queryset = Sucursales.objects.using(name_db).all()
		self.fields['ccaja'].queryset = Caja.objects.using(name_db).all()
		self.fields['ctalo'].queryset = Talo.objects.using(name_db).all()
		self.fields['auth_cgrupo'].queryset = Group.objects.using(name_db).all()

	username = forms.CharField(
		label='Usuario',
		error_messages={'required': 'Ingresa tu Usuario, '},
		widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'Nombre de usuario','required':True,})
	)
	password = forms.CharField(
		label='Contraseña',
		error_messages={'required': 'Ingresa tu Contraseña'},
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña','required':True,})
	)
	cpassword = forms.CharField(
		label='Confirmar Contraseña',
		error_messages={'required': 'Ingresa tu Contraseña'},
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirmar Contraseña','required':True,})
	)
	email = forms.CharField(
		label='Correo',
		error_messages={'required': 'Ingresa tu Contraseña'},
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo','required':True,})
	)
	telefono = forms.CharField(
		label='Telefono',
		error_messages={'required': 'Telefono'},
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'})
	)
	direccion = forms.CharField(
		label='Direccion',
		error_messages={'required': 'Direccion'},
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion'})
	)
	first_name = forms.CharField(
		label='Nombres',
		error_messages={'required': ''},
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres','required':True,})
	)

	factivacion = forms.CharField(
		label='Fecha Activacion',
		error_messages={'required': ''},
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha Activacion'})
	)
	fdesactivacion = forms.CharField(
		label='Fecha Desactivacion',
		error_messages={'required': ''},
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha Desactivacion','required':True,})
	)
	last_name = forms.CharField(
		label='Apellidos',
		error_messages={'required': ''},widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos','required':True,})
	)
	cesdo = forms.ModelChoiceField(
		label='Estado',
		widget=forms.Select(attrs={'class':'form-control','required':True,}),
		queryset=Esdo.objects.all()
	)
	ccaja = forms.ModelChoiceField(
		label='Caja',
		widget=forms.Select(attrs={'class':'form-control','required':True,}),
		queryset=Caja.objects.all()
	)
	csucur = forms.ModelChoiceField(
		label='Sucursal',
		widget=forms.Select(attrs={'class':'form-control','required':True,}),
		queryset=Sucursales.objects.all()
	)
	ctalo = forms.ModelChoiceField(
		label='Talonario',
		widget=forms.Select(attrs={'class':'form-control','required':True,}),
		queryset=Talo.objects.all()
	)
	auth_cgrupo = forms.ModelChoiceField(
		label='Grupo',
		widget=forms.Select(attrs={'class':'form-control','required':True,}),
		queryset=Group.objects.all()
	)

	widgets = {}
