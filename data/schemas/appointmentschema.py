from marshmallow import Schema, fields

from data.models.appointments import Appointment


class AppointmentSchema(Schema):
    # class Meta(Schema.Meta):
    #     model = Appointment
    #     fields = ('scheduled_by', 'is_appointment_completed', 'reason_for_appointment', 'appointment_duration', 'id', 'appointment_time', 'appointment_date', 'patient_name', 'doctor_id', 'admin_id')

    # day = fields.String(null=False, min_length=6, required=True)

    id = fields.String(dump_only=True)
    scheduled_by = fields.String(required=True)
    is_appointment_completed = fields.Boolean(required=True)
    reason_for_appointment = fields.String(required=True)
    appointment_duration = fields.String(required=True)
    appointment_date = fields.Date(required=True)
    appointment_time = fields.String(required=True)
    patient_name = fields.String(required=True)
    doctor_id = fields.String(required=True)
    # admin_id = fields.String(required=True)


