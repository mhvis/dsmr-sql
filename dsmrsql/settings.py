import os
from pathlib import Path

from dsmr_parser import telegram_specifications, clients

BASE_DIR = Path(__file__).resolve().parent.parent

# We don't have a web interface but this setting needs to be set
SECRET_KEY = 'django-insecure-rdn+o02t%!pa7)nhifk%zdyg^d5k*)cryvh+923iqc_13b-av)'

DEBUG = False

INSTALLED_APPS = [
    'dsmrsql'
]

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

USE_I18N = False
USE_TZ = True
TIME_ZONE = 'UTC'

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
