#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#

import logging

from flask import Flask
from msxsecurity import MSXSecurity
from msxswagger import MSXSwaggerConfig

from config import Config

from controllers.items_controller import ItemsApi, ItemApi
from controllers.languages_controller import LanguageApi, LanguagesApi
from helpers.consul_helper import ConsulHelper
from helpers.security_helper import SecurityHelper
from helpers.swagger_helper import SwaggerHelper
from helpers.vault_helper import VaultHelper
from helpers.cockroach_helper import CockroachHelper

logging.basicConfig(level=logging.INFO)

config = Config("helloworld.yml")
consul_helper = ConsulHelper(config.consul)
vault_helper = VaultHelper(config.vault)
swagger_helper = SwaggerHelper(config, consul_helper)
security_helper = SecurityHelper(config, consul_helper, vault_helper)

logging.info('helloworld_start_test')
app = Flask(__name__)
consul_helper.test()
logging.info('helloworld_consul_tested')
vault_helper.test()
logging.info('helloworld_vault_tested')

with CockroachHelper(config) as db:
	db.test()
logging.info('helloworld_CockroachHelper_tested')

swagger = MSXSwaggerConfig(
    app=app,
    documentation_config=swagger_helper.get_documentation_config(),
    swagger_resource=swagger_helper.get_swagger_resource())
logging.info('helloworld_swagger_created')

security = MSXSecurity(
    config=security_helper.get_config(cache_enabled=True, cache_ttl_seconds=300))
logging.info('helloworld_security_created')

swagger.api.add_resource(ItemsApi, "/api/v1/items")
swagger.api.add_resource(ItemApi, "/api/v1/items/<id>")
swagger.api.add_resource(LanguagesApi, "/api/v1/languages", resource_class_kwargs={"security": security})
swagger.api.add_resource(LanguageApi, "/api/v1/languages/<id>", resource_class_kwargs={"security": security})
app.register_blueprint(swagger.api.blueprint)

logging.info('helloworld_API_started')

if __name__ == '__main__':
    app.run()

