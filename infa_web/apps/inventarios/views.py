# -*- encoding: utf-8 -*-
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from reportlab.lib.styles import getSampleStyleSheet
from django.views.decorators.csrf import csrf_exempt


"""Falta Implementar FormView ?????????"""
from django.views.generic import FormView
from infa_web.custom.generic_views import CustomListView

from reportlab.lib.pagesizes import letter, inch
from infa_web.parameters import ManageParameters
from infa_web.routines import costing_and_stock
from infa_web.apps.articulos.models import *
from reportlab.lib.pagesizes import letter
from easy_pdf.views import PDFTemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from reportlab.lib import colors
from io import BytesIO
from .models import *
from .forms import *
import datetime
import json

def sum_invini(value):
	value_sum = str(int(value[3:])+1)
	cant_space = 5-int(len(value_sum))
	return 'II-'+(cant_space*'0')+value_sum

class InventoryView(FormView):
	template_name = 'inventarios/inventory.html'
	form_class = InventoryForm

	def get_context_data(self, **kwargs):
		context = super(InventoryView, self).get_context_data(**kwargs)
		context['title'] = 'Inventarios'
		return context

class InventoryListView(CustomListView):
	template_name = 'inventarios/list-inventory.html'
	model = Invinicab

	def get_context_data(self, **kwargs):
		context = super(InventoryListView, self).get_context_data(**kwargs)
		context['title'] = 'Lista de inventarios'
		return context

@csrf_exempt
def inventory_latest(request):
	response = {}
	c = 0
	response['data'] = {}
	response['esdo'] = {}
	response['val_tot'] = 0
	now = datetime.datetime.now()
	response['day'] = now.day
	response['month'] = now.month
	response['year'] = now.year
	response['hour'] = now.hour
	response['minute'] = now.minute

	response['ac_day'] = 0
	response['ac_month'] = 0
	response['ac_year'] = 0
	response['ac_hour'] = 0
	response['ac_minute'] = 0
	articulo = Tiarlos.objects.using(request.db).get(ntiarlos = 'ARTICULOS').pk
	try:
		value = Invinicab.objects.using(request.db).all().latest('pk')
		response['code'] = sum_invini(value.pk)
	except Invinicab.DoesNotExist:
		response['code'] = 'II-00001'
	cesdo = Esdo.objects.using(request.db).get(nesdo = 'ACTIVO')
	invini = Invinicab(cii = response['code'], cesdo = cesdo, vttotal = 0, fii = now)
	invini.save(using=request.db)
	"""
	for arlo in Arlo.objects.using(request.db).filter(ctiarlo = articulo):
		response['data'][c] = {}
		response['data'][c]['carlos'] = arlo.carlos
		response['data'][c]['cbarras'] = arlo.cbarras
		response['data'][c]['nlargo'] = arlo.nlargo
		response['data'][c]['ngpo'] = arlo.cgpo.ngpo
		response['data'][c]['canti'] = 0
		response['data'][c]['cancalcu'] = float(arlo.canti)
		response['data'][c]['vcosto'] = float(arlo.vcosto)
		c += 1
	"""
	c = 0
	for esdo in Esdo.objects.using(request.db).all():
		response['esdo'][c] = {}
		response['esdo'][c]['cesdo'] = esdo.cesdo
		response['esdo'][c]['nesdo'] = esdo.nesdo
		response['esdo'][c]['selected'] = 'selected' if esdo.nesdo == 'ACTIVO' else ''
		c += 1
	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def inventory_edit(request):
	response = {}
	c = 0
	response['data'] = {}
	response['arlo'] = {}
	response['esdo'] = {}
	value = Invinicab.objects.using(request.db).get(pk = request.POST.get('pk'))
	articulo = Tiarlos.objects.using(request.db).get(ntiarlos = 'ARTICULOS').pk
	value_extra = Arlo.objects.using(request.db).filter(ctiarlo = articulo).exclude(carlos__in = list(val.carlos.pk for val in value.invinideta_set.all()))
	response['val_tot'] = float(value.vttotal)
	response['day'] = value.fii.day
	response['month'] = value.fii.month
	response['year'] = value.fii.year
	response['hour'] = value.fii.hour
	response['minute'] = value.fii.minute
	if value.fuaii is not None:
		response['ac_day'] = value.fuaii.day
		response['ac_month'] = value.fuaii.month
		response['ac_year'] = value.fuaii.year
		response['ac_hour'] = value.fuaii.hour
		response['ac_minute'] = value.fuaii.minute
	else:
		response['ac_day'] = 0
		response['ac_month'] = 0
		response['ac_year'] = 0
		response['ac_hour'] = 0
		response['ac_minute'] = 0
	for arlo_extra in value_extra:
		response['arlo'][int(c)] = {
			'carlos': arlo_extra.carlos,
			'nlargo': arlo_extra.nlargo,
			'cbarras': arlo_extra.cbarras,
			'canti': 0,
			'vcosto': str(arlo_extra.vcosto).replace(",", "."),
			'cesdo': arlo_extra.cesdo.nesdo,
			'cmarca': arlo_extra.cmarca.nmarca,
			'cancalcu': str(arlo_extra.canti).replace(",", "."),
			'cgrupo': arlo_extra.cgpo.ngpo
		}
		c += 1
	c = 0
	for esdo in Esdo.objects.using(request.db).all():
		response['esdo'][c] = {
			'cesdo': esdo.cesdo,
			'nesdo': esdo.nesdo,
			'selected': 'selected' if esdo.cesdo == value.cesdo.cesdo else ''
		}
		c += 1
	response['count_extra'] = value_extra.count()
	return HttpResponse(json.dumps(response), "application/json")

