# encoding: utf-8

'''☎️ EDRN LDAP Sync: user sync with data from the DMCC.'''

from . import VERSION
from .constants import USER_BASE, USER_RDF_URL, USER_OBJECT_CLASSES
from .rdf import get_rdf_people, Person, Status
from .utils import add_logging_arguments, add_ldap_arguments, get_manager_password
import sys, ldap, ldap.modlist, logging, datetime, random, string, argparse

_logger = logging.getLogger(__name__)
_prog_desc = 'Synchronizes EDRN users from the DMCC SOAP (RDF) feed into the EDRN LDAP'
_password_corpus = string.ascii_letters + string.digits + string.punctuation
__version__ = VERSION


def _timestamp() -> str:
    '''Make a UTC timestamp as an ISO 8601 string.'''
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _generate_description() -> str:
    '''Make a suitable description of a person, which is just a timestamp for our purposes.'''
    return 'imported via EDRN dmccsync at ' + _timestamp()


def _generate_password() -> str:
    '''Make a random password.'''
    return '{CRYPT}' + ''.join(random.sample(_password_corpus, 16))


def _add(person: Person, connection: ldap.ldapobject.LDAPObject):
    '''Add the ``person`` to the LDAP server at ``connection``.'''
    dn = f'uid={person.uid},{USER_BASE}'
    attrs = {
        'cn': person.cn.encode('utf-8'),
        'description': _generate_description().encode('utf-8'),
        'mail': person.email.encode('utf-8'),
        'objectClass': [i.encode('utf-8') for i in USER_OBJECT_CLASSES],
        'sn': person.sn.encode('utf-8'),
        'telephoneNumber': person.phone.encode('utf-8'),
        'uid': person.uid.encode('utf-8'),
        'userPassword': _generate_password().encode('utf-8'),
    }
    modlist = ldap.modlist.addModlist(attrs)
    try:
        _logger.debug('Add new user %s', person.uid)
        connection.add_s(dn, modlist)
    except ldap.ALREADY_EXISTS:
        pass


def main():
    '''Let's do this.'''
    parser = argparse.ArgumentParser(description=_prog_desc)
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    add_logging_arguments(parser)
    add_ldap_arguments(parser)
    parser.add_argument('--userbase', default=USER_BASE, help='Base DN where users are found [%(default)s]')
    parser.add_argument('--user-rdf-url', default=USER_RDF_URL, help='URL to RDF information about people')

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel, format='%(levelname)s %(message)s')

    rdf_people = get_rdf_people(args.user_rdf_url)
    _logger.info('Users found in DMCC RDF: %d', len(rdf_people))
    active_uids, inactive_uids = set(), set()
    for person in rdf_people.values():
        if person.status == Status.ACTIVE:
            active_uids.add(person.uid)
        else:
            inactive_uids.add(person.uid)
    _logger.info('Of those, the actives number %d and the inactives %d', len(active_uids), len(inactive_uids))

    connection = ldap.initialize(args.url)
    password = get_manager_password(args)
    connection.simple_bind_s(args.manager_dn, password)
    ldap_people = connection.search_s(args.userbase, ldap.SCOPE_ONELEVEL, '(objectClass=edrnPerson)', ['uid'])
    ldap_uids = set([i[1]['uid'][0].decode('utf-8') for i in ldap_people])
    _logger.info('Number of edrnPersons in LDAP: %d', len(ldap_uids))

    # Delete all inactives
    dead_uids = inactive_uids & ldap_uids
    for dead_uid in dead_uids:
        try:
            _logger.debug('Deleting user %s', dead_uid)
            connection.delete_s(f'uid={dead_uid},{USER_BASE}')
        except ldap.NO_SUCH_OBJECT:
            pass
    _logger.info('Count of inactive users deleted: %d', len(dead_uids))

    # Add in whoever's new to LDAP
    new_uids = active_uids - ldap_uids
    for new_uid in new_uids:
        person = rdf_people[new_uid]
        _add(person, connection)
    _logger.info('Count of new users added: %d', len(new_uids))

    sys.exit(0)


if __name__ == '__main__':
    main()
