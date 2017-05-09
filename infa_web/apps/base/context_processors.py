from infa_web.apps.usuarios.models import Usuario

def var_globals(request):
	user_appem = Usuario.objects.using(request.db).get(user=request.user)
	sucursal = user_appem.csucur.nsucur
	return {
		'sucursal':sucursal,
		'subdomain':request.subdomain,
	}
