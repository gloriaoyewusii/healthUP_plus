from marshmallow import Schema, fields, validate

from data.models.medicalrecord.therapyinformation import TherapyInformation


class TherapyInformationSchema(Schema):
    class Meta:
        model = TherapyInformation
        fields = ('id', 'therapy_type', 'therapy_reason', "date", "start_time", "end_time", "number_of_sessions", "therapist_name", "therapist_id", "therapy_goal", "treatment_plan",
                  "successful_outcome", "therapy_notes")

    id = fields.String(dump_only=True)
    therapy_type = fields.String(required=True)
    therapy_reason = fields.String(required=True, validate=validate.Length(min=5))
    date = fields.Date(required=True, format="%d-%m-%Y")
    start_time = fields.String(required=True, format="%H:%M")
    end_time = fields.String(required=True, format="%H:%M")
    number_of_sessions = fields.String(required=True)
    therapist_name = fields.String(required=True)
    therapist_id = fields.String(required=True, load_only=True)
    therapy_goal = fields.String(required=True)
    treatment_plan = fields.String(required=True)
    successful_outcome = fields.Boolean(required=True)
    therapy_notes = fields.String(required=True)