from marshmallow import (
    Schema,
    fields,
    validate,
)


class MeetingResourceSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer(dump_only=True)
    meeting_name = fields.String(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    updated_at = fields.DateTime()
