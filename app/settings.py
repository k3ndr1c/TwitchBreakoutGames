"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# from celery.schedule import crontab
# import twitch

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o@8-n5a&4vd0j)$y=eyf2d$ueza56$wb2(-pfv&l#p12^unhi('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'twitch.apps.TwitchConfig',
    'corsheaders',
    'rest_framework',
    'django_celery_beat'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': str(BASE_DIR / 'db.sqlite3'),
#     }
# }

# Postgres
POSTGRES_HOST="postgres"
POSTGRES_PORT=5432
POSTGRES_USER="twitchbreakoutgames"
POSTGRES_PASSWORD="kendricandryan"
POSTGRES_DB="twitchbreakoutgames"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "NAME": POSTGRES_DB,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Redis
REDIS_HOST='redis'
REDIS_PORT=6379
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"


# Celery
CELERY_REDIS_DB = '0'
CELERY_BROKER_URL = 'redis://{0}:{1}/{2}'.format(REDIS_HOST, REDIS_PORT, CELERY_REDIS_DB)
CELERY_RESULT_BACKEND = 'redis://{0}:{1}/{2}'.format(REDIS_HOST, REDIS_PORT, CELERY_REDIS_DB)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# Celery Beat schedule
# CELERY_BEAT_SCHEDULE = {
#     "create_new_timebucket": {
#         "task": "twitch.tasks.create_new_timebucket",
#         "schedule": crontab(minute="*/1"),
#     },
# }

# Twitch API data
CLIENT_ID = 'vady69007xdupx60w6op78bq4dh8nd'
CLIENT_SECRET = 'vk510dzemn9mym6fl5m5v1c03z6szf'


# Selenium
DRIVER_PATH = str(BASE_DIR / 'chromedriver')
TWITCH_URL = 'https://www.twitch.tv/directory?sort=VIEWER_COUNT'
VIEWER_LOWER = 500
VIEWER_UPPER = 5000
