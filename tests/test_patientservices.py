from unittest import TestCase

from services.patientservice import PatientService


class TestPatientServices(TestCase):

    def test_that_patient_services_of_registration_is_functioning_correctly(self):
        patient_service = PatientService()
        patient_service.register_as_patient("John Doe", "johndoey@gmail.com", "passWO1@", "01/12/1990")
        patient_service.register_as_patient("Janey Doey", "johndoey@gmail.com", "passW1O!", "12/01/1990")