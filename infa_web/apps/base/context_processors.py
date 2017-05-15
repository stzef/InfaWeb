# -*- coding: utf-8 -*-

from infa_web.apps.usuarios.models import Usuario
from infa_web.parameters import ManageParameters


def var_globals(request):
	types_currency = {
		"colon" : {"symbol":"₡"},
		"peso-colombiano" : {"symbol":"$"},
	}

	manageParameters = ManageParameters(request.db)
	parameters = manageParameters.to_dict()

	parameters["symbol_currency"] = types_currency[parameters["type_currency"]]["symbol"]


	sucursal = None
	subdomain = None
	if request.user.is_authenticated():
		try:
			user_appem = Usuario.objects.using(request.db).get(user=request.user)
			sucursal = user_appem.csucur.nsucur
		except Usuario.DoesNotExist:
			user_appem = None
			sucursal = None
	if 'subdomain' in request:
		subdomain = request.subdomain
	return {
		'sucursal':sucursal,
		'subdomain':subdomain,
		'gparameters':parameters,
	}
