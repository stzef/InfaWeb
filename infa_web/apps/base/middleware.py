from infa_web.parameters import ManageParameters
from django.shortcuts import render,render_to_response

class verifyConfigurationFile(object):
	def process_request(self, request):
		manageParameters = ManageParameters()
		if not manageParameters.ok():
			print "Middleware executed"
			context = {"message":"Existe un problema con el Archivo de configuracion."}
			return render_to_response("layouts/error.html",context)

	"""def process_response(self, request, response):
		return response"""
