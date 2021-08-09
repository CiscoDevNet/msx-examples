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

LANGUAGE_RUSSIAN = Language(
    id="55f3028f-1b94-4edd-b14f-183b51b33d68",
    name="Russian",
    description="An East Slavic language that uses the Cyrillic alphabet.")

languages_post_args = ['name', 'description']

LANGUAGE_NOT_FOUND_TXT = 'Language Not found'

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
        return "Delete Rows is Not Supported", config.HTTP_STATUS_CODE_NOT_IMPLEMENTED



class LanguageApi(Resource):
    def get(self, id):
        with CockroachHelper(Config("helloworld.yml")) as db:
            row = db.get_row('Languages', id)

        if not row:
            return LANGUAGE_NOT_FOUND_TXT, config.HTTP_STATUS_CODE_NOT_FOUND    

        return row, config.HTTP_STATUS_CODE_OK


    def put(self, id):
        parser = reqparse.RequestParser()
        [parser.add_argument(arg) for arg in languages_post_args]
        args = parser.parse_args()
        logging.info(args)        

        with CockroachHelper(Config("helloworld.yml")) as db:
            row = db.update_row('Languages', id, args)

        if not row:
            return LANGUAGE_NOT_FOUND_TXT, config.HTTP_STATUS_CODE_NOT_FOUND    

        return row, config.HTTP_STATUS_CODE_OK


    def delete(self, id):
        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.delete_row('Languages', id)

        if result != 'DELETE 1':
            return LANGUAGE_NOT_FOUND_TXT, config.HTTP_STATUS_CODE_NOT_FOUND    

        return result, config.HTTP_STATUS_CODE_NOCONTENT
