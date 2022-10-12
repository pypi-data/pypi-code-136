from __future__ import annotations

import json
from dataclasses import asdict, dataclass, replace
from io import TextIOBase
from pathlib import Path
from typing import Any, Dict, Iterable, Literal, Mapping, Optional, Union

from atoti_core import EMPTY_MAPPING, keyword_only_dataclass

from .._path_utils import to_absolute_path
from ._config import Config, pop_optional_sub_config
from .authentication import (
    BasicAuthenticationConfig,
    KerberosConfig,
    LdapConfig,
    OidcConfig,
)
from .authentication._authentication_config import AuthenticationConfig
from .branding_config import BrandingConfig
from .client_certificate_config import ClientCertificateConfig
from .https_config import HttpsConfig
from .i18n_config import I18nConfig
from .jwt_config import JwtConfig
from .logging_config import LoggingConfig
from .user_content_storage_config import (
    UserContentStorageConfig,
    _create_user_content_storage_config_from_path_or_url,
)

_PYTHON_ONLY_OPTIONS = ["domain", "certificate_authority"]


@keyword_only_dataclass
@dataclass(frozen=True)
class SessionConfig(Config):

    app_extensions: Mapping[str, Union[str, Path]] = EMPTY_MAPPING

    authentication: Optional[AuthenticationConfig] = None

    branding: Optional[BrandingConfig] = None

    client_certificate: Optional[ClientCertificateConfig] = None

    extra_jars: Iterable[Union[str, Path]] = ()

    https: Optional[HttpsConfig] = None

    i18n: Optional[I18nConfig] = None

    java_options: Iterable[str] = ()

    jwt: Optional[JwtConfig] = None

    logging: Optional[LoggingConfig] = None

    port: int = 0

    same_site: Optional[Literal["none", "strict"]] = None

    user_content_storage: Optional[Union[Path, str, UserContentStorageConfig]] = None

    @classmethod
    def _from_mapping(cls, mapping: Mapping[str, Any]) -> SessionConfig:
        data = dict(mapping)
        return cls(
            authentication=pop_optional_sub_config(
                data,
                attribute_name="authentication",
                sub_config_class=AuthenticationConfig,
            ),
            branding=pop_optional_sub_config(
                data, attribute_name="branding", sub_config_class=BrandingConfig
            ),
            client_certificate=pop_optional_sub_config(
                data,
                attribute_name="client_certificate",
                sub_config_class=ClientCertificateConfig,
            ),
            https=pop_optional_sub_config(
                data, attribute_name="https", sub_config_class=HttpsConfig
            ),
            i18n=pop_optional_sub_config(
                data, attribute_name="i18n", sub_config_class=I18nConfig
            ),
            jwt=pop_optional_sub_config(
                data, attribute_name="jwt", sub_config_class=JwtConfig
            ),
            logging=pop_optional_sub_config(
                data, attribute_name="logging", sub_config_class=LoggingConfig
            ),
            user_content_storage=_pop_content_storage_config(data),
            **data,
        )

    def __post_init__(self) -> None:
        if self.app_extensions:
            self.__dict__["app_extensions"] = {
                name: to_absolute_path(path)
                for name, path in self.app_extensions.items()
            }

        self.__dict__["extra_jars"] = [
            to_absolute_path(jar_path) for jar_path in self.extra_jars
        ]


def _pop_content_storage_config(
    data: Dict[str, Any]
) -> Optional[UserContentStorageConfig]:
    user_content_storage = data.get("user_content_storage")
    if isinstance(user_content_storage, (str, Path)):
        # Pop the property like `pop_optional_sub_config()` would do.
        del data["user_content_storage"]
        return _create_user_content_storage_config_from_path_or_url(
            user_content_storage
        )
    return pop_optional_sub_config(
        data,
        attribute_name="user_content_storage",
        sub_config_class=UserContentStorageConfig,
    )


def get_logging_destination_io(config: SessionConfig) -> Optional[TextIOBase]:
    if config.logging:
        if isinstance(config.logging.destination, TextIOBase):
            return config.logging.destination
    return None


def serialize_config_to_json(
    config: SessionConfig,
) -> str:
    if get_logging_destination_io(config):
        # The io configured to write the logs to is not serializable and Java does not need it.
        config = replace(config, logging=replace(config.logging, destination=None))

    config_dict = asdict(
        config,
        # Remove keys for which the value is `None` (e.g. deprecated properties).
        dict_factory=lambda items: {
            key: value for key, value in items if value is not None
        },
    )

    if not config_dict.get("app_extensions"):
        # Remove empty mapping because the community edition does not allow this config option.
        del config_dict["app_extensions"]

    https_config = config_dict.get("https", {})
    for name in _PYTHON_ONLY_OPTIONS:
        https_config.pop(name, None)

    return json.dumps(config_dict)


def create_authentication_config(
    authentication: Union[
        BasicAuthenticationConfig, KerberosConfig, LdapConfig, OidcConfig
    ]
) -> AuthenticationConfig:
    if isinstance(authentication, LdapConfig):
        return AuthenticationConfig(ldap=authentication)
    if isinstance(authentication, KerberosConfig):
        return AuthenticationConfig(kerberos=authentication)
    if isinstance(authentication, BasicAuthenticationConfig):
        return AuthenticationConfig(basic=authentication)
    return AuthenticationConfig(oidc=authentication)
