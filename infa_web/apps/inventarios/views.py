from django.views.decorators.csrf import csrf_exempt
from infa_web.apps.articulos.models import *
from django.views.generic import FormView
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .utils import *
from .forms import *
import json


class InventoryView(FormView):
	template_name = 'inventarios/inventory.html'
	form_class = InventoryForm

	def get_context_data(self, **kwargs):
		context = super(InventoryView, self).get_context_data(**kwargs)
		context['title'] = 'Inventarios'
		return context

@csrf_exempt
def inventory_latest(request):
	response = {}
	c = 0
	response['data'] = {}
	try:
		value = Invinicab.objects.all().latest('pk')
		response['code'] = sum_invini(value.pk)
	except Invinicab.DoesNotExist:
		response['code'] = 'II-00001'
	for arlo in Arlo.objects.all():
		response['data'][c] = {}
		response['data'][c]['carlos'] = arlo.carlos
		response['data'][c]['cbarras'] = arlo.cbarras
		response['data'][c]['nlargo'] = arlo.nlargo
		response['data'][c]['ngpo'] = arlo.cgpo.ngpo
		response['data'][c]['canti'] = int(arlo.canti)
		response['data'][c]['vcosto'] = int(arlo.vcosto)
		c += 1
	return HttpResponse(json.dumps(response), "application/json")

def inventory_find(request, cii):
	response = {}
	try:
		value = Invinicab.objects.get(cii = cii)
		response['cii'] = value.pk
		response['type'] = 1
	except Invinicab.DoesNotExist:
		response['cii'] = cii
		response['type'] = 0
	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def inventory_save(request):
	response = {}
	response_data = json.loads(request.POST.get('data_r'))
	cii = request.POST.get('cii')
	invini = Invinicab(cii = cii)
	invini.save()
	for cii_deta in response_data:
		carlos = Arlo.objects.get(carlos = cii_deta['carlos'])
		invini_deta = Invinideta(cii = invini, carlos = carlos, nlargo = cii_deta['nlargo'], canti = cii_deta['cant'], vunita = cii_deta['vunita'], vtotal = (int(cii_deta['cant']) * float(cii_deta['vunita'])), cancalcu = cii_deta['cancalcu'], ajuent = cii_deta['ajuent'], ajusal = cii_deta['ajusal'])
		invini_deta.save()
	response['msg'] = 'Exito al guardar'
	return HttpResponse(json.dumps(response), "application/json")