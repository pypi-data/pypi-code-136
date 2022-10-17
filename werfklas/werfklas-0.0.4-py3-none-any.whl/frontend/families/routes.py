from flask import render_template, Blueprint, request, flash
from sqlalchemy.orm import Query

from src.classes.base import RearrangeDate
from src.classes.family import AddFamily, EditFamily
from src.classes.database import Child, Family, sessionSetup, Parent
from src.modules.children import find_related_children
from src.modules.common import stringdate, find_parents, generate_uuid, find_active_class
from src.modules.families import find_family, find_families, provision_edit_family, find_all_parents

session = sessionSetup()
rearrange_date = RearrangeDate()

# Blueprint Configuration
families_bp = Blueprint(
    'families_bp', __name__,
    template_folder='templates'
)


@families_bp.route('/index_families')
def index_families():
    _families = find_families(uuid=None)
    return render_template('index_families.html',
                           Families=_families,
                           _PageTitle='Familie Overzicht')


@families_bp.route('/details_family/<uuid>')
def details_family(uuid):
    _family = provision_edit_family(uuid)
    _children = find_related_children(uuid)
    print(_children)

    return render_template('details_family.html',
                           Family=_family,
                           Children=_children,
                           _PageTitle='Gezins details')


@families_bp.route('/edit_family/<uuid>')
def edit_family(uuid):
    _familyToEdit = provision_edit_family(uuid)
    print(_familyToEdit)
    _form1 = EditFamily()
    _form1.parent1_uuid.choices = [(_parent['uuid'], _parent['fullname'])
                                   for _parent in find_all_parents()]
    _form1.parent2_uuid.choices = [(_parent['uuid'], _parent['fullname'])
                                   for _parent in find_all_parents()]
    return render_template('edit_family.html',
                           familyToEdit=_familyToEdit,
                           form1=_form1,
                           _PageTitle='Gezin wijzigen')


@families_bp.route('/add_family', methods=['GET', 'POST'])
def add_family():
    _form1 = AddFamily()
    # _form1.parent1_id.choices = Query([Parent.id, Parent.firstname + ' ' + Parent.lastname]).with_session(session)
    _form1.parent1_uuid.choices = [(_parent['uuid'], _parent['fullname'])
                                   for _parent in find_all_parents()]
    _form1.parent1_uuid.choices.insert(0, (None, 'Kies een ouder'))
    _form1.parent2_uuid.choices = [(_parent['uuid'], _parent['fullname'])
                                   for _parent in find_all_parents()]
    _form1.parent2_uuid.choices.insert(0, ('x-x-x-x', 'Kies een ouder'))
    if _form1.validate_on_submit():
        id_field = request.form['id_field']
        parent1_uuid = request.form['parent1_uuid']
        parent2_uuid = request.form['parent2_uuid']
        divorced = request.form['divorced']

        if request.form['parent2_uuid'] is 'x-x-x-x':
            parent2_uuid = None
        # the data to be inserted into Sock model - the table, socks
        record = Family(id_field, parent1_uuid, parent2_uuid, divorced, generate_uuid())
        # Flask-SQLAlchemy magic adds record to database
        session.add(record)
        session.commit()
        session.close()
        # create a message to send to the template
        _message = f"Gezin {id_field} is aangemaakt."
        return render_template('add_family.html',
                               message=_message,
                               _PageTitle='Gezin toevoegen')
    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in _form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(_form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_family.html',
                               form1=_form1,
                               _PageTitle='Gezin toevoegen')


@families_bp.route('/remove_family/<uuid>')
def remove_family(uuid):
    try:
        _child_to_delete = Query(Child).with_session(session).filter(Child.family_uuid == uuid).delete()
    except:
        pass
    _family_to_delete = Query(Family).with_session(session).filter(Family.uuid == uuid).delete()
    session.commit()
    message = f"De gegevens zijn verwijderd."
    return render_template('remove_family_result.html',
                           message=message,
                           _PageTitle='Gezin verwijderen')


@families_bp.route('/edit_family_result', methods=['POST'])
def edit_family_result():
    uuid = request.form['uuid_field']
    _familyToEdit = provision_edit_family(uuid)
    _form1 = EditFamily()
    _family_to_edit = Query(Family).with_session(session).filter(Family.uuid == uuid).update(dict(
        parent1_uuid=_form1.parent1_uuid.data,
        parent2_uuid=_form1.parent2_uuid.data,
        divorced=_form1.divorced.data))
    session.commit()
    message = f"De gegevens voor {_familyToEdit['parent1']['lastname']} zijn bijgewerkt."
    return render_template('result.html',
                           message=message,
                           redirect=f'details_family/{uuid}',
                           _PageTitle='Resultaat')

