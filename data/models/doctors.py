from flask_mongoengine import MongoEngine
from mongoengine import StringField, EmailField, EmbeddedDocumentField, ListField, DictField
from data.models.appointments import Appointment
import bcrypt

db = MongoEngine()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

class Doctors(db.Document):
    doctor_name = db.StringField(required=True)
    doctor_email = db.EmailField(required=True, unique=True)
    doctor_password = db.StringField(required=True)
    doctor_specialty = db.StringField(required=True)
    doctor_appointment_details = ListField(EmbeddedDocumentField(Appointment))



