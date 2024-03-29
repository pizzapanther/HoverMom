"""
Django settings for hovermom project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
  '.hover-mom.appspot.com'
]


# Application definition

INSTALLED_APPS = (
  'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hovermom.urls'

WSGI_APPLICATION = 'hovermom.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
  "django.core.context_processors.debug",
  #"django.core.context_processors.i18n",
  #"django.core.context_processors.media",
  "django.core.context_processors.static",
  "django.core.context_processors.tz",
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
    },
  },
  'loggers': {
    'django.request': {
      'handlers': ['console'],
      'level': 'DEBUG',
      'propagate': True,
    },
  },
}

from private.settings import *
