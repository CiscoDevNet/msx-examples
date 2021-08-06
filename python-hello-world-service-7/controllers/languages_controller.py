
#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
import logging
import flask
from flask_restplus import Resource
from flask_restplus import reqparse

import config
from config import Config
from models.language import Language
from models.error import Error
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

def get_access_token():
    # Authorization: Bearer MY_ACCESS_TOKEN
    return flask.request.headers.get("Authorization", "")[7:]


class LanguagesApi(Resource):
    def __init__(self, *args, **kwargs):
        self._security = kwargs["security"]


    def get(self):
        if not self._security.has_permission("HELLOWORLD_READ_LANGUAGE", get_access_token()):
            return Error(code="my_error_code", message="permission denied").to_dict(), 403

        try: 
            with CockroachHelper(Config("helloworld.yml")) as db:
                rows = db.get_rows('Languages')
                logging.info(rows)
        except Exception as e:
            logging.error("helloworld service error:" + str(e))
            rows = [{"error": str(e)}]

        return rows, config.HTTP_STATUS_CODE_OK


    def post(self):
        if not self._security.has_permission("HELLOWORLD_WRITE_LANGUAGE", get_access_token()):
            return Error(code="my_error_code", message="permission denied").to_dict(), 403

        parser = reqparse.RequestParser()
        [parser.add_argument(arg) for arg in languages_post_args]
        args = parser.parse_args()

        logging.info(args)

        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.insert_row('Languages', args)

        return result, config.HTTP_STATUS_CODE_CREATED


    def delete(self):
        if not self._security.has_permission("HELLOWORLD_WRITE_LANGUAGE", get_access_token()):
            return Error(code="my_error_code", message="permission denied").to_dict(), 403

        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.delete_rows('Languages')

        return result, config.HTTP_STATUS_CODE_NOCONTENT



class LanguageApi(Resource):
    def __init__(self, *args, **kwargs):
        self._security = kwargs["security"]


    def get(self, id):
        if not self._security.has_permission("HELLOWORLD_READ_LANGUAGE", get_access_token()):
            return Error(code="my_error_code", message="permission denied").to_dict(), 403

        with CockroachHelper(Config("helloworld.yml")) as db:
            rows = db.get_row('Languages', id)

        return rows, config.HTTP_STATUS_CODE_OK


    def put(self, id):
        if not self._security.has_permission("HELLOWORLD_WRITE_LANGUAGE", get_access_token()):
            return Error(code="my_error_code", message="permission denied").to_dict(), 403

        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.update_row('Languages', id, 'name', args['name'])

        return result, config.HTTP_STATUS_CODE_OK


    def delete(self, id):
        if not self._security.has_permission("HELLOWORLD_WRITE_LANGUAGE", get_access_token()):
            return Error(code="my_error_code", message="permission denied").to_dict(), 403

        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.delete_row('Languages', id)

        return result, config.HTTP_STATUS_CODE_NOCONTENT
