"""
Django settings for djangoprojects project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if socket.gethostname().startswith('Sukalpo'):
  CLOUD_DEPLOY=False
else:
  CLOUD_DEPLOY=True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7gkb&mri6y2@ckx5n!f53&27^0$)--sr$925d)pmzem^#8rf&%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'rest_framework',
	'eeg',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangoprojects.urls'

WSGI_APPLICATION = 'djangoprojects.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if CLOUD_DEPLOY:
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': '***',
      'USER': '***',
      'PASSWORD': '',
      'HOST': '***',
      'PORT': '',
    }
  }
else:
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
  }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
	]
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = ( os.path.join('static'), )
