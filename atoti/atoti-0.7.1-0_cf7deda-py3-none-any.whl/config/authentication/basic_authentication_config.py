from dataclasses import dataclass
from typing import Optional

from atoti_core import keyword_only_dataclass

from .._config import Config


@keyword_only_dataclass
@dataclass(frozen=True)
class BasicAuthenticationConfig(Config):
    """The `basic authentication <https://en.wikipedia.org/wiki/Basic_access_authentication>`__ configuration.

    It is the easiest way to set up security since it only requires defining the users, their password, and their roles using :class:`~atoti_plus.security.BasicSecurity`.

    See also:
        :class:`atoti_query.BasicAuthentication`.
    """

    realm: Optional[str] = None
    """The realm describing the protected area.

    Different realms can be used to isolate sessions running on the same domain (regardless of the port).
    The realm will also be displayed by the browser when prompting for credentials.
    Defaults to some machine-wide unique ID.

    Example:

        >>> basic_auth_config = tt.BasicAuthenticationConfig(realm="Example")
    """
