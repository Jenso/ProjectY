from pinry.settings import *

import os


DEBUG = False
TEMPLATE_DEBUG = DEBUG
PRODUCTION = True

# TODO: I recommend using psycopg2 w/ postgres but sqlite3 is good enough.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'projecty_newdb',                      
        'USER': 'projecty',
        'PASSWORD': 'ASKDl23elALJKAHSDjhj2k13h',
    }
}

# TODO: Be sure to set this.
SECRET_KEY = 'KJASDKLJKLJ12312JKLKLJ213'

STATIC_URL = 'http://lookify.s3-website-eu-west-1.amazonaws.com/'
COMPRESS_URL = STATIC_URL

DEFAULT_FILE_STORAGE = STATICFILES_STORAGE = ('storages.backends.s3boto.S3BotoStorage')
COMPRESS_ROOT = STATIC_ROOT

COMPRESS_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'lookify'
GOOGLE_ANALYTICS_KEY = 'UA-31224755-3'


# Sentry (loggin) DSN value, the key used to send logs to Sentry
SENTRY_DSN = 'http://5b583ce9e2134c528c2c2c84ce4fa87d:8e82a7a561e147058d71fc4b2e4826ac@localhost:9000/1'

LOGGING = SENTRY_LOGGING

# Add raven to the list of installed apps (sentry logging client)
INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django',
    )
