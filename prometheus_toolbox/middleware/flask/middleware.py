# -*- coding: utf-8 -*-
from flask import request, g

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
from ..helpers import get_method_name


def before_request_middleware():
    """
        Should be used as a parameter when initializing app

        For example:

        app = Flask(__name__)
        app.before_request(before_request_middleware)

        :return: None
    """
    REQUESTS_TOTAL.inc()
    method = get_method_name(request)
    path = request.path
    REQUESTS_BY_PATH_METHOD.labels(path, method).inc()
    content_length = int(request.headers.get('CONTENT_LENGTH') or 0)
    REQUESTS_BODY_BYTES.observe(content_length)
    g.prometheus_middleware_event = time()


def after_request_middleware(response):
    """
        Should be used as a parameter when initializing app

        For example:

        app = Flask(__name__)
        app.after_request(after_request_middleware)

        :param response: response object
        :return: None
    """
    RESPONSES_TOTAL.inc()
    (
        RESPONSES_BY_PATH_STATUS
        .labels(
            path=request.path,
            status=str(response.status_code)
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


def exception_tracker(e):
    """
    Should be used as a parameter when initializing app

    For example:

    app = Flask(__name__)
    app.register_error_handler(Exception, exception_tracker)

    :param e: Exception instance that has been raised
    :return: None
    """
    EXCEPTIONS_BY_PATH_TYPE.labels(
        path=request.path,
        type=type(e).__name__,
    ).inc()
    if hasattr(request, 'prometheus_middleware_event'):
        (
            REQUESTS_LATENCY_BY_PATH_METHOD
            .labels(
                path=request.path,
                method=request.method,
            )
            .observe(time_since(
                g.prometheus_middleware_event
            ))
        )
    else:
        REQUESTS_LATENCY_UNKNOWN.inc()
