from infa_web.settings import BASE_DIR
import json
import os.path

from infa_web.custom.utils import get_subdomain_by_name_db

class ManageParameters(object):
	def __init__(self,domain):
		super(ManageParameters, self).__init__()
		self.domain = domain

		print "--------------------"
		print get_subdomain_by_name_db(domain) + " : " + domain
		print "--------------------"

		self.path_file = BASE_DIR + '/infa_web/params/' + self.domain + '_params.json'
		if not os.path.isfile(self.path_file):
			print "----------------------------file no exists------------------"


	def ok(self):
		try:
			with open(self.path_file) as json_data:
				return True
		except IOError as e:
			print e
			return False

	def get_all(self):
		if not self.ok(): return None

		try:
			with open(self.path_file) as json_data:
				return json.load(json_data)
			return False
		except IOError as e:
			return None
			#print "I/O error({0}): {1}".format(e.errno, e.strerror)

	def set_param_object(self,cparam,value):
		if not self.ok(): return None
		try:
			with open(self.path_file) as json_data:
				parameters = json.load(json_data)
			for parameter in parameters:
				if(parameter["cparam"] == cparam):
					parameter["value"] = value
					parameter["field"]["selected"] = value
					break

			if(self.save(parameters)):
				return True
			else:
				return False
		except IOError as e:
			return None

	def get_param_object(self,cparam):
		if not self.ok(): return None
		try:
			with open(self.path_file) as json_data:
				parameters = json.load(json_data)
			for parameter in parameters:
				if(parameter["cparam"] == cparam):
					return parameter
			return False
		except IOError as e:
			return None

	def save(self,parameters):
		if not self.ok(): return None
		try:
			with open(self.path_file,'r+') as json_data:
				json_data.seek(0)
				json_data.write(json.dumps(parameters, indent=4))
				json_data.truncate()
			return True
		except IOError as e:
			return False

	def get_param_value(self,cparam):
		if not self.ok(): return None
		try:
			with open(self.path_file) as json_data:
				parameters = json.load(json_data)
			for parameter in parameters:
				if(parameter["cparam"] == cparam):
					return parameter["value"]
			return False
		except IOError as e:
			return None
