#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
import logging
from flask import Flask
from flask_restx import Api

from config import Config
from controllers.items_controller import ItemsApi, ItemApi
from controllers.languages_controller import LanguageApi, LanguagesApi
from helpers.consul_helper import ConsulHelper

from helpers.vault_helper import VaultHelper
from helpers.cockroach_helper import CockroachHelper

logging.basicConfig(level=logging.INFO)

config = Config("helloworld.yml")
consul_helper = ConsulHelper(config.consul)
vault_helper = VaultHelper(config.vault)
config.find_consul_vault_prefix(consul_helper)

app = Flask(__name__)
consul_helper.test(config.config_prefix)
vault_helper.test(config.config_prefix)

with CockroachHelper(config) as db:
    db.test()

api = Api(app)
api.add_resource(ItemsApi, "/helloworld/api/v1/items",
                 resource_class_kwargs={"config": config})
api.add_resource(ItemApi, "/helloworld/api/v1/items/<id>",
                 resource_class_kwargs={"config": config})
api.add_resource(LanguagesApi, "/helloworld/api/v1/languages",
                 resource_class_kwargs={"config": config})
api.add_resource(LanguageApi, "/helloworld/api/v1/languages/<id>",
                 resource_class_kwargs={"config": config})

if __name__ == '__main__':
    app.run()

