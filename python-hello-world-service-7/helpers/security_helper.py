#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
from msxsecurity import MSXSecurityConfig

from config import Config
from helpers.consul_helper import ConsulHelper
from helpers.vault_helper import VaultHelper


class SecurityHelper(object):
    def __init__(self, config: Config, consul_helper: ConsulHelper, vault_helper: VaultHelper):
        self._config = config
        self._consul_helper = consul_helper
        self._vault_helper = vault_helper

    def get_config(self, cache_enabled, cache_ttl_seconds):
        sso_url = self._consul_helper.get_string(
            key=f"{self._config.config_prefix}/defaultapplication/swagger.security.sso.baseUrl",
            default=self._config.security.ssourl)
        client_id = self._consul_helper.get_string(
            key=f"{self._config.config_prefix}/helloworldservice/integration.security.clientId",
            default=self._config.security.clientid)
        client_secret = self._vault_helper.get_string(
            secret=f"{self._config.config_prefix}/helloworldservice",
            key="integration.security.clientSecret",
            default=self._config.security.clientsecret)

        return MSXSecurityConfig(
            sso_url=sso_url,
            client_id=client_id,
            client_secret=client_secret,
            cache_enabled=cache_enabled,
            cache_ttl_seconds=cache_ttl_seconds)
