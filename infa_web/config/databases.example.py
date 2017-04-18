import os
DB = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': '',
		'USER': '',
		'PASSWORD': '',
		'HOST': '',
		'PORT': '',
	},
}

if 'CURRENT_ENV_WORK' in os.environ:
	if os.environ["CURRENT_ENV_WORK"] == "DEV":
		print " DEV"
		DB = {
			'default': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2',
				'NAME': '',
				'USER': '',
				'PASSWORD': '',
				'HOST': '',
				'PORT': '',
			}
		}
