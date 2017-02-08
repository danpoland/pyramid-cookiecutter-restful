import logging.config

from pyramid.config import Configurator
from pyramid.renderers import JSON

from {{ cookiecutter.repo_name }} import settings


# Set up logging
logging.config.dictConfig(settings.LOGGING)

# Assemble pyramid settings
pyramid_settings = dict()

for key, val in settings.__dict__.items():
    if key[0:7] == 'PYRAMID':
        name = 'pyramid.{}'.format(key[8].lower())
        pyramid_settings[name] = val

config = Configurator(settings=pyramid_settings)
json_render = JSON()

config.add_renderer(None, json_render)
config.include('.models')
config.include('.routes')
config.scan()

application = config.make_wsgi_app()
