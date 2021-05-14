FROM python:3-alpine
# RUN apk update && apk add git
COPY /templates /templates
COPY /templates/test.html /templates/test.html
COPY swagger.json swagger.json
COPY src/server.py server.py
COPY src/language.py language.py
COPY src/languages_controller.py languages_controller.py
COPY src/item.py item.py
COPY src/items_controller.py items_controller.py
COPY requirements.txt requirements.txt
COPY msxswagger-0.2.0.tar.gz msxswagger-0.2.0.tar.gz
RUN pip3 install -r requirements.txt
RUN pip3 install msxswagger-0.2.0.tar.gz
EXPOSE 8082
ENTRYPOINT ["python", "server.py", "-m"]