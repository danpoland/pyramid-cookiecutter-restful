import logging.config

from pyramid.config import Configurator
from pyramid.renderers import JSON

from {{ cookiecutter.repo_name }} import settings


# Set up logging
logging.config.dictConfig(settings.LOGGING)

config = Configurator(settings=settings.PYRAMID_APP_SETTINGS)
json_render = JSON()

config.add_renderer(None, json_render)
config.include('.models')
config.include('.routes')
config.scan()

application = config.make_wsgi_app()
