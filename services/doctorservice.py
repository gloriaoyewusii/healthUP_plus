from data.models.doctors import Doctors
from repositories.doctorsrepository import DoctorsRepository


class DoctorService:

    @staticmethod
    def register_as_doctor(name : str, email : str, password : str, specialisation : str):
        doctor = Doctors(name, email, password, specialisation)
        try:
            DoctorsRepository.save_doctor_to_repo(doctor)
        except Exception as e:
            print(e)

    # def create_appointment_timelines(self, date, time):
    #

