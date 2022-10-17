from importlib import reload

from flask_wtf import FlaskForm
from sqlalchemy.orm import Query
from wtforms import SubmitField, SelectField, HiddenField, StringField, DateField, BooleanField
from wtforms.validators import InputRequired, Length, Regexp

from src.classes.base import RearrangeDate
from src.classes.database import Family, sessionSetup, Child
from src.modules.common import find_parents, get_family, get_appropriate_class
from src.modules.families import find_families

session = sessionSetup()
rearrange_date = RearrangeDate()


class AddChild(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    firstname = StringField('Voornaam', [InputRequired(),
                                         Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
                                         Length(min=2, max=25, message="Invalid sock name length")
                                         ])
    lastname = StringField('Achternaam', [InputRequired(),
                                          Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
                                          Length(min=2, max=25, message="Invalid sock name length")
                                          ])
    date_of_registration = DateField('Datum van inschrijving', [InputRequired()],
                                     format='%d-%m-%Y',
                                     render_kw={"placeholder": "dd-mm-jjjj"})
    family_uuid = SelectField(u'Ouders', [InputRequired()], coerce=str)
    date_of_birth = DateField("Geboortedatum", [InputRequired()], format='%d-%m-%Y',
                              render_kw={"placeholder": "dd-mm-jjjj"})

    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('opslaan')


class EditChild(FlaskForm):
    # id used only by update/edit
    uuid_field = HiddenField()
    firstname = StringField('Voornaam', [InputRequired(),
                                         Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
                                         Length(min=2, max=25, message="Invalid sock name length")
                                         ])
    lastname = StringField('Achternaam', [InputRequired(),
                                          Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
                                          Length(min=2, max=25, message="Invalid sock name length")
                                          ])
    date_of_registration = DateField('Datum van inschrijving', [InputRequired()], format='%d-%m-%Y',
                                     render_kw={"placeholder": "dd-mm-jjjj"})
    family_uuid = SelectField(u'Ouders', [InputRequired()], coerce=str)
    date_of_birth = DateField("Geboortedatum", [InputRequired()], format='%d-%m-%Y',
                              render_kw={"placeholder": "dd-mm-jjjj"})
    class1_uuid = SelectField(u'Klas 1', coerce=str, )
    class2_uuid = SelectField(u'Klas 2', coerce=str, )
    class3_uuid = SelectField(u'Klas 3', coerce=str, )
    # choices=[_class.class_name for _class in get_appropriate_class(Child.id)])
    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('opslaan')
