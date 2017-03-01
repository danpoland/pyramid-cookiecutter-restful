from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import configure_mappers

import zope.sqlalchemy

from {{cookiecutter.repo_name}} import settings

# import or define all models here to ensure they are attached to the
# Base.metadata prior to any initialization routines
from .mymodel import MyModel  # flake8: noqa

# run configure_mappers after defining all of the models to ensure
# all relationships can be setup
configure_mappers()


def get_session():
    """
    For when you need a db session outside the context of a request.
    """
    return get_session_factory(get_engine())()


def get_engine(configs=None, **kwargs):
    """
    :param configs: Standard, SQLAlchemy settings, if not present, uses global database settings.
    :param kwargs: Additional kwargs to pass to sqlalchemy's create_engine function.
    :return: sqlalchemy engine.
    """
    if configs:
        return engine_from_config(configs)

    # the thread local config was not available.
    return create_engine(settings.SQLALCHEMY_URL, connect_args=settings.SQLALCHEMY_CONNECT_ARGS, **kwargs)


def get_session_factory(engine):
    factory = sessionmaker()
    factory.configure(bind=engine)
    return factory


def get_tm_session(session_factory, transaction_manager):
    """
    Get a ``sqlalchemy.orm.Session`` instance backed by a transaction.

    This function will hook the session to the transaction manager which
    will take care of committing any changes.

    - When using pyramid_tm it will automatically be committed or aborted
      depending on whether an exception is raised.

    - When using scripts you should wrap the session in a manager yourself.
      For example::

          import transaction

          engine = get_engine(settings)
          session_factory = get_session_factory(engine)
          with transaction.manager:
              dbsession = get_tm_session(session_factory, transaction.manager)

    """
    dbsession = session_factory()
    zope.sqlalchemy.register(dbsession, transaction_manager=transaction_manager)
    return dbsession


def includeme(config):
    """
    Initialize the model for a Pyramid app.

    Activate this setup using ``config.include('hriservice.models')``.

    """
    config_settings = config.get_settings()

    # use pyramid_tm to hook the transaction lifecycle to the request
    config.include('pyramid_tm')

    session_factory = get_session_factory(get_engine(config_settings))
    config.registry['dbsession_factory'] = session_factory

    # make request.dbsession available for use in Pyramid
    config.add_request_method(
        # r.tm is the transaction manager used by pyramid_tm
        lambda r: get_tm_session(session_factory, r.tm),
        'dbsession',
        reify=True
    )
