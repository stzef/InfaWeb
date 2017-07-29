from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

from html import HTML
import codecs
import json
import locale
import webbrowser

from infa_web.apps.articulos.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.inventarios.models import *
from infa_web.apps.facturacion.models import *

from infa_web.apps.facturacion.views import ctimo_billing
from infa_web.routines import costing_and_stock
from infa_web.routines import *
from infa_web.apps.facturacion.bills_fn import *

from infa_web.apps.base.data_test.arlo_mov_fac import data_mvens,data_mvsas,data_invs,data_facs,data_edit_facs,data_articles,costing_and_stock_expected_values,cartera_expected_values

document_html = HTML()
locale.setlocale(locale.LC_ALL, '')

css_table = "table table-bordered table-hover table-striped"
css_sections = "panel panel-primary"
ccs_section_heading = "panel-heading"


def fc(x):
	return locale.currency(x,grouping=True)

def create_articles(array):
	c = Client()
	for data_article in array:
		c.post(reverse('add-article'),data_article,HTTP_X_REQUESTED_WITH='XMLHttpRequest')

def create_inventory():
	c = Client()
	response_inventory = c.post(reverse('inventory_latest'),HTTP_X_REQUESTED_WITH='XMLHttpRequest')
	inventory = json.loads(response_inventory.content)
	return inventory["code"]

def create_invinideta(array,cii):
	c = Client()
	for data_inv in array:
		for data_invdeta in data_inv["deta"]:
			article = Arlo.objects.get(carlos = data_invdeta["carlos"])

			canti = data_invdeta["canti"]
			vcosto = data_invdeta["vcosto"]

			cancalcu = article.canti

			ajuent = canti - article.canti
			ajusal = 0

			body_request_inventory = {
				"cii":str(cii),
				"val_tot":"15000",
				"fii":"14/10/2016 08:22",
				"cesdo":"1",
				"data_r":json.dumps([
					{
						"carlos":str(article.carlos),
						"nlargo":str(article.nlargo),
						"cancalcu":str(cancalcu),
						"canti":str(canti),
						"vcosto":str(vcosto),
						"ajuent":str(ajuent),
						"ajusal":str(ajusal),
						"cbarras":str(article.cbarras),
					}
				])
			}
			response_inventory_deta_1 = c.post(reverse('inventory_save'),body_request_inventory,HTTP_X_REQUESTED_WITH='XMLHttpRequest')

def create_mven(data):
	c = Client()
	body_request_mven_1 = data["base"]
	it_mven = 1
	for data_mvendeta in data["deta"]:
		article = Arlo.objects.get(carlos=data_mvendeta["carlos"])

		canti = data_mvendeta["canti"]
		vunita = data_mvendeta["vunita"]
		dictt = {
			"it":it_mven,
			"carlos":str(article.carlos),
			"name__carlos":str(article.nlargo),
			"canti":canti,
			"vunita":vunita,
			"vtotal":vunita*canti,
		}
		body_request_mven_1["vttotal"] += dictt["vtotal"]
		body_request_mven_1["mvdeta"].append(dictt)
		it_mven += 1
	response_mven_1 = c.post(reverse('save-movement'),json.dumps(body_request_mven_1),HTTP_X_REQUESTED_WITH='XMLHttpRequest',content_type="application/json")

def create_mvsa(data):
	c = Client()
	body_request_mvsa_1 = data["base"]
	it_mvsa = 1
	for data_mvsadeta in data["deta"]:
		article = Arlo.objects.get(carlos=data_mvsadeta["carlos"])

		canti = data_mvsadeta["canti"]
		vunita = data_mvsadeta["vunita"]

		dictt = {
			"it":it_mvsa,
			"carlos":str(article.carlos),
			"name__carlos":str(article.nlargo),
			"canti":canti,
			"vunita":vunita,
			"vtotal":vunita*canti,
		}
		body_request_mvsa_1["vttotal"] += dictt["vtotal"]
		body_request_mvsa_1["mvdeta"].append(dictt)
		it_mvsa += 1

	response_mvsa_1 = c.post(reverse('save-movement'),json.dumps(body_request_mvsa_1),HTTP_X_REQUESTED_WITH='XMLHttpRequest',content_type="application/json")

