#!/usr/bin/env python3
# Copyright 2022 David Seaward and contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
import sys
import webbrowser
from importlib import resources

from samosa.git import validate_path


def invoke():
    if len(sys.argv) <= 1:
        if validate_path(os.getcwd()):
            exit(0)
        else:
            exit(1)
    elif sys.argv[1] == "help":
        path = resources.path("samosa.resource", "WORKFLOW.md")
        webbrowser.open(str(path))
    else:
        print("Arguments not recognised.", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    invoke()
