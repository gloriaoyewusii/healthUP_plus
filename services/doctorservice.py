from models.doctorbuilder import DoctorBuilder
from repositories.doctors import Doctors


class DoctorService:
    def __init__(self):
        self.doctors = Doctors()

    def register_as_doctor(self, name : str, email : str, password : str, specialisation : str, dob : str):
        doctor = (
            DoctorBuilder()
            .set_id()
            .set_doctor_name(name)
            .set_doctor_email(email)
            .set_doctor_password(password)
            .set_doctor_specialisation(specialisation)
            .set_doctor_dob(dob)
            .build()
        )
        self.doctors.save_doctor_to_repo(doctor)

    def find_doctor_by_email(self, param):
        pass

