from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
import json



# Create your tests here.

from infa_web.apps.articulos.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.inventarios.models import *
from infa_web.routines import *

class ExampleTestCase(TestCase):

	def setUp(self):

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
				"pvta1":0,
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
				"pvta1":0,
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

		c = Client()

		# Creacion De Articulo
		for data_article in data_articles:
			response_article_1 = c.post(reverse('add-article'),data_article,HTTP_X_REQUESTED_WITH='XMLHttpRequest')
			article_1 = json.loads(response_article_1.content)
			article_1 = json.loads(article_1["object"])[0]
			print article_1

		# Creacion de Inventario Inicial Cabeza
		response_inventory = c.post(reverse('inventory_latest'),HTTP_X_REQUESTED_WITH='XMLHttpRequest')
		inventory = json.loads(response_inventory.content)

		# Creacon de Inventario Inicial Detalle
		for article in Arlo.objects.all():
			body_request_inventory = {
				"cii":str(inventory["code"]),
				"val_tot":"15000",
				"fii":"14/10/2016 08:22",
				"cesdo":"1",
				"data_r":json.dumps([
					{
						"carlos":str(article.carlos),
						"nlargo":str(article.nlargo),
						"cancalcu":"0",
						"canti":"50",
						"vcosto":"300",
						"ajuent":"50",
						"ajusal":"0",
						"cbarras":"",
					}
				])
			}
			response_inventory_deta_1 = c.post(reverse('inventory_save'),body_request_inventory,HTTP_X_REQUESTED_WITH='XMLHttpRequest')

		

		# Creacion de Movimientos
		# Creacion de Movimientos Entrada
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
		for article in Arlo.objects.all():
			canti = 2
			vunita = 300
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

		body_request_mvsa_1 = {
			"mode_view":"create",
			"cmvsa":"",
			"ctimo":"1001",
			"fmvsa":"2016-10-13",
			"citerce":"1",
			"name__citerce":"MOSTRADOR",
			"docrefe":"RA00001",
			"descri":"-",
			"cesdo":"1",
			"cbode0":"1",
			"vttotal":0,
			"is_input_movement":False,
			"mvdeta":[]
		}
		it_mvsa = 1
		for article in Arlo.objects.all():
			canti = 1
			vunita = 300
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


		for article in Arlo.objects.all():
			print ".-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
			print ".-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
			print article.nlargo
			print article.canti
			print article.vcosto
			print ".-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
			print ".-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"

	def example(self):
		pass
