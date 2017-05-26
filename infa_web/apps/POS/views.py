from django.shortcuts import render
from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView
from infa_web.apps.facturacion.models import *
from infa_web.apps.facturacion.forms import *
from infa_web.apps.articulos.models import *

from django.core.urlresolvers import reverse_lazy

from infa_web.custom.generic_views import CustomListView

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


class BillList(CustomListView):
	model = Fac
	template_name = "pos/list-billings.html"
	form_class = FacForm

	#@method_decorator(permission_required("facturacion.add_fac_pos",raise_exception=True))
<<<<<<< HEAD
	#def dispatch(self, *args, **kwargs):
	#	return super(BillList, self).dispatch(*args, **kwargs)
=======
	def dispatch(self, *args, **kwargs):
		return super(BillList, self).dispatch(*args, **kwargs)
>>>>>>> 7f1fa0717a8b71f26a8ca26c3479ff52cc002148

	def get_context_data(self,**kwargs):
		context = super(BillList, self).get_context_data(**kwargs)
		context['title'] = "Listar Facturas"
		context['sorted_object_list'] = Fac.objects.using(self.request.db).all().order_by("femi")

		return context

class BillCreate(CustomCreateView):
	model = Fac
	template_name = "pos/billing.html"
	form_class = FacForm

	#@method_decorator(permission_required("facturacion.add_fac_pos",raise_exception=True))
<<<<<<< HEAD
	#def dispatch(self, *args, **kwargs):
	#	return super(BillCreate, self).dispatch(*args, **kwargs)
=======
	def dispatch(self, *args, **kwargs):
		return super(BillCreate, self).dispatch(*args, **kwargs)
>>>>>>> 7f1fa0717a8b71f26a8ca26c3479ff52cc002148

	def get_context_data(self,**kwargs):
		print self.request.user.get_all_permissions()
		context = super(BillCreate, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)

		context['title'] = "POS"

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('save-bill')

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
from django.utils import timezone

#@permission_required("facturacion.add_fac_pos",raise_exception=True)
def BillPrint(request):

	text_footer_stzef = "AppEm - Software para administracion de Empresas sitematizaref@gmail.com"

	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'inline; attachment; filename="somefilename.pdf"'

	manageParameters = ManageParameters(request.db)
	data = request.GET

	cfac = data.get('cfac')

	factura = Fac.objects.using(request.db).get(cfac=cfac)
	factura_deta = Facdeta.objects.using(request.db).filter(cfac=factura)

	sucursal = factura.ccaja.csucur

	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=10,leftMargin=10, topMargin=0,bottomMargin=40)
	doc.pagesize = portrait((190, 1900))

	hr_linea = "___________________________________"

	elements = []

	data_header = [
		[manageParameters.get("company_name")],
		[manageParameters.get("text_header_pos_bill")],
		[manageParameters.get("company_id_name") + " : " + manageParameters.get("company_id")],
		["I.V.I Serie 5205964"],
		[sucursal.nsucur],
		["Dir:" + sucursal.dirsucur],
		["Tel:" + sucursal.telsucur],
		["Cel:" + sucursal.celsucur],
	]

	data = [
		["===============", "=========", "============"],
		["Descripcion", "Cant", "Vr. Tot"],
		["_______________", "_________", "____________"],
	]

	for facdeta in factura_deta:
		data.append([facdeta.carlos.ncorto[:10],str(facdeta.canti),""])
		data.append(["IVI","",str(facdeta.vtotal)])

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

	elements.append(Paragraph("Fecha : %s " % timezone.localtime(factura.femi),s['tirilla']))
	elements.append(Paragraph("Atendido por : %s <br/>" % factura.cvende.nvende,s['tirilla']))
	elements.append(t)
	elements.append(Paragraph(manageParameters.get("text_footer_pos_bill") ,s['tirilla']))
	elements.append(Paragraph(hr_linea ,s['tirilla']))
	elements.append(Paragraph(text_footer_stzef ,s['tirilla']))
	elements.append(Paragraph(hr_linea ,s['tirilla']))
	elements.append(Paragraph("." ,s['tirilla']))
	doc.build(elements)

	return response
