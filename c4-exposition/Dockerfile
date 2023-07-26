# To run Prometheus with Docker
# docker build -t my-prometheus .
# docker run -p 9090:9090 my-prometheus

# See https://prometheus.io/docs/prometheus/latest/installation/ for more details

# syntax=docker/dockerfile:1
FROM python:3.7-alpine

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

RUN chmod u+x ./python-examples/4-4-gunicorn-app.py

EXPOSE 8000
EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["./python-examples/4-4-gunicorn-app.py"]
