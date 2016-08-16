from django import forms
from infa_web.apps.articulos.models import *

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Arlo
		fields = "__all__"
		exclude = ["citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3"]
		widgets = {
			'cgpo':forms.Select(attrs={'class':'form-control','required':''}),
			'cesdo' : forms.Select(attrs={'class': 'form-control','required':''}),
			'ciudad' : forms.Select(attrs={'class': 'form-control','required':''}),
			'ivas_civa' : forms.Select(attrs={'class': 'form-control','required':''}),
			'citerce1' : forms.Select(attrs={'class': 'form-control','required':''}),
			'citerce2' : forms.Select(attrs={'class': 'form-control','required':''}),
			'citerce3' : forms.Select(attrs={'class': 'form-control','required':''}),
			'cmarca' : forms.Select(attrs={'class': 'form-control','required':''}),
			'cubica' : forms.Select(attrs={'class': 'form-control','required':''}),
			'ctiarlo' : forms.Select(attrs={'class': 'form-control','required':''}),

			'ncorto' : forms.TextInput(attrs={'required':True}),
			'nlargo' : forms.TextInput(attrs={'required':True}),
			'refe' : forms.TextInput(attrs={'required':True}),

			'cbarras' : forms.NumberInput(attrs={'class': 'form-control','step':'1'}),
			'mesesgara' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'1'}),
			'vcosto' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01'}),
			'stomin' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01'}),
			'stomax' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01'}),
			'canti' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01'}),
			'porult1':forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01'}),
			'porult2':forms.NumberInput(attrs={'class': 'form-control','step':'0.01'}),
			'porult3':forms.NumberInput(attrs={'class': 'form-control','step':'0.01'}),
			'porult4':forms.NumberInput(attrs={'class': 'form-control','step':'0.01'}),
			'porult5':forms.NumberInput(attrs={'class': 'form-control','step':'0.01'}),
			'porult6':forms.NumberInput(attrs={'class': 'form-control','step':'0.01'}),
			'pvta1': forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01'}),
			'pvta2': forms.NumberInput(attrs={'class': 'form-control','step':'0.01'}),
			'pvta3': forms.NumberInput(attrs={'class': 'form-control','step':'0.01'}),
			'pvta4': forms.NumberInput(attrs={'class': 'form-control','step':'0.01'}),
			'pvta5': forms.NumberInput(attrs={'class': 'form-control','step':'0.01'}),
			'pvta6': forms.NumberInput(attrs={'class': 'form-control','step':'0.01'}),

			'foto1':forms.FileInput(attrs={'class': 'form-control'}),
			'foto2':forms.FileInput(attrs={'class': 'form-control'}),
			'foto3':forms.FileInput(attrs={'class': 'form-control'})
		}
		labels = {
			'carlos':'Codigo Interno',
			'cbarras':'Codigo de Barras',
			'cgpo':'Grupo',
			'ncorto':'Nombre Corto',
			'nlargo':'Descripcion',
			'canti':'Cantidad',
			'vcosto':'Costo',
			'ifcostear':'Costear',
			'ifpvfijo':'Precio Venta Fijo',
			'cesdo':'Estado',
			'ciudad':'Ciudad',
			'ctiarlo':'Tipo de Articulo',
			'ivas_civa':'IVA',
			'stomin':'Stock Minimo',
			'stomax':'Stock Maximo',
			'pvta1':'Precio Venta 1',
			'pvta2':'Precio Venta 2',
			'pvta3':'Precio Venta 3',
			'pvta4':'Precio Venta 4',
			'pvta5':'Precio Venta 5',
			'pvta6':'Precio Venta 6',
			'citerce1':'',
			'vcosto1':'',
			'fcosto1':'',
			'citerce2':'',
			'vcosto2':'',
			'fcosto2':'',
			'citerce3':'',
			'vcosto3':'',
			'fcosto3':'',
			'ifedinom':'Nombre Editable',
			'refe':'Referencia',
			'cmarca':'Marca',
			'ifdesglo':'Desglozado',
			'mesesgara':'Garantia(Meses)',
			'cubica':'Ubicacion',
			'porult1':'Porcentaje 1',
			'porult2':'Porcentaje 2',
			'porult3':'Porcentaje 3',
			'porult4':'Porcentaje 4',
			'porult5':'Porcentaje 5',
			'porult6':'Porcentaje 6',
			'foto1':'Foto 1',
			'foto2':'Foto 2',
			'foto3':'Foto 3'
		}

class GpoForm(forms.ModelForm):
	class Meta:
		model = Gpo
		fields = "__all__"
		widgets = {
			'cesdo' : forms.Select(attrs={'class': 'form-control','required':''}),
		}
		labels = {
			'cgpo' : 'Codigo Interno',
			'ngpo' : 'Nombre',
			'cesdo' : 'Estado'
		}

class BreakdownArticleForm(forms.ModelForm):
	class Meta:
		model = Arlosdesglo
		fields = "__all__"
		exclude = ["arlosp"]
		widgets = {
			'cesdo' : forms.Select(attrs={'class': 'form-control','required': True}),
			'carlosglo' : forms.Select(attrs={'class': 'form-control','required': True}),
		}
		labels = {
			"carlosp":"",
			"itglo":"",
			"carlosglo":"",
			"cantiglo":"",
			"costoglo":"",
			"vtoglo":"",
			"cesdo":"",
		}

class BrandForm(forms.ModelForm):
	class Meta:
		model = Marca
		fields = "__all__"
		exclude = ["cmarca"]
		widgets = {
			'cesdo' : forms.Select(attrs={'class': 'form-control','required':''}),
		}
		labels = {
			'cmarca' : 'Codigo Interno',
			'nmarca' : 'Nombre',
			'cesdo' : 'Estado'
		}

class TiarlosForm(forms.ModelForm):
	class Meta:
		model = Tiarlos
		fields = "__all__"
		exclude = ["ctiarlos"]
		widgets = {}
		labels = {
			'ctiarlos' : 'Codigo Interno',
			'ntiarlos' : 'Nombre',
		}
