#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
FROM python:3.9.6-slim-buster
WORKDIR /app
ADD . /app
RUN pip3 install -r requirements.txt
EXPOSE 8082
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "8082"]