#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
import logging
from flask import Flask
from flask_restplus import Api

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

logging.info('helloworld=start_test')

app = Flask(__name__)
# consul_helper.test()
# logging.info('helloworld=consul_tested')
# vault_helper.test()
# logging.info('helloworld=vault_tested')

# with CockroachHelper(config) as db:
# 	db.test()
# logging.info('helloworld=CockroachHelper_tested')

api = Api(app)
api.add_resource(ItemsApi, "/helloworld/api/v1/items")
api.add_resource(ItemApi, "/helloworld/api/v1/items/<id>")
api.add_resource(LanguagesApi, "/helloworld/api/v1/languages")
api.add_resource(LanguageApi, "/helloworld/api/v1/languages/<id>")

logging.info('helloworld=API_started')

if __name__ == '__main__':
	app.run()
