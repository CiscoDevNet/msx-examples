from flask import Flask, Response
from msxswagger import Security, DocumentationConfig, MSXSwaggerConfig, AppInfo
from items_controller import ItemsApi, ItemApi
from languages_controller import LanguagesApi, LanguageApi

app = Flask(__name__)

documentation_config = DocumentationConfig(
    '/helloworld',
    '/helloworld/swagger.json',
    '/helloworld/swagger',
    '3.0.0',
    Security(False))

swagger = MSXSwaggerConfig(app, None, documentation_config, disable_swagger_json_generation=True)

@app.route('/helloworld/swagger.json')
def swagger_json():
    with open("swagger.json", "r") as file:
        content = file.read()
    return Response(
        content,
        mimetype='application/json',
        headers={'Content-Disposition': 'attachment;filename=swagger.json'})


swagger.api.add_resource(LanguagesApi, "/api/v1/languages")
swagger.api.add_resource(LanguageApi, "/api/v1/languages<int:id>")
swagger.api.add_resource(ItemsApi, "/api/v1/items")
swagger.api.add_resource(ItemApi, "/api/v1/items/<int:id>")

app.register_blueprint(swagger.api.blueprint)
app.run(host='0.0.0.0', port=8082)
