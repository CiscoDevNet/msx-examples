#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
import pkgutil
from os import environ
from collections import namedtuple
import yaml

ConsulConfig = namedtuple("ConsulConfig", ["host", "port", "cacert"])


class Config(object):
    def __init__(self, resource_name):
        # Load and parse the configuration.
        resource = pkgutil.get_data(__name__, resource_name)
        config = yaml.safe_load(resource)

        # Apply environment variables and create Consul config object.
        config["consul"]["host"] = environ.get("SPRING_CLOUD_CONSUL_HOST", config["consul"]["host"])
        config["consul"]["port"] = environ.get("SPRING_CLOUD_CONSUL_PORT", config["consul"]["port"])
        self.consul = ConsulConfig(**config["consul"])


