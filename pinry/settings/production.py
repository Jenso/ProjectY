from pinry.settings import *

import os


DEBUG = False
TEMPLATE_DEBUG = DEBUG
PRODUCTION = True

# TODO: I recommend using psycopg2 w/ postgres but sqlite3 is good enough.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'projecty',                      
        'USER': 'projecty',
        'PASSWORD': 'ASKDl23elALJKAHSDjhj2k13h',
    }
}

# TODO: Be sure to set this.
SECRET_KEY = 'KJASDKLJKLJ12312JKLKLJ213'
