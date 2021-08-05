#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#

import logging
from flask_restplus import Resource
from flask_restplus import reqparse

from models.item import Item
import config
from config import Config
from helpers.cockroach_helper import CockroachHelper
from helpers.consul_helper import ConsulHelper
from helpers.vault_helper import VaultHelper


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

items_post_args = ['languageid', 'languagename', 'value']

class ItemsApi(Resource):
    def get(self):
        try: 
            with CockroachHelper(Config("helloworld.yml")) as db:
                rows = db.get_rows('Items')
                logging.info(rows)
        except Exception as e:
            logging.error("helloworld service error:" + str(e))
            rows = [{"error": str(e)}]

        return rows, config.HTTP_STATUS_CODE_OK


    def post(self):
        parser = reqparse.RequestParser()
        [parser.add_argument(arg) for arg in items_post_args]
        args = parser.parse_args()

        logging.info(args)        

        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.insert_row('Items', args)

        return result, config.HTTP_STATUS_CODE_CREATED


    def delete(self):
        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.delete_rows('Items')

        return result, config.HTTP_STATUS_CODE_NOCONTENT



class ItemApi(Resource):
    def get(self, id):
        with CockroachHelper(Config("helloworld.yml")) as db:
            rows = db.get_row('Items', id)

        return rows, config.HTTP_STATUS_CODE_OK


    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('value')
        args = parser.parse_args()

        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.update_row('Items', id, 'value', args['value'])

        return result, config.HTTP_STATUS_CODE_OK


    def delete(self, id):
        with CockroachHelper(Config("helloworld.yml")) as db:
            result = db.delete_row('Items', id)

        return result, config.HTTP_STATUS_CODE_NOCONTENT
