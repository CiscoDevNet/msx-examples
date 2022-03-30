#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
FROM --platform=linux/amd64 python:3.9.6-slim-buster
WORKDIR /app
ADD . /app
RUN apt-get update \
&& apt-get install -y --no-install-recommends git \
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt
EXPOSE 8082

# Use a WSGI HTTP server like gunicorn in production.
# ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8082", "wsgi:app"]
# WARNING: This is a development server. Do not use it in a production deployment.
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "8082"]