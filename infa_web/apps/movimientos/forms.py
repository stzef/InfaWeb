# -*- coding: utf-8 -*-
from django import forms 
from infa_web.apps.movimientos.models import *
from infa_web.apps.inventarios.models import *
from infa_web.apps.terceros.models import *
from infa_web.parameters import ManageParameters

class InputMovementForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(InputMovementForm, self).__init__(*args, **kwargs)
		name_db = using
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()
		self.fields['citerce'].queryset = Tercero.objects.using(name_db).all()
		self.fields['ctimo'].queryset = Timo.objects.using(name_db).all()
		self.fields['cbode0'].queryset = Bode.objects.using(name_db).all()
		self.fields['cbode1'].queryset = Bode.objects.using(name_db).all()

		manageParameters = ManageParameters(name_db)
		default_movement = manageParameters.get_param_value("default_movement_for_input_bills")
		self.fields['ctimo'].queryset = Timo.objects.using(name_db).filter(ctimo__startswith=PREFIJO_MOVIMIENTOS_ENTRADA)
		self.fields['ctimo'].initial = default_movement

	class Meta:
		model = Mven
		fields = "__all__"
		widgets = { 
			'cesdo':forms.Select(attrs={'class':'form-control','required':True}),
			'citerce' : forms.Select(attrs={'class':'form-control','required':True,'value':DEFAULT_TERCERO}),
			'ctimo' : forms.Select(attrs={'class':'form-control','required':True}),
			'cbode0' : forms.Select(attrs={'class':'form-control','required':True}),
			'cbode1' : forms.Select(attrs={'class':'form-control','required':True}),
			'docrefe' : forms.TextInput(attrs={'class':'form-control','max_length':10,'required':True}),
			'descri' : forms.TextInput(attrs={'class':'form-control','max_length':250}),
			'detaanula' : forms.TextInput(attrs={'class':'form-control','max_length':250}),
			'vttotal' : forms.NumberInput(attrs={'class': 'form-control app-input-important','required':True,'step':'1','min':0,'data-if-currency':'true'}),
			'cmven' : forms.NumberInput(attrs={'class': 'form-control'}),
			'fmven':forms.DateInput(attrs={'class':'form-control date','required':True}),
		}
		labels = {
			'cesdo':'Estado',
			'citerce':'Tercero',
			'ctimo':'Movimiento',
			'cbode0':'Bodega',
			'cbode1':'Bodega',
			'docrefe':'Doc Refe',
			'descri':'Descripcion',
			'detaanula':'',
			'vttotal':'Valor Total',
			'cmven':'Código Interno',
			'fmven':'Fecha',
		}

class OutputMovementForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(OutputMovementForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()
		self.fields['citerce'].queryset = Tercero.objects.using(name_db).all()
		self.fields['ctimo'].queryset = Timo.objects.using(name_db).all()
		self.fields['cbode0'].queryset = Bode.objects.using(name_db).all()
		self.fields['cbode1'].queryset = Bode.objects.using(name_db).all()

		manageParameters = ManageParameters(name_db)
		default_movement = manageParameters.get_param_value("default_movement_for_output_bills")
		self.fields['ctimo'].queryset = Timo.objects.using(name_db).filter(ctimo__startswith=PREFIJO_MOVIMIENTOS_SALIDA)
		self.fields['ctimo'].initial = default_movement
		
	class Meta:
		model = Mvsa
		fields = "__all__"
		widgets = {
			'cesdo':forms.Select(attrs={'class':'form-control','required':True}),
			'citerce' : forms.Select(attrs={'class':'form-control','required':True,'value':DEFAULT_TERCERO}),
			'ctimo' : forms.Select(attrs={'class':'form-control','required':True}),
			'cbode0' : forms.Select(attrs={'class':'form-control','required':True}),
			'cbode1' : forms.Select(attrs={'class':'form-control','required':True}),
			'docrefe' : forms.TextInput(attrs={'class':'form-control','max_length':10,'required':True}),
			'descri' : forms.TextInput(attrs={'class':'form-control','max_length':250}),
			'detaanula' : forms.TextInput(attrs={'class':'form-control','max_length':250}),
			'vttotal' : forms.NumberInput(attrs={'class': 'form-control app-input-important','required':True,'step':'1','min':0,'data-if-currency':'true'}),
			'cmvsa' : forms.NumberInput(attrs={'class': 'form-control'}),
			'fmvsa':forms.DateInput(attrs={'class':'form-control date','required':True}),
		}
		labels = {
			'cesdo':'Estado',
			'citerce':'Tercero',
			'ctimo':'Movimiento',
			'cbode0':'Bodega',
			'cbode1':'Bodega',
			'docrefe':'Doc Refe',
			'descri':'Descripcion',
			'detaanula':'',
			'vttotal':'Valor Total',
			'cmvsa':'Código Interno',
			'fmvsa':'Fecha',
		}

class InputMovementDetailForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(InputMovementDetailForm, self).__init__(*args, **kwargs)

		name_db = using

		self.fields['cmven'].queryset = Mven.objects.using(name_db).all()
		self.fields['carlos'].queryset = Arlo.objects.using(name_db).all()

	class Meta:
		model = Mvendeta
		fields = "__all__"
		widgets = {
			'cmven':forms.Select(attrs={'class':'form-control'}),
			'it':forms.NumberInput(attrs={'class': 'form-control','required':True,'min':0}),
			'carlos':forms.Select(attrs={'class':'form-control','required':True}),
			#'citerce':forms.Select(attrs={'class':'form-control','required':True}),
			'nlargo':forms.TextInput(attrs={'class':'form-control'}),
			'canti':forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'1','min':0}),
			'vunita':forms.TextInput(attrs={'class': 'form-control input-currency','required':True,'min':0,'step':'0.01','data-if-currency':'true'}),
			'vtotal':forms.TextInput(attrs={'class': 'form-control input-currency','required':True,'min':0,'step':'0.01','data-if-currency':'true'}),
		}
		labels = {
			'cmven':'Codigo M Entrada',
			'it':'Item',
			'carlos':'Articulo',
			#'citerce':'Tercero',
			'nlargo':'Nombre Largo',
			'canti':'Cantidad',
			'vunita':'V Unitario',
			'vtotal':'V Total',
		}

class OutputMovementDetailForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(OutputMovementDetailForm, self).__init__(*args, **kwargs)

		name_db = using

		self.fields['cmvsa'].queryset = Mvsa.objects.using(name_db).all()
		self.fields['carlos'].queryset = Arlo.objects.using(name_db).all()

	class Meta:
		model = Mvsadeta
		fields = "__all__"
		widgets = {
			'cmvsa':forms.Select(attrs={'class':'form-control'}),
			'it':forms.NumberInput(attrs={'class': 'form-control','required':True,'min':0}),
			'carlos':forms.Select(attrs={'class':'form-control','required':True}),
			#'citerce':forms.Select(attrs={'class':'form-control','required':True}),
			'nlargo':forms.TextInput(attrs={'class':'form-control'}),
			'canti':forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'1','min':0}),
			'vunita':forms.TextInput(attrs={'class': 'form-control input-currency','required':True,'step':'0.01','min':0,'data-if-currency':'true'}),
			'vtotal':forms.TextInput(attrs={'class': 'form-control input-currency','required':True,'step':'0.01','min':0,'data-if-currency':'true'}),
		}
		labels = {
			'cmvsa':'Codigo M Entrada',
			'it':'Item',
			'carlos':'Articulo',
			#'citerce':'Tercero',
			'nlargo':'Nombre Largo',
			'canti':'Cantidad',
			'vunita':'V Unitario',
			'vtotal':'V Total',
		}

class ProccessCostingAndStock(forms.Form):
	nota_inicial = forms.CharField(label = 'Nota Inicial', widget = forms.TextInput(attrs = {'class': 'form-control', 'readonly': True}))
	fecha_nota_inicial = forms.CharField(label = 'Fecha Nota Inicial', widget = forms.TextInput(attrs = {'class': 'form-control date', 'readonly': True}))
	fecha_final = forms.CharField(label = 'Fecha Final', widget = forms.TextInput(attrs = {'class': 'form-control date', 'required': True}))

	def __init__(self, using='', *args, **kwargs):
		super(ProccessCostingAndStock, self).__init__(*args, **kwargs)

		name_db = using
		#name_db = "db_1"

		manageParameters = ManageParameters(name_db)
		try:
			invini = Invinicab.objects.using(name_db).get(pk = manageParameters.get_param_value("initial_note"))
			self.fields['nota_inicial'].initial = invini.cii
			self.fields['fecha_nota_inicial'].initial = invini.fii
		except Invinicab.DoesNotExist:
			self.fields['nota_inicial'].initial = ''
			self.fields['fecha_nota_inicial'].initial = ''

