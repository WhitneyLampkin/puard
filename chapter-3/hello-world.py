# Install Python and Prometheus Client:
# sudo apt install python3
# sudo apt install python3-pip
# pip3 install prometheus_client

import http.server
import random
import time
import unittest
from prometheus_client import start_http_server
# Counter metric import
from prometheus_client import Counter
# Gauge metric import
from prometheus_client import Gauge
# Histogram metric import
from prometheus_client import Histogram
# Import REGISTRY for unit test example
from prometheus_client import REGISTRY
# Summary metric import
from prometheus_client import Summary

# Counter metric definitions
# Track etiher the number or size of events.
REQUESTS = Counter('hello_worlds_total', 'Hello Worlds requested.')
EXCEPTIONS = Counter('hello_world_exceptions_total',
                     'Exceptions serving Hello World app.')
SALES = Counter('hello_world_sales_euro_total',
                'Euros made serving Hello World.')

# Guage metric definitions
# Snapshot of some current state.
INPROGRESS = Gauge('hello_worlds_inprogress',
                   'Number of Hello Worlds in progress.')
LAST = Gauge('hello_world_last_time_seconds',
             'The last time a Hello World was served.')
TIME = Gauge('time_seconds', 'The current time.')

# Callback
TIME.set_function(lambda: time.time())

# Summary metric definitions
# Summary is used to observe and requires that the size of the event be passed.
LATENCY = Summary('hello_world_latency_seconds',
                  'Time for a request Hello World.')

# Histogram metric definitions
# Histograms have a set of buckets that track number of events that fall into each bucket.
LATENCY_HISTOGRAM = Histogram(
    'hello_world_latency_seconds', 'Time for a request Hello World.', buckets=[0.0001, 0.0002, 0.0005, 0.001, 0.01, 0.1])


class MyHandler(http.server.BaseHTTPRequestHandler):
    # Histogram instrumentation
    @LATENCY_HISTOGRAM.time()
    def do_GET(self):
        # Metric instrumentation
        INPROGRESS.inc()  # Guage_Alternative: @INPROGRESS.track_inprogress()
        # The following line increments the counter by 1.
        REQUESTS.inc()
        # count_exceptions takes care of the exception without interfering wtih the application logic
        with EXCEPTIONS.count_exceptions():
            # Generating random exceptions
            if random.random() < 0.2:
                raise Exception
        # Generating random euro value
        euros = random.random()
        SALES.inc(euros)
        start = time.time()  # Remove when using the LATENCY_Alternative
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")
        self.wfile.write(
            "\r\nHello World for {} euros.".format(euros).encode())
        LAST.set(time.time())  # Guage_Alternative: LAST.set_to_current_time()
        INPROGRESS.dec()  # Delete when using the Guage_Alternatives
        # LATENCY_Alternative: @LATENCY.time()
        LATENCY.observe(time.time() - start)


if __name__ == "__main__":
    start_http_server(8000)
    # Changed http server and port from 'localhost' and '8001' to work wtih docker
    # server = http.server.HTTPServer(('0.0.0.0', 80), MyHandler)
    server = http.server.HTTPServer(('0.0.0.0', 80), MyHandler)
    server.serve_forever()


# Unit Test Example
# <TODO> Pull this out into a separate unit test file
FOOS = Counter('foos_total', 'The number of foo calls.')


def foo():
    FOOS.inc()


class TestFoo(unittest.TestCase):
    def test_counter_inc(self):
        before = REGISTRY.get_sample_value('foos_total')
        foo()
        after = REGISTRY.get_sample_value('foos_total')
        self.assertEqual(1, after - before)
