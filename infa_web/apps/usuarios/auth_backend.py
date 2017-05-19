from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from infa_web.apps.base.middleware import my_local_global

class UserBackend(object):

	def authenticate(self, username = None, password = None, request_bd = None):
		UserModel = get_user_model()
		try:
			user = UserModel.objects.using(request_bd).get(username = username)
			if user.check_password(password):
				return user
		except UserModel.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			print "-------------------"
			print my_local_global.db
			print "-------------------"
			return User.objects.using(my_local_global.db).get(pk=user_id)
		except User.DoesNotExist:
			return None
