#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
import http
import logging
from flask_restx import Resource
from flask_restx import reqparse
from helpers.cockroach_helper import CockroachHelper
from models.item import Item

ITEM_INPUT_ARGUMENTS = ['languageId', 'value']

ITEM_NOT_FOUND = 'Item not found'

LANGUAGE_NOT_FOUND = 'Language not found'

LANGUAGE_ID_IS_REQUIRED = 'Language id is required'


class ItemsApi(Resource):
    def __init__(self, *args, **kwargs):
        Resource.__init__(self, *args)
        self._config = kwargs["config"]

    def get(self):
        with CockroachHelper(self._config) as db:
            rows = db.get_rows('Items')
            logging.info(rows)

        items = [Item(row=x) for x in rows]
        return [x.to_dict() for x in items], http.HTTPStatus.OK

    def post(self):
        parser = reqparse.RequestParser()
        [parser.add_argument(arg) for arg in ITEM_INPUT_ARGUMENTS]
        args = parser.parse_args()
        logging.info(args)

        if "languageId" not in args or not args["languageId"]:
            return LANGUAGE_ID_IS_REQUIRED, http.HTTPStatus.BAD_REQUEST
        args['languageid'] = args.pop('languageId')

        with CockroachHelper(self._config) as db:
            language_row = db.get_row('Languages', args["languageid"])
            logging.info(language_row)
            if not language_row:
                return LANGUAGE_NOT_FOUND, http.HTTPStatus.BAD_REQUEST
            args["languagename"] = language_row["name"]

            row = db.insert_row('Items', args)
            return Item(row=row).to_dict(), http.HTTPStatus.CREATED
        return None, http.HTTPStatus.INTERNAL_SERVER_ERROR


class ItemApi(Resource):
    def __init__(self, *args, **kwargs):
        Resource.__init__(self, *args)
        self._config = kwargs["config"]

    def get(self, id):
        with CockroachHelper(self._config) as db:
            row = db.get_row('Items', id)
            if not row:
                return ITEM_NOT_FOUND, http.HTTPStatus.NOT_FOUND

            return Item(row=row).to_dict(), http.HTTPStatus.OK

    def put(self, id):
        parser = reqparse.RequestParser()
        [parser.add_argument(arg) for arg in ITEM_INPUT_ARGUMENTS]
        args = parser.parse_args()
        logging.info(args)

        if 'languageId' not in args or not args['languageId']:
            return LANGUAGE_ID_IS_REQUIRED, http.HTTPStatus.BAD_REQUEST
        args['languageid'] = args.pop('languageId')

        with CockroachHelper(self._config) as db:
            language_row = db.get_row('Languages', args["languageid"])
            if not language_row:
                return LANGUAGE_NOT_FOUND, http.HTTPStatus.BAD_REQUEST
            args["languagename"] = language_row["name"]

            row = db.update_row('Items', id, args)
            if not row:
                return ITEM_NOT_FOUND, http.HTTPStatus.NOT_FOUND
            return Item(row=row).to_dict(), http.HTTPStatus.OK

    def delete(self, id):
        with CockroachHelper(self._config) as db:
            result = db.delete_row('Items', id)
            if result != 'DELETE 1':
                return ITEM_NOT_FOUND, http.HTTPStatus.NOT_FOUND

            return result, http.HTTPStatus.NO_CONTENT




