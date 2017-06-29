# -*- coding: utf-8 -*-

from infa_web.apps.usuarios.models import Usuario
from infa_web.apps.base.models import Modules, NavMenus

from infa_web.parameters import ManageParameters
from infa_web.custom.utils import get_user_permissions
import datetime
from django.utils import timezone

from infa_web.custom.utils import get_nav_menu, get_quick_access


def var_globals(request):
	types_currency = {
		"colon" : {"symbol":"₡"},
		"peso-colombiano" : {"symbol":"$"},
	}

	manageParameters = ManageParameters(request.db)
	parameters = manageParameters.to_dict()

	nav_menu = get_nav_menu(request.user.get_all_permissions(),request.db)
	nav_quick_access = get_quick_access(request.user.get_all_permissions(),request.db)

	# "-------------------"
	# request.user.get_all_permissions()
	# type(request.user.get_all_permissions())
	# 'restaurante_comandas.delete_mesas' in request.user.get_all_permissions()
	# "-------------------"

	parameters["symbol_currency"] = types_currency[parameters["type_currency"]]["symbol"]

	modules = Modules.objects.using(request.db).filter(enabled_enterprise=True,enabled=True)

	sucursal = None
	subdomain = None
	if request.user.is_authenticated():
		try:
			user_appem = Usuario.objects.using(request.db).get(user=request.user)
			sucursal = user_appem.csucur.nsucur
			d1 = request.user.date_joined
			now = timezone.now() # datetime.datetime.now()
			dif = now - d1
			print (dif.days)
		except Usuario.DoesNotExist:
			user_appem = None
			sucursal = None
	if 'subdomain' in request:
		subdomain = request.subdomain
	return {
		'sucursal':sucursal,
		'subdomain':subdomain,
		'gparameters':parameters,
		'modules':modules,
		'nav_menu':nav_menu,
		'nav_quick_access':nav_quick_access,
	}
