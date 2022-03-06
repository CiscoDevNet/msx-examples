#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
IMAGE = ${NAME}-${VERSION}.tar.gz
OUTPUT = ${NAME}-${VERSION}-component.tar.gz

export GO111MODULE=on

build: clean package

# The following sections MUST be indented using tabs not spaces.
package:
	docker build -t ${NAME}:${VERSION} .
	docker save ${NAME}:${VERSION} | gzip > ${IMAGE}
	tar -czvf ${OUTPUT} manifest.yml helloworld.yml ${IMAGE}
	rm -f ${IMAGE}

clean:
	rm -f ${IMAGE}
	rm -f ${OUTPUT}