def create_fac(index,data,using):
	c = Client()
	body_request_fac_contado = data["base"]

	it_facdeta = 1
	for data_articulo in data["deta"]:
		article = Arlo.objects.get(carlos=data_articulo["carlos"])

		canti = data_articulo["canti"]
		#vunita = data_articulo["vunita"]
		vunita = calcular_valor_unitario(article.carlos,1,data_articulo["pordes"],data_articulo["vunita"],using)

		temp_arl = {
			"itfac":it_facdeta,
			"carlos":article.carlos,
			"name__carlos":article.nlargo,
			"canti":canti,
			"pordes":data_articulo["pordes"],
			"civa":data_articulo["civa"],
			"vunita":vunita,
			"vtotal":canti * vunita
		}
		it_facdeta += 1
		body_request_fac_contado["mvdeta"].append(temp_arl)

		body_request_fac_contado["vttotal"] += vunita

		totales = calcular_vtbase_vtiva(body_request_fac_contado["mvdeta"])
		body_request_fac_contado["vtbase"] = totales["vtbase"]
		body_request_fac_contado["vtiva"] = totales["vtiva"]

	body_request_fac_contado["vcambio"] = calcular_valor_cambio(body_request_fac_contado["ventre"],body_request_fac_contado["vttotal"])
	body_request_fac_contado["vrtefte"] = calcular_total_flete(body_request_fac_contado["brtefte"],body_request_fac_contado["prtefte"])
	body_request_fac_contado["vttotal"] = calcular_total(body_request_fac_contado["mvdeta"],body_request_fac_contado["vflete"],body_request_fac_contado["vdescu"])

	it_facpagodeta = 1
	for medio_pago in data["medios_pagos"]:

		temp_mp = {
			"it":it_facpagodeta,
			"cmpago":medio_pago["cmpago"],
			"docmpago":medio_pago["docmpago"],
			"banmpago":medio_pago["banmpago"],
			"vmpago":body_request_fac_contado["vttotal"] * ( float(medio_pago["porcentaje"]) / float(100) )
		}
		it_facpagodeta += 1
		body_request_fac_contado["medios_pagos"].append(temp_mp)

	response_fac_contado = c.post(reverse('save-bill'),json.dumps(body_request_fac_contado),HTTP_X_REQUESTED_WITH='XMLHttpRequest',content_type="application/json")
	response_fac_contado = json.loads(response_fac_contado.content)

	data_edit_facs[index]["base"]["cfac"] = response_fac_contado['related_information']['fields']["cfac"]
	data_edit_facs[index]["pk"] = response_fac_contado['related_information']['pk']

def update_fac(data,using):
	c = Client()
	body_request_fac_contado = data["base"]

	it_facdeta = 1
	for data_articulo in data["deta"]:
		article = Arlo.objects.get(carlos=data_articulo["carlos"])

		canti = data_articulo["canti"]
		#vunita = data_articulo["vunita"]
		vunita = calcular_valor_unitario(article.carlos,1,data_articulo["pordes"],data_articulo["vunita"],using)

		temp_arl = {
			"itfac":it_facdeta,
			"carlos":article.carlos,
			"name__carlos":article.nlargo,
			"canti":canti,
			"pordes":data_articulo["pordes"],
			"civa":data_articulo["civa"],
			"vunita":vunita,
			"vtotal":canti * vunita
		}
		it_facdeta += 1
		body_request_fac_contado["mvdeta"].append(temp_arl)

		body_request_fac_contado["vttotal"] += vunita

		totales = calcular_vtbase_vtiva(body_request_fac_contado["mvdeta"])
		body_request_fac_contado["vtbase"] = totales["vtbase"]
		body_request_fac_contado["vtiva"] = totales["vtiva"]

	body_request_fac_contado["vcambio"] = calcular_valor_cambio(body_request_fac_contado["ventre"],body_request_fac_contado["vttotal"])
	body_request_fac_contado["vrtefte"] = calcular_total_flete(body_request_fac_contado["brtefte"],body_request_fac_contado["prtefte"])
	body_request_fac_contado["vttotal"] = calcular_total(body_request_fac_contado["mvdeta"],body_request_fac_contado["vflete"],body_request_fac_contado["vdescu"])

	it_facpagodeta = 1
	for medio_pago in data["medios_pagos"]:

		temp_mp = {
			"it":it_facpagodeta,
			"cmpago":medio_pago["cmpago"],
			"docmpago":medio_pago["docmpago"],
			"banmpago":medio_pago["banmpago"],
			"vmpago":body_request_fac_contado["vttotal"] * ( float(medio_pago["porcentaje"]) / float(100) )
		}
		it_facpagodeta += 1
		body_request_fac_contado["medios_pagos"].append(temp_mp)




	response_fac_contado = c.post(reverse('update-bill',args=[data["pk"]]),json.dumps(body_request_fac_contado),HTTP_X_REQUESTED_WITH='XMLHttpRequest',content_type="application/json")
	response_fac_contado = json.loads(response_fac_contado.content)

