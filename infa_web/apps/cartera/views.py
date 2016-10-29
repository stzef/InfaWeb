from django.shortcuts import render

from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView
from infa_web.apps.base.constantes import *
from infa_web.parameters import ManageParameters
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from easy_pdf.views import PDFTemplateView
from infa_web.apps.movimientos.models import *
from infa_web.apps.movimientos.forms import *

class PaymentCreate(CustomCreateView):
	model = Movi
	template_name = "cartera/payment.html"
	form_class = MoviForm

	def get_context_data(self,**kwargs):
		context = super(PaymentCreate, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)
		context['form_movideta'] = MoviDetailForm(self.request.db)
		context['form_medios_pagos'] = MovipagoForm(self.request.db)

		context['mode_view'] = 'create'
		#context['url'] = reverse_lazy('save-bill')
		return context
class PaymentEdit(CustomUpdateView):
	model = Movi
	template_name = "cartera/payment.html"
	form_class = MoviForm

	def get_context_data(self,**kwargs):
		context = super(PaymentCreate, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)
		context['form_movideta'] = MoviDetailForm(self.request.db)
		context['form_medios_pagos'] = MovipagoForm(self.request.db)


		context['mode_view'] = 'edit'
		#context['url'] = reverse_lazy('save-bill')
		return context
@csrf_exempt
def PaymentSave(request):
	data = json.loads(request.body)
	response = {}
	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def PaymentUpdate(request):
	data = json.loads(request.body)
	response = {}
	return HttpResponse(json.dumps(response), "application/json")

