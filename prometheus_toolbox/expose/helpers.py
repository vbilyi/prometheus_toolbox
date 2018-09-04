# -*- coding: utf-8 -*-
import os

from prometheus_client import (
    multiprocess,
    CollectorRegistry,
    REGISTRY,
    make_wsgi_app,
)

__all__ = ["get_method_name", "get_registry", "create_wsgi_app"]


def get_method_name(request):
    m = request.method
    if m not in ('GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE',
                 'OPTIONS', 'CONNECT', 'PATCH'):
        return '<invalid method>'
    return m


def get_registry():
    if 'prometheus_multiproc_dir' in os.environ:
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
    else:
        registry = REGISTRY
    return registry


def create_wsgi_app():
    return make_wsgi_app(get_registry())
