import datetime

from data.models.doctors import Doctors
from data.models.patients import Patients
from data.models.appointments import Appointment
from repositories.patientsrepository import PatientsRepository
from services.doctorservice import DoctorService


class PatientService:

    @staticmethod
    def register_as_patient(name : str, email : str, password : str):
        try:
            patient = Patients(patient_name=name, patient_email=email, patient_password=password)
            PatientsRepository.save_patient_to_repo(patient)
        except Exception as e:
            print(e)

    @staticmethod
    # def view_available_appointments_of_doctor(doctor_name):
    #     doctor = Doctors.objects.get(doctor_name=doctor_name)
    #     if doctor is not None:
    #         DoctorService.view_weekly_appointments_for(doctor_name)

    @staticmethod
    def book_appointment(patient_name, doctor_name, appointment_day, appointment_date):
        patient = Patients.objects.get(patient_name=patient_name)
        doctor = Doctors.objects.get(doctor_name=doctor_name)
        for index in range(len(doctor.doctor_appointment_details)):
            if doctor.doctor_appointment_details[index].day == appointment_day and doctor.doctor_appointment_details[index].date == appointment_date:
                patient.update(push__booked_appointments=Appointment(day=appointment_day, date=appointment_date))
            # patient.update(push__booked_appointments=None)
                # raise Exception("Appointment not available")


    @staticmethod
    def view_booked_appointment(patient_name):
        appointments = []
        patient = Patients.objects.get(patient_name=patient_name)
        for index in range(len(patient.booked_appointments)):
            appointments.append(patient.booked_appointments[index].day)
            appointments.append(patient.booked_appointments[index].date)
        print(appointments)
        return appointments


