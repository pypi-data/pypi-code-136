from typing import NamedTuple, Optional

from ...utils import OUTPUT_DIR, from_env, validate_baseurl
from .constant import ALL_LOOKS, BASE_URL, CLIENT_ID, CLIENT_SECRET


def _all_looks_from_env() -> bool:
    parameter = from_env(ALL_LOOKS, allow_missing=True)
    return str(parameter).lower() == "true"


class Parameters(NamedTuple):
    """Parameters for Looker extraction"""

    output_directory: str
    base_url: str
    client_id: str
    client_secret: str
    timeout: Optional[int]
    is_safe_mode: bool
    all_looks: bool


def get_parameters(**kwargs) -> Parameters:
    """
    Returns parameters for Looker extraction whether they come from script
    argument, env variable or default value.
    """
    output_directory = kwargs.get("output_directory") or from_env(OUTPUT_DIR)

    base_url = validate_baseurl(kwargs.get("base_url") or from_env(BASE_URL))
    client_id = kwargs.get("client_id") or from_env(CLIENT_ID)
    client_secret = kwargs.get("client_secret") or from_env(CLIENT_SECRET)

    # timeout can be set with env variable however we don't use from_env because it has a default value
    timeout = kwargs.get("timeout")

    is_safe_mode = kwargs.get("safe_mode", False)
    all_looks = kwargs.get("all_looks") or _all_looks_from_env()

    return Parameters(
        output_directory=output_directory,
        base_url=base_url,
        client_id=client_id,
        client_secret=client_secret,
        timeout=timeout,
        is_safe_mode=is_safe_mode,
        all_looks=all_looks,
    )
