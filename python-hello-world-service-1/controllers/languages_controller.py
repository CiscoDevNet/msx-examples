#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
from flask_restplus import Resource
from models.language import Language


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
        return [LANGUAGE_ENGLISH.to_dict(), LANGUAGE_RUSSIAN.to_dict()], 200

    def post(self):
        return LANGUAGE_ENGLISH.to_dict(), 201


class LanguageApi(Resource):
    def get(self, id):
        return LANGUAGE_ENGLISH.to_dict(), 200

    def put(self, id):
        return LANGUAGE_ENGLISH.to_dict(), 200

    def delete(self, id):
        return "", 204
