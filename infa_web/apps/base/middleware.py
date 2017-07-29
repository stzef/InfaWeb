import os
from datetime import datetime
from infa_web.parameters import ManageParameters
from django.shortcuts import render,render_to_response, redirect
from django.http import HttpResponseNotFound
from termcolor import colored
from infa_web import settings
from infa_web.config import CONFIG

#from threading import local

#my_local_global = local()

class verifyConfigurationFile(object):
	def process_request(self, request):
		manageParameters = ManageParameters(request.db)
		if not manageParameters.ok():
			context = {"message":"Existe un problema con el Archivo de configuracion."}
			#return render_to_response("layouts/error.html",context)
			return render(request,"layouts/error.html",context)


class updateDateAppen(object):
	def process_request(self, request):

		request.session['empresa_actual'] = ""

		manageParameters = ManageParameters(request.db)
		current_date = datetime.now()
		current_date_format = current_date.strftime('%Y/%m/%d %H:%M:%S')

		#descomentarear Luego
		#manageParameters.set_param_object("date_appen",current_date_format)
		os.environ["date_appen"] = current_date_format


from infa_web.config.domaindb import DOMAINS
# Agrega al request el subdominio actual


class subdomainMiddleware:
	def process_request(self, request):
		print colored("\nCURRENT_DB (ENV) : %s\n" % (os.environ.get("CURRENT_DB")), 'white', attrs=['bold','reverse', 'blink'])

		host = request.META.get('HTTP_HOST', '')
		host = host.replace('www.', '').split('.')

		server = request.META.get('SERVER_NAME', '')
		if server == "testserver":
			request.subdomain = "test_local"
			request.db = DOMAINS[request.subdomain]
			#my_local_global.db = DOMAINS[request.subdomain]
			redirect('/dashboard')
		else:
			if len(host) > 2:
					request.subdomain = ''.join(host[:-2])
					# validar si dominio existe
					if not(request.subdomain in DOMAINS):
						return HttpResponseNotFound('<h1>' + request.subdomain + ' cuenta no existe.</h1>')
					request.db = DOMAINS[request.subdomain]

					print colored("CURRENT_DB (APP) : %s" % (request.db), 'white', attrs=['bold','reverse', 'blink'])
					print colored("Subdominio : %s\n" % (request.subdomain), 'white', attrs=['bold','reverse', 'blink'])

					redirect('/dashboard')

			else:
				request.db = 'default'
				redirect('/')

import pytz
from django.utils import timezone

class timeZoneMiddleware:
	def process_request(self, request):
		"""
		pass
		"""
		try:
			tzname = CONFIG[request.subdomain]["tz"]
			if tzname:
				timezone.activate(pytz.timezone(tzname))
			else:
				timezone.deactivate()
		except Exception as e:
			pass
		#if True:#'subdomain' in request:
