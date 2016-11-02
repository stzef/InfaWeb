from infa_web.settings import BASE_DIR
import json
import os.path
from django.core.exceptions import ImproperlyConfigured 

from infa_web.custom.utils import get_subdomain_by_name_db
from django.apps import AppConfig

class ManageParameters(object):
	def __init__(self,name_db):
		super(ManageParameters, self).__init__()
		self.name_db = name_db
		subdomain = get_subdomain_by_name_db(name_db)
		
		self.path_file = BASE_DIR + '/infa_web/params/' + self.name_db + '_params.json'
		if not os.path.isfile(self.path_file):
			raise ImproperlyConfigured(
				"Missing File Parameters. \nSubdomain : %s \nDatabase : %s \nPath : %s " % (subdomain,name_db,self.path_file)
			)

	def ok(self):
		try:
			with open(self.path_file) as json_data:
				return True
		except IOError as e:
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

	def to_dict(self):
		if not self.ok(): return None
		params_dict = {}
		try:
			with open(self.path_file) as json_data:
				parameters = json.load(json_data)
			for parameter in parameters:
				params_dict[parameter["cparam"]] = parameter["value"]
			return params_dict
		except IOError as e:
			return None

	"""def get_object_db(self,cparam):
		if not self.ok(): return None
		parameter = self.get_param_object(cparam)
		if parameter["type"] == "Model":
			apps = AppConfig()
			Model = apps.get_model(parameter["model"])
			kwargs = {}
			kwargs[parameter["field"]["value"]] = parameter["field"]["selected"]
			return Model.object.using(self.name_db).get(**kwargs)
	"""
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
