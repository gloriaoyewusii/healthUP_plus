from unittest import TestCase

from services.patientservice import PatientService


class TestPatientServices(TestCase):

    def test_that_patient_registration_service_is_functioning_correctly(self):
        patient_service = PatientService()
        patient_service.register_as_patient("John Doe", "johndoey@gmail.com", "passWO1@")
    def test_that_patient_can_view_available_appointment_timelines(self):
        patient_service = PatientService()
        print(patient_service.view_available_appointments_of_doctor("Jade Sola"))
    # def test_that_patient_currently_has_no_booked_appointments(self):
    #     patient_service = PatientService()