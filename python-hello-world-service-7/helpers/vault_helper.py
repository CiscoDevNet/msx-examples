#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
import hvac
import logging

from hvac.exceptions import InvalidPath

from config import VaultConfig


class VaultHelper(object):
    def __init__(self, config: VaultConfig):
        self._client = hvac.Client(
            url=config.scheme + "://" + config.host + ":" + config.port,
            token=config.token,
            verify=config.cacert)

    def get_string(self, secret, key, default):
        try:
            response = self._client.secrets.kv.v1.read_secret(secret)
            if response and response["data"] and key in response["data"]:
                return response["data"][key]
        except InvalidPath as e:
            logging.error(str(e))
        return default

    def test(self):
        # Read a secret from Vault  and it to the console.
        # Do not leak secrets in production as it is a security violation.
        secret_squirrel_location = self.get_string("thirdpartyservices/helloworldservice/", "secret.squirrel.location", "UNKNOWN")
        logging.info("Where are the acorns buried?")
        logging.info(secret_squirrel_location)


