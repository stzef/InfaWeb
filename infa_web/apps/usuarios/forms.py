# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from infa_web.apps.base.models import Esdo

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

	username = forms.CharField(
		label='Usuario',
		error_messages={'required': 'Ingresa tu Usuario, '},
		widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'Nombre de usuario'})
	)
	password = forms.CharField(
		label='Contraseña',
		error_messages={'required': 'Ingresa tu Contraseña'},
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'})
	)
	cpassword = forms.CharField(
		label='Confirmar Contraseña',
		error_messages={'required': 'Ingresa tu Contraseña'},
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirmar Contraseña'})
	)
	email = forms.CharField(
		label='Correo',
		error_messages={'required': 'Ingresa tu Contraseña'},
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo'})
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
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Nombres'})
	)

	factivacion = forms.CharField(
		label='Fecha Activacion',
		error_messages={'required': ''},
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Fecha Activacion'})
	)
	fdesactivacion = forms.CharField(
		label='Fecha Desactivacion',
		error_messages={'required': ''},
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Fecha Desactivacion'})
	)
	last_name = forms.CharField(
		label='Apellidos',
		error_messages={'required': ''},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Apellidos'})
	)
	cesdo = forms.ModelChoiceField(
		label='Estado',
		widget=forms.Select(attrs={'class':'form-control','required':True,}),
		queryset=Esdo.objects.all()
	)

	widgets = {}
