import logging
import os

from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials


class KeyVaultFetcher(object):
    def __init__(self):
        super(KeyVaultFetcher, self).__init__()
        self._credentials = None
        self._logger = logging.getLogger("ICUMister." + __name__)

        def auth_callback(server, resource, scope):
            self._credentials = ServicePrincipalCredentials(
                client_id=os.environ['AZURE_CLIENT_ID'],
                secret=os.environ['AZURE_CLIENT_SECRET'],
                tenant=os.environ['AZURE_TENANT_ID'],
                resource='https://vault.azure.net'
            )

            token = self._credentials.token
            return token['token_type'], token['access_token']

        self._client = KeyVaultClient(KeyVaultAuthentication(auth_callback))
        self._vault_url = os.environ["KEY_VAULT_URI"]

    def get_secret(self, secret_id):
        self._logger.debug("Fetching secret " + secret_id)
        secret_bundle = self._client.get_secret(self._vault_url, secret_id, '')
        return secret_bundle.value
