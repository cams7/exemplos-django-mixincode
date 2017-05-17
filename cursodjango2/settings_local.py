DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cursodjango2',               # Or path to database file if using sqlite3.
        'USER': 'mixincode',                  # Not used with sqlite3.
        'PASSWORD': 'django',                 # Not used with sqlite3.
        'HOST': '127.0.0.1',                  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                       # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS += ['debug_toolbar',]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

INTERNAL_IPS = ('127.0.0.1',)
