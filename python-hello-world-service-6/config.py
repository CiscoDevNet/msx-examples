#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
import logging
import pkgutil
from os import environ
from collections import namedtuple
import yaml


HTTP_STATUS_CODE_OK         = 200
HTTP_STATUS_CODE_CREATED    = 201
HTTP_STATUS_CODE_NOCONTENT  = 204
HTTP_STATUS_CODE_BAD_REQUEST = 400
HTTP_STATUS_CODE_NOT_FOUND  = 404
HTTP_STATUS_CODE_NOT_IMPLEMENTED   = 501


ConsulConfig = namedtuple("ConsulConfig", ["host", "port", "cacert"])
VaultConfig = namedtuple("VaultConfig", ["scheme", "host", "port", "token", "cacert"])
CockroachConfig = namedtuple("CockroachConfig", ["host", "port", "databasename","username", "sslmode", "cacert"])
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

        # Ceate cockroach config object.
        self.cockroach = CockroachConfig(**config["cockroach"])

        # Create Swagger config object.
        self.swagger = SwaggerConfig(**config["swagger"])
