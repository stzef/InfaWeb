import os
from datetime import datetime
from infa_web.parameters import ManageParameters
from django.shortcuts import render,render_to_response

class verifyConfigurationFile(object):
	def process_request(self, request):
		manageParameters = ManageParameters()
		if not manageParameters.ok():
			context = {"message":"Existe un problema con el Archivo de configuracion."}
			return render_to_response("layouts/error.html",context)


class updateDateAppen(object):
	def process_request(self, request):

		request.session['empresa_actual'] = ""

		manageParameters = ManageParameters()
		current_date = datetime.now()
		current_date_format = current_date.strftime('%Y/%m/%d %H:%M:%S')
		manageParameters.set_param_object("date_appen",current_date_format)
		os.environ["date_appen"] = current_date_format


