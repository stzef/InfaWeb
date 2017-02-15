import os
DB = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'd1e6lv1qvghpv4',
		'USER': 'zcmxfilhhxlhfe',
		'PASSWORD': 'Rv_JkDujcFszA040TuDvAnO_3p',
		'HOST': 'ec2-54-243-52-209.compute-1.amazonaws.com',
		'PORT': '5432',
	},
	#'db_1': {
	#	'ENGINE': 'django.db.backends.postgresql_psycopg2',
	#	'NAME': 'stzef',
	#	'USER': 'postgres',
	#	'PASSWORD': '123456',
	#	'HOST': 'localhost',
	#	'PORT': '',
	#},
	'test_db': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'd8kodpu1hq7be2',
		'USER': 'dfcqngdxqjohqw',
		'PASSWORD': '7063a8bae76314b9e5faa91f4b0f27449f32332bc6416948149639c86fe9ee5',
		'HOST': 'ec2-50-19-116-106.compute-1.amazonaws.com',
		'PORT': '5432',
	},
	# Comentariada por seguridad
	#'prod_db': {
	#	'ENGINE': 'django.db.backends.postgresql_psycopg2',
	#	'NAME': 'df5v4jvjh2q2ni',
	#	'USER': 'dtptogrbsesizi',
	#	'PASSWORD': 'd9gR5v91pHII6wlqVla81qM5pM',
	#	'HOST': 'ec2-174-129-223-35.compute-1.amazonaws.com',
	#	'PORT': '5432',
	#}
}

if 'CURRENT_ENV_WORK' in os.environ:
	if os.environ["CURRENT_ENV_WORK"] == "DEV":
		print " DEV"
		DB = {
			'default': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2',
				#'ENGINE': 'django.db.backends.mysql',
				'NAME': 'infaweb_db',
				'USER': 'root',
				'PASSWORD': 'stzEF0987',
				'HOST': 'localhost',
				'PORT': '',
			},
			'db_1': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2',
				'NAME': 'infaweb_db',
				'USER': 'root',
				'PASSWORD': 'stzEF0987',
				'HOST': 'localhost',
				'PORT': '',
			}
		}
