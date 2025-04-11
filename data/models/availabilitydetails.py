from flask_mongoengine import MongoEngine
from mongoengine import EnumField

from data.models.status import Status

db = MongoEngine()
class AvailabilityDetails(db.Document):
    date = db.DateField(required=True, null=False)
    start_time = db.StringField(required=True, null=False)
    end_time = db.StringField(required=True, null=False)
    status = EnumField(Status, default=Status.AVAILABLE)
    # booked_by = db.StringField(required=True, null=False)
    doctor_id = db.StringField(required=True, null=False)
    # doctor_name = db.StringField(required=True, null=False)
