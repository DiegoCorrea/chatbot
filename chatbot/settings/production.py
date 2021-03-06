"""
Django settings for chatbot project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from .common import *
from dotenv import load_dotenv

# load secret key
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'production.env'))

SECRET_KEY = os.getenv('SECRET_KEY')
DJANGO_SETTINGS_MODULE = os.getenv('DJANGO_SETTINGS_MODULE')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '.site.org',
    '.subdominio.site.org',
    'www.subdominio.site.org',
    'https://www.subdominio.site.org',
    'api.subdominio.site.org/',
    'https://api.subdominio.site.org/',
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE'),
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': int(os.getenv('DATABASE_PORT')),
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

# SITE_URL = "https://subdominio.site.org/"

DEFAULT_RENDERER_CLASSES = (
    'rest_framework.renderers.JSONRenderer',
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES
}

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
