from mongoengine import StringField, DateTimeField, EmbeddedDocument


class Appointment(EmbeddedDocument):
    day = StringField()
    date = DateTimeField()
