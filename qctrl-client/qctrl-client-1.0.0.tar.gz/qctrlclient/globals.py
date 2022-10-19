# Copyright 2022 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

import os
from functools import wraps
from typing import (
    Any,
    Callable,
)

from .auth import CliAuth
from .constants import DEFAULT_OIDC_URL

_REGISTRY = {}


def global_value(key: str) -> Callable:
    """Adds values to a global registry. If the
    `key` already exists in the registry, the
    stored value is returned.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def customized_decorator() -> Any:

            try:
                value = _REGISTRY[key]
            except KeyError:
                value = func()
                _REGISTRY[key] = value

            return value

        return customized_decorator

    return decorator


@global_value("CLI_AUTH")
def get_cli_auth() -> CliAuth:
    """Returns global `CliAuth` object."""
    return CliAuth(os.getenv("QCTRL_OIDC_URL", DEFAULT_OIDC_URL))
