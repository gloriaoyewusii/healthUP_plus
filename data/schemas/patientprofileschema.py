from marshmallow import Schema, fields

from data.models.medicalrecord.gender import Gender


class PatientProfileSchema(Schema):
    id = fields.String(dump_only=True)
    patient_id = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.Email(required=True, unique=True)
    phone_number = fields.String(required=True)
    email = fields.Email(required=True)
    address = fields.String(required=True)
    date_of_birth = fields.Date(required=True)
    gender = fields.Enum(Gender, required=True)