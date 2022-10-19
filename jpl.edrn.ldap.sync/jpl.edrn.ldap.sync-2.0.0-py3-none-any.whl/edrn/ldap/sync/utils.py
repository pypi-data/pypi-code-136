# encoding: utf-8

'''☎️ EDRN LDAP Sync: utilities.'''

from .constants import LDAP_URL, MANAGER_DN
import logging, argparse, os, getpass


def add_logging_arguments(parser: argparse.ArgumentParser):
    '''Add command-line argument support to ``parser`` for logging controls.'''
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '--debug', action='store_const', dest='loglevel', const=logging.DEBUG, default=logging.INFO,
        help='🐞 Log copious and verbose messages suitable for developers'
    )
    group.add_argument(
        '--quiet', action='store_const', dest='loglevel', const=logging.WARNING,
        help="🤫 Don't log informational messages"
    )


def add_ldap_arguments(parser: argparse.ArgumentParser):
    '''Add command-line arguments to support identifying and connecting to an LDAP server.'''
    group = parser.add_argument_group('LDAP Server', description='How to identify and authenticate with LDAP')
    group.add_argument('-H', '--url', default=LDAP_URL, help='URL to the LDAP server [%(default)s]')
    group.add_argument('-D', '--manager-dn', default=MANAGER_DN, help='DN of the manager user [%(default)s]')
    group.add_argument(
        '-w', '--password',
        help='Password for the manager DN; defaults to MANAGER_DN_PASSWORD env var, or will be prompted if unset'
    )


def get_manager_password(options: argparse.Namespace) -> str:
    '''Get the LDAP's manager password from the given ``options``. If it's not there, then try the
    MANAGER_DN_PASSWORD environment variable. And if that's not given, then prompt for it.
    '''
    password = options.password
    if not password:
        password = os.getenv('MANAGER_DN_PASSWORD')
        if not password:
            password = getpass.getpass(f'Password for {options.manager_dn}: ')
    return password
