from django.test import TestCase

from infa_web.apps.articulos.models import *
from infa_web.apps.movimientos.models import *
from infa_web.routines import *

class AnimalTestCase(TestCase):
	def setUp(self):
		pass

	def test_animals_can_speak(self):
		calculo_cantidad_costo()
		self.assertEqual(True,True)
