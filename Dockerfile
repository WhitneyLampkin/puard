# To run Prometheus with Docker
# docker build -t my-prometheus .
# docker run -p 9090:9090 my-prometheus

FROM prom/prometheus
# Update Prometheus config to use based on which chapter examples are being ran
ADD ./chapter-3/prometheus-c3.yml /etc/prometheus/