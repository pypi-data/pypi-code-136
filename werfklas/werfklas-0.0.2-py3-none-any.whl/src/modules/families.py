from datetime import date

from sqlalchemy.orm import Query

from src.classes.database import Child, sessionSetup, Teacher, Class, Family, Parent
from src.modules.common import find_parents

session = sessionSetup()


def find_families(fid):
    query_entities = [
        Family.id,
        Family.parent1_id,
        Family.parent2_id,
        Family.divorced,
    ]
    if fid is None:
        _families_from_database = Query(query_entities).with_session(session)
    else:
        return Query(query_entities).filter(Family.id == fid).with_session(session)
    _families = []
    for _family in _families_from_database:
        _families.append({
            'id': _family[0],
            'parent1_id': _family[1],
            'parent1': find_parents(_family[1]),
            'parent2_id': _family[2],
            'parent2': find_parents(_family[2]),
            'divorced': _family[3]
        })
    return _families


def provision_edit_family(fid):
    _family = find_families(fid)[0]
    _parent1 = find_parents(_family[1])
    _parent2 = find_parents(_family[2])
    _family_to_edit = {'id': _family[0],
                       'parent1': {
                           'id': _parent1[0],
                           'firstname': _parent1[1],
                           'lastname': _parent1[2],
                           'address': _parent1[3],
                           'city': _parent1[4],
                           'zipcode': _parent1[5],
                           'phone': _parent1[6],
                           'email': _parent1[7]
                       },
                       'parent2': {
                           'id': _parent2[0],
                           'firstname': _parent2[1],
                           'lastname': _parent2[2],
                           'address': _parent2[3],
                           'city': _parent2[4],
                           'zipcode': _parent2[5],
                           'phone': _parent2[6],
                           'email': _parent2[7]
                       },
                       'divorced': _family[3]
                       }
    return _family_to_edit


def find_family():
    _families_from_database = find_families('')
    # family table
    # parents opzoeken
    # tuple aanmaken voor ouders met namen enzo
