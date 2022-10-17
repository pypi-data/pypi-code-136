from flask import Blueprint, request, flash
from flask import render_template
from sqlalchemy.orm import Query

from src.modules.common import calculate_age, find_teacher, stringdate, generate_uuid, find_all_teachers
from src.classes.base import RearrangeDate
from src.classes.classroom import AddClass, EditClass
from src.classes.database import Class, Child, sessionSetup, Teacher

session = sessionSetup()
rearrange_date = RearrangeDate()

# Blueprint Configuration
classroom_bp = Blueprint(
    'classroom_bp', __name__,
    template_folder='templates'
)


@classroom_bp.route('/index_classes')
def index_classrooms():
    # get a list of unique values in the style column
    _classes_from_database = Query([
        Class.id,
        Class.class_name,
        Class.teacher_uuid,
        Class.start_date,
        Class.end_date,
        Class.uuid
    ]).with_session(session)
    _classes = []
    for _class in _classes_from_database:
        _classes.append({
            'id': _class[0],
            'class_name': _class[1] + ' ' + _class[3][0:4],
            'teacher': find_teacher(_class[2]),
            'start_date': _class[3],
            'end_date': _class[4],
            'uuid': _class[5]
        })
    return render_template('index_classrooms.html',
                           Classes=_classes,
                           _PageTitle='Klassen Overzicht')


@classroom_bp.route('/add_class', methods=['GET', 'POST'])
def add_classroom():
    _form1 = AddClass()
    _form1.teacher_uuid.choices = [(_teacher['uuid'], _teacher['fullname'])
                                   for _teacher in find_all_teachers()]
    _form1.teacher_uuid.choices.insert(0, (None, 'Kies een docent'))
    if _form1.validate_on_submit():
        id_field = request.form['id_field']
        class_name = request.form['class_name']
        teacher_uuid = request.form['teacher_uuid']
        start_date = request.form['start_date']
        start_date = rearrange_date.to_order(start_date)[0]  # Rearrange date for correct filing
        end_date = request.form['end_date']
        end_date = rearrange_date.to_order(end_date)[0]  # Rearrange date for correct filing
        record = Class(id_field, class_name, teacher_uuid, start_date, end_date, generate_uuid())
        # Flask-SQLAlchemy magic adds record to database
        session.add(record)
        session.commit()
        # create a message to send to the template
        _message = f"Klas '{class_name}' is aangemaakt."
        return render_template('add_classroom.html',
                               message=_message,
                               _PageTitle='Klas toevoegen')
    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in _form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(_form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_classroom.html',
                               form1=_form1,
                               _PageTitle='Klas toevoegen')


@classroom_bp.route('/details_class/<uuid>')
# TODO, kolom aanmaken voor wanneer kind de klas verlaat. ergens bij pasen?

def details_classroom(uuid):
    try:
        _class_from_database = Query([
            Class.class_name,
            Class.teacher_uuid,
            Class.uuid,
            Class.start_date,
            Class.end_date
        ]).with_session(session).filter(Class.uuid == uuid).all()
        _class = []
        for _class_from_database in _class_from_database:
            _class.append({
                'class_name': _class_from_database.class_name,
                'teacher_uuid': _class_from_database.teacher_uuid,
                'start_date': _class_from_database.start_date,
                'end_date': _class_from_database.end_date,
                'uuid': _class_from_database.uuid
            })
        _teacher_for_class = Query([
            Teacher.firstname,
            Teacher.lastname
        ]).with_session(session).filter(Teacher.uuid == _class_from_database.teacher_uuid).all()
        _children_in_class = Query([
            Child.firstname,
            Child.lastname,
            Child.date_of_birth,
            Child.uuid
        ]).with_session(session).filter(Child.class1_uuid == _class_from_database.uuid).all()
        _children = []
        for _c in _children_in_class:
            _children.append({
                "firstname": _c[0],
                "lastname": _c[1],
                "age": calculate_age(_c[2]),
                "id": _c[3]
            })
        return render_template('details_classroom.html',
                               Class=_class,
                               Teacher=_teacher_for_class,
                               Children=_children,
                               _PageTitle='Klas details')
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@classroom_bp.route('/edit_class/<uuid>')
def edit_classroom(uuid):
    _class_from_database = Query([
        Class.class_name,
        Class.teacher_uuid,
        Class.start_date,
        Class.end_date,
        Class.uuid
    ]).with_session(session).filter(Class.uuid == uuid).first()
    # two forms in this template
    _classToEdit = {
        'uuid': _class_from_database.uuid,
        'class_name': _class_from_database.class_name,
        'teacher_uuid': _class_from_database.teacher_uuid,
        'start_date': rearrange_date.to_list(_class_from_database.start_date)[0],
        'end_date': rearrange_date.to_list(_class_from_database.end_date)[0]}
    _form1 = EditClass()
    _form1.teacher_uuid.choices = Query([
        Teacher.uuid,
        Teacher.firstname + ' ' + Teacher.lastname]).with_session(session)
    return render_template('edit_classroom.html',
                           classToEdit=_classToEdit,
                           form1=_form1,
                           _PageTitle='Klas wijzigen')


@classroom_bp.route('/remove_class/<uuid>')
def remove_classroom(uuid):
    _class_to_remove = Query(Class).with_session(session).filter(Class.uuid == uuid).delete()
    session.commit()
    message = f"De gegevens zijn verwijderd."
    return render_template('remove_class_result.html',
                           message=message,
                           _PageTitle='Klas verwijderen')


@classroom_bp.route('/edit_class_result', methods=['POST'])
def edit_classroom_result():
    uuid = request.form['uuid_field']
    _classToEdit = {"uuid": uuid,
                      "class_name": request.form['class_name'],
                      "teacher_uuid": request.form['teacher_uuid'],
                      "start_date": rearrange_date.to_order(request.form['start_date'])[0],
                      "end_date": rearrange_date.to_order(request.form['end_date'])[0],
                      "updated": stringdate()}
    _form1 = EditClass()
    class_name = _form1.class_name.data
    teacher_uuid = _form1.teacher_uuid.data
    start_date = _form1.start_date.data
    end_date = _form1.end_date.data
    _class_to_edit = Query(Class).with_session(session).filter(Class.uuid == uuid).update(dict(
        class_name=class_name,
        teacher_uuid=teacher_uuid,
        start_date=start_date,
        end_date=end_date))
    session.commit()
    message = f"De gegevens voor {_classToEdit['class_name']} zijn bijgewerkt."
    return render_template('result.html',
                           message=message,
                           redirect=f'details_class/{uuid}',
                           _PageTitle='Resultaat')

