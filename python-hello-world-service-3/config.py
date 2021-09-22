#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
import pkgutil
from collections import namedtuple
from os import environ

import yaml
from consul import ACLPermissionDenied

ConsulConfig = namedtuple("ConsulConfig", ["host", "port", "cacert"])


class Config(object):
    def __init__(self, resource_name):
        # Load and parse the configuration.
        resource = pkgutil.get_data(__name__, resource_name)
        config = yaml.safe_load(resource)
        self._config_prefix = None

        # Apply environment variables and create Consul config object.
        config["consul"]["host"] = environ.get("SPRING_CLOUD_CONSUL_HOST", config["consul"]["host"])
        config["consul"]["port"] = environ.get("SPRING_CLOUD_CONSUL_PORT", config["consul"]["port"])
        self.consul = ConsulConfig(**config["consul"])

    # Find the correct Consul/Vault prefix.
    def find_consul_vault_prefix(self, consul_helper):
        try:
            test_value = consul_helper.get_string("thirdpartycomponents/defaultapplication/swagger.security.sso.baseUrl", None)
        except ACLPermissionDenied:
            test_value = None
        self._config_prefix = "thirdpartycomponents" if test_value else "thirdpartyservices"
        return self._config_prefix

    @property
    def config_prefix(self):
        return self._config_prefix
