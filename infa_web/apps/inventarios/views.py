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
	try:
		value = Invinicab.objects.all().latest('pk')
		response['code'] = sum_invini(value.pk)
		for arlo in Arlo.objects.all():
			response['data'] = {}
			response['data'][c]['carlos'] = arlo.carlos
			response['data'][c]['cbarras'] = arlo.cbarras
			response['data'][c]['nlargo'] = arlo.nlargo
			response['data'][c]['ngpo'] = arlo.cgpo.ngpo
			response['data'][c]['canti'] = arlo.canti
			c += 1
	except Invinicab.DoesNotExist:
		response['code'] = 'II-00001'
	return HttpResponse(json.dumps(response), "application/json")