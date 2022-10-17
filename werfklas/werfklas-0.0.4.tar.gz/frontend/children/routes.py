from importlib import reload

from flask import render_template, Blueprint, request, flash
from sqlalchemy.orm import Query
from src.modules.common import stringdate, calculate_age, calculate_startyear, find_class, find_teacher, \
    query_class_by_year, find_child, get_appropriate_class, get_family, generate_uuid
from src.classes.base import RearrangeDate
from src.classes.child import AddChild, EditChild
from src.classes.database import Child, Family, sessionSetup
from src.modules.families import provision_edit_family

session = sessionSetup()
rearrange_date = RearrangeDate()

# Blueprint Configuration
children_bp = Blueprint(
    'children_bp', __name__,
    template_folder='templates'
)


@children_bp.route('/index_children')
def index_children():
    # get a list of unique values in the style column
    _children_from_database = Query([
        Child.firstname,
        Child.lastname,
        Child.date_of_registration,
        Child.date_of_birth,
        Child.uuid
    ]).with_session(session).order_by(
        Child.date_of_birth.asc(),
        Child.date_of_registration.asc()
    )
    _children = []
    for _child in _children_from_database:
        _children.append({
            'firstname': _child[0],
            'lastname': _child[1],
            'date_of_registration': rearrange_date.to_list(_child[2])[0],
            'date_of_birth': rearrange_date.to_list(_child[3])[0],
            'uuid': _child[4],
            '_starts_in': calculate_startyear(date_of_birth=_child[3])
        })
    return render_template('index_children.html',
                           Child=_children,
                           _PageTitle=f'Kinder overzicht')


@children_bp.route('/details_child/<uuid>')
def details_child(uuid):
    _child_from_database = find_child(uuid)
    _family = provision_edit_family(_child_from_database['family_uuid'])
    _child = []
    if _child_from_database['class1_uuid'] is None or "None":
        _class_name = None
        _class_teacher = None
    else:
        _class_name = find_class(_child_from_database['class1_uuid'])
        _class_teacher = find_teacher(_class_name[1])
    _child.append({
        'firstname': _child_from_database['firstname'],
        'lastname': _child_from_database['lastname'],
        'date_of_registration': rearrange_date.to_list(_child_from_database['date_of_registration'])[0],
        'date_of_birth': rearrange_date.to_list(_child_from_database['date_of_birth'])[0],
        'uuid': _child_from_database['uuid'],
        'class_name': _class_name,
        'class_teacher': _class_teacher
    })
    _child_age = calculate_age(_child_from_database['date_of_birth'])
    return render_template('details_child.html',
                           Child=_child,
                           ChildAge=_child_age,
                           Parents=_family,
                           _PageTitle='Kind details')


@children_bp.route('/add_child/', methods=['GET', 'POST'])
def add_child():
    _form1 = AddChild()
    _form1.family_uuid.choices = [(_fam['family_uuid'], _fam['parent1'] + ' & ' + _fam['parent2'])
                                  for _fam in get_family()]
    _form1.family_uuid.choices.insert(0, (0, 'Kies een gezin'))
    if _form1.validate_on_submit():
        id_field = request.form['id_field']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        date_of_registration = request.form['date_of_registration']
        date_of_registration = rearrange_date.to_order(date_of_registration)[0]
        family_uuid = request.form['family_uuid']
        date_of_birth = request.form['date_of_birth']
        date_of_birth = rearrange_date.to_order(date_of_birth)[0]
        class1_uuid = 'None'
        class2_uuid = 'None'
        class3_uuid = 'None'
        # the data to be inserted into Sock model - the table, socks
        record = Child(id_field, firstname, lastname, date_of_registration, family_uuid, date_of_birth,
                       class1_uuid, class2_uuid, class3_uuid, generate_uuid())
        # Flask-SQLAlchemy magic adds record to database
        session.add(record)
        session.commit()
        # create a message to send to the template
        _message = f"Het kind {firstname} {lastname} is aangemaakt."
        return render_template('add_child.html',
                               message=_message,
                               _PageTitle='Kind toevoegen')
    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in _form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(_form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_child.html',
                               form1=_form1,
                               _PageTitle='Kind toevoegen')


