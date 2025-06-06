from flask_mongoengine import MongoEngine
db = MongoEngine()
class TherapyInformation(db.Document):
    therapy_type = db.StringField()
    therapy_reason = db.StringField()
    date = db.DateField()
    start_time = db.StringField()
    end_time = db.StringField()
    number_of_sessions = db.StringField()
    patient_name = db.StringField()
    patient_id = db.StringField()
    therapist_name = db.StringField()
    therapist_id = db.StringField()
    therapy_goal = db.StringField()
    treatment_plan = db.StringField()
    successful_outcome = db.BooleanField()
    therapy_notes = db.StringField()