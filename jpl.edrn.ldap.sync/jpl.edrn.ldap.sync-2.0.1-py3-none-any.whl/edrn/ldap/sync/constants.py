# encoding: utf-8

'''☎️ EDRN LDAP Sync: constants.'''

import ldap


# LDAP-related
# ------------

ALL_GROUP_DN         = 'cn=All EDRN,dc=edrn,dc=jpl,dc=nasa,dc=gov'
COMMITTEE_RDF_URL    = 'https://edrn.jpl.nasa.gov/cancerdataexpo/rdf-data/committees/@@rdf'
GROUP_BASE           = 'dc=edrn,dc=jpl,dc=nasa,dc=gov'
GROUP_OBJECT_CLASSES = ['groupOfUniqueNames', 'top']
LDAP_URL             = 'ldaps://edrn-ds.jpl.nasa.gov'
MANAGER_DN           = 'uid=admin,ou=system'
SITE_RDF_URL         = 'https://edrn.jpl.nasa.gov/cancerdataexpo/rdf-data/sites/@@rdf'
USER_BASE            = 'dc=edrn,dc=jpl,dc=nasa,dc=gov'
USER_CLASS           = 'edrnPerson'
USER_OBJECT_CLASSES  = [USER_CLASS, 'inetOrgPerson', 'organizationalPerson', 'person', 'top']
USER_RDF_URL         = 'https://edrn.jpl.nasa.gov/cancerdataexpo/rdf-data/registered-person/@@rdf'


# Map from command-line to ldap constants
# ---------------------------------------

LDAP_SCOPES = {
    'base': ldap.SCOPE_BASE,
    'one': ldap.SCOPE_ONELEVEL,
    'sub': ldap.SCOPE_SUBTREE
}
