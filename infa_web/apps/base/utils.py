from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from infa_web.apps.usuarios.models import Usuario
from infa_web.apps.restaurante_comandas.models import Meseros
from infa_web.apps.terceros.models import Vende

def get_or_none(Model, db, **kwargs):
	try:
		return Model.objects.using(db).get(**kwargs)
	except ObjectDoesNotExist:
		return None

def get_list_or_none(Model, db, **kwargs):
	obj_list = list(Model.objects.using(db).filter(**kwargs))
	if not obj_list:
		return None
	return obj_list


def get_current_user(name_db,request_user,user_django=False,user_appem=False,mesero=False,vendedor=False):
	o_mesero = None
	o_vendedor = None
	try:
		o_user_django = User.objects.using(name_db).get(username=request_user)
		try:
			o_user_appem = Usuario.objects.using(name_db).get(user= o_user_django)
			if mesero :
				o_mesero = Meseros.objects.using(name_db).get(usuario=o_user_appem)
			if vendedor :
				o_vendedor = Vende.objects.using(name_db).get(usuario=o_user_appem)
		except Usuario.DoesNotExist as e:
			o_user_appem = None
			o_mesero = None
			o_vendedor = None
	except User.DoesNotExist as e:
		o_user_django = None
		o_user_appem = None

	if user_django :
		return o_user_django
	if user_appem :
		return o_user_appem
	if mesero :
		return o_mesero
	if vendedor :
		return o_vendedor

	return None
