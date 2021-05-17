FROM python:3-alpine3.12
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY models/item.py models/item.py
COPY models/language.py models/language.py
COPY controllers/items_controller.py controllers/items_controller.py
COPY controllers/languages_controller.py controllers/languages_controller.py
RUN pip3 install -r requirements.txt
EXPOSE 8082
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "8082"]