#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
IMAGE = ${NAME}-${VERSION}.tar.gz
OUTPUT = ${NAME}-${VERSION}-component.tar.gz

build: clean package

set-up-build: clean
	cp $(PWD)/target/classes/manifest.yml $(PWD)/manifest.yml

package: set-up-build
	docker build -t ${NAME}:${VERSION} .
	docker save ${NAME}:${VERSION} | gzip > ${NAME}-${VERSION}.tar.gz
	tar -czvf ${OUTPUT} manifest.yml ${IMAGE}
	rm -f manifest.yml
	rm -f ${IMAGE}

clean:
	rm -f manifest.yml
	rm -f ${IMAGE}
	rm -f ${OUTPUT}