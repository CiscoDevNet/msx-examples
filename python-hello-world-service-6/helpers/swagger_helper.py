#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
from msxswagger import DocumentationConfig, Security, Sso

from config import Config
from helpers.consul_helper import ConsulHelper


class SwaggerHelper(object):
    def __init__(self, config: Config, consul_helper: ConsulHelper):
        self._config = config
        self._consul_helper = consul_helper

    def get_documentation_config(self):
        sso_url = self._consul_helper.get_string(
            key=f"{self._config.config_prefix}/defaultapplication/swagger.security.sso.baseUrl",
            default=self._config.swagger.ssourl)
        client_id = self._consul_helper.get_string(
            key=f"{self._config.config_prefix}/helloworldservice/public.security.clientId",
            default=self._config.swagger.clientid)

        return DocumentationConfig(
            root_path='/helloworld',
            security=Security(
                enabled=self._config.swagger.secure,
                sso=Sso(base_url=sso_url, client_id=client_id)))

    def get_swagger_resource(self):
        return self._config.swagger.swaggerjsonpath
