from datetime import datetime

from . import settings


def get_now_timestamp():
    return datetime.now(settings.TIMEZONE)


def settings_config_parser():
    """
    Parses the settings module into Pyramid Configurator settings.
    :return: dict
    """

    pyramid_settings = dict()

    for key, val in settings.__dict__.items():
        index = key.find('_')
        prefix = key[0:index]

        if prefix in ('PYRAMID', 'SQLALCHEMY'):
            name = '{}.{}'.format(prefix.lower(), key[index + 1:].lower())
            pyramid_settings[name] = val

    return pyramid_settings
