# encoding: utf-8

'''☎️ Keep the ``All EDRN`` group up-to-date.'''

from . import VERSION
from .constants import ALL_GROUP_DN as GROUP_DN
from .constants import LDAP_SCOPES
from .constants import USER_BASE, USER_CLASS
from .utils import add_logging_arguments, add_ldap_arguments, get_manager_password
import sys, ldap, argparse, logging

__version__ = VERSION
_logger = logging.getLogger(__name__)
_prog_desc = 'Synchronizes the `All EDRN` group in EDRN LDAP'
SCOPE = 'one'


def main():
    '''Here we go. Rooster sound.'''
    parser = argparse.ArgumentParser(description=_prog_desc)
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    add_logging_arguments(parser)
    add_ldap_arguments(parser)
    parser.add_argument('--userbase', default=USER_BASE, help='Base DN where users are found [%(default)s]')
    parser.add_argument(
        '-s', '--scope', default=SCOPE, choices=['base', 'one', 'sub'],
        help='Search scope to find users [%(default)s]'
    )
    parser.add_argument('--userclass', default=USER_CLASS, help='Object class expected of users [%(default)s]')
    parser.add_argument('--group', default=GROUP_DN, help='DN of the "all users" group to update [%(default)s]')

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel, format='%(levelname)s %(message)s')

    userbase, scope, userclass, group = args.userbase, args.scope, args.userclass, args.group
    connection = ldap.initialize(args.url)
    password = get_manager_password(args)
    connection.simple_bind_s(args.manager_dn, password)

    all_users = connection.search_s(userbase, LDAP_SCOPES[scope], '(objectClass={})'.format(userclass), [], attrsonly=1)
    all_users = set([i[0] for i in all_users])

    current_members = connection.search_s(group, ldap.SCOPE_BASE, '(objectClass=*)', ['uniqueMember'])
    try:
        # OpenLDAP returns the key ``uniqueMember`` with capital ``M``
        current_members = set([str(i, 'utf-8') for i in current_members[0][1]['uniqueMember']])
    except KeyError:
        # Apache DS returns the key ``uniquemember`` with lowercase ``m``
        current_members = set([str(i, 'utf-8') for i in current_members[0][1]['uniquemember']])

    to_add = all_users - current_members
    to_remove = current_members - all_users
    if to_add:
        _logger.debug('Adding these people to %s: %r', to_add, group)
        connection.modify_s(group, [(ldap.MOD_ADD, 'uniqueMember', [i.encode('utf-8') for i in to_add])])
    if to_remove:
        _logger.debug('Removing these people from %s: %r', to_remove, group)
        connection.modify_s(group, [(ldap.MOD_DELETE, 'uniqueMember', [i.encode('utf-8') for i in to_remove])])

    sys.exit(0)


if __name__ == '__main__':
    main()
