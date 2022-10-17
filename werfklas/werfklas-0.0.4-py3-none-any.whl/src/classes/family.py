from flask_wtf import FlaskForm
from sqlalchemy.orm import Query
from wtforms import SubmitField, HiddenField, StringField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, Regexp
from flask_sqlalchemy import SQLAlchemy
from src.modules.common import calculate_age, generate_uuid
from src.classes.database import Child, sessionSetup, Class, Parent

db = SQLAlchemy()
session = sessionSetup()


class AddFamily(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    parent1_uuid = SelectField(u'Ouder1', [InputRequired()], coerce=str)
    parent2_uuid = SelectField(u'Ouder2', coerce=str)
    divorced = SelectField(u'Gescheiden',
                           coerce=int,
                           choices=[(0, 'Nee'), (1, 'Ja')])
    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')


class EditFamily(FlaskForm):
    # id used only by update/edit
    uuid_field = HiddenField()
    parent1_uuid = SelectField(u'Ouders', [InputRequired()],
                             coerce=str)
    parent2_uuid = SelectField(u'Ouders',
                             coerce=str)
    divorced = SelectField(u'Gescheiden',
                           coerce=int,
                           choices=[(0, 'Nee'), (1, 'Ja')])
    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('opslaan')

