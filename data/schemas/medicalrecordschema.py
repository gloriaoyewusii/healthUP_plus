# from marshmallow import Schema, fields, validate
#
# from data.models.medicalrecord.medicalrecord import MedicalRecord
#
#
# class MedicalRecordSchema(Schema):
#     class Meta:
#         model = MedicalRecord
#         fields = ('patient_profile_id', 'therapy_record_id')
#     patient_profile_id = fields.String(required=True)
#     therapy_record_id = fields.String(required=True)