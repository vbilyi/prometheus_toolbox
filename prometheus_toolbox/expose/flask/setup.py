# -*- coding: utf-8 -*-
from werkzeug.wsgi import DispatcherMiddleware

from .middleware import (
    before_request_middleware,
    after_request_middleware,
    exception_tracker,
)
from ..helpers import create_wsgi_app


def add_metrics_endpoint(app):
    """
    This function dispatches Prometheus WSGI App
    Usage example:

    from prometheus_toolbox.expose.flask import add_metrics_endpoint
    app = Flask(__name__)
    app = add_metrics_endpoint(app)

    :param app: app instance
    :return: app instance with metrics endpoint
    """
    app_dispatch = DispatcherMiddleware(app, {
        '/metrics': create_wsgi_app(),
    })
    return app_dispatch


def setup_default_metrics(app):
    """
    This function adds default middlewares to app
    Usage example:

    from prometheus_toolbox.expose.flask import setup_default_metrics
    app = Flask(__name__)
    setup_default_metrics(app)

    :param app:
    :return: None
    """
    app.before_request(before_request_middleware)
    app.after_request(after_request_middleware)
    app.register_error_handler(Exception, exception_tracker)
