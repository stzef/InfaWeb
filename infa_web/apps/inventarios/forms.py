# -*- encoding: utf-8 -*-
from infa_web.parameters import ManageParameters
from infa_web.apps.articulos.models import *
from django import forms
from .models import *

class InventoryForm(forms.Form):
	def __init__(self, using='', *args, **kwargs):
		super(InventoryForm, self).__init__(*args, **kwargs)

	codigo = forms.CharField(label = 'Codigo', widget = forms.TextInput(attrs = {'class': 'form-control', 'required': True, 'readonly': True}))

class InventoryReportStocksForm(forms.Form):

	nota_inicial = forms.CharField(label = 'Nota Inicial', widget = forms.TextInput(attrs = {'class': 'form-control', 'readonly': True}))
	fecha_nota_inicial = forms.CharField(label = 'Fecha Nota Inicial', widget = forms.TextInput(attrs = {'class': 'form-control', 'readonly': True}))
	fecha_final = forms.CharField(label = 'Fecha Final', widget = forms.TextInput(attrs = {'class': 'form-control date', 'required': True}))
	group_report = forms.ChoiceField(choices = [('G', 'Grupos'), ('M', 'Marcas')], initial = ('G'), label = 'Agrupar por:', widget = forms.RadioSelect())
	type_report = forms.MultipleChoiceField(choices = [('1', 'Mostrar Cantidades en Ceros'), ('2', 'Recalcular Entradas y Salidas')], label = 'Realizar:', widget = forms.CheckboxSelectMultiple())
	grupos = forms.ChoiceField(label = 'Grupos', widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))
	marcas = forms.ChoiceField(label = 'Marcas', widget = forms.Select(attrs = {'class': 'form-control'}))

	def __init__(self, using='', *args, **kwargs):
		super(InventoryReportStocksForm, self).__init__(*args, **kwargs)
		
		name_db = using
		self.fields['grupos'].choices = [('', 'Seleccione un Grupo'), ('ALL', 'Todos los Grupos')]+[(x.pk, x.ngpo) for x in Gpo.objects.using(name_db).all()]
		self.fields['marcas'].choices = [('', 'Seleccione una Marca'), ('ALL', 'Todos los Marcas')]+[(x.pk, x.nmarca) for x in Marca.objects.using(name_db).all()]
		manageParameters = ManageParameters(name_db)
		try:
			invini = Invinicab.objects.using(name_db).get(pk = manageParameters.get_param_value("initial_note"))
			self.fields['nota_inicial'].initial = invini.cii
			self.fields['fecha_nota_inicial'].initial = str(invini.fii.year)+'-'+str(invini.fii.month)+'-'+str(invini.fii.day)
		except Invinicab.DoesNotExist:
			self.fields['nota_inicial'].initial = ''
			self.fields['fecha_nota_inicial'].initial = ''

class InventoryReportForm(forms.Form):
	nota_inicial = forms.CharField(label = 'Nota Inicial', widget = forms.TextInput(attrs = {'class': 'form-control', 'readonly': True}))
	fecha_nota_inicial = forms.CharField(label = 'Fecha Creacion', widget = forms.TextInput(attrs = {'class': 'form-control', 'readonly': True}))
	fecha_actualizacion = forms.CharField(label = 'Fecha Ultima Actualizacion', widget = forms.TextInput(attrs = {'class': 'form-control', 'readonly': True}))
	estado = forms.CharField(label = 'Estado', widget = forms.TextInput(attrs = {'class': 'form-control', 'readonly': True}))
	grupo = forms.ChoiceField(label = 'Grupo', widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))
	order = forms.ChoiceField(choices = [('nlargo', 'Nombre'), ('carlos', 'Codigo')], initial = ('nlargo'), label = "Ordenar por", widget = forms.RadioSelect())
	type_report = forms.ChoiceField(choices = [('cant_vr', 'Cantidades y Vr Total')], initial = 'cant_vr', label = 'Tipo Reporte', widget = forms.RadioSelect())
	val_cero = forms.ChoiceField(choices = [('true', 'Mostrar valores en ceros')], label = "Visualizar", widget = forms.RadioSelect())

	def __init__(self, using='', *args, **kwargs):
		name_db = using

		invini = Invinicab.objects.using(name_db).get(pk = kwargs.pop('invini', None))
		super(InventoryReportForm, self).__init__(*args, **kwargs)
		self.fields['grupo'].choices = [('', 'Seleccione un Grupo'), ('ALL', 'Todos los Grupos')]+[(x.pk, x.ngpo) for x in Gpo.objects.using(name_db).all()]
		self.fields['nota_inicial'].initial = invini.cii
		self.fields['fecha_nota_inicial'].initial = invini.fii
		self.fields['fecha_actualizacion'].initial = invini.fuaii
		self.fields['estado'].initial = invini.cesdo.nesdo
