#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# Author:  Bryce Harrington <bryce@canonical.com>
#
# Copyright (C) 2019 Bryce W. Harrington
#
# Released under GNU GPLv2 or later, read the file 'LICENSE.GPLv2+' for
# more information.

import sys
import pprint

DEBUGGING = False


def dbg(msg):
    """Prints information if debugging is enabled"""
    if DEBUGGING:
        if type(msg) is str:
            sys.stderr.write("{}\n".format(msg))
        else:
            pprint.pprint(msg)


def warn(msg):
    """Prints message to stderr"""
    sys.stderr.write("Warning: {}\n".format(msg))


def die(msg, code=1):
    """Prints message to stderr and exits with given code"""
    sys.stderr.write("Error: {}\n".format(msg))
    sys.exit(code)
