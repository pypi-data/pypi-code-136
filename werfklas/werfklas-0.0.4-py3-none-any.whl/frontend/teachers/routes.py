from flask import Blueprint, request, flash
from flask import render_template
from sqlalchemy.orm import Query

from src.modules.common import find_teacher, generate_uuid
from src.classes.teacher import AddTeacher, EditTeacher
from src.classes.database import sessionSetup, Teacher

session = sessionSetup()

# Blueprint Configuration
teachers_bp = Blueprint(
    'teachers_bp', __name__,
    template_folder='templates'
)


@teachers_bp.route('/index_teacher')
def index_teachers():
    # get a list of unique values in the style column
    _teachers_from_database = Query([
        Teacher.uuid,
        Teacher.firstname,
        Teacher.lastname,
    ]).with_session(session)
    _teachers = []
    for _teacher in _teachers_from_database:
        _teachers.append({
            'uuid': _teacher[0],
            'firstname': _teacher[1],
            'lastname': _teacher[2],
        })
    return render_template('index_teachers.html',
                           Teachers=_teachers,
                           _PageTitle='Docenten Overzicht')


@teachers_bp.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    _form1 = AddTeacher()
    if _form1.validate_on_submit():
        id_field = request.form['id_field']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        # the data to be inserted into Sock model - the table, socks
        record = Teacher(id_field, firstname, lastname, generate_uuid())
        # Flask-SQLAlchemy magic adds record to database
        session.add(record)
        session.commit()
        # create a message to send to the template
        _message = f"Leraar '{firstname} {lastname}' is aangemaakt."
        return render_template('add_teacher.html',
                               message=_message,
                               _PageTitle='Docent toevoegen')
    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in _form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(_form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_teacher.html',
                               form1=_form1,
                               _PageTitle='Docent toevoegen')


@teachers_bp.route('/details_teacher/<uuid>')
def details_teacher(uuid):
    try:
        _teacher_from_database = Query([
            Teacher.firstname,
            Teacher.lastname,
            Teacher.uuid,
        ]).with_session(session).filter(Teacher.uuid == uuid).all()
        _teacher = []
        for _teacher_from_database in _teacher_from_database:
            _teacher.append({
                'firstname': _teacher_from_database.firstname,
                'lastname': _teacher_from_database.lastname,
                'uuid': _teacher_from_database.uuid
            })
        return render_template('details_teacher.html',
                               Teacher=_teacher,
                               _PageTitle='Docent details')
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@teachers_bp.route('/edit_teacher/<uuid>')
def edit_teacher(uuid):
    _teacherToEdit = find_teacher(uuid)
    _form1 = EditTeacher()
    return render_template('edit_teacher.html',
                           teacherToEdit=_teacherToEdit,
                           form1=_form1,
                           _PageTitle='Docent wijzigen')


@teachers_bp.route('/edit_teacher_result', methods=['POST'])
def edit_teacher_result():
    uuid = request.form['uuid_field']
    _teacher_from_database = find_teacher(uuid)
    _teacherToEdit = {'uuid': uuid,
                      'firstname': _teacher_from_database.firstname,
                      'lastname': _teacher_from_database.lastname}
    _form1 = EditTeacher()
    _teacher_to_edit = Query(Teacher).with_session(session).filter(Teacher.uuid == uuid).update(dict(
        firstname=_form1.firstname.data,
        lastname=_form1.lastname.data))
    session.commit()
    message = f"De gegevens voor {_teacherToEdit['firstname']} zijn bijgewerkt."
    return render_template('result1.html',
                           message=message,
                           redirect=f'details_teacher/{uuid}',
                           _PageTitle='Resultaat')


@teachers_bp.route('/remove_teacher/<uuid>')
def remove_teacher(uuid):
    _teacher_to_remove = Query(Teacher).with_session(session).filter(Teacher.id == uuid).delete()
    session.commit()
    message = f"De gegevens zijn verwijderd."
    return render_template('remove_teacher_result.html',
                           message=message,
                           _PageTitle='Docent verwijderen')