@children_bp.route('/edit_child/<uuid>')
# TODO
# Klas toewijzen?
def edit_child(uuid):
    _child_from_database = Query([
        Child.firstname,
        Child.lastname,
        Child.date_of_birth,
        Child.date_of_registration,
        Child.uuid,
        Child.family_uuid,
        Child.class1_uuid,
        Child.class2_uuid,
        Child.class3_uuid
    ]).with_session(session).filter(Child.uuid == uuid).first()
    print(f'FamilyID: {_child_from_database.family_uuid}')
    print(f'all: {_child_from_database}')
    # two forms in this template
    _child_to_edit = {'firstname': _child_from_database.firstname,
                      'lastname': _child_from_database.lastname,
                      'date_of_birth': rearrange_date.to_list(_child_from_database.date_of_birth)[0],
                      'date_of_registration': rearrange_date.to_list(_child_from_database.date_of_registration)[0],
                      'uuid': _child_from_database.uuid,
                      'family_uuid': _child_from_database.family_uuid,
                      'class1_uuid': _child_from_database.class1_uuid,
                      'class2_uuid': _child_from_database.class2_uuid,
                      'class3_uuid': _child_from_database.class3_uuid}
    _form1 = EditChild()
    _form1.class1_uuid.choices = get_appropriate_class(uuid, years=4)
    _form1.class2_uuid.choices = get_appropriate_class(uuid, years=4)
    _form1.class3_uuid.choices = get_appropriate_class(uuid=uuid, years=6)
    _form1.family_uuid.choices = [(_fam['family_uuid'], _fam['parent1'] + ' & ' + _fam['parent2'])
                                  for _fam in get_family()]

    return render_template('edit_child.html',
                           childToEdit=_child_to_edit,
                           form1=_form1,
                           _PageTitle=f'Kind wijzigen')


@children_bp.route('/remove_child/<uuid>')
def remove_child(uuid):
    _child_to_remove = Query(Child).with_session(session).filter(Child.uuid == uuid).delete()
    session.commit()
    message = f"De gegevens zijn verwijderd."
    return render_template('remove_child_result.html',
                           message=message,
                           _PageTitle='Kind verwijderen')


@children_bp.route('/edit_child_result', methods=['POST'])
def edit_child_result():
    uuid = request.form['uuid_field']
    _child_parents = Query(Child.family_uuid).filter(Child.uuid == uuid).with_session(session).first()[0]
    _childToEdit = {"uuid": uuid,
                    "firstname": request.form['firstname'],
                    "lastname": request.form['lastname'],
                    "date_of_birth": rearrange_date.to_order(request.form['date_of_birth'])[0],
                    "date_of_registration": rearrange_date.to_order(request.form['date_of_registration'])[0],
                    "family_uuid": request.form['family_uuid'],
                    "class1_uuid": request.form['class1_uuid'],
                    "class2_uuid": request.form['class2_uuid'],
                    "class3_uuid": request.form['class3_uuid'],
                    "updated": stringdate()}

    available_groups = query_class_by_year(
        calculate_startyear(Query(Child.date_of_birth).filter_by(uuid=uuid).with_session(session)[0][0])[3:7])
    # Now forming the list of tuples for SelectField
    _form1 = EditChild()
    _form1.class1_uuid.choices = get_appropriate_class(uuid=uuid, years=4)
    _form1.class2_uuid.choices = get_appropriate_class(uuid=uuid, years=4)
    _form1.class3_uuid.choices = get_appropriate_class(uuid=uuid, years=6)
    _form1.family_uuid.choices = [(_fam['family_uuid'], _fam['parent1'] + ' & ' + _fam['parent2'])
                                  for _fam in get_family()]
    _child_to_edit = Query(Child).with_session(session).filter(Child.uuid == uuid).update(dict(
        firstname=_form1.firstname.data,
        lastname=_form1.lastname.data,
        date_of_registration=_form1.date_of_registration.data,
        date_of_birth=_form1.date_of_birth.data,
        class1_uuid=_form1.class1_uuid.data,
        class2_uuid=_form1.class2_uuid.data,
        class3_uuid=_form1.class3_uuid.data
    ))
    session.commit()
    message = f"De gegevens voor {_childToEdit['firstname']} zijn bijgewerkt."
    return render_template('result.html',
                           message=message,
                           redirect=f'details_child/{uuid}',
                           _PageTitle='Resultaat')
