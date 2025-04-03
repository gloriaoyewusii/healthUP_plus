import datetime
from unittest import TestCase

from services.patientservice import PatientService


class TestPatientServices(TestCase):

    def test_that_patient_registration_service_is_functioning_correctly(self):
        patient_service = PatientService()
        patient_service.register_as_patient("John Doe", "johndoey@gmail.com", "passWO1@")
    def test_that_patient_can_view_available_appointment_timelines(self):
        patient_service = PatientService()
        print(patient_service.view_available_appointments_of_doctor("Jade Sola"))
    def test_that_patient_currently_can_book_appointment(self):
        patient_service = PatientService()
        patient_service.book_appointment("John Doe", "Jade Sola", "Wednesday", datetime.datetime(2025, 4, 1, 10, 40))
    def test_that_patient_can_view_booked_appointment(self):
        patient_service = PatientService()
        patient_service.book_appointment("John Doe", "Jade Sola", "Friday", datetime.datetime(2025, 4, 3, 12, 35))
        patient_service.view_booked_appointment("John Doe")

