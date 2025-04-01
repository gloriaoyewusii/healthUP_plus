import datetime
from unittest import TestCase

from services.doctorservice import DoctorService


class TestDoctorServices(TestCase):

    def test_that_doctor_can_register_into_healthup(self):
        doctor_service = DoctorService()
        doctor_service.register_as_doctor("Jeff Bezos", "jeffb@gmail.com", "passWO1@", "Neurosurgery")
        doctor_service.register_as_doctor("Mark Zuck", "mzuck@gmail.com", "passW1O!", "Ophthamology")

    def test_that_doctor_can_create_appointment_timelines(self):
        doctor_service = DoctorService()
        doctor_service.create_appointment_time("Wednesday", datetime.datetime(2025, 4, 1, 10, 00))
        doctor_service.create_appointment_time("Wednesday", datetime.datetime(2025, 4, 1, 11, 30))
        doctor_service.create_appointment_time("Friday", datetime.datetime(2025, 4, 3, 12, 00))

    def test_that_doctor_can_view_created_appointment_timelines(self):
        doctor_service = DoctorService()
        doctor_service.create_appointment_time("Wednesday", datetime.datetime(2025, 4, 1, 10, 40))
        doctor_service.create_appointment_time("Friday", datetime.datetime(2025, 4, 3, 12, 35))
        print(doctor_service.view_created_appointments())