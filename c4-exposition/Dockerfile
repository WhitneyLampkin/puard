# # To run Prometheus with Docker
# # docker build -t my-prometheus .
# # docker run -p 9090:9090 my-prometheus

# # See https://prometheus.io/docs/prometheus/latest/installation/ for more details

# # syntax=docker/dockerfile:1
# FROM python:3.7-alpine

# WORKDIR /app
# COPY . .
# ## RUN pip3 install -r requirements.txt
# ## RUN pip install gunicorn
# ## RUN chmod u+x ./python-examples/4-4-gunicorn-app.py
# ## RUN gunicorn -w 2 -c ./python-examples/4-4-gunicorn-app.py app:app

# EXPOSE 8000
# EXPOSE 8080

# ENTRYPOINT ["python3"]

# ## CMD ["./python-examples/4-4-gunicorn-app.py"]
# ## CMD ["gunicorn"  , "-w", "2", "-c", "0.0.0.0:8000", "app:app"]
# ## CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "app:app"]

# # install dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt /app/requirements.txt
# RUN pip install -r requirements.txt

# # copy project
# COPY . /app

# CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]

FROM python:3.8.0-slim
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN cd ./python-examples
EXPOSE 8000
EXPOSE 8080
# CMD ["python", "app.py"]
CMD ["gunicorn", "-w","3", "-b", "0.0.0.0:8000", "python-examples.4-4-gunicorn-app:app"]
