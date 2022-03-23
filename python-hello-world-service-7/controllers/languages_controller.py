#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
import http
import logging

import flask
from flask_restx import Resource
from flask_restx import reqparse

from models.error import Error
from models.language import Language
from helpers.cockroach_helper import CockroachHelper

LANGUAGE_INPUT_ARGUMENTS = ['name', 'description']

LANGUAGE_NOT_FOUND = 'Language not found'


def get_access_token():
    # Authorization: Bearer MY_ACCESS_TOKEN
    return flask.request.headers.get("Authorization", "")[7:]


class LanguagesApi(Resource):
    def __init__(self, *args, **kwargs):
        self._config = kwargs["config"]
        self._security = kwargs["security"]

    def get(self):
        if not self._security.has_permission("HELLOWORLD_READ_LANGUAGE", get_access_token()):
            return Error(code="my_error_code", message="permission denied").to_dict(), 403

        with CockroachHelper(self._config) as db:
            rows = db.get_rows('Languages')
            logging.info(rows)

        languages = [Language(row=x) for x in rows]
        return [x.to_dict() for x in languages], http.HTTPStatus.OK

    def post(self):
        if not self._security.has_permission("HELLOWORLD_WRITE_LANGUAGE", get_access_token()):
            return Error(code="my_error_code", message="permission denied").to_dict(), 403

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
        self._security = kwargs["security"]

    def get(self, id):
        if not self._security.has_permission("HELLOWORLD_READ_LANGUAGE", get_access_token()):
            return Error(code="my_error_code", message="permission denied").to_dict(), 403

        with CockroachHelper(self._config) as db:
            row = db.get_row('Languages', id)
            if not row:
                return LANGUAGE_NOT_FOUND, http.HTTPStatus.NOT_FOUND

            return Language(row=row).to_dict(), http.HTTPStatus.OK

    def put(self, id):
        if not self._security.has_permission("HELLOWORLD_WRITE_LANGUAGE", get_access_token()):
            return Error(code="my_error_code", message="permission denied").to_dict(), 403

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
        if not self._security.has_permission("HELLOWORLD_WRITE_LANGUAGE", get_access_token()):
            return Error(code="my_error_code", message="permission denied").to_dict(), 403

        with CockroachHelper(self._config) as db:
            result = db.delete_row("Languages", id)
            if result == "DELETE 1":
                 return None, http.HTTPStatus.NO_CONTENT

            return LANGUAGE_NOT_FOUND, http.HTTPStatus.NOT_FOUND


