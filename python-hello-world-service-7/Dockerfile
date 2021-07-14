#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
FROM python:3-alpine3.12
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY config.py config.py
COPY swagger.json swagger.json
COPY helpers/consul_helper.py helpers/consul_helper.py
COPY helpers/vault_helper.py helpers/vault_helper.py
COPY helpers/swagger_helper.py helpers/swagger_helper.py
COPY helpers/security_helper.py helpers/security_helper.py
COPY models/error.py models/error.py
COPY models/item.py models/item.py
COPY models/language.py models/language.py
COPY controllers/items_controller.py controllers/items_controller.py
COPY controllers/languages_controller.py controllers/languages_controller.py
RUN apk update && apk add git
RUN pip3 install -r requirements.txt
EXPOSE 8082
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "8082"]