from unittest import TestCase

from data.models import PatientProfile
from repositories.patientsrepository import Patients

class TestPatientRepository(TestCase):
    def test_that_patient_repository_stores_patient_information(self):
        patient_builder = PatientProfile()
        patients = Patients()

        patient_builder.set_patient_name("A B")
        patient_builder.set_patient_dob("01/01/1990")
        patient_builder.set_patient_email("a@b.com")
        patient_builder.set_patient_password("pass@WO1")
        patient_builder.set_id()
        patient = patient_builder.build()
        patients.save_patient_to_repo(patient)


    def test_that_stored_patient_information_can_be_retrieved(self):
        patients = Patients()
        self.assertEqual("johndoey@gmail.com", patients.find_patient_by_id(1)["email_address"])