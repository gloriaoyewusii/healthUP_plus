from marshmallow import Schema, fields

from data.models.doctors import Doctors


class DoctorSchema(Schema):
    class Meta(Schema.Meta):
        model = Doctors
        fields = ('id', 'doctor_name', 'doctor_email', 'doctor_specialty')

    id = fields.String(dump_only=True)
    doctor_name = fields.String(required=True)
    doctor_email = fields.Email(required=True, unique=True)
    doctor_specialty = fields.String(required=True)


