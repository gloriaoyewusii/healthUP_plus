from unittest import TestCase

from data.models.patients import Patients
from data.repositories import PatientsRepository

class TestPatientRepository(TestCase):
    def test_that_patient_repository_stores_patient_information_correctly(self):
        patients = Patients(patient_name="Ja Doe", patient_email="jadoe@gmail.com", patient_password="password")
        PatientsRepository.save_patient_to_repo(patients)
        self.assertEqual(1, PatientsRepository.count())
    def test_that_patient_repository_does_not_store_duplicate_patient_email(self):
        with self.assertRaises(Exception):
            patients = Patients(patient_name="Doe Ja", patient_email="jadoe@gmail.com", patient_password="password")
            PatientsRepository.save_patient_to_repo(patients)

        self.assertEqual(1, PatientsRepository.count())

    def test_that_stored_patient_information_can_be_retrieved(self):
        self.assertEqual("Ja Doe" + "\n" + "jadoe@gmail.com", PatientsRepository.find_patient_by_id("67ebd31ecea985737bf538ff"))

    def test_that_stored_patient_information_can_be_deleted_from_repo(self):
        Patients(patient_name="To Delete", patient_email="todelete@gmail.com", patient_password="password")
        PatientsRepository.delete_patient_from_repo("todelete@gmail.com")
        self.assertEqual(1, PatientsRepository.count())

