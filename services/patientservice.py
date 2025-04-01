from data.models import PatientProfile
from repositories.patientsrepository import Patients


class PatientService:
    def __init__(self):
        self.patients = Patients()

    def register_as_patient(self, name : str, email : str, password : str, dob : str):
        patient = (
            PatientProfile()
            .set_id()
            .set_patient_name(name)
            .set_patient_email(email)
            .set_patient_password(password)
            .set_patient_dob(dob)
            .build()
        )
        self.patients.save_patient_to_repo(patient)

    def find_patient_by_email(self, param):
        pass