def articles_list_invini(request):
	data_arlo = {}
	data_arlo['arlo'] = {}
	orderBy = request.GET.get('orderBy')
	cii = request.GET.get('cii')
	invini = Invinideta.objects.using(request.db).filter(cii = cii)
	if request.GET.get('buscarPor'):
		invini = invini.filter(carlos__nlargo__icontains = request.GET.get('buscarPor'))
	else:
		invini
	invini = Paginator(invini.order_by(orderBy), 10)
	page = request.GET.get('page')
	invini = invini.page(page)
	if len(invini.object_list) < 10:
		data_arlo['response'] = 0
	else:
		data_arlo['response'] = 1
	for queryset in invini:
		data_arlo['arlo'][queryset.carlos.pk] = {
			'carlos': queryset.carlos.pk,
			'nlargo': queryset.nlargo,
			'cbarras': queryset.carlos.cbarras,
			'canti': str(queryset.canti).replace(",", "."),
			'vcosto': str(queryset.vunita).replace(",", "."),
			'cesdo': queryset.carlos.cesdo.nesdo,
			'cmarca': queryset.carlos.cmarca.nmarca,
			'cancalcu': str(queryset.cancalcu).replace(",", "."),
			'cgrupo': queryset.carlos.cgpo.ngpo
		}
	return HttpResponse(json.dumps(data_arlo), content_type="application/json")

