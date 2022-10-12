#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# Copyright (C) 2022 Authors
#
# Released under GNU GPLv2 or later, read the file 'LICENSE.GPLv2+' for
# more information.
#
# Authors:
#   Bryce Harrington <bryce@canonical.com>

"""Global constants"""

ARCHES_ALL = ["amd64", "arm64", "armhf", "armel", "i386", "powerpc", "ppc64el", "s390x", "riscv64"]
ARCHES_PPA = ["amd64", "arm64", "armhf", "i386", "powerpc", "ppc64el", "s390x"]
ARCHES_PPA_EXTRA = ["riscv64"]
ARCHES_AUTOPKGTEST = ["amd64", "arm64", "armhf", "i386", "ppc64el", "s390x"]

URL_LPAPI = "https://api.launchpad.net/devel"
URL_AUTOPKGTEST = "https://autopkgtest.ubuntu.com"
