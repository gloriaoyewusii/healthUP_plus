import datetime


from data.models.appointments import Appointment
from data.models.doctors import Doctors
from data.repositories.doctorsinterface import DoctorsInterface


class DoctorsRepository(DoctorsInterface):

    @staticmethod
    def save_doctor_to_repo(doctor):
        doctor.save()
        return doctor

    @staticmethod
    def count():
        count = Doctors.objects.count({})
        return count

    @staticmethod
    def delete_doctor_from_repo(doctor_email : str):
        return Doctors.objects(doctor_email=doctor_email).delete()

    @staticmethod
    def find_doctor_by_id(doctor_id : str):
        doctor = Doctors.objects.get(id=doctor_id)
        return doctor

    @staticmethod
    def find_doctor_by_email(doctor_email : str):
        doctor = Doctors.objects.get(doctor_email=doctor_email)
        return doctor

    @staticmethod
    def find_all_doctors():
        all_doctors = []
        doctors = Doctors.objects()
        for doctor in doctors:
            all_doctors.append(doctor.doctor_name)
        return all_doctors

    @staticmethod
    def save_doctors_open_appointment(doctor_email, appointment_day:str, appointment_date : datetime):
        doctor = Doctors.objects(doctor_email=doctor_email).update(push__doctor_appointment_details=Appointment(day=appointment_day, date=appointment_date))
        doctor.save()