from django.shortcuts import render
from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView
from infa_web.apps.facturacion.models import *
from infa_web.apps.facturacion.forms import *
from infa_web.apps.articulos.models import *

from django.core.urlresolvers import reverse_lazy


class BillCreate(CustomCreateView):
	model = Fac
	template_name = "pos/billing.html"
	form_class = FacForm

	def get_context_data(self,**kwargs):
		context = super(BillCreate, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)

		# Datos de Prueba
		#usuario = Usuario.objects.using(self.request.db).filter()[0]

		#talonario_MOS = usuario.ctalomos
		#talonario_POS = usuario.ctalopos
		# Datos de Prueba

		#medios_pago = [(serializers.serialize("json", [x],use_natural_foreign_keys=True, use_natural_primary_keys=True)) for x in MediosPago.objects.using(self.request.db).all()]
		medios_pago = MediosPago.objects.using(self.request.db).all()

		context['medios_pago'] = medios_pago

		context['title'] = "Facturas"
		context['form_movement_detail'] = FacdetaForm(self.request.db)
		context['form_medios_pagos'] = FacpagoForm(self.request.db)

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('save-bill')

		context['data_validation'] = manageParameters.to_dict()

		context['company_logo'] = manageParameters.get_param_value('company_logo')

		#context['data_validation']['top_discount_bills'] = manageParameters.get_param_value('top_discount_bills')
		#context['data_validation']['rounding_discounts'] = manageParameters.get_param_value('rounding_discounts')
		#context['data_validation']['top_sales_invoice'] = manageParameters.get_param_value('top_sales_invoice')
		#context['data_validation']['invoice_below_minimum_sales_price'] = manageParameters.get_param_value('invoice_below_minimum_sales_price')
		#context['data_validation']['maximum_amount_items_billing'] = manageParameters.get_param_value('maximum_amount_items_billing')
		#context['data_validation']['invoice_without_stock'] = manageParameters.get_param_value('invoice_without_stock')

		# Datos de Prueba
		context['data_validation']['maximum_number_items_billing'] = 10
		# Datos de Prueba

		context['data_validation']['formas_pago'] = {}
		context['data_validation']['formas_pago']['FORMA_PAGO_CONTADO'] = str(FORMA_PAGO_CONTADO)
		context['data_validation']['formas_pago']['FORMA_PAGO_CREDITO'] = str(FORMA_PAGO_CREDITO)

		context['data_validation']['medios_pago'] = {}
		context['data_validation']['medios_pago']['MEDIO_PAGO_EFECTIVO'] = str(MEDIO_PAGO_EFECTIVO)
		context['data_validation']['medios_pago']['DEFAULT_BANCO'] = str(DEFAULT_BANCO)

		context['is_fac_anulada'] = False

		context['data_validation_json'] = json.dumps(context['data_validation'])

		grupos = Gpo.objects.using(self.request.db).all()
		for grupo in grupos:
			grupo.articulos = Arlo.objects.using(self.request.db).filter(cgpo=grupo)

		context['grupos'] = grupos

		return context

import reportlab
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape, portrait
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def some_view(request):
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

	# Create the PDF object, using the response object as its "file."
	#p = canvas.Canvas(response)
	#p = canvas.Canvas({response})

	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	#p.drawString(100, 100, "Hello world.")
	#p.setPageSize((200, 700)) #some page size, given as a tuple in points

	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=5,leftMargin=5, topMargin=5,bottomMargin=5)
	doc.pagesize = portrait((200, 700))

	elements = []

	data = [
		["Descripcion", "Cant", "Vr. Tot"],
		["MANTENIMIENTO Y BACKUP", "1", "60.000"],
		["MANTENIMIENTO PORTATILES", "2", "100.000"],
		["MANTENIMIENTO PORTATIL CO", "1", "50.000"],
	]

	style = TableStyle([
		('ALIGN',(1,1),(-2,-2),'RIGHT'),
		('TEXTCOLOR',(1,1),(-2,-2),colors.red),
		('VALIGN',(0,0),(0,-1),'TOP'),
		('TEXTCOLOR',(0,0),(0,-1),colors.blue),
		('ALIGN',(0,-1),(-1,-1),'CENTER'),
		('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
		('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
		#('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
		('BOX', (0,0), (-1,-1), 0.25, colors.black),
	])

	#Configure style and word wrap
	s = getSampleStyleSheet()
	s = s["BodyText"]
	#s.wordWrap = 'CJK'
	s.wordWrap = 'LTR'
	data2 = [[Paragraph(cell, s) for cell in row] for row in data]
	t=Table(data2)
	t.setStyle(style)

	#Send the data and build the file
	elements.append(t)
	doc.build(elements)




	# Close the PDF object cleanly, and we're done.
	#p.showPage()
	#p.save()
	return response
# Create your views here.
