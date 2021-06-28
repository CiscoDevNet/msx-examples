#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
from flask_restplus import Resource
from flask_restplus import reqparse

from models.language import Language
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

class LanguagesApi(Resource):
    def get(self):
        config = Config("helloworld.yml")
        with CockroachHelper(config.cockroach) as db:
            rows = db.get_rows('Languages')

        return rows, 200


class LanguageApi(Resource):
    def get(self, id):
        config = Config("helloworld.yml")
        with CockroachHelper(config.cockroach) as db:
            rows = db.get_row('Languages', id)

        return rows, 200

    def post(self, id):
        return LANGUAGE_ENGLISH.to_dict(), 200        

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        config = Config("helloworld.yml")
        with CockroachHelper(config.cockroach) as db:
            statusmessage = db.updste_row('Languages', id, 'name', args['name'])

        return statusmessage, 200


    def delete(self, id):
        return "", 204
