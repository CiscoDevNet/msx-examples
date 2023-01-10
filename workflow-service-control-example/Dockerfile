#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
FROM --platform=linux/amd64 nginx:latest
COPY ./build/services /usr/share/nginx/html/workflowexecutorui/
COPY ./config/nginx.conf /etc/nginx/conf.d/default.conf