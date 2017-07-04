import json

from .forms import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from infa_web.apps.usuarios.forms import *
from django.http import HttpResponse, JsonResponse

from infa_web.apps.base.constantes import *

from django.contrib.auth.models import User, Group
from infa_web.apps.terceros.models import Vende
from infa_web.apps.restaurante_comandas.models import Meseros,Talocoda
from infa_web.apps.usuarios.models import Usuario
from infa_web.apps.base.models import Talo

from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def RegistarUsuario(request):
	if request.method == "GET" :
		form = ManageUsers(request.db)
		return render(request, 'usuarios/registrar.html', {'form': form})


	data = request.POST

	# General
	cesdo = CESDO_ACTIVO
	estado = Esdo.objects.using(request.db).get(cesdo=cesdo)

	ccaja = data["ccaja"]
	caja = Caja.objects.using(request.db).get(ccaja=ccaja)

	csucur = data["csucur"]
	sucursal = Sucursales.objects.using(request.db).get(csucur=csucur)

	foto = "1" # data["foto"]
	ctalocoda = "1" # data["ctalocoda"]
	talocoda = Talocoda.objects.using(request.db).get(ctalocoda=ctalocoda)
	porventa = "0" # data["porventa"]
	# User Django
	first_name = data["first_name"]
	last_name = data["last_name"]
	username = data["username"]
	password = data["password"]
	cpassword = data["cpassword"]
	auth_cgrupo = data["auth_cgrupo"]
	# User App
	finusu = "2017-05-12 00:00:00" # data["factivacion"]
	fveusu = "2017-05-12 00:00:00" # data["fdesactivacion"]
	ifprises = "1" # data["ifprises"]
	ctalomos = data["ctalo"] # data["ctalomos"]
	talomos = Talo.objects.using(request.db).get(ctalo=ctalomos)
	ctalopos = data["ctalo"] # data["ctalopos"]
	talopos = Talo.objects.using(request.db).get(ctalo=ctalopos)
	# Vendedor
	nvende = "%s %s" % (first_name,last_name)
	# Meseros
	nmero = "%s %s" % (first_name,last_name)
	telmero = " - "
	dirmero = " - "

	issuperuser = False # data["direccion"]



	response = {
		"message" : "El usuario %s Se registro." % username
	}
	# Crear Usuario Django
	try:
		user = User(
			first_name=first_name,
			is_staff=issuperuser,
			is_superuser=issuperuser,
			last_name=last_name,
			username=username,
		)
		if 'password' in data and 'cpassword' in data:
			if data['password'] != "":
				if data['password'] == data['cpassword'] :
					user.set_password(data['password'])
				else:
					response["message"] = "Las claves no coinciden"
					return HttpResponse(json.dumps(response), "application/json",status=400)

		user.save(using=request.db)

		user.groups.clear()
		group = Group.objects.using(request.db).get(id=auth_cgrupo)
		user.groups.add(group)
	except Exception as e:
		print e
		response["message"] = "Ha Ocurrido un Error"
		if 'auth_user_username_key' in e.message:
			response["message"] = "El Nombre de Usuario %s ya Existe" % username
		return HttpResponse(json.dumps(response), "application/json",status=400)


	usuario = Usuario(
		user = user,
		finusu = finusu,
		fveusu = fveusu,
		cesdo = estado,
		foto = foto,
		ifprises = ifprises,
		ccaja = caja,
		ctalomos = talomos,
		ctalopos = talopos,
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
		ctalocoda = talocoda,
		cesdo = estado,
		telmero = telmero,
		dirmero = dirmero,
		foto = foto,
		usuario = usuario,
	)
	mesero.save(using=request.db)

	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def AdministrarUsuario(request):

	if request.method == "GET" :
		usuarios = User.objects.using(request.db).all().order_by("username")
		form = ManageUsers(request.db)

		for usuario in usuarios:
			try:
				usuario.appemuser = Usuario.objects.using(request.db).get(user=usuario)
			except Exception as e:
				usuario.appemuser = None
		return render(request, 'usuarios/administrar.html', {'usuarios': usuarios,'form': form})

	response = {
		"message" : "Edicion de usuarios completada"
	}

	data = request.POST

	cesdo = CESDO_ACTIVO
	estado = Esdo.objects.using(request.db).get(cesdo=cesdo)

	first_name = data["first_name"]
	last_name = data["last_name"]
	npassword = data["npassword"]
	cpassword = data["cpassword"]

	nvende = "%s %s" % (first_name,last_name)
	# Meseros
	nmero = "%s %s" % (first_name,last_name)

	if 'ccaja' in data and data['ccaja'] != "":
		ccaja = data["ccaja"]
		caja = Caja.objects.using(request.db).get(ccaja=ccaja)

	if 'csucur' in data and data['csucur'] != "":
		csucur = data["csucur"]
		sucursal = Sucursales.objects.using(request.db).get(csucur=csucur)

	if 'ctalo' in data and data['ctalo'] != "":
		ctalomos = data["ctalo"] # data["ctalomos"]
		talomos = Talo.objects.using(request.db).get(ctalo=ctalomos)

	if 'ctalo' in data and data['ctalo'] != "":
		ctalopos = data["ctalo"] # data["ctalopos"]
		talopos = Talo.objects.using(request.db).get(ctalo=ctalopos)

	user = User.objects.using(request.db).get(id=data["id"])

	user.email = data["email"]
	user.first_name = data["first_name"]
	user.last_name = data["last_name"]

	user.is_active = True if "is_active" in data else False
	user.is_superuser = True if "is_superuser" in data else False

	user.date_joined = data["date_joined"]

	if 'npassword' in data and 'cpassword' in data:
		if data['npassword'] != "":
			if data['npassword'] == data['cpassword'] :
				print data['npassword']
				user.set_password(data['npassword'])
				response["message"] = "Clave cambiada"
			else:
				response["message"] = "Las claves no coinciden"
				return HttpResponse(json.dumps(response), "application/json",status=400)



	user.save(using=request.db)

	try:
		usuario = Usuario.objects.using(request.db).get(user=user)
		#usuario.cesdo =
		#usuario.foto =

		if 'ccaja' in data and data["ccaja"] != "":
			usuario.ccaja = caja
		if 'csucur' in data and data["csucur"] != "":
			usuario.csucur = sucursal
		if 'ctalo' in data and data["ctalo"] != "":
			usuario.ctalomos = talomos
			usuario.ctalopos = talopos
		if 'auth_cgrupo' in data and data["auth_cgrupo"] != "":
			auth_cgrupo = data["auth_cgrupo"]

		usuario.save(using=request.db)
	except Exception as e:
		response["message"] += "<br>No se ha podido actualizar el Usuario"

	try:
		vendedor = Vende.objects.using(request.db).get(usuario=usuario)
		nvende = "%s %s" %(user.first_name, user.last_name)
		#porventa =
		#cesdo =
		vendedor.save(using=request.db)
	except Exception as e:
		response["message"] += "<br>No se ha podido actualizar el Vendedor"


	try:
		mesero = Meseros.objects.using(request.db).get(usuario=usuario)
		mesero.nmero = "%s %s" %(user.first_name, user.last_name)
		#mesero.ctalocoda =
		#mesero.cesdo =
		#mesero.telmero =
		#mesero.dirmero =
		#mesero.foto =
		mesero.save(using=request.db)
	except Exception as e:
		response["message"] += "<br>No se ha podido actualizar el Mesero"

	return JsonResponse(response)


