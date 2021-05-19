#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
from flask import Flask, Response
from flask_restplus import Api
from msxswagger import MSXSwaggerConfig, Security, DocumentationConfig

from controllers.items_controller import ItemsApi, ItemApi
from controllers.languages_controller import LanguageApi, LanguagesApi

app = Flask(__name__)
api = Api(app)
api.add_resource(ItemsApi, "/helloworld/api/v1/items")
api.add_resource(ItemApi, "/helloworld/api/v1/items/<id>")
api.add_resource(LanguagesApi, "/helloworld/api/v1/languages")
api.add_resource(LanguageApi, "/helloworld/api/v1/languages/<id>")


# Configure Swagger Documentation
@app.route('/helloworld/swagger.json')
def swagger_json():
	with app.open_resource("swagger.json", "r") as file:
		content = file.read()
	return Response(
		content,
		mimetype='application/json',
		headers={'Content-Disposition': 'attachment;filename=swagger.json'})


documentation_config = DocumentationConfig(
	'/helloworld',
	'/helloworld/swagger.json',
	'/helloworld/swagger',
	'3.0.0',
	Security(False))

swagger = MSXSwaggerConfig(
	app,
	None,
	documentation_config,
	disable_swagger_json_generation=True)

app.register_blueprint(swagger.api.blueprint)


if __name__ == '__main__':
	app.run()