def list_inv(cii):
	section = document_html.div(klass=css_sections)
	section.div(klass=ccs_section_heading).h1("Creacion de Inventario Inicial")
	invinicab = Invinicab.objects.get(cii=cii)
	section.p("Invetario Inicial Creado : %s\n" % cii)

	table = section.table(klass=css_table)
	thead = table.thead().tr()
	thead.th("carlos")
	thead.th("canti")
	thead.th("vunita")
	thead.th("vtotal")
	thead.th("cancalcu")
	thead.th("ajuent")
	thead.th("ajusal")

	for invinideta in Invinideta.objects.filter(cii=cii):
		tr = table.tr()
		tr.td(str(invinideta.carlos.carlos))
		tr.td(str(invinideta.canti))
		tr.td(str(fc(invinideta.vunita)))
		tr.td(str(fc(invinideta.vtotal)))
		tr.td(str(invinideta.cancalcu))
		tr.td(str(invinideta.ajuent))
		tr.td(str(invinideta.ajusal))


def list_articles(report):
	pass

def list_mven():
	section = document_html.div(klass=css_sections)
	section.div(klass=ccs_section_heading).h1("Creacion de Movimientos Entrada")
	section_body = section.div(klass="panel-body")
	for mven in Mven.objects.all():
		sub_section = section_body.div(klass=css_sections)
		sub_section.div(klass=ccs_section_heading).p("Movimiento de Entrada %s\nFecha:%s\nDoc Ref:%s\nT Movimiento:%s\n" % (mven.cmven,mven.fmven,mven.docrefe,mven.ctimo))
		table = sub_section.div(klass="panel-body").table(klass=css_table)
		thead = table.thead().tr()
		thead.th("carlos")
		thead.th("nlargo")
		thead.th("canti")
		thead.th("vunita")
		thead.th("vtotal")

		for mvendeta in Mvendeta.objects.filter(cmven = mven.cmven):
			tr = table.tr()
			tr.td(str(mvendeta.carlos.carlos))
			tr.td(str(mvendeta.nlargo))
			tr.td(str(mvendeta.canti))
			tr.td(str(fc(mvendeta.vunita)))
			tr.td(str(fc(mvendeta.vtotal)))

def list_mvsa():
	section = document_html.div(klass=css_sections)
	section.div(klass=ccs_section_heading).h1("Creacion de Movimientos Salida")
	for mvsa in Mvsa.objects.all():
		section.p("Movimiento de Entrada %s\nFecha:%s\nDoc Ref:%s\nT Movimiento:%s\n" % (mvsa.cmvsa,mvsa.fmvsa,mvsa.docrefe,mvsa.ctimo))
		table = section.table(klass=css_table)
		thead = table.thead().tr()
		thead.th("carlos")
		thead.th("nlargo")
		thead.th("canti")
		thead.th("vunita")
		thead.th("vtotal")
		for mvendeta in Mvsadeta.objects.filter(cmvsa = mvsa.cmvsa):
			tr = table.tr()
			tr.td(str(mvendeta.carlos.carlos))
			tr.td(str(mvendeta.nlargo))
			tr.td(str(mvendeta.canti))
			tr.td(str(fc(mvendeta.vunita)))
			tr.td(str(fc(mvendeta.vtotal)))

def list_fac():
	section = document_html.div(klass=css_sections)
	section.div(klass=ccs_section_heading).h1("Creacion de Factura")
	for fac in Fac.objects.all():
		section.p("Factura %s\nFecha:%s\nForma Pago:%s\nVr. Total:%s\n" % (fac.cfac,fac.femi,fac.ctifopa,fc(fac.vttotal)))

		table = section.table(klass=css_table)
		thead = table.thead().tr()
		thead.th("itfac")
		thead.th("carlos")
		thead.th("nlargo")
		thead.th("canti")
		thead.th("civa")
		thead.th("vunita")
		thead.th("vbase")
		thead.th("viva")
		thead.th("vtotal")
		thead.th("pordes")
		thead.th("vcosto")

		for facdeta in Facdeta.objects.filter(cfac = fac.pk):
			tr = table.tr()
			tr.td(str(facdeta.itfac))
			tr.td(str(facdeta.carlos))
			tr.td(str(facdeta.nlargo))
			tr.td(str(facdeta.canti))
			tr.td(str(facdeta.civa))
			tr.td(str(fc(facdeta.vunita)))
			tr.td(str(fc(facdeta.vbase)))
			tr.td(str(fc(facdeta.viva)))
			tr.td(str(fc(facdeta.vtotal)))
			tr.td(str(facdeta.pordes))
			tr.td(str(fc(facdeta.vcosto)))

