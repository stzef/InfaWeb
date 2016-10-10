from django.test import TestCase
from django.test import Client

# Create your tests here.

from infa_web.apps.articulos.models import *
from infa_web.apps.movimientos.models import *
from infa_web.apps.inventarios.models import *
from infa_web.routines import *

class ExampleCase(TestCase):

	def setUp(self):
		pass

	def example(self):
		c = Client()
		response = c.post('http://stzef.appem.com:8000/articles/add/', {},HTTP_X_REQUESTED_WITH='XMLHttpRequest')
		#response = c.post('http://stzef.appem.com:8000/articles/add/', {},content_type="multipart/form-data",HTTP_X_REQUESTED_WITH='XMLHttpRequest')
		print response
