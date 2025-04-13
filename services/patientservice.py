from datetime import datetime
from time import strptime

from flask import make_response

from data.models.doctors import Doctors
from data.models.medicalrecord.gender import Gender
from data.models.medicalrecord.patientinformation import PatientProfile
from data.models.patients import Patients
from data.models.appointments import Appointment
from data.repositories.patientprofilerepository import PatientProfileRepository
from data.repositories.patientsrepository import PatientsRepository
from data.schemas.patientprofileschema import PatientProfileSchema


class PatientService:

    @staticmethod
    def register_as_patient(name : str, email : str, password : str):
        try:
            patient = Patients(patient_name=name, patient_email=email, patient_password=password)
            PatientsRepository.save_patient_to_repo(patient)
        except Exception as e:
            print(e)

    @staticmethod
    def create_patient_profile(patient_id:str, first_name : str, last_name : str, phone_number : str, email : str, address : str, date_of_birth  :str, gender : Gender):
        try:
            dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
            patient_profile = PatientProfile(patient_id=patient_id, first_name=first_name, last_name=last_name, phone_number=phone_number,email=email, address=address, date_of_birth=dob, gender=gender)
            PatientProfileRepository.save_patient_profile_to_repo(patient_profile)
        except Exception as e:
            print(e)
    @staticmethod
    def find_patient_profile(profile_id : str):
        try:
            patient_profile = PatientProfileRepository.find_patient_profile_by_id(profile_id)
            return patient_profile
        except Exception as e:
            print(e)
    @staticmethod
    def update_patient_profile(profile_id):
        try:
            profile = PatientProfileRepository.update_patient_profile(profile_id)
            return profile
        except Exception as e:
            print(e)
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


