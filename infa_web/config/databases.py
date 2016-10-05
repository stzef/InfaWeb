
# Configuraciones de bases de datos
DB = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'infaweb_db',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': 'localhost',
		'PORT': '5432',
	},
	'db_1': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'stzef',
		'USER': 'postgres',
		'PASSWORD': '123456',
		'HOST': 'localhost',
		'PORT': '5432',
	}
}