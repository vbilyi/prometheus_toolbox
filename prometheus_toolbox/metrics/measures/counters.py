# -*- coding: utf-8 -*-
from prometheus_client import Counter

from ..utils import with_web_service_prefix

REQUESTS_TOTAL = Counter(
    with_web_service_prefix('http_requests_total'),
    'Total count of requests')

RESPONSES_TOTAL = Counter(
    with_web_service_prefix('http_responses_total'),
    'Total count of responses')

REQUESTS_LATENCY_UNKNOWN = Counter(
    with_web_service_prefix('http_requests_unknown_latency'),
    'Count of requests for which the latency was unknown')

REQUESTS_BY_PATH_METHOD = Counter(
    with_web_service_prefix('http_requests_total_by_path_method'),
    'Count of requests by path, method.',
    ['path', 'method'])

RESPONSES_BY_PATH_STATUS = Counter(
    with_web_service_prefix('http_responses_by_path_status'),
    'Count of responses by status.',
    ['path', 'status'])

EXCEPTIONS_BY_PATH_TYPE = Counter(
    with_web_service_prefix('http_exceptions_by_path_type'),
    'Count of exceptions by path, type.',
    ['path', 'type'])
