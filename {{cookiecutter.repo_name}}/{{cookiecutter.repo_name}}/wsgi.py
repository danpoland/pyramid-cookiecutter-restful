import logging.config

from pyramid.config import Configurator
from pyramid.renderers import JSON

from {{ cookiecutter.repo_name }} import settings
from {{ cookiecutter.repo_name }}.utilities import settings_config_parser


# Set up logging
logging.config.dictConfig(settings.LOGGING)

config = Configurator(settings=settings_config_parser())
json_render = JSON()

config.add_renderer(None, json_render)
config.include('.models')
config.include('.routes')
config.scan()

application = config.make_wsgi_app()
