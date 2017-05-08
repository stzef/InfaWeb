import os
import dj_database_url

if "DATABASE_URL" in os.environ:
	DB = {
		'default' : dj_database_url.parse(os.environ.get("DATABASE_URL"), conn_max_age=600)
		'fitness_juice_db' : dj_database_url.parse(os.environ.get("DATABASE_URL"), conn_max_age=600)
	}
else:
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
