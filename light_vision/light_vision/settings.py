from pathlib import Path
from django.utils.translation import gettext_lazy as _

import logging
import logging.config
import os
import sys
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Basic setup env variables
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(os.path.join(BASE_DIR, '.env')) # reading .env file

# BASE_DIR_1 = env('UI_BASE_DIR')
# print("BASE_DIR_1",BASE_DIR_1)
sys.path.insert(0, BASE_DIR) #setting python pkgs in sys path
USE_I18N = True

ENVIRONMENT =  'DEV'
if ENVIRONMENT == 'DEV':
    DEBUG = True


# VERSION = '1.0'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2m5e=*4i^dxhr7^3+m^)q2nhw*fyy^=jqf$ir&t$p^+*dni3hx"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_app',
    'client_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'light_vision.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'admin_app' ,'templates'),
            os.path.join(BASE_DIR,'client_app' ,'templates'),
        ],
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

WSGI_APPLICATION = 'light_vision.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'light_vision_db',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT': '3306',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------------------------------------------------------------------
# LOGGING


# APP_LOGGER_FUNCTION_IN_PARAMS = env('UI_APP_LOGGER_FUNCTION_IN_PARAMS')
# APP_LOGGER_FUNCTION_OUT_PARAMS = env('UI_APP_LOGGER_FUNCTION_OUT_PARAMS')
# logging.config.dictConfig(LOGGING)

# APP_URL= "http://127.0.0.1:8000/"

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR ,'media','sdata')
STATIC_URL  = 'static/'
# STATICFILES_DIRS =[os.path.join(BASE_DIR,'media','sdata')]
MEDIA_URL  = 'dynamic/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media','ddata')
# My mail 
MY_MAIL = "diliplj5@gmail.com"

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = MY_MAIL
EMAIL_HOST_PASSWORD = 'xdxauijjaibxrihm'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'TestSite Team <noreply@example.com>'

AUTH_USER_MODEL = 'admin_app.AddUser'

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'testsite_app'
# EMAIL_HOST_PASSWORD = 'mys3cr3tp4ssw0rd'
# EMAIL_USE_TLS = True
