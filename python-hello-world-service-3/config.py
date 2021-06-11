#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
import logging
import pkgutil
from os import environ
from collections import namedtuple
import yaml

ConsulConfig = namedtuple("Consul", ["host", "port", "cacert"])


class Config(object):
    def __init__(self, resource_name):
        # Load and parse the configuration.
        resource = pkgutil.get_data(__name__, resource_name)
        config = yaml.safe_load(resource)

        # Bind config to environment based on expected injections.
        if "SPRING_CLOUD_CONSUL_HOST" in environ:
            config["consul"]["host"] = environ.get("SPRING_CLOUD_CONSUL_HOST")
        if "SPRING_CLOUD_CONSUL_PORT" in environ:
            config["consul"]["port"] = environ.get("SPRING_CLOUD_CONSUL_PORT")

        # Map configuration to object.
        self.consul = ConsulConfig(**config["consul"])

