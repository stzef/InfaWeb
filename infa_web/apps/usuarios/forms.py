# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate

class loginForm(forms.Form):
	username = forms.CharField(error_messages={'required': 'Ingresa tu Usuario, '},widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'nombre de usuario','autofocus':''}))
	password = forms.CharField(error_messages={'required': 'Ingresa tu Contraseña'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}))

	def auth_user(self, request_bd):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username = username, password = password, request_bd = request_bd)
		return user