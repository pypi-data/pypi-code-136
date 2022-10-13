import warnings
from typing import Union, Callable, Optional, TypeVar, Type, Any
import logging
from pathlib import Path
from abc import ABC, abstractmethod

from clients_core.authentication.token_handler import OIDCTokenHandler, TokenHandler
from clients_core.rest_client import RestClient
from clients_core.secured_rest_client import SecuredRestClient
from clients_core.authentication.cache import DictCache
from clients_core.authentication.token_cache import TokenCache
from clients_core.api_match_client import (
    ServiceDirectoryMatchClient,
    MatchSpec,
    GatewayMatchClient,
    ApiMatchClient,
)
from clients_core.exceptions import ClientValueError
from clients_core.service_clients import E360ServiceClient
from sd_clients import ApiGatewayProvider, ServiceDirectoryClient
from sd_clients.settings import Settings


logger = logging.getLogger(__name__)

T = TypeVar("T")


class ClientStore(ABC):
    """
    This class contains helper functions for getting hold for REST clients for various E360 services
    """

    _api_gateway_key: Optional[str] = None
    _oidc_user_id: Optional[str] = None
    _token_cache: Optional[TokenHandler] = None
    _verify_ssl: bool = True
    _match_client: ApiMatchClient

    def __init__(
        self,
        match_client: ApiMatchClient,
        api_gateway_key: str = None,
        token_cache: TokenHandler = None,
        oidc_user_id: str = None,
        verify_ssl: bool = True,
    ):
        if not api_gateway_key and not token_cache:
            raise ValueError(
                "api_gateway_key or token_cache must be provided for initialization"
            )
        if api_gateway_key and token_cache:
            raise ValueError(
                "api_gateway_key and token_cache provided. Please only provide the authentication method wished to be used."
            )
        self._match_client = match_client
        self._api_gateway_key = api_gateway_key
        self._token_cache = token_cache
        self._oidc_user_id = oidc_user_id
        self._verify_ssl = verify_ssl
        if token_cache and not oidc_user_id:
            warnings.warn(
                "OIDC authentication set-up, but no `oidc_user_id` provided. Some features may not work as expected."
            )

    @property
    def oidc_user_id(self) -> Optional[str]:
        return self._oidc_user_id

    @classmethod
    def create_from_settings(
        cls, settings_path: Union[Path, str] = Settings.settings_path
    ) -> "ClientStore":
        f"""Initialze The client store using a settings file. This will be under the default location {Settings.settings_path}
        or it can be on a custom location specified as an argument.

        Args:
            settings_path: The path to the settings file

        Returns:
            New ClientStore instance

        """
        if not isinstance(settings_path, Path):
            settings_path = Path(settings_path)
        settings = Settings(settings_path=settings_path)
        if settings.is_api_gateway_mode:
            return cls.create_with_gateway(settings.api_gateway_key, settings.api_gateway_url, settings.verify_ssl)  # type: ignore
        elif settings.is_oidc_mode:
            return cls.create_with_oidc(
                settings.service_directory_url,  # type: ignore
                settings.oidc_endpoint_url,  # type: ignore
                settings.oidc_client_id,  # type: ignore
                settings.oidc_client_secret,  # type: ignore
                settings.oidc_user_id,
                settings.verify_ssl,
            )  # type: ignore
        else:
            raise ClientValueError(
                "Improperly configured, no valid OIDC or Api-Gateway settings"
            )

    @classmethod
    def create_with_gateway(
        cls,
        api_key: str,
        gateway_url: str = Settings.api_gateway_url,
        verify_ssl: bool = True,
    ) -> "ClientStore":
        provider = ApiGatewayProvider(gateway_url)
        match_client = GatewayMatchClient(provider)
        return cls(match_client, api_key, None, None, verify_ssl)

    @classmethod
    def create_with_oidc(
        cls,
        service_directory_url: str,
        oidc_endpoint: str,
        client_id: str,
        client_secret: str,
        oidc_user_id: str = None,
        verify_ssl: bool = True,
        token_cache_callback: Callable = None,
    ) -> "ClientStore":
        token_handler = OIDCTokenHandler(
            f"{oidc_endpoint.rstrip('/')}/connect/token",
            client_id,
            client_secret,
            verify_ssl,
        )
        token_cache = (
            token_cache_callback(token_handler)
            if token_cache_callback
            else TokenCache(DictCache(), token_handler)
        )
        rest_client = SecuredRestClient(
            service_directory_url,
            ["service-directory-service"],
            token_cache,
            verify_ssl=verify_ssl,
        )
        sd_client = ServiceDirectoryClient(rest_client)
        match_client = ServiceDirectoryMatchClient(sd_client)
        return cls(match_client, None, token_cache, oidc_user_id, verify_ssl)

    @property
    def is_api_gateway_mode(self) -> bool:
        return bool(self._api_gateway_key) and not bool(self._token_cache)

    def get_rest_client(self, match_spec: MatchSpec) -> RestClient:
        if self.is_api_gateway_mode:
            return self._match_client.get_simple_client(
                match_spec,
                extra_params={"apiKey": self._api_gateway_key},
                verify_ssl=self._verify_ssl,
            )
        else:
            return self._match_client.get_secured_client(
                match_spec, self._token_cache, verify_ssl=self._verify_ssl
            )

    def _get_service_client(
        self,
        match_spec: MatchSpec,
        ServiceClass: Type[T],
        attr: str,
        user_id: str = None,
        **kwargs: Any,
    ) -> T:
        if not user_id:
            user_id = self._oidc_user_id
        if not hasattr(self, attr):
            setattr(self, attr, self.get_rest_client(match_spec))
        return ServiceClass(getattr(self, attr), user_id=user_id, **kwargs)  # type: ignore

    @abstractmethod
    def get_vrs_plotly_client(
        self, user_id: str = None, **kwargs: Any
    ) -> E360ServiceClient:
        raise NotImplementedError("This function is not implemented")

    @abstractmethod
    def get_vrs_client(self, user_id: str = None, **kwargs: Any) -> E360ServiceClient:
        raise NotImplementedError("This function is not implemented")

    @abstractmethod
    def get_workspace_asset_client(
        self, user_id: str = None, **kwargs: Any
    ) -> E360ServiceClient:
        raise NotImplementedError("This function is not implemented")

    @abstractmethod
    def get_workspace_container_client(
        self, user_id: str = None, **kwargs: Any
    ) -> E360ServiceClient:
        raise NotImplementedError("This function is not implemented")

    @abstractmethod
    def get_fs_client(self, user_id: str = None, **kwargs: Any) -> E360ServiceClient:
        raise NotImplementedError("This function is not implemented")

    @abstractmethod
    def get_adt_definition_client(
        self, user_id: str = None, **kwargs: Any
    ) -> E360ServiceClient:
        raise NotImplementedError("This function is not implemented")

    @abstractmethod
    def get_adt_client(self, user_id: str = None, **kwargs: Any) -> E360ServiceClient:
        raise NotImplementedError("This function is not implemented")

    def get_dashboard_client(
        self, user_id: str = None, **kwargs: Any
    ) -> E360ServiceClient:
        raise NotImplementedError("This function is not implemented")

    def get_fss_client(self, user_id: str = None, **kwargs: Any) -> E360ServiceClient:
        raise NotImplementedError("This function is not implemented")
