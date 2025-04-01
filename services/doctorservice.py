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
    def view_weekly_appointments_for(doctor_name):
        dokie = Doctors.objects.get(doctor_name=doctor_name)
        # print(dokie.doctor_appointment_details[0].date)
        weekly_appointments = []
        for index in range(len(dokie.doctor_appointment_details)):
            weekly_appointments.append(dokie.doctor_appointment_details[index].day)
            weekly_appointments.append(dokie.doctor_appointment_details[index].date)
        print(weekly_appointments)
        return weekly_appointments




    def __str__(self):
        return f"Name: {Doctors.doctor_name}\nEmail: {Doctors.doctor_email}\nPassword: {Doctors.doctor_password}"

    @staticmethod
    def view_daily_appointments_for(doctor_name, appointment_day):
        doctor = Doctors.objects.get(doctor_name=doctor_name, doctor_appointment_details__day=appointment_day)
        day_appointments = []
        for index in range(len(doctor.doctor_appointment_details)):
            if doctor.doctor_appointment_details[index].day == appointment_day:
                day_appointments.append(doctor.doctor_appointment_details[index].date)
        print(day_appointments)
        return day_appointments


