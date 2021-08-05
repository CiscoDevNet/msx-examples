#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
import logging
from flask_restplus import Resource
from flask_restplus import reqparse

from models.language import Language
import config
from config import Config
from helpers.cockroach_helper import CockroachHelper

LANGUAGE_ENGLISH = Language(
    id="01f643a5-7e34-4366-af1a-9cce5e5c68e8",
    name="English",
    description="A West Germanic language that uses the Roman alphabet.")

languages_post_args = ['name', 'description']

LANGUAGE_RUSSIAN = Language(
    id="55f3028f-1b94-4edd-b14f-183b51b33d68",
    name="Russian",
    description="An East Slavic language that uses the Cyrillic alphabet.")

class LanguagesApi(Resource):
    def get(self):
        try: 
            with CockroachHelper(Config("helloworld.yml")) as db:
                rows = db.get_rows('Languages')
                logging.info(rows)
        except Exception as e:
            logging.error("helloworld service error:" + str(e))
            rows = [{"error": str(e)}]

        return rows, config.HTTP_STATUS_CODE_OK


    def post(self):
        parser = reqparse.RequestParser()
        [parser.add_argument(arg) for arg in languages_post_args]
        args = parser.parse_args()

        logging.info(args)

        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.insert_row('Languages', args)

        return result, config.HTTP_STATUS_CODE_CREATED


    def delete(self):
        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.delete_rows('Languages')

        return result, config.HTTP_STATUS_CODE_NOCONTENT



class LanguageApi(Resource):
    def get(self, id):
        with CockroachHelper(Config("helloworld.yml")) as db:
            rows = db.get_row('Languages', id)

        return rows, config.HTTP_STATUS_CODE_OK

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.update_row('Languages', id, 'name', args['name'])

        return result, config.HTTP_STATUS_CODE_OK


    def delete(self, id):
        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.delete_row('Languages', id)

        return result, config.HTTP_STATUS_CODE_NOCONTENT
