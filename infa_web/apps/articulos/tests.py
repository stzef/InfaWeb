from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
import json

from termcolor import colored
from tabulate import tabulate

from infa_web.routines import costing_and_stock

from infa_web.bills_fn import *


# Create your tests here.

from infa_web.apps.articulos.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.inventarios.models import *
from infa_web.routines import *

class ExampleTestCase(TestCase):

	using = "default"


	def setUp(self):
		c = Client()

		data_mvens = [
			[
				{
					"carlos" : 1000,
					"canti" : 10,
					"vunita" : 1000
				},
				{
					"carlos" : 1001,
					"canti" : 10,
					"vunita" : 1000
				},
			],
		]

		data_mvsas = [
			[
				{
					"carlos" : 1000,
					"canti" : 10,
					"vunita" : 1000
				},
				{
					"carlos" : 1001,
					"canti" : 10,
					"vunita" : 1000
				},
			],
		]

		data_invs = [
			{
				"cii" : "",
				"deta" : [
					{
						"carlos" : 1000,
						"canti" : 10,
						"vcosto" : 500
					},
					{
						"carlos" : 1001,
						"canti" : 10,
						"vcosto" : 500
					}
				]
			}
		]
		"""
		{
			"cmpago" : 1000,
			"nmpago" : "Efectivo",
			"porcentaje" : 0,
		},
		{
			"cmpago" : 1001,
			"nmpago" : "Tarjeta",
			"porcentaje" : 0,
		},
		{
			"cmpago" : 1002,
			"nmpago" : "Cheque",
			"porcentaje" : 0,
		},
		{
			"cmpago" : 1003,
			"nmpago" : "Nota Credito",
			"porcentaje" : 0,
		},
		"""
		data_facs = [
			{
				"brtefte":0,
				"prtefte":0,
				"medios_pagos":[
						{
							"cmpago" : 1000,
							"nmpago" : "Efectivo",
							"porcentaje" : 100,
							"docmpago" : 0,
							"banmpago" : 1000,
						},
				],
				"deta":[
					{
						"carlos" : 1000,
						"canti" : 5,
						"vunita" : 500,
						"pordes" : 0,
						"civa" :1,
					},
					{
						"carlos" : 1001,
						"canti" : 5,
						"vunita" : 500,
						"pordes" : 0,
						"civa" :1,
					},
				],
			},
		]

		data_articles = [
			{
				"cbarras":4634563421231,
				"ncorto":"Articulo 1",
				"refe":"",
				"nlargo":"Articulo 1",
				"cgpo":1,
				"cmarca":1,
				"ctiarlo":1,
				"cunidad":1,
				"canti":0,
				"vcosto":0,
				"porult1":0,
				"pvta1":500,
				"porult2":0,
				"pvta2":0,
				"porult3":0,
				"pvta3":0,
				"porult4":0,
				"pvta4":0,
				"porult5":0,
				"pvta5":0,
				"porult6":0,
				"pvta6":0,
				"ifcostear":"on",
				"stomin":1,
				"stomax":100,
				"mesesgara":0,
				"ivas_civa":1,
				"cubica":1,
				"cesdo":1
			},
			{
				"cbarras":98078967898978,
				"ncorto":"Articulo 2",
				"refe":"",
				"nlargo":"Articulo 2",
				"cgpo":1,
				"cmarca":1,
				"ctiarlo":1,
				"cunidad":1,
				"canti":0,
				"vcosto":0,
				"porult1":0,
				"pvta1":500,
				"porult2":0,
				"pvta2":0,
				"porult3":0,
				"pvta3":0,
				"porult4":0,
				"pvta4":0,
				"porult5":0,
				"pvta5":0,
				"porult6":0,
				"pvta6":0,
				"ifcostear":"on",
				"stomin":1,
				"stomax":100,
				"mesesgara":0,
				"ivas_civa":1,
				"cubica":1,
				"cesdo":1
			},
		]

		# Creacion De Articulo
		print colored("\nCreacion de Articulos", 'white', attrs=['bold','reverse', 'blink'])
		data_table_articles = []
		for data_article in data_articles:
			response_article_1 = c.post(reverse('add-article'),data_article,HTTP_X_REQUESTED_WITH='XMLHttpRequest')
			article_1 = json.loads(response_article_1.content)
			article_1 = json.loads(article_1["object"])[0]
			data_table_articles.append([article_1["pk"],article_1["fields"]["nlargo"]])
		print tabulate(data_table_articles,headers=["Cod", "Nombre"],tablefmt="fancy_grid")



		# Creacion de Inventario Inicial Cabeza
		print colored("\nCreacion de Inventario Inicial", 'white', attrs=['bold','reverse', 'blink'])
		response_inventory = c.post(reverse('inventory_latest'),HTTP_X_REQUESTED_WITH='XMLHttpRequest')
		inventory = json.loads(response_inventory.content)
		print "Invetario Inicial Creado : " + inventory["code"]



		# Creacon de Inventario Inicial Detalle
		data_table_invinideta = []
		for data_inv in data_invs:
			for data_invdeta in data_inv["deta"]:
				article = Arlo.objects.get(carlos = data_invdeta["carlos"])

				canti = data_invdeta["canti"]
				vcosto = data_invdeta["vcosto"]

				cancalcu = article.canti

				ajuent = canti - article.canti
				ajusal = 0

				body_request_inventory = {
					"cii":str(inventory["code"]),
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
				data_table_invinideta.append([article.carlos,canti,vcosto])
			print tabulate(data_table_invinideta,headers=["Articulo", "Cantidad", "Costo"],tablefmt="fancy_grid")



		# Creacion de Movimientos
		# Creacion de Movimientos Entrada
		print colored("\nCreacion de Movimientos Entrada", 'white', attrs=['bold','reverse', 'blink'])
		for data_mven in data_mvens:
			body_request_mven_1 = {
				"mode_view":"create",
				"cmven":"",
				"ctimo":"1001",
				"fmven":"2016-10-13",
				"citerce":"1",
				"name__citerce":"MOSTRADOR",
				"docrefe":"RA00001",
				"descri":"-",
				"cesdo":"1",
				"cbode0":"1",
				"vttotal":0,
				"is_input_movement":True,
				"mvdeta":[]
			}
			it_mven = 1
			data_table_mven = []
			for data_mvendeta in data_mven:
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
				data_table_mven.append([article.carlos,article.nlargo,canti,vunita])
			response_mven_1 = c.post(reverse('save-movement'),json.dumps(body_request_mven_1),HTTP_X_REQUESTED_WITH='XMLHttpRequest',content_type="application/json")
			print tabulate(data_table_mven,headers=["Cod","nombre", "Cantidad", "V Unitario"],tablefmt="fancy_grid")



		# Creacion de Movimientos Salida
		print colored("\nCreacion de Movimientos Salida", 'white', attrs=['bold','reverse', 'blink'])
		for data_mvsa in data_mvsas:
			body_request_mvsa_1 = {
				"mode_view":"create",
				"cmvsa":"",
				"ctimo":"2001",
				"fmvsa":"2016-10-13",
				"citerce":"1",
				"name__citerce":"MOSTRADOR",
				"docrefe":"SA00001",
				"descri":"-",
				"cesdo":"1",
				"cbode0":"1",
				"vttotal":0,
				"is_input_movement":False,
				"mvdeta":[]
			}
			it_mvsa = 1
			data_table_mvsa = []
			for data_mvsadeta in data_mvsa:
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

				data_table_mvsa.append([article.carlos,article.nlargo,canti,vunita])
			response_mvsa_1 = c.post(reverse('save-movement'),json.dumps(body_request_mvsa_1),HTTP_X_REQUESTED_WITH='XMLHttpRequest',content_type="application/json")
			print tabulate(data_table_mvsa,headers=["Cod","nombre", "Cantidad", "V Unitario"],tablefmt="fancy_grid")



		# Creacion de Facturas - CONTADO
		print colored("\nCreacion de Factura - CONTADO", 'white', attrs=['bold','reverse', 'blink'])
		

		body_request_fac_contado = {
			"mode_view":"create",
			"cfac":"",
			"citerce":"1",
			"name__citerce":"MOSTRADOR",
			"cvende":"1",
			"cdomici":"1",
			"ctifopa":"1001",
			"femi":"2016-10-18",
			"fpago":"2016-10-18",
			"cemdor":"1",
			"ccaja":"1",
			"cesdo":"1",
			"descri":"",
			"vttotal":0,
			"ventre":0,
			"vcambio":0,
			"vtbase":0,
			"vtiva":0,
			"brtefte":0,
			"prtefte":0,
			"vrtefte":0,
			"vflete":0,
			"vdescu":0,
			"it":"",
			"cmpago":"",
			"vmpago":"",
			"medios_pagos":[],
			"mvdeta":[]
		}
		data_table_fac = []
		for data_facdeta in data_facs:
			body_request_fac_contado["brtefte"] = data_facdeta["brtefte"]
			body_request_fac_contado["prtefte"] = data_facdeta["prtefte"]

			it_facdeta = 1
			for data_articulo in data_facdeta["deta"]:
				article = Arlo.objects.get(carlos=data_articulo["carlos"])

				canti = data_articulo["canti"]
				#vunita = data_articulo["vunita"]
				vunita = calcular_valor_unitario(article.carlos,1,data_articulo["pordes"],self.using)

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

			it_facpagodeta = 1
			for medio_pago in data_facdeta["medios_pagos"]:
				temp_mp = {
					"it":it_facpagodeta,
					"cmpago":medio_pago["cmpago"],
					"docmpago":medio_pago["docmpago"],
					"banmpago":medio_pago["banmpago"],
					"vmpago":body_request_fac_contado["vttotal"] * ( medio_pago["porcentaje"] / 100 )
				}
				it_facpagodeta += 1
				body_request_fac_contado["medios_pagos"].append(temp_mp)

			body_request_fac_contado["vcambio"] = calcular_valor_cambio(body_request_fac_contado["ventre"],body_request_fac_contado["vttotal"])
			body_request_fac_contado["vttotal"] = calcular_total(body_request_fac_contado["mvdeta"],body_request_fac_contado["vflete"],body_request_fac_contado["vdescu"])
			
			body_request_fac_contado["vrtefte"] = calcular_total_flete(body_request_fac_contado["brtefte"],body_request_fac_contado["prtefte"])
			
			response_fac_contado = c.post(reverse('save-bill'),json.dumps(body_request_fac_contado),HTTP_X_REQUESTED_WITH='XMLHttpRequest',content_type="application/json")
			response_fac_contado = json.loads(response_fac_contado.content)
			data_table_fac.append([response_fac_contado["cfac"]])

		#print json.dumps(body_request_fac_contado,indent=4)
		print tabulate(data_table_fac,headers=["Cod"],tablefmt="fancy_grid")



	def costing_and_stock(self):

		costing_and_stock(False,True,{},self.using)


		print colored("\nCostos y Existencias Finales", 'white', attrs=['bold','reverse', 'blink'])
		data_table_costing_and_stock = []
		for article in Arlo.objects.all():
			data_table_costing_and_stock.append([article.carlos,article.nlargo,article.canti,article.vcosto])
		print tabulate(data_table_costing_and_stock,headers=["Cod","nombre", "Cantidad", "V Unitario"],tablefmt="fancy_grid")
