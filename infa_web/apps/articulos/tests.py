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
		c = Client()
		#csrf_client = Client(enforce_csrf_checks=True)

		# Creacion De Articulo
		response_article_1 = c.post(reverse('add-article'),{
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
		},HTTP_X_REQUESTED_WITH='XMLHttpRequest')
		article_1 = json.loads(response_article_1.content)
		article_1 = json.loads(article_1["object"])[0]

		# Creacion de Inventario Inicial Cabeza
		response_inventory = c.post(reverse('inventory_latest'),HTTP_X_REQUESTED_WITH='XMLHttpRequest')
		inventory = json.loads(response_inventory.content)

		# Creacon de Inventario Inicial Detalle
		response_inventory_deta_1 = c.post(reverse('inventory_save'),{
																		"cii":str(inventory["code"]),
																		"val_tot":"15000",
																		"fii":"14/10/2016 08:22",
																		"cesdo":"1",
																		"data_r":json.dumps([
																			{
																				"carlos":str(article_1["pk"]),
																				"nlargo":str(article_1["fields"]["nlargo"]),
																				"cancalcu":"0",
																				"canti":"50",
																				"vcosto":"300",
																				"ajuent":"50",
																				"ajusal":"0",
																				"cbarras":"",
																			}
																		])
																	},HTTP_X_REQUESTED_WITH='XMLHttpRequest')

		# Creacion de Movimientos
		# Creacion de Movimientos Entrada
		response_mven_1 = c.post(reverse('save-movement'),)


		print ".-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
		print ".-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
		print response_inventory_deta_1.content
		print ".-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
		print ".-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
		#response_inventory_deta_2 = c.post(reverse('inventory_save'),{},HTTP_X_REQUESTED_WITH='XMLHttpRequest')
		#response_inventory_deta_3 = c.post(reverse('inventory_save'),{},HTTP_X_REQUESTED_WITH='XMLHttpRequest')

	def example(self):
		pass