@csrf_exempt
def inventory_save(request):
	response = {}
	list_carlos = []
	response_data = json.loads(request.POST.get('data_r'))
	cii = request.POST.get('cii')
	val_tot = request.POST.get('val_tot')
	cesdo = Esdo.objects.using(request.db).get(cesdo = request.POST.get('cesdo'))
	fii = datetime.datetime.strptime(request.POST.get('fii'), '%d/%m/%Y %H:%M')
	try:
		invini = Invinicab.objects.using(request.db).get(cii = cii)
		invini.cesdo = cesdo
		invini.fuaii = datetime.datetime.now()
		invini.vttotal = float(val_tot)
		invini.fii = fii
		invini.save(using=request.db)
		for cii_deta in response_data:
			try:
				invini_deta = Invinideta.objects.using(request.db).get(cii = invini, carlos = cii_deta['carlos'])
				invini_deta.nlargo = cii_deta['nlargo']
				invini_deta.canti = float(cii_deta['canti'])
				invini_deta.vunita = float(cii_deta['vcosto'])
				invini_deta.vtotal = (float(cii_deta['canti']) * float(cii_deta['vcosto']))
				invini_deta.cancalcu = cii_deta['cancalcu']
				invini_deta.ajuent = cii_deta['ajuent']
				invini_deta.ajusal = cii_deta['ajusal']
				invini_deta.save(using=request.db)
			except Invinideta.DoesNotExist:
				carlos = Arlo.objects.using(request.db).get(carlos = cii_deta['carlos'])
				invini_deta = Invinideta(cii = invini, 
					carlos = carlos, 
					nlargo = cii_deta['nlargo'], 
					canti = cii_deta['canti'], 
					vunita = cii_deta['vcosto'], 
					vtotal = (float(cii_deta['canti']) * float(cii_deta['vcosto'])), 
					cancalcu = cii_deta['cancalcu'], 
					ajuent = cii_deta['ajuent'], 
					ajusal = cii_deta['ajusal']
				)
			invini_deta.save(using=request.db)
	except Invinicab.DoesNotExist:
		invini = Invinicab(cii = cii, cesdo = cesdo, vttotal = val_tot, fii = fii)
		invini.save(using=request.db)
		manageParameters = ManageParameters()
		sv_cant = False
		if manageParameters.get_param_value("initial_note") == '@':
			manageParameters.set_param_object("initial_note", cii)
			sv_cant = True
		for cii_deta in response_data:
			carlos = Arlo.objects.using(request.db).get(carlos = cii_deta['carlos'])
			list_carlos.append(carlos.pk)
			invini_deta = Invinideta(cii = invini, 
				carlos = carlos, 
				nlargo = cii_deta['nlargo'], 
				canti = cii_deta['canti'], 
				vunita = cii_deta['vcosto'], 
				vtotal = (float(cii_deta['canti']) * float(cii_deta['vcosto'])), 
				cancalcu = cii_deta['cancalcu'], 
				ajuent = cii_deta['ajuent'], 
				ajusal = cii_deta['ajusal']
			)
			invini_deta.save(using=request.db)
			if sv_cant is True:
				carlos.canti = cii_deta['cant']
				carlos.vcosto = cii_deta['vcosto']
				carlos.save(using=request.db)
		for carlos_falt in Arlo.objects.using(request.db).exclude(pk__in = list_carlos):
			invini_deta = Invinideta(cii = invini, 
									carlos = carlos_falt, 
									nlargo = carlos_falt.nlargo, 
									canti = 0, 
									vunita = carlos_falt.vcosto, 
									vtotal = 0, 
									cancalcu = carlos_falt.canti, 
									ajuent = 0, 
									ajusal = 0
							)
			invini_deta.save(using=request.db)
			if sv_cant is True:
				carlos_falt.canti = 0
				carlos_falt.vcosto = 0
				carlos_falt.save(using=request.db)
	response['code'] = cii
	return HttpResponse(json.dumps(response), "application/json")


@csrf_exempt
def inventory_save_extra(request):
	response = {}
	list_carlos = []
	cii = Invinicab.objects.using(request.db).get(pk = request.GET.get('cii'))
	response_data = json.loads(request.POST.get('data_r'))
	for cii_deta in response_data:
		carlos = Arlo.objects.using(request.db).get(carlos = response_data[cii_deta]['carlos'])
		invini_deta = Invinideta(cii = cii, 
								carlos = carlos, 
								nlargo = response_data[cii_deta]['nlargo'], 
								canti = 0, 
								vunita = float(response_data[cii_deta]['vcosto']), 
								vtotal = 0, 
								cancalcu = float(response_data[cii_deta]['cancalcu']), 
								ajuent = 0, 
								ajusal = 0
					)
		invini_deta.save(using=request.db)
	response['response'] = 'Exito al agregar nuevos articulos'
	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def get_name_arlo(request):
	response = {}
	c = 0
	response['data'] = {}
	articulo = Tiarlos.objects.using(request.db).get(ntiarlos = 'ARTICULOS').pk
	for arlo in Arlo.objects.using(request.db).filter(ctiarlo = articulo):
		response['data'][c] = {}
		response['data'][c]['carlos'] = arlo.carlos
		response['data'][c]['nlargo'] = arlo.nlargo.encode("utf-8")
		c += 1
	return HttpResponse(json.dumps(response), "application/json")

