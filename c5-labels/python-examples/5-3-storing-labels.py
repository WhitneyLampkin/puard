import http.server
from prometheus_client import start_http_server, Counter

REQUESTS = Counter('hello_worlds_total',
                   'Hello Worlds requested.',
                   # Example of multiple label names being used
                   labelnames=['path', 'method'])

FETCHES = Counter('cache_fetches_total',
                  'Fetches from the cache.',
                  labelnames=['cache'])


class MyCache(object):
    def __init__(self, name):
        self._fetches = FETCHES.labels(name)
        self._cache = {}

    def fetch(self, item):
        self._fetches.inc()
        return self._cache.get(item)

    def store(self, item, value):
        self._cache[item] = value


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Specifying the values of the counter metric's labels in the same order as defined on line 7 above.
        REQUESTS.labels(self.path, self.command).inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")


if __name__ == "__main__":
    start_http_server(8001)
    # Changed http server and port from 'localhost' and '8001' to work with docker
    # server = http.server.HTTPServer(('0.0.0.0', 80), MyHandler)
    server = http.server.HTTPServer(('0.0.0.0', 80), MyHandler)
    server.serve_forever()
