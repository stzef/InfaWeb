from infa_web.settings import BASE_DIR
import json
class ManageParameters(object):
	def __init__(self):
		super(ManageParameters, self).__init__()


	def get_param_object(self,cparam):
		with open(BASE_DIR + '/infa_web/params/params.json') as json_data:
			parameters = json.load(json_data)
		for parameter in parameters:
			if(parameter["cparam"] == cparam):
				return parameter

	def get_param_value(self,cparam):
		with open(BASE_DIR + '/infa_web/params/params.json') as json_data:
			parameters = json.load(json_data)
		for parameter in parameters:
			if(parameter["cparam"] == cparam):
				return parameter["value"]
