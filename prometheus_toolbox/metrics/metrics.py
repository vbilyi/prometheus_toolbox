from prometheus_client import Counter, Histogram

REQUESTS_TOTAL = Counter('django_http_requests_before_middlewares_total',
                         'Total count of requests before middlewares run.')

responses_total = Counter(
    'django_http_responses_before_middlewares_total',
    'Total count of responses before middlewares run.')

requests_latency_before = Histogram(
    'django_http_requests_latency_including_middlewares_seconds',
    ('Histogram of requests processing time (including middleware '
     'processing time).'))

requests_unknown_latency_before = Counter(
    'django_http_requests_unknown_latency_including_middlewares_total',
    ('Count of requests for which the latency was unknown (when computing '
     'django_http_requests_latency_including_middlewares_seconds).'))
