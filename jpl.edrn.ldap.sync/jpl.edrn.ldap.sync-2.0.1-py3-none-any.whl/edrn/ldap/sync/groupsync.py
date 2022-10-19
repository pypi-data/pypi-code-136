# encoding: utf-8

'''☎️ EDRN LDAP Sync: group sync with data from the DMCC.'''

from . import VERSION
from .constants import USER_RDF_URL, SITE_RDF_URL, COMMITTEE_RDF_URL, GROUP_BASE, GROUP_OBJECT_CLASSES, USER_BASE
from .rdf import get_rdf_people, get_rdf_sites, get_rdf_collab_groups, Group
from .utils import add_logging_arguments, add_ldap_arguments, get_manager_password
import sys, ldap, ldap.modlist, logging, argparse

__version__ = VERSION
_logger = logging.getLogger(__name__)
_prog_desc = 'Synchronizes EDRN groups from the DMCC SOAP (RDF) feed into the EDRN LDAP'


def _add_to_ldap(connection: ldap.ldapobject.LDAPObject, group: Group):
    '''Add to the LDAP directory at the given ``connection`` the ``group``.'''
    dn = f'cn={group.cn},{GROUP_BASE}'
    name = group.cn.encode('utf-8')
    members = [f'uid={i.uid},{USER_BASE}'.encode('utf-8') for i in group.members]
    attrs = {
        'objectClass': [i.encode('utf-8') for i in GROUP_OBJECT_CLASSES],
        'cn': name,
        'description': name,
        'uniqueMember': members
    }
    modlist = ldap.modlist.addModlist(attrs)
    try:
        _logger.debug('Trying to add group %s', dn)
        connection.add_s(dn, modlist)
    except ldap.ALREADY_EXISTS:
        _logger.debug('%s already exists, so modifying its members', dn)
        mods = [(ldap.MOD_REPLACE, 'uniqueMember', members)]
        connection.modify_s(dn, mods)


def main():
    '''Here we go. Daddy.'''
    parser = argparse.ArgumentParser(description=_prog_desc)
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    add_logging_arguments(parser)
    add_ldap_arguments(parser)
    parser.add_argument('--user-rdf-url', default=USER_RDF_URL, help='URL to RDF info about people [%(default)s]')
    parser.add_argument('--site-rdf-url', default=SITE_RDF_URL, help='URL to RDF info about sites [%(default)s]')
    parser.add_argument('--committee-rdf-url', default=COMMITTEE_RDF_URL, help='URL to RDF info about committees [%(default)s]')

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel, format='%(levelname)s %(message)s')

    rdf_people = get_rdf_people(args.user_rdf_url)
    _logger.info('Users found in DMCC RDF: %d', len(rdf_people))
    rdf_sites = get_rdf_sites(rdf_people, args.site_rdf_url)
    _logger.info('Sites found in DMCC RDF: %d', len(rdf_sites))
    rdf_collab_groups = get_rdf_collab_groups(rdf_people, args.committee_rdf_url)
    _logger.info('Collab Groups found in DMCC RDF: %d', len(rdf_collab_groups))

    connection = ldap.initialize(args.url)
    password = get_manager_password(args)
    connection.simple_bind_s(args.manager_dn, password)

    for group in rdf_sites.values():
        _add_to_ldap(connection, group)
    for group in rdf_collab_groups.values():
        _add_to_ldap(connection, group)

    sys.exit(0)
