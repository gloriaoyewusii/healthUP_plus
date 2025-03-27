from unittest import TestCase

from services.doctorservice import DoctorService


class TestDoctorServices(TestCase):

    def test_that_doctor_services_of_registration_is_functioning_correctly(self):
        doctor_service = DoctorService()
        doctor_service.register_as_doctor("Jeff Bezos", "jeffb@gmail.com", "passWO1@", "Neurosurgery", "01/12/1959")
        doctor_service.register_as_doctor("Mark Zuck", "mzuck@gmail.com", "passW1O!", "Ophthamology", "12/01/1979")