# from flask_mongoengine import MongoEngine
#
# from data.models.medicalrecord.patientinformation import PatientProfile
# from data.models.medicalrecord.therapyinformation import TherapyInformation
#
# db = MongoEngine()
# class MedicalRecord(db.Document):
#     patient_profile = db.ReferenceField(PatientProfile, required=True)
#     therapy_record = db.ListField(db.ReferenceField(TherapyInformation, required=True))