# -*- encoding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, ListView
from infa_web.apps.articulos.models import *
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .utils import *
from .forms import *
import datetime
import json

articulo = Tiarlos.objects.get(ntiarlos = 'ARTICULOS').pk

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
	value_extra = Arlo.objects.filter(ctiarlo = articulo).exclude(carlos__in = list(val.carlos.pk for val in value.invinideta_set.all()))
	response['val_tot'] = int(value.vttotal)
	response['day'] = value.fii.day
	response['month'] = value.fii.month
	response['year'] = value.fii.year
	response['hour'] = value.fii.hour
	response['minute'] = value.fii.minute

	response['ac_day'] = value.fuaii.day
	response['ac_month'] = value.fuaii.month
	response['ac_year'] = value.fuaii.year
	response['ac_hour'] = value.fuaii.hour
	response['ac_minute'] = value.fuaii.minute
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
	for arlo in Arlo.objects.filter(ctiarlo = articulo):
		response['data'][c] = {}
		response['data'][c]['carlos'] = arlo.carlos
		response['data'][c]['nlargo'] = arlo.nlargo.encode("utf-8")
		c += 1
	return HttpResponse(json.dumps(response), "application/json")
