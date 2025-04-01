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
    def view_available_appointments_of_doctor(doctor_name):
        doctor = Doctors.objects.get(doctor_name=doctor_name)
        if doctor is not None:
            DoctorService.view_weekly_appointments_for(doctor_name)