import os

# Relacion subdominio a base de datos
# key : subdominio, value : alias database
# test_local - DataBase Test - test_manager.py

DOMAINS = {
	'fitnessjuice' : 'fitness_juice_db',
}

if 'CURRENT_ENV_WORK' in os.environ:
	if os.environ["CURRENT_ENV_WORK"] == "DEV":
		DOMAINS = {
			'testfitness' : 'testfitness_db',
		}
