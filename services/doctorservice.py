import datetime

from data.models.doctors import Doctors
from data.models.appointments import Appointment

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
    def create_appointment_time(name, appointment_day : str, appointment_date : datetime.datetime):
        appointments = []
        try:
            appointment = DoctorsRepository.save_doctors_open_appointment(name, appointment_day, appointment_date)
            appointments.append(appointment)
            print(appointments)
        except Exception as e:
            print(e)
        # try:
        #     # appointment_details = Appointment(day=appointment_day, date=appointment_date)
        #     # Doctors.objects(doctor_name=name).update(doctor_appointment_details=appointment_details)
        #     DoctorsRepository.save_doctors_open_appointment(Doctors.objects(doctor_name=name).update(set_appointment_day=appointment_day))
        #     DoctorsRepository.save_doctors_open_appointment(Doctors.objects(doctor_name=name).update(set_appointment_date=appointment_date))

            # AppointmentRepository.save_appointments_to_repo(Appointment(day=appointment_day, date=appointment_date))
        # except Exception as e:
        #     print(e)

    @staticmethod
    def view_created_appointments(doctor_name):
        doctor = Doctors.objects.get(doctor_name=doctor_name)
        appointments = []
        length = len(doctor.doctor_appointment_details)
        for index in range(length):
            appointments.append(doctor.doctor_appointment_details[index])
        return appointments



    def __str__(self):
        return f"Name: {Doctors.doctor_name}\nEmail: {Doctors.doctor_email}\nPassword: {Doctors.doctor_password}"


