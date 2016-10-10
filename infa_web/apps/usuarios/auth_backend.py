from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class UserBackend(object):

	def authenticate(self, username = None, password = None, request_bd = None):
		try:
			print request_bd
			user_model = User.objects.using(request_bd).get(username = username)
			if user_model.check_password(password):
				return user_model
			return None
		except User.DoesNotExist:
			return None