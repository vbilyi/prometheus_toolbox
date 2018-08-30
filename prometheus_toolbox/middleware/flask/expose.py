# -*- coding: utf-8 -*-
import os

from prometheus_client import (
    make_wsgi_app,
    multiprocess,
    CollectorRegistry,
    REGISTRY,
)
from werkzeug.wsgi import DispatcherMiddleware

if 'prometheus_multiproc_dir' in os.environ:
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
else:
    registry = REGISTRY


def add_metrics_endpoint(app):
    """
    This function dispatches Prometheus WSGI App
    Usage example:

    from prometheus_toolbox.middleware.flask.urls import add_metrics_endpoint

    app = add_metrics_endpoint(app)

    :param app: app instance
    :return: app instance with metrics endpoint
    """
    app_dispatch = DispatcherMiddleware(app, {
        '/metrics': make_wsgi_app(registry),
    })
    return app_dispatch
