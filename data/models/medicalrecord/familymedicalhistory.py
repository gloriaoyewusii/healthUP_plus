from flask_mongoengine import MongoEngine
db = MongoEngine()
class FamilyMedicalHistory(db.Document):
    relation = db.StringField(required=True)
    age = db.StringField(required=True)
    health_condition = db.StringField(required=True)
    alive = db.BooleanField(required=True)
    notes = db.StringField(required=True)