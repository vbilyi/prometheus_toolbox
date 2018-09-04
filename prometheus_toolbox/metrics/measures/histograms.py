from prometheus_client import Histogram

from prometheus_toolbox.expose.helpers import get_registry
from ..utils import powers_of


REQUESTS_LATENCY_BY_PATH_METHOD = Histogram(
    name='http_requests_latency_by_path_method',
    documentation='Histogram of request processing time labelled by path, method.',
    registry=get_registry(),
    labelnames=['path', 'method'],
)

REQUESTS_BODY_BYTES = Histogram(
    name='http_requests_body_total_bytes',
    documentation='Histogram of requests by body size.',
    registry=get_registry(),
    buckets=powers_of(2, 30),
)

RESPONSES_BODY_BYTES = Histogram(
    name='http_responses_body_total_bytes',
    documentation='Histogram of responses by body size.',
    registry=get_registry(),
    buckets=powers_of(2, 30),
)
