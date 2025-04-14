from flask_mongoengine import MongoEngine
db = MongoEngine()
class MedicationInformation(db.Document):
    drug_name = db.StringField(required=True, null=False)
    drug_purpose = db.StringField(required=True, null=False)
    route_of_administration = db.StringField(required=True, null=False)
    dosage = db.StringField(required=True, null=False)
    dosage_frequency = db.StringField(required=True, null=False)
    # start_date = db.DateField(required=True, null=False)
    # end_date = db.DateField(required=True, null=False)
    prescribing_provider = db.StringField(required=True, null=False)
    allergies = db.StringField(required=True, null=False)