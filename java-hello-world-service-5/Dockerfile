#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
ARG BASE_VERSION=3.10.0-12
FROM dockerhub.cisco.com/vms-platform-dev-docker/vms-java:$BASE_VERSION

EXPOSE 9515

# Rebuild cacerts as JKS (as required by not-going-to-be-commons-ssl for SAML) until a fix for
# Debian bug #898678 is published or we mount the truststore to a different location
RUN sed -i -e 's/keystore.type=pkcs12/keystore.type=jks/' /etc/java-11-openjdk/security/java.security &&\
    rm /etc/ssl/certs/java/cacerts &&\
    update-ca-certificates -f

RUN apt-get update
RUN apt-get install -y curl

ENV SERVICE_JAR helloworldservice.jar

COPY bin/dockerlaunch.sh /service/dockerlaunch.sh
RUN chmod 755 /service/dockerlaunch.sh
ENTRYPOINT ["/service/dockerlaunch.sh"]

COPY target/$SERVICE_JAR /service/