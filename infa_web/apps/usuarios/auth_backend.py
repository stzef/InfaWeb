from django.contrib.auth import get_user_model

class UserBackend(object):

	def authenticate(self, username = None, password = None, request_bd = None):
		UserModel = get_user_model()
		try:
			user = UserModel.objects.using(request_bd).get(username = username)
			if user.check_password(password):
				return user
		except UserModel.DoesNotExist:
			return None