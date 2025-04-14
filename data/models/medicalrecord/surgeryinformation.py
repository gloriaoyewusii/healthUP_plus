from flask_mongoengine import MongoEngine
db = MongoEngine()
class SurgeryRecord(db.Document):
    surgery_name = db.StringField(required=True)
    surgery_date = db.DateField(required=True)
    surgeon_name = db.StringField(required=True)
# add surgeon team name details later
    facility_name = db.StringField(required=True)
    surgery_reason = db.StringField(required=True)
    procedure_description = db.StringField(required=True)
    successful_outcome = db.BooleanField(required=True)
