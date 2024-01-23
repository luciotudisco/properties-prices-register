"""
Django settings for ppr project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

import sentry_sdk

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default="").split(" ")

# Application definition

INSTALLED_APPS = [
    "corsheaders",
    "django_celery_results",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "health_check",
    "rest_framework",
    "properties.apps.PropertiesConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ppr.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ppr.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("DB_USER", "user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 500,
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "ppr": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CELERY_ACCEPT_CONTENT = ["application/json"]

CELERY_TASK_SERIALIZER = "json"

SQS_DEFAULT_QUEUE_URL = os.getenv("SQS_DEFAULT_QUEUE_URL", "")

CELERY_TASK_DEFAULT_QUEUE = SQS_DEFAULT_QUEUE_URL.split("/")[-1]  # Get the queue name

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")

CELERY_BROKER_TRANSPORT_OPTIONS = {
    "region": "eu-west-1",
    "visibility_timeout": 3600,
    "polling_interval": 1,
    "predefined_queues": {CELERY_TASK_DEFAULT_QUEUE: {"url": SQS_DEFAULT_QUEUE_URL}},
}

ALGOLIA_APP_ID = os.environ.get("ALGOLIA_APP_ID")

ALGOLIA_API_KEY = os.environ.get("ALGOLIA_API_KEY")

ALGOLIA_PROPERTIES_INDEX_NAME = os.environ.get("ALGOLIA_PROPERTIES_INDEX_NAME", "properties")

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "test")

AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY", "test")

SENTRY_DNS = os.environ.get("SENTRY_DNS")

GEOCODE_API_KEY = os.environ.get("GEOCODE_API_KEY", "")

GEOCODE_API_URL = "https://trueway-geocoding.p.rapidapi.com/Geocode"

GEOCODE_API_HOST = "trueway-geocoding.p.rapidapi.com"

PROPERTY_PRICE_REGISTER_BASE_URL = "https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf"

CORS_ALLOW_ALL_ORIGINS = True

sentry_sdk.init(
    dsn=SENTRY_DNS,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
