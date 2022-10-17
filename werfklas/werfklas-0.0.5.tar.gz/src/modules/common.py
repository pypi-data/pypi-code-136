from datetime import date

from sqlalchemy.orm import Query, lazyload

from src.classes.base import RearrangeDate
from src.classes.database import Child, sessionSetup, Teacher, Class, Family, Parent
import uuid

session = sessionSetup()
rearrange_date = RearrangeDate()


def generate_uuid():
    _uuid = uuid.uuid4()
    return str(_uuid)


def find_children(uuid):
    _children_from_database = Query(
        [Child.id, Child.firstname, Child.date_of_birth, Child.family, Child.class_uuid]).filter(
        Child.family == uuid).with_session(session)
    _child = []
    for _c in _children_from_database:
        if _c[4] is None:
            _class_name = 'N/A'
        else:
            _class_name = Query(Class.class_name).filter(Class.id == _c[4]).with_session(session)[0][0]
        _child.append({
            'id': _c[0],
            'firstname': _c[1],
            'date_of_birth': _c[2],
            'child_age': calculate_age(_c[2]),
            'family': _c[3],
            'class': _class_name
        })
    return _child


def calculate_age(geboortedatum):
    from datetime import datetime, date

    _date_str = geboortedatum
    _dto = datetime.strptime(_date_str, '%Y-%m-%d').date()
    _today = date.today()
    calculated_age = _today.year - _dto.year - ((_today.month, _today.day) < (_dto.month, _dto.day))
    # self._leeftijd = age
    return calculated_age


def query_class_by_year(child_start_date):
    print(f'startdatum: {child_start_date}')
    classes_from_db = Query(Class).with_entities(Class.uuid, Class.start_date, Class.class_name, Class.teacher_uuid, Class.end_date).with_session(session).order_by(Class.start_date.asc())
    classes = []
    for c in classes_from_db:
        if c[1][0:4] <= child_start_date <= c[4][0:4]:
            print(f'in {c}')
            _c_teacher = Query(Teacher).with_entities(Teacher.uuid, Teacher.firstname, Teacher.lastname).with_session(session).filter_by(uuid=c[3])[0]
            print(f'cteacher: {_c_teacher}')
            classes.append({
                'class_uuid': c[0],
                'class_name': f"{c[2]} {c[1][0:4]} - {_c_teacher[1]} {_c_teacher[2]}"
            })
    return classes


def calculate_startyear(date_of_birth, years=4):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    datetime_object = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    new_date = datetime_object + relativedelta(years=years)
    return datetime.strftime(new_date, "%m-%Y").replace(' 0', ' ')


def find_class(uuid):
    return Query(Class).with_entities(
        Class.class_name,
        Class.teacher_uuid,
        Class.start_date,
        Class.end_date,
        Class.uuid
    ).filter(Class.uuid == uuid).with_session(session)[0]


def find_parents(uuid):
    if uuid == 'x-x-x-x':
        return None
    return Query(Parent).with_entities(
        Parent.uuid,
        Parent.firstname,
        Parent.lastname,
        Parent.address,
        Parent.zipcode,
        Parent.city,
        Parent.phone,
        Parent.email
    ).filter(Parent.uuid == uuid).with_session(session).first()


def find_teacher(uuid):
    return Query(Teacher).with_entities(
        Teacher.firstname,
        Teacher.lastname,
        Teacher.uuid
    ).filter(Teacher.uuid == uuid).with_session(session)[0]


def find_all_teachers():
    _teachers = Query(Teacher).with_entities(Teacher.firstname, Teacher.lastname, Teacher.uuid).with_session(session)
    _all_teachers = []
    for _teacher in _teachers:
        _all_teachers.append({
            'uuid': _teacher['uuid'],
            'fullname': _teacher['firstname'] + ' ' + _teacher['lastname'],
        })
    return _all_teachers



def find_child(uuid):
    return Query(Child).with_entities(
        Child.firstname,
        Child.lastname,
        Child.date_of_registration,
        Child.date_of_birth,
        Child.uuid,
        Child.family_uuid,
        Child.class1_uuid,
        Child.class2_uuid,
        Child.class3_uuid
    ).filter_by(uuid=uuid).with_session(session).first()


def find_waiting_children():
    _children_from_database = Query(Child).with_entities(
        Child.uuid,
        Child.firstname,
        Child.lastname,
        Child.date_of_birth,
        Child.date_of_registration,
        Child.class1_uuid
    ).filter(Child.class1_uuid == "None").order_by(
        Child.date_of_birth.asc(),
        Child.date_of_registration.asc()
    ).with_session(session).all()

    _w_children = []
    for c in _children_from_database:
        _starts_in_year = calculate_startyear(c[3])
        _w_children.append({
            'uuid': c[0],
            'firstname': c[1],
            'lastname': c[2],
            'date_of_birth': c[3],
            'class1_uuid': c[5],
            '_starts_in': _starts_in_year,
            'date_of_registration': rearrange_date.to_list(c[4])[0]
        })
    return _w_children


def stringdate():
    _today = date.today()
    _date_list = str(_today).split('-')
    # build string in format 01-01-2000
    _date_string = _date_list[1] + "-" + _date_list[2] + "-" + _date_list[0]
    return _date_string


def get_family():
    session.close()
    _families = Query([Family.uuid, Family.parent1_uuid, Family.parent2_uuid]).with_session(session).all()
    _fam_with_parents = []
    for _fam in _families:
        parent1 = find_parents(_fam['parent1_uuid'])
        parent2 = find_parents(_fam['parent2_uuid'])
        print(parent2)
        if parent2 is None:
            _fam_with_parents.append({
                'family_uuid': _fam['uuid'],
                'parent1': parent1['firstname']+' '+parent1['lastname'],
                'parent2': ''
            })
        else:
            _fam_with_parents.append({
                'family_uuid': _fam['uuid'],
                'parent1': parent1['firstname']+' '+parent1['lastname'],
                'parent2': parent2['firstname']+' '+parent2['lastname']
            })
    session.close()
    return _fam_with_parents


def get_appropriate_class(uuid, years):
    available_groups = query_class_by_year(calculate_startyear(Query(Child.date_of_birth).filter_by(uuid=uuid).with_session(session)[0][0], years=years)[3:7])
    groups_list = []
    for i in available_groups:
        groups_list.append((i["class_uuid"], i["class_name"]))
    groups_list.insert(0, (None, 'Kies een klas'))
    print(groups_list)
    return groups_list


def assign_child_to_class():
    pass
#TODO
# vanuit index direct een klas toewijzen, via een popup?


def find_active_class(uuid):
    current_date = date.today()
    class1 = Query(Class).with_entities(Class.uuid, Class.start_date, Class.end_date).filter_by(uuid=uuid)
    print(class1)
    if  class1['start_date'] >= current_date <= class1['end_date']:
        print('Active')
        return True
    else:
        return False