# -*- coding: utf-8 -*-
import os

from django.http import HttpResponse
from prometheus_client import (
    multiprocess,
    generate_latest,
    CollectorRegistry,
    REGISTRY,
    CONTENT_TYPE_LATEST,
)

try:
    # Python 2
    from BaseHTTPServer import HTTPServer
except ImportError:
    # Python 3
    from http.server import HTTPServer


def export_to_django_view(request):
    """Exports /metrics as a Django view.
    You can use django_prometheus.urls to map /metrics to this view.
    """
    if 'prometheus_multiproc_dir' in os.environ:
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
    else:
        registry = REGISTRY
    metrics_page = generate_latest(registry)
    return HttpResponse(
        metrics_page,
        content_type=CONTENT_TYPE_LATEST,
    )
