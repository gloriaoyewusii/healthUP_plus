from marshmallow import Schema, fields

from data.models.appointments import Appointment


class AppointmentSchema(Schema):
    class Meta(Schema.Meta):
        model = Appointment
        fields = ('day', 'date')

    day = fields.String(required=True)
    date = fields.DateTime(required=True)


