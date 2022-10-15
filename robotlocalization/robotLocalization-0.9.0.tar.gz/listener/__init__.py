# -*- coding: utf-8 -*-
"""
"""
import sys
import os

import configargparse
import pkg_resources

ROBOT_LISTENER_API_VERSION = 2

def robotL10NListener():
    return

def end_test(name, attrs):
    if attrs['status'] == 'FAIL':
        print(f'Test "{name}" failed: {attrs["message"]}')
        input('Press enter to continue.')

def init_config():
    p = configargparse.ArgParser(default_config_files=[".robotLocalization.yml"])
    # disagnose options
    p.add_argument("-v", "--verbose", help="enable verbose mode", env_var="VERBOSE",
        default=False, action='store_true')
    p.add_argument("-d", "--debug", env_var="DEBUG", default=False, action='store_true')
    p.add_argument("-n", "--dry_run", help="enable dry run mode.", action='store_true')
    p.add_argument("--locale", help="specify locale", default="en", action='store')

    # cli operand

    c = vars(p.parse_args())

    if c["verbose"]:
        print(f"config={c}")

    return c, p

def main():
    # config, argparser = init_config()
    grc = 0

    sys.stderr.write("successfully completed.\n" if grc == 0 else f"failed. rc={grc}\n")

    sys.exit(grc)
