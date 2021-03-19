#
# Copyright (c) 2021 Cisco Systems, Inc
# All Rights reserved
#
build: clean package
IMAGE = ${NAME}:${VERSION}
OUTPUT = ${NAME}-${VERSION}

package:
	npm install
	npm run build
	docker build -t ${IMAGE} .
	docker save ${IMAGE} | gzip > ./config/${OUTPUT}.tar.gz
	tar -czvf ${OUTPUT}-component.tar.gz  -C ./config manifest.yml ${OUTPUT}.tar.gz
	rm -rf ./config/${OUTPUT}.tar.gz

clean:
	rm -rf config/${OUTPUT}.tar.gz

