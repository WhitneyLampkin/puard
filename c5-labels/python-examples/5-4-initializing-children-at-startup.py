from prometheus_client import Counter

REQUESTS = Counter('http_requests_total',
                   'HTTP requests.',
                   labelnames=['path'])
REQUESTS.labels('/foo')
REQUESTS.labels('/bar')

# TODO: Add other code
