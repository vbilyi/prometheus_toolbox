from prometheus_client import Counter, Histogram
from prometheus_toolbox.metrics.utils import with_prefix, powers_of

REQUESTS_TOTAL = Counter(
    with_prefix('http_requests_total'),
    'Total count of requests')

RESPONSES_TOTAL = Counter(
    with_prefix('http_responses_total'),
    'Total count of responses')

REQUESTS_LATENCY_BY_PATH_METHOD = Histogram(
    with_prefix('http_requests_latency_by_path_method'),
    'Histogram of request processing time labelled by path, method.',
    ['path', 'method'])

REQUESTS_LATENCY_UNKNOWN = Counter(
    with_prefix('http_requests_unknown_latency'),
    'Count of requests for which the latency was unknown')

REQUESTS_BY_PATH_METHOD = Counter(
    with_prefix('http_requests_total_by_path_method'),
    'Count of requests by path, method.',
    ['path', 'method'])

REQUESTS_BODY_BYTES = Histogram(
    with_prefix('http_requests_body_total_bytes'),
    'Histogram of requests by body size.',
    buckets=powers_of(2, 30))

RESPONSES_BODY_BYTES = Histogram(
    with_prefix('http_responses_body_total_bytes'),
    'Histogram of responses by body size.',
    buckets=powers_of(2, 30))

RESPONSES_BY_STATUS = Counter(
    with_prefix('http_responses_total_by_status'),
    'Count of responses by status.',
    ['status'])

EXCEPTIONS_BY_PATH = Counter(
    with_prefix('http_exceptions_total_by_view'),
    'Count of exceptions by path.',
    ['path'])
