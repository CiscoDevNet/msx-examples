#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
import flask
from flask_restplus import Resource
from models.error import Error
from models.language import Language


LANGUAGE_ENGLISH = Language(
    id="01f643a5-7e34-4366-af1a-9cce5e5c68e8",
    name="English",
    description="A West Germanic language that uses the Roman alphabet.")


LANGUAGE_RUSSIAN = Language(
    id="55f3028f-1b94-4edd-b14f-183b51b33d68",
    name="Russian",
    description="An East Slavic language that uses the Cyrillic alphabet.")


def get_access_token():
    # Authorization: Bearer MY_ACCESS_TOKEN
    return flask.request.headers.get("Authorization", "")[7:]


class LanguagesApi(Resource):
    def __init__(self, *args, **kwargs):
        self._security = kwargs["security"]

    def get(self):
        if self._security.has_permission("HELLOWORLD_READ_LANGUAGE", get_access_token()):
            return [LANGUAGE_ENGLISH.to_dict(), LANGUAGE_RUSSIAN.to_dict()], 200
        return Error(code="my_error_code", message="permission denied").to_dict(), 403

    def post(self):
        if self._security.has_permission("HELLOWORLD_WRITE_LANGUAGE", get_access_token()):
            return LANGUAGE_ENGLISH.to_dict(), 201
        return Error(code="my_error_code", message="permission denied").to_dict(), 403


class LanguageApi(Resource):
    def __init__(self, *args, **kwargs):
        self._security = kwargs["security"]

    def get(self, id):
        if self._security.has_permission("HELLOWORLD_READ_LANGUAGE", get_access_token()):
            return LANGUAGE_ENGLISH.to_dict(), 200
        return Error(code="my_error_code", message="permission denied").to_dict(), 403

    def put(self, id):
        if self._security.has_permission("HELLOWORLD_WRITE_LANGUAGE", get_access_token()):
            return LANGUAGE_ENGLISH.to_dict(), 200
        return Error(code="my_error_code", message="permission denied").to_dict(), 403

    def delete(self, id):
        if self._security.has_permission("HELLOWORLD_WRITE_LANGUAGE", get_access_token()):
            return "", 204
        return Error(code="my_error_code", message="permission denied").to_dict(), 403
