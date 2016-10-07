
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
	'db_1': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'infaweb_db',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': 'localhost',
		'PORT': '',
	},
	'test_db': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'd9vpdvlh4hqqa1',
		'USER': 'mfidvowuxajqob',
		'PASSWORD': 'LwZANgRLUBPQ5Gee8nDasSlmmB',
		'HOST': 'ec2-54-243-54-21.compute-1.amazonaws.com',
		'PORT': '5432',
	}
}
