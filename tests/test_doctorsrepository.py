import datetime
from unittest import TestCase
from data.models.doctors import Doctors
from repositories.doctorsrepository import DoctorsRepository
from services.doctorservice import DoctorService


class TestDoctorRepository(TestCase):
    def test_that_doctor_repository_stores_doctor_information(self):
        doctor = Doctors(doctor_name="John Doe", doctor_email="do_ja091@gmail.com", doctor_password="jDoE@123", doctor_specialty="Optician")
        DoctorsRepository.save_doctor_to_repo(doctor)
        self.assertIsNotNone(doctor)
    def test_that_doctor_john_doe_details_can_be_retrieved_from_repository_by_id(self):
        self.assertEqual("John Doe", DoctorsRepository.find_doctor_by_id("67ebf0885944a0f75f2b689f"))
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
    def test_that_all_doctors_details_can_be_retrieved_from_repo_and_all_registered_patients_can_be_counted(self):
        print(DoctorsRepository.find_all_doctors())
        self.assertEqual(2, DoctorsRepository.count())
        # self.assertEqual(4, len(DoctorsRepository.find_all_doctors()))
    def test_that_doctor_details_can_be_removed_from_repo(self):
        DoctorsRepository.delete_doctor_from_repo(doctor_email="do_ja091@gmail.com")
        self.assertEqual(DoctorsRepository.count(), 1)
    def test_that_doctors_repo_save_appointments_can_create_appointments(self):
        DoctorsRepository.save_doctors_open_appointment("Jade Sola", "Monday", datetime.datetime(2025, 12, 25, 12))
        # DoctorService.create_appointment_time("Jade Sola", "Monday", datetime.datetime(2025, 12, 25, 12))
        # self.assertEqual(DoctorsRepository.find_doctors_open_appointments("Jade Sola"))
