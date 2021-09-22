#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
import logging

from flask import Flask
from msxswagger import MSXSwaggerConfig

from config import Config

from controllers.items_controller import ItemsApi, ItemApi
from controllers.languages_controller import LanguageApi, LanguagesApi
from helpers.consul_helper import ConsulHelper
from helpers.swagger_helper import SwaggerHelper
from helpers.vault_helper import VaultHelper
from helpers.cockroach_helper import CockroachHelper

logging.basicConfig(level=logging.INFO)

config = Config("helloworld.yml")
consul_helper = ConsulHelper(config.consul)
vault_helper = VaultHelper(config.vault)
config.find_consul_vault_prefix(consul_helper)
swagger_helper = SwaggerHelper(config, consul_helper)

app = Flask(__name__)
consul_helper.test(config.config_prefix)
vault_helper.test(config.config_prefix)

with CockroachHelper(config) as db:
    db.test()

swagger = MSXSwaggerConfig(
    app=app,
    documentation_config=swagger_helper.get_documentation_config(),
    swagger_resource=swagger_helper.get_swagger_resource())

swagger.api.add_resource(ItemsApi, "/api/v1/items",
                         resource_class_kwargs={"config": config})
swagger.api.add_resource(ItemApi, "/api/v1/items/<id>",
                         resource_class_kwargs={"config": config})
swagger.api.add_resource(LanguagesApi, "/api/v1/languages",
                         resource_class_kwargs={"config": config})
swagger.api.add_resource(LanguageApi, "/api/v1/languages/<id>",
                         resource_class_kwargs={"config": config})
app.register_blueprint(swagger.api.blueprint)

if __name__ == '__main__':
    app.run()

