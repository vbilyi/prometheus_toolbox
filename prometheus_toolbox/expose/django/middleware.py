# -*- coding: utf-8 -*-
import django

from prometheus_toolbox.metrics.measures.counters import (
    REQUESTS_BY_PATH_METHOD,
    REQUESTS_LATENCY_UNKNOWN,
    REQUESTS_TOTAL,
    RESPONSES_BY_PATH_STATUS,
    RESPONSES_TOTAL,
    EXCEPTIONS_BY_PATH_TYPE,
)
from prometheus_toolbox.metrics.measures.histograms import (
    REQUESTS_BODY_BYTES,
    REQUESTS_LATENCY_BY_PATH_METHOD,
    RESPONSES_BODY_BYTES,
)
from prometheus_toolbox.metrics.utils import time, time_since
from .base import BaseMetricsMiddleware
from ..helpers import get_method_name

if django.VERSION >= (1, 10, 0):
    from django.utils.deprecation import MiddlewareMixin
else:
    MiddlewareMixin = object


class AfterRequestMiddleware(BaseMetricsMiddleware, MiddlewareMixin):

    """Monitoring middleware that should run after other middlewares."""

    def process_request(self, request):
        REQUESTS_TOTAL.inc()
        method = get_method_name(request)
        path = request.path
        REQUESTS_BY_PATH_METHOD.labels(path, method).inc()
        content_length = int(request.META.get('CONTENT_LENGTH', 0))
        REQUESTS_BODY_BYTES.observe(content_length)
        request.prometheus_middleware_event = time()

    def process_response(self, request, response):
        RESPONSES_TOTAL.inc()
        (
            RESPONSES_BY_PATH_STATUS
            .labels(
                path=request.path,
                status=str(response.status_code),
            ).inc()
        )
        if hasattr(response, 'content'):
            RESPONSES_BODY_BYTES.observe(len(response.content))
        if hasattr(request, 'prometheus_middleware_event'):
            (
                REQUESTS_LATENCY_BY_PATH_METHOD
                .labels(
                    path=request.path,
                    method=request.method,
                )
                .observe(time_since(
                    request.prometheus_middleware_event
                ))
            )
        else:
            REQUESTS_LATENCY_UNKNOWN.inc()
        return response

    def process_exception(self, request, exception):
        EXCEPTIONS_BY_PATH_TYPE.labels(
            path=request.path,
            type=type(exception).__name__,
        ).inc()
        if hasattr(request, 'prometheus_middleware_event'):
            (
                REQUESTS_LATENCY_BY_PATH_METHOD
                .labels(
                    path=request.path,
                    method=request.method,
                )
                .observe(time_since(
                    request.prometheus_middleware_event
                ))
            )
        else:
            REQUESTS_LATENCY_UNKNOWN.inc()
