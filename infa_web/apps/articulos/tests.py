from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


# Create your tests here.

from infa_web.apps.articulos.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.inventarios.models import *
from infa_web.routines import *

class ExampleTestCase(TestCase):

	def setUp(self):
		print "setup"
		c = Client()
		#csrf_client = Client(enforce_csrf_checks=True)
		response = c.post(reverse('add-article'),{
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
		print response.content

	def example(self):
		print "method"
