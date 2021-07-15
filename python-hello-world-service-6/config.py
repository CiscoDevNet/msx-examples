#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#

import pkgutil
from os import environ
from collections import namedtuple
import yaml

ConsulConfig = namedtuple("ConsulConfig", ["host", "port", "cacert"])
VaultConfig = namedtuple("VaultConfig", ["scheme", "host", "port", "token", "cacert"])
CockroachConfig = namedtuple("CockroachConfig", ["host", "port", "databasename","username", "sslmode"])
SwaggerConfig = namedtuple("SwaggerConfig", ["rootpath", "secure", "ssourl", "clientid", "swaggerjsonpath"])

class Config(object):
    def __init__(self, resource_name):
        # Load and parse the configuration.
        resource = pkgutil.get_data(__name__, resource_name)
        config = yaml.safe_load(resource)

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

        # Apply environment variables and create cockroach config object.
        config["cockroach"]["host"] = environ.get("SPRING_CLOUD_COCKROACH_HOST", config["cockroach"]["host"])
        config["cockroach"]["port"] = environ.get("SPRING_CLOUD_COCKROACH_PORT", config["cockroach"]["port"])
        config["cockroach"]["databasename"] = environ.get("SPRING_CLOUD_COCKROACH_DATABASENAME", config["cockroach"]["databasename"])
        config["cockroach"]["username"] = environ.get("SPRING_CLOUD_COCKROACH_USERNAME", config["cockroach"]["username"])
        config["cockroach"]["sslmode"] = environ.get("SPRING_CLOUD_COCKROACH_SSLMODE", config["cockroach"]["sslmode"])
        self.cockroach = CockroachConfig(**config["cockroach"])

        # Create Swagger config object.
        self.swagger = SwaggerConfig(**config["swagger"])