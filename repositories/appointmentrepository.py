from mongoengine import connect

from data.models.appointments import Appointment

connect("healthup_db")
class AppointmentRepository:

    @staticmethod
    def save_appointments_to_repo(appointment):
        appointment.save()

    @staticmethod
    def find_all_appointments():
        all_appointments = []
        appointments = Appointment.objects()
        for appointment in appointments:
            all_appointments.append(appointment.day)
            all_appointments.append(appointment.date)
        return all_appointments

    @staticmethod
    def __dict__():
        return {f"Day: {Appointment.day}\nDate: {Appointment.date}"}

