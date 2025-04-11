from mongoengine import Document, StringField, EmailField, EmbeddedDocumentListField
from flask_mongoengine import MongoEngine
db = MongoEngine()
from data.models.appointments import Appointment


class Patients(db.Document):
    patient_name = db.StringField(required=True, null=False)
    patient_email = db.EmailField(required=True, unique=True, null=False)
    patient_password = db.StringField(required=True, null=False)
    # booked_appointments = EmbeddedDocumentListField(Appointment)


