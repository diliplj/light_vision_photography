"""
Django settings for photography_jan_6 project.
Generated by 'django-admin startproject' using Django 3.2.3.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Basic setup env variables
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env()  # reading .env file

ENVIRONMENT = env("ENV")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yqn18qb^mmay&p2cdf(usa9a1&_y%vxy)xe_l7g%*6our5qss@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'admin_poll.apps.AdminPollConfig',
    'django_cleanup.apps.CleanupConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'photography_jan_6.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'admin_poll' ,'templates','admin_poll'),
            os.path.join(BASE_DIR, 'admin_poll' ,'templates','admin_poll','includes'),
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

WSGI_APPLICATION = 'photography_jan_6.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



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

#LOGGING
# APP_LOGGING_LEVEL = env('APP_LOGGING_LEVEL')
# APP_LOGGER_FUNCTION_IN_PARAMS = env('APP_LOGGER_FUNCTION_IN_PARAMS')
# APP_LOGGER_FUNCTION_OUT_PARAMS = env('APP_LOGGER_FUNCTION_OUT_PARAMS')
# APP_URL = env('APP_URL')


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         # 'verbose': {'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(message)s'},
#         'verbose': {'format': '%(asctime)s %(levelname)s %(message)s'},
#         'simple': {'format': '%(levelname)s %(message)s'},
#     },
#     'handlers': {
#         'app_scripts': {
#             'level': env('APP_LOGGING_LEVEL'),
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'formatter': 'verbose',
#             'filename': os.path.join(BASE_DIR, 'admin_poll', 'logs', 'app_scripts.log'),
#             'when': 'W4',
#             'interval': 1,
#             'backupCount': 4
#         },
#         'app': {
#             'level': env('APP_LOGGING_LEVEL'),
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'formatter': 'verbose',
#             'filename': os.path.join(BASE_DIR, 'admin_poll', 'logs', 'app.log'),
#             'when': 'W4',
#             'interval': 1,
#             'backupCount': 4
#         },
#         'app_threads': {
#             'level': env('APP_LOGGING_LEVEL'),
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'formatter': 'verbose',
#             'filename': os.path.join(BASE_DIR, 'admin_poll', 'logs', 'app_threads.log'),
#             'when': 'W4',
#             'interval': 1,
#             'backupCount': 4
#         },

#     },
#     'loggers': {
#         'app_scripts': {'handlers': ['app_scripts'], 'level': env('APP_LOGGING_LEVEL'), 'propagate': False, },
#         'app': {'handlers': ['app'], 'level': env('APP_LOGGING_LEVEL'), 'propagate': False, },
#         'app_threads': {'handlers': ['app_threads'], 'level': env('APP_LOGGING_LEVEL'), 'propagate': False, },

#     }
# }


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'admin_poll', 'media', 'sdata')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'admin_poll', 'media', 'ddata')


# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'admin_poll', 'media', 'ssdata'),
    os.path.join(BASE_DIR, 'admin_poll', 'media', 'ddata'),
    # os.path.join(SITE_ROOT, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'admin_poll.AddUser'

LOGIN_REDIRECT_URL = "/admin_page/home/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

# My mail 
MY_MAIL = "diliplj5@gmail.com"

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = MY_MAIL
EMAIL_HOST_PASSWORD = 'xdxauijjaibxrihm'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'Light Vision Photography Team <noreply@example.com>'
