#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#

from flask import Flask

from config import Config
from msxswagger import MSXSwaggerConfig, Security, DocumentationConfig, Sso
from controllers.items_controller import ItemsApi, ItemApi
from controllers.languages_controller import LanguageApi, LanguagesApi

from helpers.consul_helper import ConsulHelper
from helpers.vault_helper import VaultHelper
from helpers.cockroach_helper import CockroachHelper


SSO_URL = "https://dev-plt-aio1.lab.ciscomsx.com/idm"
PUBLIC_CLIENT_ID = "hello-world-service-public-client"
PRIVATE_CLIENT_ID = "hello-world-service-private-client"
PRIVATE_CLIENT_SECRET = "make-up-a-private-client-secret-and-keep-it-safe"

app = Flask(__name__)

config = Config("helloworld.yml")
consul = ConsulHelper(config.consul)
vault = VaultHelper(config.vault)

app = Flask(__name__)
consul.test()
# vault.test()

with CockroachHelper(config.cockroach) as db:
	db.test()

swagger_config = DocumentationConfig(
	root_path='/helloworld',
	security=Security(True, Sso(base_url=SSO_URL, client_id=PUBLIC_CLIENT_ID)))

swagger = MSXSwaggerConfig(
	app,
	swagger_config,
	swagger_resource="swagger.json")

swagger.api.add_resource(ItemsApi, "/api/v1/items")
swagger.api.add_resource(ItemApi, "/api/v1/items/<id>")
swagger.api.add_resource(LanguagesApi, "/api/v1/languages")
swagger.api.add_resource(LanguageApi, "/api/v1/languages/<id>")
app.register_blueprint(swagger.api.blueprint)

if __name__ == '__main__':
	app.run()
