from prometheus_client import Histogram

from ..utils import with_web_service_prefix, powers_of


REQUESTS_LATENCY_BY_PATH_METHOD = Histogram(
    with_web_service_prefix('http_requests_latency_by_path_method'),
    'Histogram of request processing time labelled by path, method.',
    ['path', 'method'])

REQUESTS_BODY_BYTES = Histogram(
    with_web_service_prefix('http_requests_body_total_bytes'),
    'Histogram of requests by body size.',
    buckets=powers_of(2, 30))

RESPONSES_BODY_BYTES = Histogram(
    with_web_service_prefix('http_responses_body_total_bytes'),
    'Histogram of responses by body size.',
    buckets=powers_of(2, 30))
