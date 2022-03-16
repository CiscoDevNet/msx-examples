#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
from flask import Flask
from flask_restx import Api

from config import Config
from controllers.items_controller import ItemsApi, ItemApi
from controllers.languages_controller import LanguageApi, LanguagesApi
from helpers.consul_helper import ConsulHelper
import logging

from helpers.vault_helper import VaultHelper

logging.basicConfig(level=logging.INFO)

config = Config("helloworld.yml")
consul_helper = ConsulHelper(config.consul)
vault_helper = VaultHelper(config.vault)
config.find_consul_vault_prefix(consul_helper)

app = Flask(__name__)
consul_helper.test(config.config_prefix)
vault_helper.test(config.config_prefix)

api = Api(app)
api.add_resource(ItemsApi, "/helloworld/api/v1/items")
api.add_resource(ItemApi, "/helloworld/api/v1/items/<id>")
api.add_resource(LanguagesApi, "/helloworld/api/v1/languages")
api.add_resource(LanguageApi, "/helloworld/api/v1/languages/<id>")

if __name__ == '__main__':
	app.run()
