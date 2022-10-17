from flask import render_template, Blueprint, request, flash
from sqlalchemy.orm import Query

from src.classes.base import RearrangeDate
from src.classes.family import AddFamily, EditFamily
from src.classes.database import Child, Family, sessionSetup, Parent
from src.classes.parent import EditParent, AddParent
from src.modules.common import stringdate, find_children, generate_uuid

session = sessionSetup()
rearrange_date = RearrangeDate()


# Blueprint Configuration
parents_bp = Blueprint(
    'parents_bp', __name__,
    template_folder='templates'
)


@parents_bp.route('/index_parents')
def index_parents():
    # get a list of unique values in the style column
    _parents_from_database = Query([
        Parent.uuid,
        Parent.lastname,
        Parent.firstname,
        Parent.address,
        Parent.zipcode,
        Parent.city,
        Parent.email,
        Parent.phone
    ]).with_session(session).order_by(
        Parent.lastname.asc(),
    )
    _parents = []
    for _parent in _parents_from_database:
        _parents.append({
            'uuid': _parent[0],
            'lastname': _parent[1],
            'firstname': _parent[2],
            'address': _parent[3],
            'zipcode': _parent[4],
            'city': _parent[5],
            'email': _parent[6],
            'phone': _parent[7]
        })
    return render_template('index_parents.html',
                           Parents=_parents,
                           _PageTitle='Ouder Overzicht')


@parents_bp.route('/details_parent/<uuid>')
def details_parent(uuid):
    try:
        _parent_from_database = Query([
            Parent.firstname,
            Parent.lastname,
            Parent.address,
            Parent.zipcode,
            Parent.city,
            Parent.email,
            Parent.phone,
        ]).filter_by(uuid=uuid).with_session(session).first()
        _parent = {
                'uuid': uuid,
                'firstname': _parent_from_database.firstname,
                'lastname': _parent_from_database.lastname,
                'address': _parent_from_database.address,
                'zipcode': _parent_from_database.zipcode,
                'city': _parent_from_database.city,
                'email': _parent_from_database.email,
                'phone': _parent_from_database.phone
            }
        return render_template('details_parent.html',
                               Parent=_parent,
                               _PageTitle='Ouder details')
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@parents_bp.route('/edit_parent/<uuid>')
def edit_parent(uuid):
    _parent_from_database = Query([
        Parent.firstname,
        Parent.lastname,
        Parent.address,
        Parent.zipcode,
        Parent.city,
        Parent.email,
        Parent.phone,
        Parent.uuid,
    ]).filter_by(uuid=uuid).with_session(session).first()
    _parentToEdit = {
            'uuid': _parent_from_database.uuid,
            'firstname': _parent_from_database.firstname,
            'lastname': _parent_from_database.lastname,
            'address': _parent_from_database.address,
            'zipcode': _parent_from_database.zipcode,
            'city': _parent_from_database.city,
            'email': _parent_from_database.email,
            'phone': _parent_from_database.phone
        }
    _form1 = EditParent()
    return render_template('edit_parent.html',
                           parentToEdit=_parentToEdit,
                           form1=_form1,
                           _PageTitle='Ouder wijzigen')


@parents_bp.route('/add_parent', methods=['GET', 'POST'])
def add_parent():
    _form1 = AddParent()
    if _form1.validate_on_submit():
        id_field = request.form['id_field']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address = request.form['address']
        zipcode = request.form['zipcode']
        city = request.form['city']
        email = request.form['email']
        phone = request.form['phone']
        # the data to be inserted into Sock model - the table, socks
        record = Parent(id_field, firstname, lastname, address, zipcode, city, email, phone, generate_uuid())
        # Flask-SQLAlchemy magic adds record to database
        session.add(record)
        session.commit()
        # create a message to send to the template
        _message = f"Ouder {firstname} {lastname} is aangemaakt."
        return render_template('add_parent.html',
                               message=_message,
                               _PageTitle='Ouder toevoegen')
    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in _form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(_form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_parent.html',
                               form1=_form1,
                               _PageTitle='Ouder toevoegen')



@parents_bp.route('/remove_parent/<uuid>')
def remove_parent(uuid):
    _parent_to_delete = Query(Parent).with_session(session).filter(Parent.uuid == uuid).delete()
    session.commit()
    message = f"De gegevens zijn verwijderd."
    return render_template('remove_parent_result.html',
                           message=message,
                           _PageTitle='Ouder verwijderen')


@parents_bp.route('/edit_parent_result', methods=['POST'])
def edit_parent_result():
    uuid = request.form['uuid_field']
    _parentToEdit = {"uuid": uuid,
                    "lastname": request.form['lastname'],
                    "firstname": request.form['firstname'],
                    "address": request.form['address'],
                    "zipcode": request.form['zipcode'],
                    "city": request.form['city'],
                    "email": request.form['email'],
                    "phone": request.form['phone'],
                    "updated": stringdate()}
    _form1 = EditParent()
    _parent_to_edit = Query(Parent).with_session(session).filter(Parent.uuid == uuid).update(dict(
        lastname=_form1.lastname.data,
        firstname=_form1.firstname.data,
        address=_form1.address.data,
        zipcode=_form1.zipcode.data,
        city=_form1.city.data,
        email=_form1.email.data,
        phone=_form1.phone.data))
    session.commit()
    message = f"De gegevens voor {_parentToEdit['lastname']} zijn bijgewerkt."
    return render_template('result.html',
                           message=message,
                           redirect=f'details_parent/{uuid}',
                           _PageTitle='Resultaat')
