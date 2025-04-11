from marshmallow import Schema, fields


from data.models.patients import Patients
from data.schemas.appointmentschema import AppointmentSchema


class PatientSchema(Schema):
    class Meta(Schema.Meta):
        model = Patients
        fields = ('id', 'patient_name', 'patient_email')

    id = fields.String(dump_only=True)
    patient_name = fields.String(required=True)
    patient_email = fields.Email(required=True, unique=True)
    # patient_appointment_details = fields.List(fields.Nested(AppointmentSchema, required=True))


