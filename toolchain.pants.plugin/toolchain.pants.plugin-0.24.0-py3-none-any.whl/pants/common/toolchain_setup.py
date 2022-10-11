# Copyright © 2020 Toolchain Labs, Inc. All rights reserved.
#
# Toolchain Labs, Inc. CONFIDENTIAL
#
# This file includes unpublished proprietary source code of Toolchain Labs, Inc.
# The copyright notice above does not evidence any actual or intended publication of such source code.
# Disclosure of this source code or any related proprietary information is strictly prohibited without
# the express written permission of Toolchain Labs, Inc.

# This pylint ignore is due to the migration of the pants options API, when we remove backward compatibility we should also remove this line
# pylint: disable=unexpected-keyword-arg
from __future__ import annotations

import logging

from pants.option.option_types import StrOption
from pants.option.subsystem import Subsystem

_logger = logging.getLogger(__name__)


class ToolchainSetupError(Exception):
    """Raised if the toolchain settings are not properly configured."""


class ToolchainSetup(Subsystem):
    options_scope = "toolchain-setup"
    help = """Setup specific to the Toolchain codebase."""
    showed_warning = False
    repo = StrOption(
        "--repo",
        default=None,
        help="The name of this repo (typically its name in GitHub)",
    )
    org = StrOption(
        "--org",
        default=None,
        help="The organization name on your Toolchain account (typically the same as the org name in GitHub)",
    )
    _base_url = StrOption(
        "--base-url",
        default="https://app.toolchain.com",
        advanced=True,
        help="Toolchain base url",
    )

    def safe_get_repo_name(self) -> str | None:
        return self.repo or None

    @property
    def org_name(self) -> str:
        if not self.org:
            raise ToolchainSetupError(
                'Please set org = "<your org name>" in the [toolchain-setup] section in pants.toml.'
                "Set this to the organization name on your Toolchain account (typically the same as the org name in GitHub)."
            )
        return self.org

    @property
    def base_url(self) -> str:
        return self._base_url

    def get_repo_name(self) -> str:
        repo = self.safe_get_repo_name()
        if not repo:
            raise ToolchainSetupError("Repo must be set under toolchain-setup.repo.")
        return repo
