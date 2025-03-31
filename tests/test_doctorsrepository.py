from unittest import TestCase

from models.doctorprofile import DoctorProfile
from repositories.doctors import Doctors

class TestDoctorRepository(TestCase):
    def test_that_doctor_repository_stores_doctor_information(self):
        doctor_builder = DoctorProfile()
        doctors = Doctors()

        doctor_builder.set_doctor_name("Gloria O")
        doctor_builder.set_doctor_dob("01/01/1992")
        doctor_builder.set_doctor_email("glow@gmail.com")
        doctor_builder.set_doctor_password("pass@WO1")
        doctor_builder.set_doctor_specialisation("Neurosurgeon")
        doctor_builder.set_id()
        doctor = doctor_builder.build()
        doctors.save_doctor_to_repo(doctor)


    def test_that_stored_doctor_information_can_be_retrieved(self):
        doctors = Doctors()
        self.assertIsNotNone(doctors.find_doctor_by_id(1))
        self.assertEqual("glow@gmail.com", doctors.find_doctor_by_id(1)["doctor_email"])