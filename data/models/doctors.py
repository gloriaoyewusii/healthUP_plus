from mongoengine import Document, StringField, EmailField, connect

class Doctors(Document):
    doctor_name = StringField(required=True)
    doctor_email = EmailField(required=True, unique=True)
    doctor_password = StringField(required=True)
    doctor_specialty = StringField(required=True)

