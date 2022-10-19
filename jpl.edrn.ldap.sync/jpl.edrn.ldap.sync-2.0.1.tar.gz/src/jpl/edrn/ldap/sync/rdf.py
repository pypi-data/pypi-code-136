# encoding: utf-8

'''☎️ EDRN LDAP Sync: Resource Description Format classes and functions.'''


import rdflib, logging, enum
from dataclasses import dataclass

_logger = logging.getLogger(__name__)


# RDF Predicates
# --------------

_account_pred_uri  = rdflib.term.URIRef('http://xmlns.com/foaf/0.1/accountName')
_chair_pred_uri    = rdflib.term.URIRef('http://edrn.nci.nih.gov/xml/rdf/edrn.rdf#chair')
_cochair_pred_uri  = rdflib.term.URIRef('http://edrn.nci.nih.gov/xml/rdf/edrn.rdf#coChair')
_com_type_pred_uri = rdflib.term.URIRef('http://edrn.nci.nih.gov/xml/rdf/edrn.rdf#committeeType')
_email_pred_uri    = rdflib.term.URIRef('http://xmlns.com/foaf/0.1/mbox')
_gn_pred_uri       = rdflib.term.URIRef('http://xmlns.com/foaf/0.1/givenname')
_member_pred_uri   = rdflib.term.URIRef('http://edrn.nci.nih.gov/xml/rdf/edrn.rdf#member')
_phone_pred_uri    = rdflib.term.URIRef('http://xmlns.com/foaf/0.1/phone')
_pi_pred_uri       = rdflib.term.URIRef('http://edrn.nci.nih.gov/rdf/schema.rdf#pi')
_sn_pred_uri       = rdflib.term.URIRef('http://xmlns.com/foaf/0.1/surname')
_staff_pred_uri    = rdflib.term.URIRef('http://edrn.nci.nih.gov/rdf/schema.rdf#staff')
_status_pred_uri   = rdflib.term.URIRef('http://edrn.nci.nih.gov/rdf/schema.rdf#employmentActive')


# RDF object types
# ----------------

_site_type = rdflib.term.URIRef('http://edrn.nci.nih.gov/rdf/types.rdf#Site')
_committee_type = rdflib.term.URIRef('http://edrn.nci.nih.gov/rdf/types.rdf#Committee')


# Classes & Enums
# ---------------

class Status(enum.Enum):
    '''The status of an EDRN person.'''
    UNKNOWN = -1
    INACTIVE = 0
    ACTIVE = 1


@dataclass(order=True, frozen=True)
class Person(object):
    '''And EDRN person.'''
    uid: str
    sn: str
    gn: str
    email: str
    phone: str
    status: Status
    subject_uri: str

    @property
    def cn(self) -> str:
        return f'{self.gn} {self.sn}'


@dataclass(order=True, frozen=True)
class Group(object):
    '''A geneeric group (could be a site or a committee) with a common name and members.'''
    cn: str
    members: set


class Site(Group):
    '''An EDRN funded site.'''
    pass


class Committee(Group):
    '''An EDRN committee.'''
    pass


# Functions
# ---------

def parse(url: str):
    '''Parse the given RDF ``url`` and return a dict of statements (subject URIs to predicates), which itself is a dict
    of predicate URIs to sequences of objects.
    '''
    statements = {}
    graph = rdflib.Graph()
    graph.parse(url)
    for s, p, o in graph:
        predicates = statements.get(s, dict())
        objects = predicates.get(p, list())
        objects.append(o)
        predicates[p] = objects
        statements[s] = predicates
    _logger.debug('Read %d statements from %s', len(statements), url)
    return statements


def sv(predicate_uri: rdflib.term.URIRef, predicates: dict) -> object:
    '''From the dict of ``predicates`` return the first value only matching ``predicate_uri`` or ``None``
    if the predicate doesn't occur within the ``predicates``. Here, ``sv`` means "single value".
    '''
    return predicates.get(predicate_uri, [None])[0]


def get_rdf_type(predicates: dict) -> rdflib.term.URIRef:
    '''Get the single RDF type of the object described by the given ``predicates``, or ``None`` if it's
    not available.
    '''
    return predicates.get(rdflib.RDF.type, [None])[0]


