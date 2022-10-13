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
    family_id = SelectField(u'Ouders', [InputRequired()],
                         coerce=int,
                         choices=[(_fam['family_id'], _fam['parent1']+' & '+_fam['parent2']) for _fam in get_family()])
    date_of_birth = DateField("Geboortedatum", [InputRequired()], format='%d-%m-%Y',
                              render_kw={"placeholder": "dd-mm-jjjj"})

    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('opslaan')


class EditChild(FlaskForm):
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
    date_of_registration = DateField('Datum van inschrijving', [InputRequired()], format='%d-%m-%Y',
                                     render_kw={"placeholder": "dd-mm-jjjj"})
    family_id = SelectField(u'Ouders', [InputRequired()],
                         coerce=int,
                         choices=[(_fam['family_id'], _fam['parent1']+' & '+_fam['parent2']) for _fam in get_family()])
    date_of_birth = DateField("Geboortedatum", [InputRequired()], format='%d-%m-%Y',
                              render_kw={"placeholder": "dd-mm-jjjj"})
    class_id = SelectField(u'Klas', coerce=int,)
                           # choices=[_class.class_name for _class in get_appropriate_class(Child.id)])
    redo_school_year = BooleanField(u'Schooljaar overdoen')
    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('opslaan')
