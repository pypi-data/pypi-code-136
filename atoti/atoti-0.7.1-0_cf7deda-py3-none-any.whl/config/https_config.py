from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union

from atoti_core import keyword_only_dataclass

from ._config import Config, convert_path_to_absolute_string


@keyword_only_dataclass
@dataclass(frozen=True)
class HttpsConfig(Config):
    """The PKCS 12 keystore configuration to enable HTTPS on the application.

    Note:
        This requires the :mod:`atoti-plus <atoti_plus>` plugin.

    Note:
        PEM or DER certificates can be `converted to PKCS 12 with OpenSSL <https://stackoverflow.com/questions/56241667/convert-certificate-in-der-or-pem-to-pkcs12/56244685#56244685>`__.

    Example:

        >>> https_config = tt.HttpsConfig(certificate="../cert.p12", password="secret")

    """

    certificate: Union[Path, str]
    """The path to the certificate."""

    password: str
    """The password to read the certificate."""

    domain: str = "localhost"
    """The domain certified by the certificate."""

    certificate_authority: Optional[Union[str, Path]] = None
    """Path to the custom certificate authority to use to verify the HTTPS connection.

    Required when *certificate* is not signed by some trusted public certificate authority.
    """

    def __post_init__(self) -> None:
        convert_path_to_absolute_string(self, "certificate")
