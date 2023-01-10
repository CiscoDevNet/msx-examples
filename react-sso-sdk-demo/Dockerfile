#
# Copyright (c) 2021 Cisco Systems, Inc
# All Rights reserved
#
FROM --platform=linux/amd64 nginx:latest
COPY ./build/ /usr/share/nginx/html/reactSsoSdkDemo
COPY ./config/nginx.conf /etc/nginx/conf.d/default.conf