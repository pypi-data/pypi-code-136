# Copyright © 2019 Toolchain Labs, Inc. All rights reserved.
#
# Toolchain Labs, Inc. CONFIDENTIAL
#
# This file includes unpublished proprietary source code of Toolchain Labs, Inc.
# The copyright notice above does not evidence any actual or intended publication of such source code.
# Disclosure of this source code or any related proprietary information is strictly prohibited without
# the express written permission of Toolchain Labs, Inc.

from toolchain.pants.auth.plugin import toolchain_auth_plugin
from toolchain.pants.auth.rules import get_auth_rules
from toolchain.pants.buildsense.rules import rules_buildsense_reporter

# Allows pants to automatically detect the remote auth plugin and activate it.
remote_auth = toolchain_auth_plugin


def rules():
    return (
        *get_auth_rules(),
        *rules_buildsense_reporter(),
    )
