from django.test import TestCase
from django.test import Client

# Create your tests here.

from infa_web.apps.articulos.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.inventarios.models import *
from infa_web.routines import *

class ExampleCase(TestCase):
	c = Client()

	def setUp(self):
		print "hola"
		response = c.post('/article/add/', {'username': 'john', 'password': 'smith'})
		print response.status_code

	def example(self):
		print "hola"
