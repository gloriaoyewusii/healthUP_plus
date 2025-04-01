from mongoengine import Document, StringField, DateField, EmailField, connect

connect("healthup_db")

class DoctorsProfiles(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    phone_number = StringField(required=True)
    address = StringField(required=True)
    date_of_birth = DateField(required=True)
    specialisation = StringField()