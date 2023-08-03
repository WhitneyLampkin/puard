import http.server
from prometheus_client import start_http_server, Counter

REQUESTS = Counter('hello_worlds_total',
                   'Hello Worlds requested.',
                   labelnames=['path'])


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.labels(self.path).inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")


if __name__ == "__main__":
    start_http_server(8001)
    # Changed http server and port from 'localhost' and '8001' to work with docker
    # server = http.server.HTTPServer(('0.0.0.0', 80), MyHandler)
    server = http.server.HTTPServer(('0.0.0.0', 80), MyHandler)
    server.serve_forever()
