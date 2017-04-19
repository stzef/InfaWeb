import os

DB = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': os.getenv('APPEM_DEFAULT_DB_NAME',''),
		'USER': os.getenv('APPEM_DEFAULT_DB_USER',''),
		'PASSWORD': os.getenv('APPEM_DEFAULT_DB_PASSWORD',''),
		'HOST': os.getenv('APPEM_DEFAULT_DB_HOST',''),
		'PORT': os.getenv('APPEM_DEFAULT_DB_PORT',''),
	},
	'fitness_juice_db': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': os.getenv('APPEM_FITNESS_JUICE_DB_NAME',''),
		'USER': os.getenv('APPEM_FITNESS_JUICE_DB_USER',''),
		'PASSWORD': os.getenv('APPEM_FITNESS_JUICE_DB_PASSWORD',''),
		'HOST': os.getenv('APPEM_FITNESS_JUICE_DB_HOST',''),
		'PORT': os.getenv('APPEM_FITNESS_JUICE_DB_PORT',''),
	}
}

if 'CURRENT_ENV_WORK' in os.environ:
	if os.environ["CURRENT_ENV_WORK"] == "DEV":
		print " DEV"
		DB = {
			'default': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2',
				'NAME': 'infaweb_db',
				'USER': 'root',
				'PASSWORD': 'stzEF0987',
				'HOST': 'localhost',
				'PORT': '',
			},
			'testfitness_db': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2',
				'NAME': 'testfitness_db',
				'USER': 'root',
				'PASSWORD': 'stzEF0987',
				'HOST': 'localhost',
				'PORT': '',
			},
		}
