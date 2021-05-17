FROM python:3-alpine3.12
RUN apk update && apk add git
COPY src/server.py server.py
COPY src/language.py language.py
COPY src/languages_controller.py languages_controller.py
COPY src/item.py item.py
COPY src/items_controller.py items_controller.py
COPY swagger.json swagger.json
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8082
ENTRYPOINT ["python", "server.py", "-m"]