from django import forms
from infa_web.apps.articulos.models import *

class addArticle(forms.ModelForm):
	class Meta:
		model = Arlo
		fields = ["carlos","cbarras","cgpo","ncorto","nlargo","canti","vcosto","ifcostear","ifpvfijo","cesdo","ciudad","ivas_civa","stomin","stomax","pvta1","pvta2","pvta3","pvta4","pvta5","pvta6","citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3","ifedinom","refe","cmarca","ifdesglo","mesesgara","cubica","porult1","porult2","porult3","porult4","porult5","porult6","foto1","foto2","foto3",]
		"""widgets = {
			'categoria':forms.Select(attrs={'class':'form-control','required':''}),
			'nBienServicio': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cual es tu bien/servicio','required':''}),
			'descripcion': forms.Textarea(attrs={'rows': 2, 'class':'form-control','placeholder':'Describe tu bien/servicio','required':''}),
			'precio': forms.NumberInput(attrs={'class':'form-control','min':'0'}),
		}
		
		labels = {
			'categoria': ('Categoria'),
			'nBienServicio': ('Bien/Servicios'),
		}
		"""
