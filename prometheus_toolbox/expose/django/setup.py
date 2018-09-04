# -*- coding: utf-8 -*-
from django.http import HttpResponse
from prometheus_client import (
    generate_latest,
    CONTENT_TYPE_LATEST,
)

from ..helpers import get_registry


def export_to_django_view(request):
    """Exports /metrics as a Django view.
    You can use django_prometheus.urls to map /metrics to this view.
    """
    metrics_page = generate_latest(get_registry())
    return HttpResponse(
        metrics_page,
        content_type=CONTENT_TYPE_LATEST,
    )
