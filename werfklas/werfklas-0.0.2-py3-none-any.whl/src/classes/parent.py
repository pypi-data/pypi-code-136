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
    updated = HiddenField()
    submit = SubmitField('opslaan')


def find_children(fid):
    _children_from_database = Query(
        [Child.id, Child.firstname, Child.date_of_birth, Child.parents, Child.class_id]).filter(
        Child.parents == fid).with_session(session)
    _child = []
    for _c in _children_from_database:
        if _c[4] is None:
            _class_name = 'N/A'
        else:
            _class_name = Query(Class.class_name).filter(Class.id == _c[4]).with_session(session)[0][0]
        _child.append({
            'id': _c[0],
            'firstname': _c[1],
            'date_of_birth': _c[2],
            'child_age': calculate_age(_c[2]),
            'parents': _c[3],
            'class': _class_name
        })
    return _child
