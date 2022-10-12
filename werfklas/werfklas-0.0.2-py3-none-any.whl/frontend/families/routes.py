from flask import render_template, Blueprint, request, flash
from sqlalchemy.orm import Query

from src.classes.base import RearrangeDate
from src.classes.family import AddFamily, EditFamily
from src.classes.database import Child, Family, sessionSetup
from src.modules.children import find_related_children
from src.modules.common import stringdate, find_parents
from src.modules.families import find_family, find_families, provision_edit_family

session = sessionSetup()
rearrange_date = RearrangeDate()

# Blueprint Configuration
families_bp = Blueprint(
    'families_bp', __name__,
    template_folder='templates'
)


@families_bp.route('/index_families')
def index_families():
    return render_template('index_families.html',
                           Families=find_families(fid=None),
                           _PageTitle='Familie Overzicht')


@families_bp.route('/details_family/<fid>')
def details_family(fid):
    try:
        # _family = find_families(fid=fid)
        _family = provision_edit_family(fid)
        _children = find_related_children(fid)
        return render_template('details_family.html',
                               Family=_family,
                               Children=_children,
                               _PageTitle='Gezins details')
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@families_bp.route('/edit_family/<fid>')
def edit_family(fid):
    _familyToEdit = provision_edit_family(fid)
    return render_template('edit_family.html',
                           familyToEdit=_familyToEdit,
                           form1=EditFamily(),
                           _PageTitle='Gezin wijzigen')


@families_bp.route('/add_family', methods=['GET', 'POST'])
def add_family():
    _form1 = AddFamily()
    if _form1.validate_on_submit():
        id_field = request.form['id_field']
        parent1_id = request.form['parent1_id']
        parent2_id = request.form['parent2_id']
        divorced = request.form['divorced']
        # the data to be inserted into Sock model - the table, socks
        record = Family(id_field, parent1_id, parent2_id, divorced)
        # Flask-SQLAlchemy magic adds record to database
        session.add(record)
        session.commit()
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


@families_bp.route('/remove_family/<fid>')
def remove_family(fid):
    try:
        _child_to_delete = Query(Child).with_session(session).filter(Child.family_id == fid).delete()
    except:
        pass
    _family_to_delete = Query(Family).with_session(session).filter(Family.id == fid).delete()
    session.commit()
    message = f"De gegevens zijn verwijderd."
    return render_template('remove_family_result.html',
                           message=message,
                           _PageTitle='Gezin verwijderen')


@families_bp.route('/edit_family_result', methods=['POST'])
def edit_family_result():
    fid = request.form['id_field']
    _familyToEdit = provision_edit_family(fid)
    _form1 = EditFamily()
    if _form1.validate_on_submit():
        parent1_id = _form1.parent1_id.data
        parent2_id = _form1.parent2_id.data
        divorced = _form1.divorced.data
        _family_to_edit = Query(Family).with_session(session).filter(Family.id == fid).update(dict(
            parent1_id=parent1_id,
            parent2_id=parent2_id,
            divorced=divorced))
        session.commit()
        message = f"De gegevens voor {_familyToEdit['parent1']['lastname']} zijn bijgewerkt."
        return render_template('result.html',
                               message=message,
                               redirect=f'details_family/{fid}',
                               _PageTitle='Resultaat')
    else:
        # show validaton errors
        _familyToEdit["id"] = fid
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in _form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(_form1, field).label.text,
                    error
                ), 'error')
        return render_template('edit_family.html',
                               form1=_form1,
                               familyToEdit=_familyToEdit,
                               redirect=f'details_family/{fid}',
                               choice='edit',
                               _PageTitle='Resultaat')
