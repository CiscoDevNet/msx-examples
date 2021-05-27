#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
from flask import Flask
from msxswagger import MSXSwaggerConfig, Security, DocumentationConfig, Sso
from controllers.items_controller import ItemsApi, ItemApi
from controllers.languages_controller import LanguageApi, LanguagesApi


app = Flask(__name__)
sso = Sso(base_url='https://dev-plt-aio1.lab.ciscomsx.com/idm',
          client_id='hello-world-service-public-client')

documentation_config = DocumentationConfig(
	root_path='/helloworld',
	security=Security(True, sso))

swagger = MSXSwaggerConfig(
	app,
	documentation_config,
	swagger_resource="swagger.json")

swagger.api.add_resource(ItemsApi, "/api/v1/items")
swagger.api.add_resource(ItemApi, "/api/v1/items/<id>")
swagger.api.add_resource(LanguagesApi, "/api/v1/languages")
swagger.api.add_resource(LanguageApi, "/api/v1/languages/<id>")
app.register_blueprint(swagger.api.blueprint)

if __name__ == '__main__':
	app.run()
