#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
IMAGE = ${NAME}-${VERSION}.tar.gz
OUTPUT = ${NAME}-${VERSION}-component.tar.gz

build: clean package

package:
	docker build -t ${NAME}:${VERSION} .
	docker save ${NAME}:${VERSION} | gzip > ${IMAGE}
	tar -czvf ${OUTPUT} manifest.yml ${IMAGE}
	rm -f ${IMAGE}
	shasum -a 256 ${OUTPUT} | cut -d " " -f 1 | xxd -r -p | base64

clean:
	rm -f ${IMAGE}
	rm -f ${OUTPUT}
