from flask_mongoengine import MongoEngine
from mongoengine import EmbeddedDocumentField, ListField

from data.models.availabilitydetails import AvailabilityDetails

db = MongoEngine()



class Doctors(db.Document):
    doctor_name = db.StringField(required=True, null=False)
    doctor_email = db.EmailField(null=False, required=True, unique=True)
    doctor_password = db.StringField(null=False, required=True)
    doctor_specialty = db.StringField(required=True)
    # doctor_time_slots = db.DictField(required=True)
    # doctor_appointment_details = ListField(EmbeddedDocumentField(Appointment))
    # doctor_availability_details = ListField(EmbeddedDocumentField(AvailabilityDetails))


