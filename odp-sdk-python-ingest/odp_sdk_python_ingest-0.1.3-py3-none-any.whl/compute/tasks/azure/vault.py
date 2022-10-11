from azure.keyvault.secrets import SecretClient
from azure.identity._internal.client_credential_base import ClientCredentialBase
from prefect.tasks.secrets import SecretBase
from prefect.utilities.tasks import defaults_from_attrs
import logging

from odp.compute.secrets import get_runtime_secret_backend, get_client_credential

from typing import *

__all__ = ["AzureSecretTask", "azure_secret_task"]

LOG = logging.getLogger(__name__)


class AzureSecretTask(SecretBase):

    KUBERNETES_SECRET_NAME = "azure-sp-secret"

    def __init__(
        self,
        key_vault_name: Optional[str] = None,
        secret_name: Optional[str] = None,
        decode_cb: Optional[Callable] = None,
        **kwargs: Dict,
    ):
        super().__init__(**kwargs)
        self.key_vault_name = key_vault_name
        self.secret_name = secret_name
        self.decode_cb = decode_cb

    @defaults_from_attrs("key_vault_name", "secret_name", "decode_cb")
    def run(
        self,
        key_vault_name: Optional[str] = None,
        secret_name: Optional[str] = None,
        decode_cb: Optional[Callable] = None,
        credential: Optional[ClientCredentialBase] = None,
    ) -> Any:

        if not credential:
            credential = get_client_credential()

        client = SecretClient(
            vault_url=f"https://{key_vault_name}.vault.azure.net", credential=credential
        )

        LOG.debug(f"Retrieving secret {key_vault_name}.{secret_name}")

        ret = client.get_secret(secret_name).value
        if decode_cb:
            ret = decode_cb(ret)
        return ret


azure_secret_task = AzureSecretTask()
