# -*- encoding: utf-8 -*-
from infa_web.parameters import ManageParameters
from infa_web.apps.articulos.models import *
from django import forms
from .models import *

class InventoryForm(forms.Form):
	codigo = forms.CharField(label = 'Codigo', widget = forms.TextInput(attrs = {'class': 'form-control', 'required': True, 'readonly': True}))

class InventoryReportStocksForm(forms.Form):
	nota_inicial = forms.CharField(label = 'Nota Inicial', widget = forms.TextInput(attrs = {'class': 'form-control', 'readonly': True, 'required': True, 'title': 'Debe agregar un inventario inicial en parametros'}))
	fecha_nota_inicial = forms.CharField(label = 'Fecha Nota Inicial', widget = forms.TextInput(attrs = {'class': 'form-control', 'readonly': True, 'required': True, 'title': 'Debe agregar un inventario inicial en parametros'}))
	fecha_final = forms.CharField(label = 'Fecha Final', widget = forms.TextInput(attrs = {'class': 'form-control date', 'required': True}))
	group_report = forms.ChoiceField(choices = [('G', 'Grupos'), ('M', 'Marcas')], initial = ('G'), label = 'Agrupar por:', widget = forms.RadioSelect())
	type_report = forms.MultipleChoiceField(choices = [('1', 'Guardar Existencias'), ('2', 'Mostrar Cantidades en Ceros'), ('3', 'Recalcular Entradas y Salidas')], label = 'Realizar:', widget = forms.CheckboxSelectMultiple())
	grupos = forms.ChoiceField(label = 'Grupos', choices = [('', 'Seleccione un Grupo'), ('ALL', 'Todos los Grupos')]+[(x.pk, x.ngpo) for x in Gpo.objects.all()], widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))
	marcas = forms.ChoiceField(label = 'Marcas', choices = [('', 'Seleccione una Marca'), ('ALL', 'Todos los Marcas')]+[(x.pk, x.nmarca) for x in Marca.objects.all()], widget = forms.Select(attrs = {'class': 'form-control'}))

	def __init__(self, *args, **kwargs):
			super(InventoryReportStocksForm, self).__init__(*args, **kwargs)
			manageParameters = ManageParameters()
			try:
				invini = Invinicab.objects.get(pk = manageParameters.get_param_value("initial_note"))
				self.fields['nota_inicial'].initial = invini.cii
				self.fields['fecha_nota_inicial'].initial = invini.fii
			except Invinicab.DoesNotExist:
				self.fields['nota_inicial'].initial = ''
				self.fields['fecha_nota_inicial'].initial = ''