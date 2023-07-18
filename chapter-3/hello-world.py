# Install Python and Prometheus Client:
# sudo apt install python3
# sudo apt install python3-pip
# pip3 install prometheus_client

import http.server
from prometheus_client import start_http_server


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")


if __name__ == "__main__":
    start_http_server(8000)
    # Changed http server and port from 'localhost' and '8001' to work wtih docker
    # server = http.server.HTTPServer(('0.0.0.0', 80), MyHandler)
    server = http.server.HTTPServer(('0.0.0.0', 80), MyHandler)
    server.serve_forever()
