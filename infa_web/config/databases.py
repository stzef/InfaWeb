
# Configuraciones de bases de datos
DB = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'infaweb_db',
		'USER': 'postgres',
		'PASSWORD': '123456',
		'HOST': 'localhost',
		'PORT': '',
	},
	'appem_test': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'appem_test',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': 'localhost',
		'PORT': '',
	},
	'db_1': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'appem_stzef',
		'USER': 'postgres',
		'PASSWORD': '123456',
		'HOST': 'localhost',
		'PORT': '',
	}
}
