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
