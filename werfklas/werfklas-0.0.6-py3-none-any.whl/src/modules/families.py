from datetime import date

from sqlalchemy.orm import Query

from src.classes.database import Child, sessionSetup, Teacher, Class, Family, Parent
from src.modules.common import find_parents

session = sessionSetup()


def find_all_parents():
    # session.close()
    _parents = Query(Parent).with_entities(Parent.uuid, Parent.firstname, Parent.lastname).with_session(session)
    _all_parents = []
    for _parent in _parents:
        _all_parents.append({
            'uuid': _parent['uuid'],
            'fullname': _parent['firstname'] + ' ' + _parent['lastname'],
        })
    # session.close()
    return _all_parents


def find_families(uuid):
    query_entities = [
        Family.uuid,
        Family.parent1_uuid,
        Family.parent2_uuid,
        Family.divorced,
    ]
    if uuid is None:
        _families_from_database = Query(query_entities).with_session(session)
    else:
        _families_from_database = Query(query_entities).filter(Family.uuid == uuid).with_session(session)
    _families = []
    for _family in _families_from_database:
        _families.append({
            'uuid': _family['uuid'],
            'parent1_uuid': _family['parent1_uuid'],
            'parent1': find_parents(_family['parent1_uuid']),
            'parent2_uuid': _family['parent2_uuid'],
            'parent2': find_parents(_family['parent2_uuid']),
            'divorced': _family['divorced']
        })
    return _families


def provision_edit_family(uuid):
    _family = find_families(uuid)[0]
    _parent1 = find_parents(_family['parent1_uuid'])
    _parent2 = find_parents(_family['parent2_uuid'])
    _family_to_edit = {'uuid': _family['uuid'],
                       'divorced': _family['divorced'],
                       'parent1': {
                           'uuid': _parent1['uuid'],
                           'firstname': _parent1['firstname'],
                           'lastname': _parent1['lastname'],
                           'address': _parent1['address'],
                           'city': _parent1['city'],
                           'zipcode': _parent1['zipcode'],
                           'phone': _parent1['phone'],
                           'email': _parent1['email']
                       },
                       }
    if _parent2:
        _family_to_edit.update({
            'parent2': {
                'uuid': _parent2['uuid'],
                'firstname': _parent2['firstname'],
                'lastname': _parent2['lastname'],
                'address': _parent2['address'],
                'city': _parent2['city'],
                'zipcode': _parent2['zipcode'],
                'phone': _parent2['phone'],
                'email': _parent2['email']
            }})
    else:
        _family_to_edit.update({
            'parent2': {}})
    return _family_to_edit


def find_family():
    _families_from_database = find_families('')
    # family table
    # parents opzoeken
    # tuple aanmaken voor ouders met namen enzo
