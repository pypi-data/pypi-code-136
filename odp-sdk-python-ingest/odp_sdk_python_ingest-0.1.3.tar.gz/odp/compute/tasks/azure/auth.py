from azure.identity import ClientSecretCredential, DefaultAzureCredential
from prefect.tasks.secrets import SecretBase
from prefect.utilities.tasks import defaults_from_attrs

from typing import *


__all__ = ["AzureDefaultCredentialTask"]


class AzureDefaultCredentialTask(SecretBase):
    def __init__(
        self,
        authority: Optional[str] = None,
        exclude_cli_credential: Optional[bool] = False,
        exclude_environment_credential: Optional[bool] = False,
        exclude_managed_identity_credential: Optional[bool] = False,
        exclude_powershell_credential: Optional[bool] = False,
        exclude_visual_studio_code_credential: Optional[bool] = False,
        exclude_shared_token_cache_credential: Optional[bool] = False,
        exclude_interactive_browser_credential: Optional[bool] = False,
        interactive_browser_tenant_id: Optional[str] = None,
        managed_identity_client_id: Optional[str] = None,
        shared_cache_username: Optional[str] = None,
        shared_cache_tenant_id: Optional[str] = None,
        visual_studio_code_tenant_id: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.authority = authority
        self.exclude_cli_credential = exclude_cli_credential
        self.exclude_environment_credential = exclude_environment_credential
        self.exclude_managed_identity_credential = exclude_managed_identity_credential
        self.exclude_powershell_credential = exclude_powershell_credential
        self.exclude_visual_studio_code_credential = (
            exclude_visual_studio_code_credential
        )
        self.exclude_shared_token_cache_credential = (
            exclude_shared_token_cache_credential
        )
        self.exclude_interactive_browser_credential = (
            exclude_interactive_browser_credential
        )
        self.interactive_browser_tenant_id = interactive_browser_tenant_id
        self.managed_identity_client_id = managed_identity_client_id
        self.shared_cache_username = shared_cache_username
        self.shared_cache_tenant_id = shared_cache_tenant_id
        self.visual_studio_code_tenant_id = visual_studio_code_tenant_id

    @defaults_from_attrs(
        "authority"
        "exclude_cli_credential"
        "exclude_environment_credential"
        "exclude_managed_identity_credential"
        "exclude_powershell_credential"
        "exclude_visual_studio_code_credential"
        "exclude_shared_token_cache_credential"
        "exclude_interactive_browser_credential"
        "interactive_browser_tenant_id"
        "managed_identity_client_id"
        "shared_cache_username"
        "shared_cache_tenant_id"
        "visual_studio_code_tenant_id"
    )
    def run(
        self,
        authority: Optional[str] = None,
        exclude_cli_credential: Optional[bool] = None,
        exclude_environment_credential: Optional[bool] = None,
        exclude_managed_identity_credential: Optional[bool] = None,
        exclude_powershell_credential: Optional[bool] = None,
        exclude_visual_studio_code_credential: Optional[bool] = None,
        exclude_shared_token_cache_credential: Optional[bool] = None,
        exclude_interactive_browser_credential: Optional[bool] = None,
        interactive_browser_tenant_id: Optional[str] = None,
        managed_identity_client_id: Optional[str] = None,
        shared_cache_username: Optional[str] = None,
        shared_cache_tenant_id: Optional[str] = None,
        visual_studio_code_tenant_id: Optional[str] = None,
    ):
        return DefaultAzureCredential(
            authority=authority,
            exclude_cli_credential=exclude_cli_credential,
            exclude_environment_credential=exclude_environment_credential,
            exclude_managed_identity_credential=exclude_managed_identity_credential,
            exclude_powershell_credential=exclude_powershell_credential,
            exclude_visual_studio_code_credential=exclude_visual_studio_code_credential,
            exclude_shared_token_cache_credential=exclude_shared_token_cache_credential,
            exclude_interactive_browser_credential=exclude_interactive_browser_credential,
            interactive_browser_tenant_id=interactive_browser_tenant_id,
            managed_identity_client_id=managed_identity_client_id,
            shared_cache_username=shared_cache_username,
            shared_cache_tenant_id=shared_cache_tenant_id,
            visual_studio_code_tenant_id=visual_studio_code_tenant_id,
        )
