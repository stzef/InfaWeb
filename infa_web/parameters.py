from infa_web.settings import BASE_DIR
import json
class ManageParameters(object):
	def __init__(self):
		super(ManageParameters, self).__init__()
		self.path_file = BASE_DIR + '/infa_web/params/params.json'


	def get_all(self):
		try:
			with open(self.path_file) as json_data:
				return json.load(json_data)
		except IOError as e:
			print "--------------------------"
			print type(e)
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
			print "--------------------------"
			return e
	def get_param_object(self,cparam):
		try:
			with open(self.path_file) as json_data:
				parameters = json.load(json_data)
			for parameter in parameters:
				if(parameter["cparam"] == cparam):
					return parameter
		except IOError as e:
			return e

	def save(self,parameters):
		try:
			with open(self.path_file,'r+') as json_data:
				json_data.seek(0)
				json_data.write(json.dumps(parameters, indent=4))
				json_data.truncate()
			return True
		except IOError as e:
			return e

	def get_param_value(self,cparam):
		try:
			with open(self.path_file) as json_data:
				parameters = json.load(json_data)
			for parameter in parameters:
				if(parameter["cparam"] == cparam):
					return parameter["value"]
		except IOError as e:
			return e
