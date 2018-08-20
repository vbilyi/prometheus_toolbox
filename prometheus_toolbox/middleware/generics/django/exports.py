from django.http import HttpResponse
from prometheus_client import multiprocess

try:
    # Python 2
    from BaseHTTPServer import HTTPServer
except ImportError:
    # Python 3
    from http.server import HTTPServer
import os
import prometheus_client


def export_to_django_view(request):
    """Exports /metrics as a Django view.
    You can use django_prometheus.urls to map /metrics to this view.
    """
    if 'prometheus_multiproc_dir' in os.environ:
        registry = prometheus_client.CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
    else:
        registry = prometheus_client.REGISTRY
    metrics_page = prometheus_client.generate_latest(registry)
    return HttpResponse(
        metrics_page,
        content_type=prometheus_client.CONTENT_TYPE_LATEST)
