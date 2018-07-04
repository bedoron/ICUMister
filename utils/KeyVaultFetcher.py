from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials


class KeyVaultFetcher(object):
    def __init__(self, config_json):
        super(KeyVaultFetcher, self).__init__()
        self._keyvault = config_json.get("keyvault")
        self._credentials = None

        def auth_callback(server, resource, scope):
            self._credentials = ServicePrincipalCredentials(
                client_id=self._keyvault.get('client_id'),
                secret=self._keyvault.get('secret'),
                tenant=self._keyvault.get('tenant'),
                resource='https://vault.azure.net'
            )

            token = self._credentials.token
            return token['token_type'], token['access_token']

        self._client = KeyVaultClient(KeyVaultAuthentication(auth_callback))
        self._vault_url = self._keyvault.get('vault_url')

    def get_secret(self, secret_id):
        secret_bundle = self._client.get_secret(self._vault_url, secret_id, '')
        return secret_bundle.value
