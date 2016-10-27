from django.test import TestCase  
from django.test import Client
from django.core.urlresolvers import reverse
import json
import codecs

import locale
locale.setlocale(locale.LC_ALL, '')

from termcolor import colored
from tabulate import tabulate

from infa_web.routines import costing_and_stock

from infa_web.bills_fn import *


# Create your tests here.

from infa_web.apps.articulos.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.inventarios.models import *
from infa_web.apps.facturacion.models import *
from infa_web.routines import *

from infa_web.apps.facturacion.views import ctimo_billing

from infa_web.apps.base.data_test.arlo_mov_fac import data_mvens,data_mvsas,data_invs,data_facs,data_edit_facs,data_articles,costing_and_stock_expected_values,cartera_expected_values

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

	#print json.dumps(body_request_fac_contado, indent=4)

	
	
	response_fac_contado = c.post(reverse('update-bill',args=[data["pk"]]),json.dumps(body_request_fac_contado),HTTP_X_REQUESTED_WITH='XMLHttpRequest',content_type="application/json")
	response_fac_contado = json.loads(response_fac_contado.content)

def list_articles(report):
	pass

def list_mven(report):
	text = "\nCreacion de Movimientos Entrada\n"
	print colored(text, 'white', attrs=['bold','reverse', 'blink'])
	report.write(text)
	for mven in Mven.objects.all():
		text = "Movimiento de Entrada %s\nFecha:%s\nDoc Ref:%s\nT Movimiento:%s\n" % (mven.cmven,mven.fmven,mven.docrefe,mven.ctimo)
		print text
		report.write(text)
		data_table_mven = []
		for mvendeta in Mvendeta.objects.filter(cmven = mven.cmven):
			data_table_mven.append([mvendeta.carlos.carlos,mvendeta.nlargo,mvendeta.canti,fc(mvendeta.vunita),fc(mvendeta.vtotal)])
		text = tabulate(data_table_mven,headers=["Cod","nombre", "Cantidad", "Vr. Unitario","Vr. Total"],tablefmt="fancy_grid")
		print text
		report.write(text)
		text = "\n"
		print text
		report.write(text)

def list_mvsa(report):
	text = "\nCreacion de Movimientos Salida\n"
	print colored(text, 'white', attrs=['bold','reverse', 'blink'])
	report.write(text)
	for mvsa in Mvsa.objects.all():
		text = "Movimiento de Entrada %s\nFecha:%s\nDoc Ref:%s\nT Movimiento:%s\n" % (mvsa.cmvsa,mvsa.fmvsa,mvsa.docrefe,mvsa.ctimo)
		print text
		report.write(text)
		data_table_mvsa = []
		for mvendeta in Mvsadeta.objects.filter(cmvsa = mvsa.cmvsa):
			data_table_mvsa.append([mvendeta.carlos.carlos,mvendeta.nlargo,mvendeta.canti,fc(mvendeta.vunita),fc(mvendeta.vtotal)])
		text = tabulate(data_table_mvsa,headers=["Cod","nombre", "Cantidad", "Vr. Unitario","Vr. Total"],tablefmt="fancy_grid")
		print text
		report.write(text)
		text = "\n"
		print text
		report.write(text)

def list_fac(report):
	text = "\nCreacion de Factura\n"
	print colored(text, 'white', attrs=['bold','reverse', 'blink'])
	report.write(text)
	for fac in Fac.objects.all():
		text = "Factura %s\nFecha:%s\nForma Pago:%s\nVr. Total:%s\n" % (fac.cfac,fac.femi,fac.ctifopa,fc(fac.vttotal))
		print text
		report.write(text)
		data_table_fac = []

		for facdeta in Facdeta.objects.filter(cfac = fac.pk):
			data_table_fac.append([facdeta.itfac,facdeta.carlos,facdeta.nlargo,facdeta.canti,facdeta.civa,fc(facdeta.vunita),fc(facdeta.vbase),fc(facdeta.viva),fc(facdeta.vtotal),facdeta.pordes,fc(facdeta.vcosto)])

		text = tabulate(data_table_fac,headers=["Item","Cod","Articulos","Cantidad","IVA","Vr. Unitario","Vr. Base","Vr. Iva","Vt Total","Descuento","Vr. costo"],tablefmt="fancy_grid")
		print text
		report.write(text)
		text = "\n"
		print text
		report.write(text)

