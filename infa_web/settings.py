"""
Django settings for infa_web project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-5g%k^qyp3o@isqyrh8s80n1g-)90@msfcg)#-1xk%+*(ib)j0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.devappem.com']
APPEND_SLASH=True

AWS_STORAGE_BUCKET_NAME = os.environ.get("APPEM_AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.environ.get("APPEM_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("APPEM_AWS_SECRET_ACCESS_KEY")

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

DJANGO_APPS = [
	"djrill",
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	'storages',
]
PROJECT_APPS = [
	'infa_web.apps.base',
	'infa_web.apps.terceros',
	'infa_web.apps.articulos',
	'infa_web.apps.inventarios',
	'infa_web.apps.movimientos',
	'infa_web.apps.usuarios',
	'infa_web.apps.facturacion',
	'infa_web.apps.POS',
	'infa_web.apps.cartera',
	'easy_pdf',
	'infa_web.apps.base.templatetags',
]
PROJECT_APPS_RESTAURANT = [
	'infa_web.apps.restaurante_comandas',
	'infa_web.apps.restaurante_inventarios',
	'infa_web.apps.restaurante_menus',
	'infa_web.apps.restaurante_movimientos',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + PROJECT_APPS_RESTAURANT
EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
MANDRILL_API_KEY = "F0iN_O0DFD9oEVd-A8zswA"

MIDDLEWARE_CLASSES = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'infa_web.apps.base.middleware.subdomainMiddleware',
	'infa_web.apps.base.middleware.verifyConfigurationFile',
	'infa_web.apps.base.middleware.updateDateAppen',
]

ROOT_URLCONF = 'infa_web.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'infa_web.apps.base.context_processors.var_globals',
			],
		},
	},
]


LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'infa_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

from infa_web.config.databases import DB

DATABASES = DB

SITE_ID = 1

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'infa_web.apps.usuarios.auth_backend.UserBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-CO'

LOGIN_URL = '/login'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = False

USE_THOUSAND_SEPARATOR = True

THOUSAND_SEPARATOR = '.'

DECIMAL_SEPARATOR = '.'

NUMBER_GROUPING = 3

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = 'static'
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,'infa_web/static')

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'infa_web/static'),
)
