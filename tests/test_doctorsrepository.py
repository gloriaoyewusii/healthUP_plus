from unittest import TestCase
from data.models.doctors import Doctors
from repositories.doctorsrepository import DoctorsRepository

class TestDoctorRepository(TestCase):
    def test_that_doctor_repository_stores_doctor_information(self):
        doctor = Doctors(doctor_name="John Doe", doctor_email="do_ja091@gmail.com", doctor_password="jDoE@123", doctor_specialty="Optician")
        DoctorsRepository.save_doctor_to_repo(doctor)
        self.assertIsNotNone(doctor)
    def test_that_doctor_john_doe_details_can_be_retrieved_from_repository_by_id(self):
        self.assertEqual("John Doe", DoctorsRepository.find_doctor_by_id("67eb7d1645acd7d8bbe20156"))
    def test_that_multiple_doctors_with_same_email_cannot_be_added_to_repository(self):
        doctor_jade = Doctors(doctor_name="Jade Sola", doctor_email="jade@gmail.com", doctor_password="password", doctor_specialty="Doctor")
        DoctorsRepository.save_doctor_to_repo(doctor_jade)
        self.assertIsNotNone(doctor_jade)
        with self.assertRaises(Exception):
            doctor_phil = Doctors(doctor_name="Phil Jones", doctor_email="jade@gmail.com", doctor_password="passNword", doctor_specialty="Biomedical Doctor")
            DoctorsRepository.save_doctor_to_repo(doctor_phil)
            self.assertIsNone(doctor_phil)
    def test_that_doctor_jade_details_can_be_retrieved_from_repo_by_email(self):
        self.assertEqual("Jade Sola", DoctorsRepository.find_doctor_by_email("jade@gmail.com"))