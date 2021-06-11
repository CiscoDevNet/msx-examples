import consul
import urllib3.util
import logging

from config import ConsulConfig


class ConsulHelper(object):
    def __init__(self, config: ConsulConfig):
        url = urllib3.util.parse_url(config.host)
        if url.scheme == "https":
            self._consul = consul.Consul(
                host=url.hostname,
                port=config.port,
                scheme=url.scheme,
                verify=config.cacert)

        else:
            self._consul = consul.Consul(
                host=url.hostname,
                port=config.port,
                scheme=url.scheme)

    def get_string(self, key, default):
        index, data = self._consul.kv.get(key)
        return data["Value"].decode("utf-8") if data else default

    def test(self):
        # Read our favourites from Consul and print them to the console.
        # Do not leak config in production as it is a security violation.
        favourite_colour = self.get_string("thirdpartyservices/helloworldservice/favourite.color", "UNKNOWN")
        logging.info("My favourite color is %s.", favourite_colour)
        favourite_food = self.get_string("thirdpartyservices/helloworldservice/favourite.food", "UNKNOWN")
        logging.info("My favourite food is %s.", favourite_food)
        favourite_dinosaur = self.get_string("thirdpartyservices/helloworldservice/favourite.dinosaur", "UNKNOWN")
        logging.info("My favourite dinosaur is %s.", favourite_dinosaur)
