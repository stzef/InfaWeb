from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class UserBackend(object):

	def authenticate(self, username = None, password = None, request_bd = None):
		return None
		UserModel = get_user_model()
		try:
			user = UserModel.objects.using(request_bd).get(username = username)
			if user.check_password(password):
				return user
		except UserModel.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
