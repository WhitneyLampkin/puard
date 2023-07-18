# To run Prometheus with Docker
# docker build -t my-prometheus .
# docker run -p 9090:9090 my-prometheus

# See https://prometheus.io/docs/prometheus/latest/installation/ for more details

#FROM prom/prometheus
# Update Prometheus config to use based on which chapter examples are being ran
#ADD prometheus-c3.yml /etc/prometheus/

# syntax=docker/dockerfile:1
FROM python:3.7-alpine

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

RUN chmod u+x hello-world.py

EXPOSE 8000

ENTRYPOINT ["python3", "hello-world.py"]

# CMD ["hello-world.py"]
