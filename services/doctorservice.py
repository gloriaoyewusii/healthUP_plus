import datetime

from data.models.doctors import Doctors
from data.models.appointments import Appointment
from repositories.appointmentrepository import AppointmentRepository
from repositories.doctorsrepository import DoctorsRepository


class DoctorService:

    @staticmethod
    def register_as_doctor(name : str, email : str, password : str, specialisation : str):

        try:
            doctor = Doctors(doctor_name=name, doctor_email=email, doctor_password=password, doctor_specialty=specialisation)
            DoctorsRepository.save_doctor_to_repo(doctor)
        except Exception as e:
            print(e)

    @staticmethod
    def create_appointment_time(appointment_day : str, appointment_date : datetime.datetime):
        try:
            AppointmentRepository.save_appointments_to_repo(Appointment(day=appointment_day, date=appointment_date))
        except Exception as e:
            print(e)

    @staticmethod
    def view_created_appointments():
        try:
            AppointmentRepository.find_all_appointments()
        except Exception as e:
            print(e)

    def __str__(self):
        return f"Name: {Doctors.doctor_name}\nEmail: {Doctors.doctor_email}\nPassword: {Doctors.doctor_password}"

