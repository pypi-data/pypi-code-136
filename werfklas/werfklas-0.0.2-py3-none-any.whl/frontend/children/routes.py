from flask import render_template, Blueprint, request, flash
from sqlalchemy.orm import Query

from src.modules.common import stringdate, calculate_age, calculate_startyear, find_class, find_teacher, \
    query_class_by_year, find_child, get_appropriate_class
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
        Child.id
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
            'id': _child[4],
            '_starts_in': calculate_startyear(_child[3])
        })
    return render_template('index_children.html',
                           Child=_children,
                           _PageTitle='Kinder overzicht')


@children_bp.route('/details_child/<kid>')
def details_child(kid):
    _child_from_database = find_child(kid)
    _family = provision_edit_family(_child_from_database['family_id'])
    _child = []
    if _child_from_database['class_id'] is None:
        _class_name = None
        _class_teacher = None
    else:
        _class_name = find_class(_child_from_database['class_id'])
        _class_teacher = find_teacher(_class_name[1])
    _child.append({
        'firstname': _child_from_database['firstname'],
        'lastname': _child_from_database['lastname'],
        'date_of_registration': rearrange_date.to_list(_child_from_database['date_of_registration'])[0],
        'date_of_birth': rearrange_date.to_list(_child_from_database['date_of_birth'])[0],
        'id': _child_from_database['id'],
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
    if _form1.validate_on_submit():
        id_field = request.form['id_field']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        date_of_registration = request.form['date_of_registration']
        date_of_registration = rearrange_date.to_order(date_of_registration)[0]
        family_id = request.form['family_id']
        date_of_birth = request.form['date_of_birth']
        date_of_birth = rearrange_date.to_order(date_of_birth)[0]
        redo_school_year = None
        class_id = None
        # the data to be inserted into Sock model - the table, socks
        record = Child(id_field, firstname, lastname, date_of_registration, family_id, date_of_birth, redo_school_year, class_id)
        # Flask-SQLAlchemy magic adds record to database
        session.add(record)
        session.commit()
        # create a message to send to the template
        _message = f"The data for sock {firstname} {lastname} has been submitted."
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


@children_bp.route('/edit_child/<cid>')
#TODO
# Klas toewijzen?
def edit_child(cid):
    _id = cid
    _child_from_database = Query([
        Child.firstname,
        Child.lastname,
        Child.date_of_birth,
        Child.date_of_registration,
        Child.id,
        Child.family_id,
        Child.class_id
    ]).with_session(session).filter(Child.id == _id).first()
    # two forms in this template
    _child_to_edit = {'firstname': _child_from_database.firstname,
                      'lastname': _child_from_database.lastname,
                      'date_of_birth': rearrange_date.to_list(_child_from_database.date_of_birth)[0],
                      'date_of_registration': rearrange_date.to_list(_child_from_database.date_of_registration)[0],
                      'id': _child_from_database.id,
                      'family_id': _child_from_database.family_id,
                      'class_id': _child_from_database.class_id}
    # available_groups = query_class_by_year(calculate_startyear(Query(Child.date_of_birth).filter_by(id=cid).with_session(session)[0][0])[3:7])
    # #Now forming the list of tuples for SelectField
    # groups_list = []
    # for i in available_groups:
    #     groups_list.append((i["class_id"], i["class_name"]))
    _form1 = EditChild()
    _form1.class_id.choices = get_appropriate_class(cid)
    return render_template('edit_child.html',
                           childToEdit=_child_to_edit,
                           form1=_form1,
                           _PageTitle='Kind wijzigen')


@children_bp.route('/remove_child/<cid>')
def remove_child(cid):
    _child_to_remove = Query(Child).with_session(session).filter(Child.id == cid).delete()
    session.commit()
    message = f"De gegevens zijn verwijderd."
    return render_template('remove_child_result.html',
                           message=message,
                           _PageTitle='Kind verwijderen')


@children_bp.route('/edit_child_result', methods=['POST'])
def edit_child_result():
    cid = request.form['id_field']
    _child_parents = Query(Child.family_id).filter(Child.id == cid).with_session(session).first()[0]
    _childToEdit = {"id": cid,
                    "firstname": request.form['firstname'],
                    "lastname": request.form['lastname'],
                    "date_of_birth": rearrange_date.to_order(request.form['date_of_birth'])[0],
                    "date_of_registration": rearrange_date.to_order(request.form['date_of_registration'])[0],
                    "family_id": _child_parents,
                    "class_id": request.form['class_id'],
                    "updated": stringdate()}

    available_groups = query_class_by_year(calculate_startyear(Query(Child.date_of_birth).filter_by(id=cid).with_session(session)[0][0])[3:7])
    #Now forming the list of tuples for SelectField
    groups_list = []
    for i in available_groups:
        groups_list.append((i["class_id"], i["class_name"]))
    _form1 = EditChild()
    _form1.class_id.choices = groups_list
    if _form1.validate_on_submit():
        firstname = _form1.firstname.data
        lastname = _form1.lastname.data
        date_of_birth = _form1.date_of_birth.data
        date_of_registration = _form1.date_of_registration.data
        class_id = _form1.class_id.data
        _child_to_edit = Query(Child).with_session(session).filter(Child.id == cid).update(dict(
            firstname=firstname,
            lastname=lastname,
            date_of_registration=date_of_registration,
            date_of_birth=date_of_birth,
            class_id=class_id))
        session.commit()
        message = f"De gegevens voor {_childToEdit['firstname']} zijn bijgewerkt."
        return render_template('result.html',
                               message=message,
                               redirect=f'details_child/{cid}',
                               _PageTitle='Resultaat')
    else:
        # show validaton errors
        _childToEdit["id"] = cid
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in _form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(_form1, field).label.text,
                    error
                ), 'error')
        return render_template('edit_child.html',
                               form1=_form1,
                               childToEdit=_childToEdit,
                               choice='edit',
                               redirect=f'details_child/{cid}',
                               _PageTitle='Resultaat')

