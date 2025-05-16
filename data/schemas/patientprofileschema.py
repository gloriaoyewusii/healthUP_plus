from marshmallow import Schema, fields, validate

from data.models.medicalrecord.gender import Gender
from data.models.medicalrecord.patientinformation import PatientProfile


class PatientProfileSchema(Schema):
    class Meta:
        model = PatientProfile
        fields = ('id', 'patient_id', 'first_name', 'last_name', 'phone_number', 'email', 'address', 'date_of_birth', 'gender')
    id = fields.String(dump_only=True)
    patient_id = fields.String(required=True, load_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    phone_number = fields.String(required=True, validate=validate.Length(11))
    email = fields.Email(required=True, unique=True)
    address = fields.String(required=True)
    date_of_birth = fields.Date(required=True, format="%d-%m-%Y")
    gender = fields.Enum(Gender, required=True)