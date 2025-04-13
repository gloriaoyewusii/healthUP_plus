from data.models.appointments import Appointment

class AppointmentRepository:

    @staticmethod
    def save_appointment_to_db(appointment: Appointment):
        appointment.save()
        return appointment
    @staticmethod
    def get_appointment_by_id(appointment_id):
        return Appointment.objects.get(id=appointment_id)