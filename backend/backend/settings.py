"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG',True)

ALLOWED_HOSTS = [
    "piggy-finance.com",
    "www.piggy-finance.com",
    "localhost",
    "localhost:8080",
    os.getenv('HOST_IP','0.0.0.0'),
    "testserver",
    "127.0.0.1",
]

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',
    'api',
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

MIDDLEWARE = [
    'api.middleware.SocialAuthDebugMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
]

ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"

ROOT_URLCONF = "backend.urls"

CSRF_TRUSTED_ORIGINS = ['https://piggy-finance.com', 'https://www.piggy-finance.com']


# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'allauth': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

# Templates
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

WSGI_APPLICATION = "backend.wsgi.application"

# Google OAuth settings

GOOGLE_REDIRECT_URI = os.getenv('GOOGLE_REDIRECT_URI')

SOCIALACCOUNT_ADAPTER = "api.adapter.SocialAccountAdapter"

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email"
        ],
        "AUTH_PARAMS": {
            "access_type": "online"
        }
    }
}


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Nginx settings
SECURE_PROXY_SSL_HEADER = ('X-Forwarded-Proto', 'https')
print(SECURE_PROXY_SSL_HEADER)
USE_X_FORWARDED_HOST = True


# DynamoDB settings

DYNAMODB = {
    'REGION': os.getenv('DYNAMODB_REGION', 'us-west-2'),  # e.g., 'us-west-2'
    'TABLE_NAME': 'piggy-finance-db',
    # Additional settings as needed
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

#Sqlite3 settings for admin

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Database engine
        'NAME': BASE_DIR / 'db.sqlite3',         # Database name
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS settings

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'x-xsrf-token',
]