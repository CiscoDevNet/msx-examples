#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
import consul
import urllib3.util
import logging

from config import ConsulConfig


class ConsulHelper(object):
    def __init__(self, config: ConsulConfig):
        url = urllib3.util.parse_url(config.host)
        self._client = consul.Consul(
            host=url.hostname,
            port=config.port,
            scheme=url.scheme,
            verify=config.cacert)

    def get_string(self, key, default):
        index, data = self._client.kv.get(key)
        return data["Value"].decode("utf-8") if data else default

    def test(self, prefix):
        # Read our favourites from Consul and print them to the console.
        # Do not leak config in production as it is a security violation.
        favourite_colour = self.get_string(f"{prefix}/helloworldservice/favourite.color", "UNKNOWN")
        logging.info(f"My favourite color is {favourite_colour}")
        favourite_food = self.get_string(f"{prefix}/helloworldservice/favourite.food", "UNKNOWN")
        logging.info(f"My favourite food is {favourite_food}")
        favourite_dinosaur = self.get_string(f"{prefix}/helloworldservice/favourite.dinosaur", "UNKNOWN")
        logging.info(f"My favourite dinosaur is {favourite_dinosaur}")

