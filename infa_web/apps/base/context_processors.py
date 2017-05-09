from infa_web.apps.usuarios.models import Usuario

def var_globals(request):
	sucursal = None
	subdomain = None
	if request.user.is_authenticated():
		user_appem = Usuario.objects.using(request.db).get(user=request.user)
		sucursal = user_appem.csucur.nsucur
	if 'subdomain' in request:
		subdomain = request.subdomain
	return {
		'sucursal':sucursal,
		'subdomain':subdomain,
	}
