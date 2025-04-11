from flask_mongoengine import MongoEngine



from mongoengine import StringField, DateTimeField, EmbeddedDocument

db = MongoEngine()

class Appointment(db.Document):
    # day = db.StringField(null=False, min_length=6, required=True)
    appointment_date = db.DateField()
    appointment_time = db.StringField()
    patient_name = db.StringField()
    is_appointment_completed = db.BooleanField()
    reason_for_appointment = db.StringField()
    appointment_duration = db.StringField()
    scheduled_by = db.StringField()
    doctor_id = db.StringField()
    admin_id = db.StringField()

    # def __str__(self):
    #     return str(self.date)