class CarteraSearchForm(forms.Form):
	fecha_inicio = forms.CharField(label = 'Fecha Inicio', widget = forms.TextInput(attrs = {'class': 'form-control date', 'required': True}))
	fecha_fin = forms.CharField(label = 'Fecha Fin', widget = forms.TextInput(attrs = {'class': 'form-control date', 'required': True}))
	tercero = forms.ChoiceField(label = 'Tercero', widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))

	def __init__(self, *args, **kwargs):
		fecha_inicio = kwargs.pop('fecha_inicio', None)
		fecha_fin = kwargs.pop('fecha_fin', None)
		tercero = kwargs.pop('tercero', None)
		request_db = kwargs.pop('request_db', None)
		super(CarteraSearchForm, self).__init__(*args, **kwargs)
		self.fields['tercero'].choices = [('', 'Seleccione una opcion')]+[('all', 'Todos')]+[(x.pk, x.nameFull()) for x in Tercero.objects.using(request_db).all().order_by('ape1')]
		if fecha_inicio: self.fields['fecha_inicio'].initial = fecha_inicio
		if fecha_fin: self.fields['fecha_fin'].initial = fecha_fin
		if tercero: self.fields['tercero'].initial = tercero

class MoviForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(MoviForm, self).__init__(*args, **kwargs)

		name_db = using

		self.fields['ctimo'].queryset = Timo.objects.using(name_db).all()
		self.fields['citerce'].queryset = Tercero.objects.using(name_db).all()
		self.fields['cesdo'].queryset = Esdo.objects.using(name_db).all()
		self.fields['ccaja'].queryset = Caja.objects.using(name_db).all()

	class Meta:
		model = Movi
		fields = "__all__"
		widgets = { 
			'ctimo' : forms.Select(attrs={'class':'form-control','required':True}),
			'citerce' : forms.Select(attrs={'class':'form-control','required':True}),
			'cesdo' : forms.Select(attrs={'class':'form-control','required':True}),
			'ccaja' : forms.Select(attrs={'class':'form-control','required':True}),
			#'civa' : forms.Select(attrs={'class':'form-control','required':True}),
			'fmovi' : forms.DateInput(attrs={'class':'form-control date','required':True}),
			'fmovifin' : forms.DateInput(attrs={'class':'form-control date','required':True}),
			#'ndiadeu' : forms.NumberInput(attrs={'class': 'form-control'}),
			#'ndiacobro' : forms.NumberInput(attrs={'class': 'form-control'}),
			'cmovi' : forms.TextInput(attrs={'class':'form-control'}),
			'descrimovi' : forms.TextInput(attrs={'class':'form-control'}),
			'doctar' : forms.TextInput(attrs={'class':'form-control'}),
			'bantar' : forms.TextInput(attrs={'class':'form-control'}),
			'docch' : forms.TextInput(attrs={'class':'form-control'}),
			'banch' : forms.TextInput(attrs={'class':'form-control'}),
			'detaanula' : forms.TextInput(attrs={'class':'form-control'}),
			'vttotal' : forms.TextInput(attrs={'class': 'form-control input-currency','required':True}),
			'vefe' : forms.TextInput(attrs={'class': 'form-control input-currency','required':True}),
			'vtar' : forms.TextInput(attrs={'class': 'form-control input-currency','required':True}),
			'vch' : forms.TextInput(attrs={'class': 'form-control input-currency','required':True}),
			'ventre' : forms.TextInput(attrs={'class': 'form-control input-currency','required':True}),
			'vcambio' : forms.TextInput(attrs={'class': 'form-control input-currency','required':True}),
			#'vcuota' : forms.TextInput(attrs={'class': 'form-control input-currency','required':True}),
			'baseiva' : forms.TextInput(attrs={'class': 'form-control input-currency','required':True}),
			'vtiva' : forms.TextInput(attrs={'class': 'form-control input-currency','required':True}),
			#'vtsuma' : forms.TextInput(attrs={'class': 'form-control input-currency','required':True}),
			'vtdescu' : forms.TextInput(attrs={'class': 'form-control input-currency','required':True}),
			
		}
		labels = {
			'fmovi' :'Fecha Creacion',
			'fmovifin' :'',
			#'ndiadeu' :'',
			#'ndiacobro' :'',
			'cmovi' :'Codigo Movimiento',
			'descrimovi' :'Descripcion',
			'doctar' :'Doc Tarjeta',
			'bantar' :'Bando de la Tarjeta',
			'docch' :'Doc. Cheque',
			'banch' :'Banco Cheque',
			'detaanula' :'Detalle anulacion',
			'vttotal' :'Vr. Total',
			'vefe' :'Vr. Efectivo',
			'vtar' :'Vr. Tarjeta',
			'vch' :'Vr. Cheque',
			'ventre' :'Vr. Entregado',
			'vcambio' :'Vr. Cambio',
			#'vcuota' :'',
			'baseiva' :'Base IVA',
			'vtiva' :'Vr. Total IVA',
			#'vtsuma' :'',
			'vtdescu' :'Vr. Descuento',
			'ctimo' :'Tipo Movimiento',
			'citerce' :'Tercero',
			'cesdo' :'Estado',
			'ccaja' :'Caja',
			#'civa' :'IVA',
		}

class MoviDetailForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(MoviDetailForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cmovi'].queryset = Movi.objects.using(name_db).all()

	class Meta:
		model = Movideta
		fields = "__all__"
		widgets = { 
			'cmovi' : forms.Select(attrs={'class':'form-control','required':True}),
			'itmovi' : forms.TextInput(attrs={'class':'form-control','required':True}),
			'docrefe' : forms.TextInput(attrs={'class':'form-control'}),
			'detalle' : forms.TextInput(attrs={'class':'form-control','required':True}),
			'vmovi':forms.TextInput(attrs={'class': 'form-control input-currency','required':True,'min':0}),
			#'ccta' : forms.Select(attrs={'class':'form-control','required':True}),
			#'vdebi' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0,'data-if-currency':'true'}),
			#'vcredi' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0,'data-if-currency':'true'}),
			#'vinte' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0,'data-if-currency':'true'}),
			#'prointe' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0,'data-if-currency':'true'}),
			#'abo_capi' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0,'data-if-currency':'true'}),
			#'abo_pinte' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0,'data-if-currency':'true'}),
			#'ndiainte' : forms.NumberInput(attrs={'class': 'form-control','required':True,'min':0,}),
			#'vinte_cal' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0,'data-if-currency':'true'}),
			#'abo_inte' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0,'data-if-currency':'true'}),
			#'vcomi' : forms.NumberInput(attrs={'class': 'form-control','required':True,'step':'0.01','min':0,'data-if-currency':'true'}),

		}
		labels = {
			'cmovi' : 'Codigo Movimiento',
			'itmovi' : 'Item',
			'docrefe' : 'Doc Referencia',
			#'ccta' : '',
			'detalle' : 'Detalle',
			'vmovi' : 'Vr. Total',
			
			#'vdebi' : '',
			#'vcredi' : '',
			#'valor' : 'Valor',

			#'vinte' : '',
			#'prointe' : '',
			#'abo_capi' : '',
			#'abo_pinte' : '',
			#'ndiainte' : '',
			#'vinte_cal' : '',
			#'abo_inte' : '',
			#'vcomi' : '',
		}

class MovipagoForm(forms.ModelForm):
	def __init__(self, using='', *args, **kwargs):
		super(MovipagoForm, self).__init__(*args, **kwargs)

		name_db = using
		self.fields['cmpago'].widget.attrs.update({'required': True, 'class': 'form-control'})
		self.fields['cmpago'].queryset = MediosPago.objects.using(name_db).all()
		self.fields['banmpago'].widget.attrs.update({'required': True, 'class': 'form-control'})
		self.fields['cmovi'].queryset = Movi.objects.using(name_db).all()
		self.fields['banmpago'].queryset = Banfopa.objects.using(name_db).all()

	class Meta:
		model = Movipago
		fields = "__all__"
		widgets = {
			'cmovi' : forms.Select(attrs={'class':'form-control','required':True}),
			'it' : forms.TextInput(attrs={'class':'form-control','required':True}),
			'docmpago' : forms.TextInput(attrs={'class':'form-control'}),
			'vmpago' : forms.TextInput(attrs={'class': 'input-currency form-control','required':True,'step':'0.01','min':0}),
		}
		labels = {
			'cmovi' : 'Codigo Factura',
			'it' : 'Item',
			'cmpago' : 'Medio de Pago',
			'docmpago' : 'Doc. Medio Pago',
			'banmpago' : 'Ban. Medio Pago',
			'vmpago' : 'Valor Medio Pago',
		}
