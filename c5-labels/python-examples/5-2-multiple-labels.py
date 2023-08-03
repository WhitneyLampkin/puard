import http.server
from prometheus_client import start_http_server, Counter

REQUESTS = Counter('hello_worlds_total',
                   'Hello Worlds requested.',
                   # Example of multiple label names being used
                   labelnames=['path', 'method'])


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
