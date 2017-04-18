import os

# Relacion subdominio a base de datos
# key : subdominio, value : alias database
# test_local - DataBase Test - test_manager.py

DOMAINS = {
	'testempresa' : 'default',
}

if 'CURRENT_ENV_WORK' in os.environ:
	if os.environ["CURRENT_ENV_WORK"] == "DEV":
		DOMAINS = {
			'testempresa' : 'default',
		}