def list_movi(report):
	text = "\nCreacion de Movimientos\n"
	print colored(text, 'white', attrs=['bold','reverse', 'blink'])
	report.write(text)
	for movi in Movi.objects.all():
		text = "Movimiento %s\nFecha:%s\nT Movi:%s\nVr. Total:%s\n" % (movi.cmovi,movi.fmovi,movi.ctimo,fc(movi.vttotal))
		print text
		report.write(text)
		data_table_movi = []

		for movideta in Movideta.objects.filter(cmovi = movi.pk):
			data_table_movi.append([movideta.itmovi,movideta.docrefe,fc(movideta.vmovi)])

		text = tabulate(data_table_movi,headers=["Item","Doc Ref", "Vr. Total"],tablefmt="fancy_grid")
		print text
		report.write(text)
		text = "\n"
		print text
		report.write(text)


class ExampleTestCase(TestCase):

	using = "default"
	cii = None


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
		report = codecs.open("report_test.txt", "w", "utf-8")



		text = "\nCreacion de Inventario Inicial\n"
		print colored(text, 'white', attrs=['bold','reverse', 'blink'])
		report.write(text)
		invinicab = Invinicab.objects.get(cii=self.cii)
		text = "Invetario Inicial Creado : %s\n" % self.cii
		print text
		report.write(text)



		data_table_invinideta = []
		for invinideta in Invinideta.objects.filter(cii=self.cii):
			data_table_invinideta.append([invinideta.carlos.carlos,invinideta.canti,fc(invinideta.vunita),fc(invinideta.vtotal),invinideta.cancalcu,invinideta.ajuent,invinideta.ajusal])
		text = tabulate(data_table_invinideta,headers=["Articulo", "Cantidad", "Costo","Vr. Total","Cant Calc","Ajus. Entra","Ajus. Sal"],tablefmt="fancy_grid")
		print text
		report.write(text)



		list_mvsa(report)

		list_mven(report)

		list_fac(report)

		list_movi(report)



		result_c_s = costing_and_stock(False,True,{},self.using)
		text = "\nCostos y Existencias Finales\n"
		print colored(text, 'white', attrs=['bold','reverse', 'blink'])
		report.write(text)
		data_table_costing_and_stock = []
		for article in Arlo.objects.all():
			data_table_costing_and_stock.append([article.carlos,article.nlargo,article.canti,fc(article.vcosto)])
			expected_values = costing_and_stock_expected_values[article.carlos]

			msg_error_assert_canti = "Se esperaba una Cantidad de %s para el Articulo %s - %s pero se obtuvo %s" %(expected_values["canti"],article.carlos,article.nlargo,article.canti)
			msg_error_assert_vcosto = "Se esperaba un Costo de %s para el Articulo %s - %s pero se obtuvo %s" %(expected_values["vcosto"],article.carlos,article.nlargo,article.vcosto)

			self.assertEqual(article.canti, expected_values["canti"],msg_error_assert_canti)
			self.assertEqual(float(article.vcosto), float(expected_values["vcosto"]),msg_error_assert_vcosto)

		text = tabulate(data_table_costing_and_stock,headers=["Cod","nombre", "Cantidad", "Vr. Unitario"],tablefmt="fancy_grid")
		print text
		report.write(text)



		text = "\nCartera por Tercero\n"
		print colored(text, 'white', attrs=['bold','reverse', 'blink'])
		report.write(text)
		for tercero in Tercero.objects.all():

			expected_values = cartera_expected_values[tercero.pk]

			text = "Tercero : %s\n" % tercero.rasocial
			print text
			report.write(text)
			
			ctimo_cr = ctimo_billing('ctimo_cxc_billing', self.using)
			ctimo_ab = ctimo_billing('ctimo_ab_billing', self.using)
			movidetas = Movideta.objects.using(self.using).filter(cmovi__citerce = tercero.pk, cmovi__ctimo__in = [ctimo_cr, ctimo_ab]).order_by('cmovi__fmovi')
			
			data_table_cartera = []
			vttotal_cartera = 0
			for movideta in movidetas:
				data_table_cartera.append([movideta.itmovi,movideta.docrefe,fc(movideta.vmovi)])
				vttotal_cartera += movideta.vmovi

			msg_error_assert_cartera = "Para el Tercero %s Se esperaba una Cartea de %s Pero se obtuvo una de %s" % (tercero.rasocial,expected_values["vttotal"],vttotal_cartera)
			
			self.assertEqual(vttotal_cartera, expected_values["vttotal"],msg_error_assert_cartera)

			text = tabulate(data_table_cartera,headers=["Item","Doc Ref", "Vr. Total"],tablefmt="fancy_grid")
			print text
			report.write(text)


		report.close()
