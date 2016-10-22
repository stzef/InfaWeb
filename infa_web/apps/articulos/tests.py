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

from infa_web.apps.base.data_test.arlo_mov_fac import data_mvens,data_mvsas,data_invs,data_facs,data_articles,costing_and_stock_expected_values
def fc(x):
	return locale.currency(x,grouping=True)
class ExampleTestCase(TestCase):

	using = "default"
	cii = None


	def setUp(self):
		c = Client()

		# Creacion De Articulo
		for data_article in data_articles:
			response_article_1 = c.post(reverse('add-article'),data_article,HTTP_X_REQUESTED_WITH='XMLHttpRequest')
			article_1 = json.loads(response_article_1.content)
			article_1 = json.loads(article_1["object"])[0]



		# Creacion de Inventario Inicial Cabeza
		response_inventory = c.post(reverse('inventory_latest'),HTTP_X_REQUESTED_WITH='XMLHttpRequest')
		inventory = json.loads(response_inventory.content)
		self.cii = inventory["code"]



		# Creacon de Inventario Inicial Detalle
		for data_inv in data_invs:
			for data_invdeta in data_inv["deta"]:
				article = Arlo.objects.get(carlos = data_invdeta["carlos"])

				canti = data_invdeta["canti"]
				vcosto = data_invdeta["vcosto"]

				cancalcu = article.canti

				ajuent = canti - article.canti
				ajusal = 0

				body_request_inventory = {
					"cii":str(self.cii),
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



		# Creacion de Movimientos Entrada
		for data_mven in data_mvens:
			body_request_mven_1 = data_mven["base"]
			it_mven = 1
			for data_mvendeta in data_mven["deta"]:
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



		# Creacion de Movimientos Salida
		for data_mvsa in data_mvsas:
			body_request_mvsa_1 = data_mvsa["base"]
			it_mvsa = 1
			for data_mvsadeta in data_mvsa["deta"]:
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



		# Creacion de Facturas
		for data_facdeta in data_facs:
			body_request_fac_contado = data_facdeta["base"]

			it_facdeta = 1
			for data_articulo in data_facdeta["deta"]:
				article = Arlo.objects.get(carlos=data_articulo["carlos"])

				canti = data_articulo["canti"]
				#vunita = data_articulo["vunita"]
				vunita = calcular_valor_unitario(article.carlos,1,data_articulo["pordes"],data_articulo["vunita"],self.using)

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
			for medio_pago in data_facdeta["medios_pagos"]:

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

			
			
			response_fac_contado = c.post(reverse('save-bill'),json.dumps(body_request_fac_contado),HTTP_X_REQUESTED_WITH='XMLHttpRequest',content_type="application/json")
			response_fac_contado = json.loads(response_fac_contado.content)



	def costing_and_stock(self):
		report = codecs.open("report.txt", "w", "utf-8")

		text = "\nCreacion de Articulos\n"
		print colored(text, 'white', attrs=['bold','reverse', 'blink'])
		report.write(text)
		data_table_articles = []
		for article in Arlo.objects.all():
			data_table_articles.append([article.carlos,article.nlargo,article.canti,fc(article.vcosto)])
		text = tabulate(data_table_articles,headers=["Cod", "Nombre","Cantidad","Costo"],tablefmt="fancy_grid")
		print text
		report.write(text)



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

		report.close()
