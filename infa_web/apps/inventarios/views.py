# -*- encoding: utf-8 -*-
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, ListView
from reportlab.lib.pagesizes import letter, inch
from infa_web.apps.articulos.models import *
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from reportlab.lib import colors
from io import BytesIO
from .models import *
from .utils import *
from .forms import *
import datetime
import json

class InventoryView(FormView):
	template_name = 'inventarios/inventory.html'
	form_class = InventoryForm

	def get_context_data(self, **kwargs):
		context = super(InventoryView, self).get_context_data(**kwargs)
		context['title'] = 'Inventarios'
		return context

class InventoryListView(ListView):
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
	articulo = Tiarlos.objects.get(ntiarlos = 'ARTICULOS').pk
	try:
		value = Invinicab.objects.all().latest('pk')
		response['code'] = sum_invini(value.pk)
	except Invinicab.DoesNotExist:
		response['code'] = 'II-00001'
	for arlo in Arlo.objects.filter(ctiarlo = articulo):
		response['data'][c] = {}
		response['data'][c]['carlos'] = arlo.carlos
		response['data'][c]['cbarras'] = arlo.cbarras
		response['data'][c]['nlargo'] = arlo.nlargo
		response['data'][c]['ngpo'] = arlo.cgpo.ngpo
		response['data'][c]['canti'] = 0
		response['data'][c]['cancalcu'] = int(arlo.canti)
		response['data'][c]['vcosto'] = int(arlo.vcosto)
		c += 1
	c = 0
	for esdo in Esdo.objects.all():
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
	response['data_extra'] = {}
	response['esdo'] = {}
	value = Invinicab.objects.get(pk = request.POST.get('pk'))
	articulo = Tiarlos.objects.get(ntiarlos = 'ARTICULOS').pk
	value_extra = Arlo.objects.filter(ctiarlo = articulo).exclude(carlos__in = list(val.carlos.pk for val in value.invinideta_set.all()))
	response['val_tot'] = int(value.vttotal)
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
	for arlo in value.invinideta_set.all():
		response['data'][c] = {}
		response['data'][c]['carlos'] = arlo.carlos.pk
		response['data'][c]['cbarras'] = arlo.carlos.cbarras
		response['data'][c]['nlargo'] = arlo.nlargo
		response['data'][c]['ngpo'] = arlo.carlos.cgpo.ngpo
		response['data'][c]['canti'] = int(arlo.canti)
		response['data'][c]['cancalcu'] = int(arlo.cancalcu)
		response['data'][c]['vcosto'] = int(arlo.vunita)
		c += 1
	c = 0
	for arlo_extra in value_extra:
		response['data_extra'][c] = {}
		response['data_extra'][c]['carlos'] = arlo_extra.carlos
		response['data_extra'][c]['cbarras'] = arlo_extra.cbarras
		response['data_extra'][c]['nlargo'] = arlo_extra.nlargo
		response['data_extra'][c]['ngpo'] = arlo_extra.cgpo.ngpo
		response['data_extra'][c]['cancalcu'] = int(arlo_extra.canti)
		response['data_extra'][c]['canti'] = 0
		response['data_extra'][c]['vcosto'] = int(arlo_extra.vcosto)
		c += 1
	c = 0
	for esdo in Esdo.objects.all():
		response['esdo'][c] = {}
		response['esdo'][c]['cesdo'] = esdo.cesdo
		response['esdo'][c]['nesdo'] = esdo.nesdo
		response['esdo'][c]['selected'] = 'selected' if esdo.cesdo == value.cesdo.cesdo else ''
		c += 1
	response['count_extra'] = value_extra.count()
	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def inventory_save(request):
	response = {}
	response_data = json.loads(request.POST.get('data_r'))
	cii = request.POST.get('cii')
	val_tot = request.POST.get('val_tot')
	cesdo = Esdo.objects.get(cesdo = request.POST.get('cesdo'))
	fii = datetime.datetime.strptime(request.POST.get('fii'), '%d/%m/%Y %H:%M')
	try:
		invini = Invinicab.objects.get(cii = cii)
		invini.cesdo = cesdo
		invini.fuaii = datetime.datetime.now()
		invini.vttotal = val_tot
		invini.fii = fii
		invini.save()
		for cii_deta in response_data:
			carlos = Arlo.objects.get(carlos = cii_deta['carlos'])
			try:
				invini_deta = Invinideta.objects.get(cii = invini, carlos = carlos)
				invini_deta.nlargo = cii_deta['nlargo']
				invini_deta.canti = cii_deta['cant']
				invini_deta.vunita = cii_deta['vunita']
				invini_deta.vtotal = (int(cii_deta['cant']) * float(cii_deta['vunita']))
				invini_deta.cancalcu = cii_deta['cancalcu']
				invini_deta.ajuent = cii_deta['ajuent']
				invini_deta.ajusal = cii_deta['ajusal']
				invini_deta.save()	
			except Invinideta.DoesNotExist:
				invini_deta = Invinideta(cii = invini, carlos = carlos, nlargo = cii_deta['nlargo'], canti = cii_deta['cant'], vunita = cii_deta['vunita'], vtotal = (int(cii_deta['cant']) * float(cii_deta['vunita'])), cancalcu = cii_deta['cancalcu'], ajuent = cii_deta['ajuent'], ajusal = cii_deta['ajusal'])
				invini_deta.save()
	except Invinicab.DoesNotExist:
		invini = Invinicab(cii = cii, cesdo = cesdo, vttotal = val_tot, fii = fii)
		invini.save()
		for cii_deta in response_data:
			carlos = Arlo.objects.get(carlos = cii_deta['carlos'])
			invini_deta = Invinideta(cii = invini, carlos = carlos, nlargo = cii_deta['nlargo'], canti = cii_deta['cant'], vunita = cii_deta['vunita'], vtotal = (int(cii_deta['cant']) * float(cii_deta['vunita'])), cancalcu = cii_deta['cancalcu'], ajuent = cii_deta['ajuent'], ajusal = cii_deta['ajusal'])
			invini_deta.save()
	response['msg'] = 'Exito al guardar'
	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def get_name_arlo(request):
	response = {}
	c = 0
	response['data'] = {}
	articulo = Tiarlos.objects.get(ntiarlos = 'ARTICULOS').pk
	for arlo in Arlo.objects.filter(ctiarlo = articulo):
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

	def post(self, request, *args, **kwargs):
		invini = request.POST.get('nota_inicial')
		fecha_nota_inicial = request.POST.get('fecha_nota_inicial')
		fecha_final = request.POST.get('fecha_final')
		group_report = request.POST.get('group_report')
		type_report = request.POST.get('type_report')
		now = datetime.datetime.now()
		content = []

		buff = BytesIO()
		styles = getSampleStyleSheet()
		nombre_empresa = Paragraph("ALMACEN EL EJEMPLO", styles['h2'])
		it_empresa = Paragraph("Iden. 0000000000000-0", styles['Normal'])
		titulo = Paragraph("Listado de Existencias desde "+str(fecha_nota_inicial)+" hasta "+str(fecha_final), styles['Normal'])

		data= [['Código', 'Nombre', 'Existencia'],
		['10', '11', '12'],
		['20', '21', '22'],
		['30', '31', '32']]
		t=Table(data, 190)
		t.setStyle(TableStyle([
			('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			('VALIGN',(0,0),(0,-1),'TOP'),
			('LINEABOVE',(0,1),(-1,1),0.25,colors.black),
		]))

		content.append(nombre_empresa)
		content.append(it_empresa)
		content.append(titulo)
		content.append(t)
		doc = SimpleDocTemplate(buff, pagesize = letter, rightMargin = 15, leftMargin = 15, topMargin = 15, bottomMargin = 15)
		doc.build(content)
		response = HttpResponse(content_type = 'application/pdf')
		response.write(buff.getvalue())
		buff.close()
		#response['Content-Disposition'] = 'attachment: filename=stocks-'+str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'.pdf'
		return response