from marshmallow import Schema, fields

from data.models.doctors import Doctors
from data.schemas.appointmentschema import AppointmentSchema


class DoctorSchema(Schema):
    class Meta(Schema.Meta):
        model = Doctors
        fields = ('id', 'doctor_name', 'doctor_email', 'doctor_specialty')

        # fields = ('id', 'doctor_name', 'doctor_email', 'doctor_specialty', 'doctor_appointment_details')

    id = fields.String(dump_only=True)
    doctor_name = fields.String(required=True)
    doctor_email = fields.Email(required=True, unique=True)
    doctor_specialty = fields.String(required=True)
    # doctor_appointment_details = fields.List(fields.Nested(AppointmentSchema, required=True))


