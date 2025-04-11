from marshmallow import Schema, fields

from data.models.status import Status


class AvailabilityDetailSchema(Schema):

    id = fields.String(dump_only=True)
    date = fields.Date(required=True)
    start_time = fields.String(required=True)
    end_time = fields.String(required=True)
    status = fields.Enum(Status, required=True)
    booked_by = fields.String(required=True)
    doctor_id = fields.String(required=True)