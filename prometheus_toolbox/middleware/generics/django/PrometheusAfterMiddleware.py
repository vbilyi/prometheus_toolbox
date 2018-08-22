from prometheus_toolbox.metrics.utils import time, time_since
from prometheus_toolbox.middleware.base import BaseMonitoringMiddleware
from prometheus_toolbox.metrics import (
    REQUESTS_BODY_BYTES,
    REQUESTS_BY_METHOD,
    REQUESTS_LATENCY_BY_PATH_METHOD,
    REQUESTS_LATENCY_UNKNOWN,
    REQUESTS_TOTAL,
    RESPONSES_BODY_BYTES,
    RESPONSES_BY_PATH_STATUS,
    RESPONSES_TOTAL,
    EXCEPTIONS_BY_PATH,
    EXCEPTIONS_BY_TYPE
)


import django
from django.urls import reverse as get_view_path

if django.VERSION >= (1, 10, 0):
    from django.utils.deprecation import MiddlewareMixin
else:
    MiddlewareMixin = object


class PrometheusAfterMiddleware(BaseMonitoringMiddleware, MiddlewareMixin):

    """Monitoring middleware that should run after other middlewares."""

    def _method(self, request):
        m = request.method
        if m not in ('GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE',
                     'OPTIONS', 'CONNECT', 'PATCH'):
            return '<invalid method>'
        return m

    def _get_path(self, request):
        path = "<undefined path>"
        if hasattr(request, 'resolver_match'):
            if request.resolver_match is not None:
                if request.resolver_match.view_name is not None:
                    path = get_view_path(request.resolver_match.view_name)
        return path

    def process_request(self, request):
        REQUESTS_TOTAL.inc()
        method = self._method(request)
        REQUESTS_BY_METHOD.labels(method).inc()
        content_length = int(request.META.get('CONTENT_LENGTH') or 0)
        REQUESTS_BODY_BYTES.observe(content_length)
        request.prometheus_middleware_event = time()

    def process_response(self, request, response):
        RESPONSES_TOTAL.inc()
        RESPONSES_BY_PATH_STATUS\
            .labels(
                path=self._get_path(request),
                status=str(response.status_code)
            ).inc()
        if hasattr(response, 'content'):
            RESPONSES_BODY_BYTES.observe(len(response.content))
        if hasattr(request, 'prometheus_middleware_event'):
            REQUESTS_LATENCY_BY_PATH_METHOD\
                .labels(
                    path=self._get_path(request),
                    method=request.method)\
                .observe(time_since(
                    request.prometheus_middleware_event
                ))
        else:
            REQUESTS_LATENCY_UNKNOWN.inc()
        return response

    def process_exception(self, request, exception):
        EXCEPTIONS_BY_TYPE.labels(type(exception).__name__).inc()
        EXCEPTIONS_BY_PATH.labels(self._get_path(request)).inc()
        if hasattr(request, 'prometheus_middleware_event'):
            REQUESTS_LATENCY_BY_PATH_METHOD\
                .labels(
                    path=self._get_path(request),
                    method=request.method)\
                .observe(time_since(
                    request.prometheus_after_middleware_event
                ))
        else:
            REQUESTS_LATENCY_UNKNOWN.inc()
