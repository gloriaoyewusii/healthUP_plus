from mongoengine import connect

from data.models.doctors import Doctors

connect("healthup_db")
class DoctorsRepository:

    @staticmethod
    def save_doctor_to_repo(doctor):
        doctor.save()

    @staticmethod
    def count():
        count = Doctors.objects.count_documents({})
        return count

    @staticmethod
    def delete_doctor_from_repo(doctor : Doctors):
        return doctor.delete()

    @staticmethod
    def find_doctor_by_id(doctor_id : str):
        doctor = Doctors.objects.get(id=doctor_id)
        return doctor.doctor_name

    @staticmethod
    def find_doctor_by_email(doctor_email : str):
        doctor = Doctors.objects.get(doctor_email=doctor_email)
        return doctor.doctor_name

    @staticmethod
    def find_all_doctors():
        doctors = Doctors.objects.all()
        return doctors
