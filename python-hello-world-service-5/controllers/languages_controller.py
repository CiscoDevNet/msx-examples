#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
import http
import logging
from flask_restplus import Resource
from flask_restplus import reqparse
from models.language import Language
from helpers.cockroach_helper import CockroachHelper

LANGUAGE_INPUT_ARGUMENTS = ['name', 'description']

LANGUAGE_NOT_FOUND = 'Language not found'


class LanguagesApi(Resource):
    def __init__(self, *args, **kwargs):
        self._config = kwargs["config"]
        
    def get(self):
        with CockroachHelper(self._config) as db:
            rows = db.get_rows('Languages')
            logging.info(rows)

        languages = [Language(row=x) for x in rows]
        return [x.to_dict() for x in languages], http.HTTPStatus.OK

    def post(self):
        parser = reqparse.RequestParser()
        [parser.add_argument(arg) for arg in LANGUAGE_INPUT_ARGUMENTS]
        args = parser.parse_args()
        logging.info(args)

        with CockroachHelper(self._config) as db:
            row = db.insert_row('Languages', args)
            return Language(row=row).to_dict(), http.HTTPStatus.CREATED


class LanguageApi(Resource):
    def __init__(self, *args, **kwargs):
        self._config = kwargs["config"]

    def get(self, id):
        with CockroachHelper(self._config) as db:
            row = db.get_row('Languages', id)
            if not row:
                return LANGUAGE_NOT_FOUND, http.HTTPStatus.NOT_FOUND

            return Language(row=row).to_dict(), http.HTTPStatus.OK

    def put(self, id):
        parser = reqparse.RequestParser()
        [parser.add_argument(arg) for arg in LANGUAGE_INPUT_ARGUMENTS]
        args = parser.parse_args()
        logging.info(args)        

        with CockroachHelper(self._config) as db:
            row = db.update_row('Languages', id, args)
            if not row:
                return LANGUAGE_NOT_FOUND, http.HTTPStatus.NOT_FOUND

            return Language(row=row).to_dict(), http.HTTPStatus.OK

    def delete(self, id):
        with CockroachHelper(self._config) as db:
            result = db.delete_row("Languages", id)
            if result == "DELETE 1":
                 return None, http.HTTPStatus.NO_CONTENT

            return LANGUAGE_NOT_FOUND, http.HTTPStatus.NOT_FOUND


