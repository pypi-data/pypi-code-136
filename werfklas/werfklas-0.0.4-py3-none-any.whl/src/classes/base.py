from datetime import date, datetime

from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField


class DeleteForm(FlaskForm):
    id_field = HiddenField()
    purpose = HiddenField()
    submit = SubmitField('Delete This Sock')


class RearrangeDate:
    def to_order(self, date_entry):
        return [datetime.strptime(date_entry, '%d-%m-%Y').strftime('%Y-%m-%d') for d in date_entry]

    def to_list(self, date_entry):
        return [datetime.strptime(date_entry, '%Y-%m-%d').strftime('%d-%m-%Y') for d in date_entry]

