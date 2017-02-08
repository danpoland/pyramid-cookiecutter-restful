import logging

from pyramid.view import view_config, notfound_view_config
from pyramid.response import Response

from {{ cookiecutter.repo_name }} import settings


log = logging.getLogger(__name__)


@notfound_view_config(append_slash=True, renderer='json')
def notfound_view(request):
    request.response.status = 404
    return {'error': 'Route not found.'}


@view_config(context=Exception)
def exception_view(context, request):
    log.error("The error was: %s" % context, exc_info=context)

    if settings.LOG_LEVEL == logging.DEBUG:
        return Response(status=500, json={'internal_server_error': str(context)})

    return Response(status=500)
