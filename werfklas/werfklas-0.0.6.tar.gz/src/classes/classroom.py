from flask_wtf import FlaskForm
from sqlalchemy.orm import Query
from wtforms import SubmitField, SelectField, HiddenField, StringField, DateField
from wtforms.validators import InputRequired, Length, Regexp

from src.classes.database import Teacher, sessionSetup

session = sessionSetup()


class AddClass(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    class_name = StringField('Naam van de Klas', [InputRequired(),
                                                  Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
                                                  Length(min=2, max=25, message="Invalid sock name length")
                                                  ])
    teacher_uuid = SelectField(u'Docent', [InputRequired()], coerce=str)
    start_date = DateField('Datum van starten', [InputRequired()], format='%d-%m-%Y',
                           render_kw={"placeholder": "dd-mm-jjjj"})
    end_date = DateField('Datum van stoppen', [InputRequired()], format='%d-%m-%Y',
                         render_kw={"placeholder": "dd-mm-jjjj"})

    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')


class EditClass(FlaskForm):
    # id used only by update/edit
    uuid_field = HiddenField()
    class_name = StringField('Naam van de Klas', [InputRequired(),
                                                  Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
                                                  Length(min=2, max=25, message="Invalid sock name length")
                                                  ])
    teacher_uuid = SelectField(u'Docent', [InputRequired()], coerce=str)
    start_date = DateField('Datum van starten', [InputRequired()], format='%d-%m-%Y',
                           render_kw={"placeholder": "dd-mm-jjjj"})
    end_date = DateField('Datum van stoppen', [InputRequired()], format='%d-%m-%Y',
                         render_kw={"placeholder": "dd-mm-jjjj"})

    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')
