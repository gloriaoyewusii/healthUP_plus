from mongoengine import Document, StringField, EmailField, EmbeddedDocumentListField

from data.models.appointments import Appointment


class Patients(Document):
    patient_name = StringField(required=True)
    patient_email = EmailField(required=True, unique=True)
    patient_password = StringField(required=True)
    booked_appointment = EmbeddedDocumentListField(Appointment)


