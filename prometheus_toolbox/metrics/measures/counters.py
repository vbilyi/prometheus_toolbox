# -*- coding: utf-8 -*-
from prometheus_client import Counter

from prometheus_toolbox.expose.helpers import get_registry

REQUESTS_TOTAL = Counter(
    name='http_requests_total',
    documentation='Total count of requests',
    registry=get_registry(),
)

RESPONSES_TOTAL = Counter(
    name='http_responses_total',
    documentation='Total count of responses',
    registry=get_registry(),
)

REQUESTS_LATENCY_UNKNOWN = Counter(
    name='http_requests_unknown_latency',
    documentation='Count of requests for which the latency was unknown',
    registry=get_registry(),
)

REQUESTS_BY_PATH_METHOD = Counter(
    name='http_requests_total_by_path_method',
    documentation='Count of requests by path, method.',
    registry=get_registry(),
    labelnames=['path', 'method'],
)

RESPONSES_BY_PATH_STATUS = Counter(
    name='http_responses_by_path_status',
    documentation='Count of responses by status.',
    registry=get_registry(),
    labelnames=['path', 'status'],
)

EXCEPTIONS_BY_PATH_TYPE = Counter(
    name='http_exceptions_by_path_type',
    documentation='Count of exceptions by path, type.',
    registry=get_registry(),
    labelnames=['path', 'type'],
)
