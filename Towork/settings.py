""" SETTINGS """

import os
from pathlib import Path

import dj_database_url
import environ

env = environ.Env()
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    'https://towork-ng.onrender.com', 'https://*.github.dev']


INSTALLED_APPS = [
    'users',
    'seek',
    'workers',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    "allauth.socialaccount.providers.github",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Towork.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'Towork.wsgi.application'

DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Default Pages
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SITE_ID = 1

SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"

# Simplified static file serving.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
