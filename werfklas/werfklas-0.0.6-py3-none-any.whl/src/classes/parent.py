from flask_wtf import FlaskForm
from sqlalchemy.orm import Query
from wtforms import SubmitField, HiddenField, StringField, BooleanField
from wtforms.validators import InputRequired, Length, Regexp
from flask_sqlalchemy import SQLAlchemy
from src.modules.common import calculate_age
from src.classes.database import Child, sessionSetup, Class

db = SQLAlchemy()
session = sessionSetup()


class AddParent(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    firstname = StringField('Voornaam', [InputRequired(),
                                         Regexp(r'^[A-Za-z\s\-\']+$', message="Ongeldige naam invoer"),
                                         Length(min=2, max=25, message="Invoer ongeldig, lengte te kort")
                                         ])
    lastname = StringField('Achternaam', [InputRequired(),
                                          Regexp(r'^[A-Za-z\s\-\']+$', message="Ongeldige naam invoer"),
                                          Length(min=2, max=25, message="Invoer ongeldig, lengte te kort")
                                          ])
    address = StringField('Adres', [
        Length(min=0, max=25, message="Invoer ongeldig, lengte te kort")
    ])
    zipcode = StringField('Postcode', [
        Length(min=0, max=25, message="Invoer ongeldig, lengte te kort")
    ])
    city = StringField('Woonplaats')
    email = StringField('E-mail')
    phone = StringField('Telefoonnummer')
    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')


class EditParent(FlaskForm):
    # id used only by update/edit
    uuid_field = HiddenField()
    firstname = StringField('Voornaam', [InputRequired(),
                                         Regexp(r'^[A-Za-z\s\-\']+$', message="Ongeldige naam invoer"),
                                         Length(min=2, max=25, message="Invoer ongeldig, lengte te kort")
                                         ])
    lastname = StringField('Achternaam', [InputRequired(),
                                          Regexp(r'^[A-Za-z\s\-\']+$', message="Ongeldige naam invoer"),
                                          Length(min=2, max=25, message="Invoer ongeldig, lengte te kort")
                                          ])
    address = StringField('Adres', [
        Length(min=0, max=25, message="Invoer ongeldig, lengte te kort")
    ])
    zipcode = StringField('Postcode', [
        Length(min=0, max=25, message="Invoer ongeldig, lengte te kort")
    ])
    city = StringField('Woonplaats')
    email = StringField('E-mail')
    phone = StringField('Telefoonnummer')
    updated = HiddenField()
    submit = SubmitField('opslaan')

