"""
Django settings for chatbot project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# chatbot
BASE_DIR = Path(__file__).resolve().parent.parent.parent.as_posix()

LOG_FILE = "".join(['>> ', BASE_DIR, '/logs/info.log'])

# Application definition
FIRST_LOAD_APPS = [
]

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'corsheaders',
    'chatterbot.ext.django_chatterbot',
    'rest_framework',
]

OUR_APPS = [
    'apps.bot.apps.ChatBotConfig'
]

INSTALLED_APPS = FIRST_LOAD_APPS + DEFAULT_APPS + THIRD_PARTY_APPS + OUR_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # External Middleware
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'chatbot.urls'

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

WSGI_APPLICATION = 'chatbot.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Bahia'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

CORS_ORIGIN_ALLOW_ALL = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_DIRS = (
    "".join([BASE_DIR, '/static']),
)
STATIC_URL = '/static/'
# STATIC_ROOT = "".join([BACKEND_DIR, '/static'])
STATIC_ROOT = "".join([BASE_DIR, '/static_served/'])

MEDIA_URL = '/media/'
# MEDIA_ROOT = "".join([BACKEND_DIR, '/media'])
MEDIA_ROOT = "".join([BASE_DIR, '/media_served/'])

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'https://localhost:8000',
    'http://localhost:3000',
    'https://localhost:3000',
    'http://127.0.0.1:8000',
    'https://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'https://127.0.0.1:3000',
    'http://127.0.0.1',
    'https://127.0.0.1',
    'http://0.0.0.0:3000',
    'https://0.0.0.0:3000',
    'http://0.0.0.0',
    'https://0.0.0.0',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'Content-Type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

SERVER_EMAIL = 'diego.correa@ufba.br'
DEFAULT_FROM_EMAIL = 'diego.correa@ufba.br'
