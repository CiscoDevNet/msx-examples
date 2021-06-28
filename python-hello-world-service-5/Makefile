#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#

IMAGE = ${NAME}-${VERSION}.tar.gz
OUTPUT = ${NAME}-${VERSION}-component.tar.gz

build: clean package

package:
	docker build -t ${NAME}:${VERSION} .
	docker save ${NAME}:${VERSION} | gzip > ${IMAGE}
	tar -czvf ${OUTPUT} manifest.yml helloworld.yml ${IMAGE}
	rm -f ${IMAGE}

clean:
	rm -f ${IMAGE}
	rm -f ${OUTPUT}