def list_movi():
	section = document_html.div(klass=css_sections)
	section.div(klass=ccs_section_heading).h1("Creacion de Movimientos")
	for movi in Movi.objects.all():
		section.p("Movimiento %s\nFecha:%s\nT Movi:%s\nVr. Total:%s\n" % (movi.cmovi,movi.fmovi,movi.ctimo,fc(movi.vttotal)))

		table = section.table(klass=css_table)
		thead = table.thead().tr()
		thead.th("Item")
		thead.th("Documento Referencia")
		thead.th("Total")

		for movideta in Movideta.objects.filter(cmovi = movi.pk):
			tr = table.tr()
			tr.td(str(movideta.itmovi))
			tr.td(str(movideta.docrefe))
			tr.td(str(fc(movideta.vmovi)))

class ExampleTestCase(TestCase):

	using = "default"
	cii = None
	name_file_reporte = 'report_test/report.html'
	name_file_template = 'report_test/template_test.html'


	def setUp(self):

		# Creacion De Articulo
		create_articles(data_articles)

		# Creacion de Inventario Inicial Cabeza
		self.cii = create_inventory()

		# Creacon de Inventario Inicial Detalle
		create_invinideta(data_invs,self.cii)

		# Creacion de Movimientos Entrada
		for data_mven in data_mvens:
			create_mven(data_mven)

		# Creacion de Movimientos Salida
		for data_mvsa in data_mvsas:
			create_mvsa(data_mvsa)

		# Creacion de Facturas
		for index,data_facdeta in enumerate(data_facs):
			create_fac(index,data_facdeta,self.using)

		# Creacion de Facturas
		for data_edit_facdeta in data_edit_facs:
			update_fac(data_edit_facdeta,self.using)

	def costing_and_stock(self):
		report = codecs.open(self.name_file_reporte, "w", "utf-8")

		list_inv(self.cii)

		list_mvsa()

		list_mven()

		list_fac()

		list_movi()

		result_c_s = costing_and_stock(False,True,{},self.using)

		section = document_html.div(klass=css_sections)
		section.div(klass=ccs_section_heading).h1("Costos y Existencias Finales")
		table = section.table(klass=css_table)
		thead = table.thead().tr()
		thead.th("carlos")
		thead.th("nlargo")
		thead.th("canti")
		thead.th("vcosto")
		for article in Arlo.objects.all():
			tr = table.tr()
			tr.td(str(article.carlos))
			tr.td(str(article.nlargo))
			tr.td(str(article.canti))
			tr.td(str(fc(article.vcosto)))

			expected_values = costing_and_stock_expected_values[article.carlos]

			msg_error_assert_canti = "Se esperaba una Cantidad de %s para el Articulo %s - %s pero se obtuvo %s" %(expected_values["canti"],article.carlos,article.nlargo,article.canti)
			msg_error_assert_vcosto = "Se esperaba un Costo de %s para el Articulo %s - %s pero se obtuvo %s" %(expected_values["vcosto"],article.carlos,article.nlargo,article.vcosto)

			self.assertEqual(article.canti, expected_values["canti"],msg_error_assert_canti)
			self.assertEqual(float(article.vcosto), float(expected_values["vcosto"]),msg_error_assert_vcosto)



		section = document_html.div(klass=css_sections)
		section.div(klass=ccs_section_heading).h1("Cartera por Tercero")
		for tercero in Tercero.objects.all():
			section.p("Tercero : %s\n" % tercero.rasocial)
			table = section.table(klass=css_table)
			thead = table.thead().tr()
			thead.th("itmovi")
			thead.th("docrefe")
			thead.th("vmovi")

			expected_values = cartera_expected_values[tercero.pk]


			ctimo_cr = ctimo_billing('ctimo_cxc_billing', self.using)
			ctimo_ab = ctimo_billing('ctimo_ab_billing', self.using)
			movidetas = Movideta.objects.using(self.using).filter(cmovi__citerce = tercero.pk, cmovi__ctimo__in = [ctimo_cr, ctimo_ab]).order_by('cmovi__fmovi')

			vttotal_cartera = 0
			for movideta in movidetas:
				tr = table.tr()
				tr.td(str(movideta.itmovi))
				tr.td(str(movideta.docrefe))
				tr.td(str(fc(movideta.vmovi)))
				vttotal_cartera += movideta.vmovi

			msg_error_assert_cartera = "Para el Tercero %s Se esperaba una Cartea de %s Pero se obtuvo una de %s" % (tercero.rasocial,expected_values["vttotal"],vttotal_cartera)

			#self.assertEqual(vttotal_cartera, expected_values["vttotal"],msg_error_assert_cartera)



		with open(self.name_file_template, 'r') as template:
			data=template.read().replace('::content::', str(document_html))



		report.write(str(data))
		report.close()
		webbrowser.open_new_tab(self.name_file_reporte)
