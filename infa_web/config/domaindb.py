import os

# Relacion subdominio a base de datos
# key : subdominio, value : alias database
# test_local - DataBase Test - test_manager.py

DOMAINS = {
	'huevos' : 'prod_db',
	'testempresa' : 'test_db',
	#'test_local' : 'default',
}

if 'CURRENT_ENV_WORK' in os.environ:
	if os.environ["CURRENT_ENV_WORK"] == "DEV":
		DOMAINS = {
			'stzef' : 'db_1',
			'testempresa' : 'db_1',
		}
