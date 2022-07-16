import os
from pathlib import Path
import dsmr_parser.clients


# Build paths inside the project like this: BASE_DIR / 'subdir'.
from dsmr_parser import telegram_specifications, clients

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rdn+o02t%!pa7)nhifk%zdyg^d5k*)cryvh+923iqc_13b-av)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'dsmrsql',
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

ROOT_URLCONF = 'dsmrsql.urls'

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

WSGI_APPLICATION = 'dsmrsql.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DSMR_DB_NAME', 'dsmr'),
        'USER': os.getenv('DSMR_DB_USER', 'dsmr'),
        'PASSWORD': os.getenv('DSMR_DB_PASSWORD', 'dsmr'),
        'HOST': os.getenv('DSMR_DB_HOST', 'localhost'),
        'PORT': os.getenv('DSMR_DB_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# DSMR settings
DSMR_DEVICE = os.getenv('DSMR_DEVICE', '/dev/ttyUSB0')
dsmr_serials = {
    'V2_2': clients.SERIAL_SETTINGS_V2_2,
    'V4': clients.SERIAL_SETTINGS_V4,
    'V5': clients.SERIAL_SETTINGS_V5
}
DSMR_SERIAL_SETTINGS = dsmr_serials[os.getenv('DSMR_SERIAL_SETTINGS', 'V5')]
dsmr_telegrams = {
    'V2_2': telegram_specifications.V2_2,
    'V3': telegram_specifications.V3,
    'V4': telegram_specifications.V4,
    'V5': telegram_specifications.V5,
}
DSMR_TELEGRAM_SPECIFICATION = dsmr_telegrams[os.getenv('DSMR_TELEGRAM_SPECIFICATION', 'V5')]