class InventoryReportStocks(FormView):
	template_name = 'inventarios/inventory-report-stocks.html'
	form_class = InventoryReportStocksForm

	def get_context_data(self, **kwargs):
		context = super(InventoryReportStocks, self).get_context_data(**kwargs)
		context['title'] = 'Reporte existencias inventarios'
		return context

class InventoryPDFStocks(PDFTemplateView):
	template_name = "inventarios/pdf_inventory_stock.html"

	def get_context_data(self, **kwargs):
		context = super(InventoryPDFStocks, self).get_context_data(**kwargs)
		data = self.request.GET
		type_report = data.getlist('type_report')
		costing_and_stock({'start_date': datetime.datetime.strptime(data.get('fecha_nota_inicial'), '%Y-%m-%d'), 'end_date': datetime.datetime.strptime(data.get('fecha_final'), '%Y-%m-%d')}, True) if '2' in type_report else ''
		context['invini'] = Invinicab.objects.using(self.request.db).get(pk = data.get('nota_inicial'))
		invinideta_set = Invinideta.objects.using(self.request.db).filter(cii = data.get('nota_inicial')).order_by('carlos__cgpo', 'carlos__carlos') if data.get('group_report') == 'G' else Invinideta.objects.using(self.request.db).filter(cii = data.get('nota_inicial')).order_by('carlos__cmarca', 'carlos__carlos')
		invinideta_set = invinideta_set.filter(carlos__cmarca = data.get('marcas')) if ((data.get('marcas') != 'ALL' and data.get('marcas') != '') and data.get('group_report') == 'M') else invinideta_set.filter(carlos__cgpo = data.get('grupos')) if ((data.get('grupos') != 'ALL' and data.get('grupos') != '') and data.get('group_report') == 'G') else invinideta_set
		context['invinideta_set'] = invinideta_set if '1' in type_report else invinideta_set.exclude(carlos__canti = 0.00)
		context['orientation'] = 'letter'
		context['data'] = data
		context['title'] = 'Existencias'
		return context

class InventoryReport(FormView):
	template_name = 'inventarios/inventory-report.html'
	form_class = InventoryReportForm

	def get_form_kwargs(self):
		kwargs = super(InventoryReport, self).get_form_kwargs()
		kwargs['invini'] = self.request.GET.get('invini')
		return kwargs

	def get_context_data(self, **kwargs):
		context = super(InventoryReport, self).get_context_data(**kwargs)
		context['title'] = 'Impresion de la nota del inventario inicial'
		return context

class InventoryPDF(PDFTemplateView):

	def get_template_names(self):
		return "inventarios/pdf_inventory_"+self.request.GET.get('type_report')+".html"

	def get_context_data(self, **kwargs):
		context = super(InventoryPDF, self).get_context_data(**kwargs)
		data = self.request.GET
		context['orientation'] = 'letter'
		context['invini'] = Invinicab.objects.using(self.request.db).get(pk = data.get('nota_inicial'))
		invinideta_set = Invinideta.objects.using(self.request.db).filter(cii = data.get('nota_inicial')).order_by('carlos__cgpo', 'carlos__'+data.get('order'))
		invinideta_set = invinideta_set.exclude(canti = 0) if data.get('val_cero') != 'true' else invinideta_set
		context['invinideta_set'] = invinideta_set.filter(carlos__cgpo = data.get('grupo')) if data.get('grupo') != 'ALL' and data.get('grupos') != '' else invinideta_set
		context['data'] = data
		context['title'] = 'Nota inicial '+data.get('nota_inicial')
		context['sum_tot'] = "{:.2f}".format(sum((data.vunita * data.canti) for data in invinideta_set))
		return context
