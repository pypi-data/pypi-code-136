from datetime import date

from sqlalchemy.orm import Query

from src.classes.child import rearrange_date
from src.classes.database import Child, sessionSetup, Teacher, Class, Family, Parent
from src.modules.classrooms import get_classroom
from src.modules.common import find_parents, calculate_age, find_class

session = sessionSetup()


def find_related_children(fid):
    query_entities = [
        Child.id,
        Child.family_id,
        Child.firstname,
        Child.lastname,
        Child.date_of_birth,
        Child.class_id
    ]
    _queried_child = Query(query_entities).filter(Child.family_id == fid).with_session(session)
    _classes = Query(Class).with_entities(Class.id, Class.class_name, Class.start_date).with_session(session)
    children = []
    for c in _queried_child:
        children.append({
            'id': c['id'],
            'family_id': c['family_id'],
            'firstname': c['firstname'],
            'lastname': c['lastname'],
            'age': calculate_age(c['date_of_birth']),
            'classroom': get_classroom(c['class_id'])
        })
    # calculate age
    # find class
    return children
