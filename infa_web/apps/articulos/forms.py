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
		}
		labels = {
			'carlos':'Codigo Interno',
			'cbarras':'Codigo de Barras',
			'cgpo':'Grupo',
			'ncorto':'Nombre Corto',
			'nlargo':'Nombre Largo',
			'canti':'Cantidad',
			'vcosto':'Costo',
			'ifcostear':'Costear',
			'ifpvfijo':'Precio Venta Fijo',
			'cesdo':'Estado',
			'ciudad':'Ciudad',
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
