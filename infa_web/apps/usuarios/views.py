from .forms import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from infa_web.apps.usuarios.forms import *

from django.contrib.auth.models import User
from infa_web.apps.terceros.models import Vende
from infa_web.apps.restaurante_comandas.models import Meseros
from infa_web.apps.usuarios.models import Usuario


class loginView(FormView):
	template_name = 'usuarios/login.html'
	success_url = '/dashboard'
	form_class = loginForm

	def get_context_data(self, **kwargs):
		context = super(loginView, self).get_context_data(**kwargs)
		# context['domain'] = self.request.subdomain
		return context

	def form_valid(self, form):
		response = form.auth_user(request_bd = self.request.db)
		if response is not None:
			auth_login(self.request, response)
			return HttpResponseRedirect('/dashboard')
		else:
			return self.form_invalid(form)
		return super(loginView, self).form_valid(form)
def RegistarUsuario(request):
	if request.method == "GET" :
		form = ManageUsers(request.db)
		return render(request, 'usuarios/registrar.html', {'form': form})

	data = json.loads(request.body)

	# General
	cesdo = data["cesdo"]
	estado = Esdo.objects.using(request.db).get(cesdo=cesdo)

	ccaja = data[""]
	caja = Caja.objects.using(request.db).get(ccaja=ccaja)

	csucur = data[""]
	sucursal = Sucursales.objects.using(request.db).get(csucur=csucur)

	foto = data[""]
	ctalocoda = data[""]
	porventa = data[""]
	# User Django
	first_name = data["first_name"]
	last_name = data["last_name"]
	username = data["username"]
	password = data["password"]
	cpassword = data["cpassword"]
	# User App
	finusu = data["factivacion"]
	fveusu = data["fdesactivacion"]
	ifprises = data[""]
	ctalomos = data[""]
	ctalopos = data[""]
	# Vendedor
	nvende = "%s %s" % (first_name,last_name)
	# Meseros
	nmero = "%s %s" % (first_name,last_name)
	telmero = data["telefono"]
	dirmero = data["direccion"]

	# Crear Usuario Django
	user = User(
		first_name=first_name,
		is_staff=False,
		is_superuser=True,
		last_name=last_name,
		username=username,
	)
	user.set_password(password)
	user.save(using=request.db)

	usuario = Usuario(
		user = user,
		finusu = finusu,
		fveusu = fveusu,
		cesdo = estado,
		foto = foto,
		ifprises = ifprises,
		ccaja = caja,
		ctalomos = ctalomos,
		ctalopos = ctalopos,
		csucur = sucursal,
	)
	usuario.save(using=request.db)
	vendedor = Vende(
		#cvende,
		nvende = nvende,
		porventa = porventa,
		cesdo = estado,
		usuario = usuario,
	)
	vendedor.save(using=request.db)
	mesero = Meseros(
		#cmero,
		nmero = nmero,
		ctalocoda = ctalocoda,
		cesdo = estado,
		telmero = telmero,
		dirmero = dirmero,
		foto = foto,
		usuario = usuario,
	)

	response = {}
	return HttpResponse(json.dumps(response), "application/json")
