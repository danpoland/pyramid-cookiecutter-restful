"""
Settings for the Pyramid project.

This replaces Pyramid's PasteDeploy ini files.
Configurations to be controlled pragmatically, and utilize environment variables.

For a full list of Pyramid settings see:
http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/environment.html
"""

import os
import logging
import pytz


DEPLOY_ENV = os.getenv('DEPLOY_ENV')

LOG_LEVEL = logging.ERROR
DB_LOG_LEVEL = logging.ERROR

# Pyramid (settings with a PYRAMID_ prefix are later converted to the corresponding lower cased, dot separated setting)
PYRAMID_RELOAD_TEMPLATES = False
PYRAMID_DEBUG_AUTHORIZATION = False
PYRAMID_DEBUG_NOTFOUND = False
PYRAMID_DEBUG_ROUTEMATCH = False
PYRAMID_DEFAULT_LOCALE_NAME = 'en'

# --- EVERYTHING ABOVE IS OVERRIDABLE by environment specific configs ---

if DEPLOY_ENV == 'production':
    from .production import *
elif DEPLOY_ENV == 'development':
    from .development import *
else:
    raise Exception('Invalid value for DEPLOY_ENV: {}'.format(DEPLOY_ENV))


# Pyramid settings
PYRAMID_APP_SETTINGS = {
    'pyramid.reload_templates': PYRAMID_RELOAD_TEMPLATES,
    'pyramid.debug_authorization': PYRAMID_DEBUG_AUTHORIZATION,
    'pyramid.debug_notfound': PYRAMID_DEBUG_NOTFOUND,
    'pyramid.debug_routematch': PYRAMID_DEBUG_ROUTEMATCH,
    'pyramid.default_locale_name': 'en',
}


TIMEZONE = pytz.utc

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s:%(lineno)s][%(threadName)s] %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
        },
        '{{ cookiecutter.repo_name }}': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
        },
        'sqlalchemy.engine': {
            'handlers': ['console'],
            'level': DB_LOG_LEVEL,
        }
    },
}

# Database
DATABASE = {
    'URL_SCHEMA': 'postgresql',
    'NAME': os.getenv('DB_NAME'),
    'USER': os.getenv('DB_USER'),
    'PASSWORD': os.getenv('DB_PASSWORD'),
    'HOST': os.getenv('DB_HOST'),
    'PORT': os.getenv('DB_PORT'),
    'OPTIONS': {}
}

SQLALCHEMY_URL = '{URL_SCHEMA}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(**DATABASE)
SQLALCHEMY_CONNECT_ARGS = DATABASE.get('OPTIONS', {})
