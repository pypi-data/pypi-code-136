from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union

from atoti_core import keyword_only_dataclass

from ._config import Config, convert_path_to_absolute_string


@keyword_only_dataclass
@dataclass(frozen=True)
class ClientCertificateConfig(Config):
    """The JKS truststore config to enable client certificate authentication (also called mutual TLS or mTLS) on the application.

    This requires :class:`atoti.HttpsConfig` to be configured.

    It can be used alongside the other authentication providers.
    If a user presents valid certificates they will be authenticated, if not they will have to authenticate using the other configured security provider.

    Opening a query session on a session protected with this config can be done using :class:`atoti_query.ClientCertificate`.

    Example:
        >>> client_certificate = tt.ClientCertificateConfig(
        ...     trust_store="../truststore.jks", trust_store_password="secret"
        ... )
        >>> https = tt.HttpsConfig(certificate="../cert.p12", password="secret")

    """

    trust_store: Union[Path, str]
    """Path to the truststore file generated with the certificate used to sign client certificates."""

    trust_store_password: Optional[str]
    """Password protecting the truststore."""

    username_regex: str = "CN=(.*?)(?:,|$)"
    """Regex to extract the username from the certificate."""

    def __post_init__(self) -> None:
        convert_path_to_absolute_string(self, "trust_store")
