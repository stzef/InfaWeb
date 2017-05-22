from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#from infa_web.apps.base.middleware import my_local_global

class UserBackend(object):

	def authenticate(self, username = None, password = None, request_bd = None):
		UserModel = get_user_model()
		try:
			user = UserModel.objects.using(request_bd).get(username = username)
			if user.check_password(password):
				return user
		except UserModel.DoesNotExist:
			return None

	def get_user(self, user_id, *args):
		try:
			'''
				Modificacion al codigo duente de Django 1.9.6
				archivo django/contrib/auth/__init__.py
				function get_user
				linea 174

				...
				user = backend.get_user(user_id) # Original
				user = backend.get_user(user_id, request) # Modificada
				...

				Se agrego el request como parametro ( en la tupla args )

			'''
			request = args[0]
			return User.objects.using(request.db).get(pk=user_id)
			#return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
