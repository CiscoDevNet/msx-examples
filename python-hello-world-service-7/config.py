#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
import pkgutil
from os import environ
from collections import namedtuple
import yaml
from consul import ACLPermissionDenied

ConsulConfig = namedtuple("ConsulConfig", ["host", "port", "cacert"])
VaultConfig = namedtuple("VaultConfig", ["scheme", "host", "port", "token", "cacert"])
CockroachConfig = namedtuple("CockroachConfig", ["host", "port", "databasename","username", "sslmode", "cacert"])
SwaggerConfig = namedtuple("SwaggerConfig", ["rootpath", "secure", "ssourl", "clientid", "swaggerjsonpath"])
SecurityConfig = namedtuple("SecurityConfig", ["ssourl", "clientid", "clientsecret", "sslverify"])


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

        # Apply environment variables and create Vault config object.
        config["vault"]["scheme"] = environ.get("SPRING_CLOUD_VAULT_SCHEME", config["vault"]["scheme"])
        config["vault"]["host"] = environ.get("SPRING_CLOUD_VAULT_HOST", config["vault"]["host"])
        config["vault"]["port"] = environ.get("SPRING_CLOUD_VAULT_PORT", config["vault"]["port"])
        config["vault"]["token"] = environ.get("SPRING_CLOUD_VAULT_TOKEN", config["vault"]["token"])
        self.vault = VaultConfig(**config["vault"])

        # Create Cockroach config object.
        self.cockroach = CockroachConfig(**config["cockroach"])

        # Create Swagger config object.
        self.swagger = SwaggerConfig(**config["swagger"])

        # Create Security config object.
        self.security = SecurityConfig(**config["security"])

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