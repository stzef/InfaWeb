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
		#response = c.post('stzef.appem.com:8000/states/add/', {},HTTP_X_REQUESTED_WITH='XMLHttpRequest')
		#response = c.post(reverse('add-state'), {"nesdo":"a","cesdo":1})
		response = c.get("ttp://stzef.appem.com:8000/articles/add/")
		print response.content

	def example(self):
		print "method"
