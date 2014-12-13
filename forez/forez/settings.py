"""
Django settings for forez project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from __future__ import unicode_literals
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0rasfgzktp(iur(9q$v)upmbj(rx426zj&ojgwa4$s_=f4q71i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

OAUTH2_PROVIDER_APPLICATION_MODEL = 'clients.GardenClient'
AUTH_USER_MODEL = 'users.GardenUser'
# AUTH_PROFILE_MODULE = 'users.UserProfile'
# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'oauth2_provider',
    'users',
    'utils',
    'clients',
    'teams',
    'oauths',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.FormParser',
            'rest_framework.parsers.JSONParser',
    ),
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'},
    'ACCESS_TOKEN_EXPIRE_SECONDS': 360000,
    'REQUEST_APPROVAL_PROMPT': 'auto',
    # 'CLIENT_ID_GENERATOR_CLASS': 'clients.generators.GardenClientIdGenerator',
    # 'CLIENT_SECRET_GENERATOR_CLASS': 'clients.generators.GardenClientSecretGenerator',
}

SWAGGER_SETTINGS = {
    "enabled_methods": [  # Specify which methods to enable in Swagger UI
        'get',
        'post',
        'put',
        'delete'
    ],
}

MEDIA_ROOT = '/home/sungjin/webp/forez/forez/web_content/resource/images'
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    #'E:/Django/Projects/solutoire/templates'
    '/home/sungjin/webp/forez/forez/web_content/templates'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
)

ROOT_URLCONF = 'forez.urls'

WSGI_APPLICATION = 'forez.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME':  'gardenplatform',
#        'USER': 'sungjin',
#        'PASSWORD': 'rkems',
#        'HOST': '211.189.127.121',
#        'PORT': '3306',
#    }

     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': '/home/sungjin/webp/forez/forez/sqlite3.db'
     }

}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "/home/sungjin/webp/forez/forez/web_content/templates/registration"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home/sungjin/webp/forez/forez/web_content/templates',
)
