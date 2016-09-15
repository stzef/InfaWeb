from django.shortcuts import render,render_to_response 
from django.views.generic import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy 
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
import json
from infa_web.parameters import ManageParameters


from infa_web.apps.facturacion.models import *
from infa_web.apps.facturacion.forms import *
from infa_web.apps.base.forms import *

manageParameters = ManageParameters()

@csrf_exempt
def BillSave(request):
	data = json.loads(request.body)
	response = {}
	response["error"] = False
	response["message"] = "Factura Guardada con Exito"

	print (json.dumps(data,indent=4))
	#print json.dumps(data, indent=4)

	#Crear Fac
	"""Fac.objects.create()"""

	#Crear Facdeta
	"""for facdeta in data["facdeta"]
		Facdeta.objects.create()"""

	#Crear Mvsa
	"""Mvsa.objects.create()"""

	#Crear Mvsadeta
	"""for mvsadeta in data["facdeta"]
		Mvsadeta.objects.create()"""

	#Crear Movi
	#Crear Movideta

	return HttpResponse(json.dumps(response), "application/json")

class BillCreate(CreateView):
	model = Fac
	template_name = "facturacion/billing.html"
	form_class = FacForm

	def get_context_data(self,**kwargs):
		context = super(BillCreate, self).get_context_data(**kwargs)

		context['title'] = "Facturar"
		form_movement_detail = FacdetaForm()
		context['form_movement_detail'] = form_movement_detail

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('save-bill')

		context['data_validation'] = {}
		context['data_validation']['top_discount_bills'] = manageParameters.get_param_value('top_discount_bills')
		context['data_validation']['rounding_discounts'] = manageParameters.get_param_value('rounding_discounts')
		context['data_validation']['top_sales_invoice'] = manageParameters.get_param_value('top_sales_invoice')
		context['data_validation']['invoice_below_minimum_sales_price'] = manageParameters.get_param_value('invoice_below_minimum_sales_price')
		context['data_validation_json'] = json.dumps(context['data_validation'])

		return context

def bill_proccess_view_annulment(request):
	form = CommonForm()
	return render(request,"facturacion/procesos/annulment.html",{"form":form})

def bill_proccess_fn_annulment(request):
	data = json.loads(request.body)

	return HttpResponse(json.dumps({"message":"Se realizo exitosamente el cambio"}), content_type="application/json",status=200)
