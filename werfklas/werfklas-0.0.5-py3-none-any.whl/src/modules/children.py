from datetime import date

from sqlalchemy.orm import Query

from src.classes.child import rearrange_date
from src.classes.database import Child, sessionSetup, Teacher, Class, Family, Parent
from src.modules.classrooms import get_classroom
from src.modules.common import find_parents, calculate_age, find_class

session = sessionSetup()


def find_related_children(uuid):
    query_entities = [
        Child.uuid,
        Child.family_uuid,
        Child.firstname,
        Child.lastname,
        Child.date_of_birth,
        Child.class1_uuid,
        Child.class2_uuid,
        Child.class3_uuid
    ]
    _queried_child = Query(query_entities).filter(Child.family_uuid == uuid).with_session(session)
    children = []
    for c in _queried_child:
        children.append({
            'uuid': c['uuid'],
            'family_uuid': c['family_uuid'],
            'firstname': c['firstname'],
            'lastname': c['lastname'],
            'age': calculate_age(c['date_of_birth']),
            'classroom1': get_classroom(c['class1_uuid']),
            'classroom2': get_classroom(c['class2_uuid']),
            'classroom3': get_classroom(c['class3_uuid'])
        })
    return children
