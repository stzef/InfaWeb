
# Configuraciones de bases de datos
DB = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'infaweb_db',
		'USER': 'postgres',
		'PASSWORD': '123456',
		'HOST': 'localhost',
		'PORT': '5432',
	},
	'db_1': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'stzef',
		'USER': 'postgres',
		'PASSWORD': '123456',
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
	},
	'prod_db': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'df5v4jvjh2q2ni',
		'USER': 'dtptogrbsesizi',
		'PASSWORD': 'd9gR5v91pHII6wlqVla81qM5pM',
		'HOST': 'ec2-174-129-223-35.compute-1.amazonaws.com',
		'PORT': '5432',
	}
}
"""
DB = {
	'db_1': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'infaweb_db',
		'USER': 'postgres',
		'PASSWORD': '123456',
		'HOST': 'localhost',
		'PORT': '5432',
	},
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'infaweb_db',
		'USER': 'postgres',
		'PASSWORD': '123456',
		'HOST': 'localhost',
		'PORT': '5432',
	},
}
"""
