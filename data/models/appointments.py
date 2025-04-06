from flask_mongoengine import MongoEngine



from mongoengine import StringField, DateTimeField, EmbeddedDocument

db = MongoEngine()

class Appointment(db.EmbeddedDocument):
    day = db.StringField()
    date = db.DateTimeField()
