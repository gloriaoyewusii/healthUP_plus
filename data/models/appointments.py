from flask_mongoengine import MongoEngine



from mongoengine import StringField, DateTimeField, EmbeddedDocument

db = MongoEngine()

class Appointment(EmbeddedDocument):
    day = StringField()
    date = DateTimeField()
