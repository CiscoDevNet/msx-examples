#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
from flask_restx import Resource
from models.item import Item


HELLO_WORLD_ENGLISH = Item(
    id="68963944-a88c-4e39-98fd-d77878231d81",
    language_id="01f643a5-7e34-4366-af1a-9cce5e5c68e8",
    language_name="English",
    value="Hello, World!")

HELLO_WORLD_RUSSIAN = Item(
    id="62ef8e5f-628a-4f8b-92c9-485981205d92",
    language_id="55f3028f-1b94-4edd-b14f-183b51b33d68",
    language_name="Russian",
    value="Привет мир!")


class ItemsApi(Resource):
    def get(self):
        return [HELLO_WORLD_ENGLISH.to_dict(), HELLO_WORLD_RUSSIAN.to_dict()], 200

    def post(self):
        return HELLO_WORLD_ENGLISH.to_dict(), 201


class ItemApi(Resource):
    def get(self, id):
        return HELLO_WORLD_ENGLISH.to_dict(), 200

    def put(self, id):
        return HELLO_WORLD_ENGLISH.to_dict(), 200

    def delete(self, id):
        return "", 204
