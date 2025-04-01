from mongoengine import connect

from data.models.appointments import Appointment

connect("healthup_db")
class AppointmentRepository:

    @staticmethod
    def save_appointments_to_repo(appointment):
        appointment.save()
