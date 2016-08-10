from django import forms
from infa_web.apps.articulos.models import *

class Article(forms.ModelForm):
	class Meta:
		model = Arlo
		fields = "__all__"
		exclude = ["citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3"]
		widgets = {
			'carlos':forms.NumberInput(attrs={'class':'form-control','required':''}),
			'cbarras': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Codigo de Barras','required':''}),
			'ncorto': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Corto','required':''}),
			'nlargo': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Largo'}),
		}
		labels = {
			'carlos': 'Cod. Articulo',
			'cbarras': 'Codigo de Barras',
			'ncorto': 'Nombre Corto',
			'nlargo': 'Nombre Largo',
			'cgpo': 'Grupo'
		}
