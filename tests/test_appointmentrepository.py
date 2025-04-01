import datetime
from unittest import TestCase
from data.models.appointments import Appointment
from repositories.appointmentrepository import AppointmentRepository


class TestAppointmentRepository(TestCase):
    def test_that_appointment_details_can_be_accurately_stored(self):
        appointment = Appointment(day="Tuesday", date=datetime.datetime(2025, 4, 1, 9, 30))
        self.assertEqual(appointment.day, "Tuesday")
        appointment2 = Appointment(day="Tuesday", date=datetime.datetime(2025, 4, 1, 11, 30))
        self.assertIsNotNone(appointment.date)
        AppointmentRepository.save_appointments_to_repo(appointment)
        AppointmentRepository.save_appointments_to_repo(appointment2)
    def test_that_all_appointments_can_be_retrieved(self):
        print(AppointmentRepository.find_all_appointments())