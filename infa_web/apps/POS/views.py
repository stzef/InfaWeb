from django.shortcuts import render
from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView
from infa_web.apps.facturacion.models import *
from infa_web.apps.facturacion.forms import *
from infa_web.apps.articulos.models import *

from django.core.urlresolvers import reverse_lazy

from infa_web.custom.generic_views import CustomListView

class BillList(CustomListView):
	model = Fac
	template_name = "pos/list-billings.html"
	form_class = FacForm

	def get_context_data(self,**kwargs):
		context = super(BillList, self).get_context_data(**kwargs)
		context['title'] = "Listar Facturas"
		context['sorted_object_list'] = Fac.objects.using(self.request.db).all().order_by("femi")
		print context['sorted_object_list']

		return context

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
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def some_view(request):

	text_footer_stzef = "AppEm - Software para administracion de Empresas sitematizaref@gmail.com"

	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'inline; attachment; filename="somefilename.pdf"'

	manageParameters = ManageParameters(request.db)
	data = request.GET

	cfac = data.get('cfac')

	factura = Fac.objects.using(request.db).get(cfac=cfac)
	factura_deta = Facdeta.objects.using(request.db).filter(cfac=factura)

	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=10,leftMargin=10, topMargin=0,bottomMargin=40)
	doc.pagesize = portrait((190, 1900))

	hr_linea = "___________________________________"

	elements = []

	data_header = [
		[manageParameters.get("company_name")],
		[manageParameters.get("text_header_pos_bill")],
	]

	data = [
		["===============", "=========", "============"],
		["Descripcion", "Cant", "Vr. Tot"],
		["_______________", "_________", "____________"],
	]

	for facdeta in factura_deta:
		data.append([facdeta.carlos.ncorto[:10],str(facdeta.canti),str(facdeta.vtotal)])

	data.append(["_______________", "_________", "____________"])
	data.append(["Total","-->",str(factura.vttotal)])
	data.append(["===============", "=========", "============"])

	style_table_header = TableStyle([
		('ALIGN',(1,1),(-2,-2),'RIGHT'),
		('TEXTCOLOR',(1,1),(-2,-2),colors.red),
		('VALIGN',(0,0),(0,-1),'TOP'),
		('TEXTCOLOR',(0,0),(0,-1),colors.blue),
		('ALIGN',(0,-1),(-1,-1),'CENTER'),
		('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
		('TEXTCOLOR',(0,-1),(-1,-1),colors.green),

		('LEFTPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),

		('BOX', (0,0), (-1,-1), 0.25, colors.black),
	])

	style_table_facdeta = TableStyle([
		('ALIGN',(1,1),(-2,-2),'RIGHT'),
		('TEXTCOLOR',(1,1),(-2,-2),colors.red),
		('VALIGN',(0,0),(0,-1),'TOP'),
		('TEXTCOLOR',(0,0),(0,-1),colors.blue),
		('ALIGN',(0,-1),(-1,-1),'CENTER'),
		('VALIGN',(0,-1),(-1,-1),'MIDDLE'),

		('LEFTPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),

		('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
	])

	#Configure style and word wrap
	s = getSampleStyleSheet()

	s.add(ParagraphStyle(name='tirilla',fontSize=8,leading=12,rightMargin=0,leftMargin=0, topMargin=0,bottomMargin=0))
	s.add(ParagraphStyle(name='header',fontSize=8,leading=12,alignment=TA_CENTER))

	bodytext = s["tirilla"]
	headertext = s["header"]
	#s.wordWrap = 'CJK'
	bodytext.wordWrap = 'LTR'
	data2 = [[Paragraph(cell, bodytext) for cell in row] for row in data]
	t=Table(data2)
	t.setStyle(style_table_facdeta)

	data2_header = [[Paragraph(cell, headertext) for cell in row] for row in data_header]
	t_header=Table(data2_header)
	t_header.setStyle(style_table_header)

	elements.append(t_header)
	elements.append(Paragraph("<br/>Factura No. %s" % factura.cfac,s['tirilla']))
	elements.append(Paragraph("Fecha : %s " % factura.femi,s['tirilla']))
	elements.append(Paragraph("Atendido por : %s <br/>" % factura.cvende.nvende,s['tirilla']))
	elements.append(t)
	elements.append(Paragraph(manageParameters.get("text_footer_pos_bill") ,s['tirilla']))
	elements.append(Paragraph(hr_linea ,s['tirilla']))
	elements.append(Paragraph(text_footer_stzef ,s['tirilla']))
	elements.append(Paragraph(hr_linea ,s['tirilla']))
	doc.build(elements)

	return response
