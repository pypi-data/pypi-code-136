from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField
from wtforms.validators import InputRequired, Length, Regexp


class AddTeacher(FlaskForm):
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

    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')


class EditTeacher(FlaskForm):
    # id used only by update/edit
    uuid_field = HiddenField()
    lastname = StringField('Achternaam', [InputRequired(),
        Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
        Length(min=2, max=25, message="Invalid sock name length")
        ])
    firstname = StringField('Voornaam', [InputRequired(),
        Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
        Length(min=2, max=25, message="Invalid sock name length")
        ])
    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('opslaan')