def get_rdf_people(url: str) -> dict:
    '''Return all people currently in RDF as a mapping from user ID to ``Person`` objects. Skip anyone who is
    without an account name.
    '''
    statements, people = parse(url), {}
    for subject_uri, predicates in statements.items():
        uid = sv(_account_pred_uri, predicates)
        if not uid: continue
        uid = str(uid).lower()

        status = sv(_status_pred_uri, predicates)
        if not status:
            status = Status.UNKNOWN
        elif str(status) == 'Former employee':
            status = Status.INACTIVE
        else:
            status = Status.ACTIVE

        sn = sv(_sn_pred_uri, predicates)
        sn = str(sn) if sn else 'UNKNOWN'
        gn = sv(_gn_pred_uri, predicates)
        gn = str(gn) if gn else 'UNKNOWN'

        email = sv(_email_pred_uri, predicates)
        if not email:
            email = 'UNKNOWN@UNKNOWN.COM'
        else:
            # Strip the 'mailto:'
            email = str(email[7:])

        p = Person(str(uid), str(sn), str(gn), email, str(sv(_phone_pred_uri, predicates)), status, subject_uri)
        people[uid] = p

    return people


def get_rdf_sites(rdf_people: dict, url: str) -> dict:
    '''Return all sites currently in RDF as a mapping from site name (which is the bizarre convention of
    the principal investigator's last name plus the name of the institution) to ``Site`` objects. We skip
    any site for which we cannot determine a PI. This takes as input the ``rdf_people`` output from
    ``get_rdf_people`` and the ``url`` to the site RDF data source.
    '''
    people = {i.subject_uri: i for i in rdf_people.values()}
    statements, sites = parse(url), {}
    for predicates in statements.values():
        if get_rdf_type(predicates) != _site_type: continue     # Not a Site? Skip it
        title = sv(rdflib.DCTERMS.title, predicates)            # Grab thte name of the site
        title = str(title).strip().replace(',', '')             # DMCC data is always weirdly padded; see [1]
        if not title: continue                                  # Unnamed? Skipt it
        pi = people.get(sv(_pi_pred_uri, predicates))           # Find the PI
        if not pi: continue                                     # No principal investigator? Skip it
        site_name = f'{pi.sn} {title}'                          # Figure out weird site name we use in EDRN
        members = set([pi])                                     # Start with the pi
        for person_uri in predicates.get(_staff_pred_uri, []):  # For each member's RDF subject URI
            member = people.get(person_uri)                     # Find the member
            if member: members.add(member)                      # If we got one, note it
        site = Site(site_name, members)
        sites[site_name] = site
    return sites


def get_rdf_collab_groups(rdf_people: dict, url: str) -> dict:
    '''Get the collaborative groups (only) from the committee RDF source at ``url`` and filling each
    group with people from ``rdf_people``, returning a dict of committee CN to ``Committee``.
    '''
    people = {i.subject_uri: i for i in rdf_people.values()}
    statements, groups = parse(url), {}
    for predicates in statements.values():
        if get_rdf_type(predicates) != _committee_type: continue
        if str(sv(_com_type_pred_uri, predicates)).strip() != 'Collaborative Group': continue
        title = sv(rdflib.DCTERMS.title, predicates)
        title = str(title).strip()
        if not title: continue
        title = title[0:title.rindex(' Cancers Research Group')]
        members = set()
        chair = people.get(sv(_chair_pred_uri, predicates))
        if chair: members.add(chair)
        cochair = people.get(sv(_cochair_pred_uri, predicates))
        if cochair: members.add(cochair)
        for person_uri in predicates.get(_member_pred_uri, []):
            member = people.get(person_uri)
            if member: members.add(member)
        group = Committee(title, members)
        groups[title] = group
    return groups


# [1] While the common name for some sites may indeed be "Boutros The University of California, Los Angeles",
# the best practices for LDAP (see https://cutt.ly/aBNFeUE) suggest avoiding any special characaters in
# naming attributes in RDNs. Chris Mattmann established the practice of replacing commas with spaces in
# an earlier version of this software, but this left a group named with an awkward double-space. Here, we
# elect to just drop commas.
