from mongoengine import Document, StringField, DateTimeField


class Appointment(Document):
    day = StringField()
    date = DateTimeField()
    # time = DateTimeField()
