import re
from models.patient import Patient
class PatientBuilder:
    def __init__(self):
        self.patient_model = Patient()
        self.count = 0


    def set_id(self):
        self.patient_model.id_number = self.count + 1
        self.count += 1
        return self

    def set_patient_name(self, patient_name:str):
        name_pattern = r'^[A-Za-z]+\s[A-Za-z]+$'
        if not re.match(name_pattern, patient_name):
            raise ValueError('Invalid Patient Name')
        self.patient_model.patient_name = patient_name
        return self

    def set_patient_email(self, patient_email:str):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(email_pattern, patient_email):
            raise Exception('Invalid email')
        # if self.patients_collection.find({"email": patient_email}):
        #     raise Exception('Email already exists')
        self.patient_model.email_address = patient_email
        return self

    def set_patient_password(self, patient_password:str):
        password_pattern = r'^[a-zA-Z0-9]+$'
        if len(patient_password) < 8 and not re.match(password_pattern, patient_password):
            raise ValueError('Invalid password')
        self.patient_model.password = patient_password
        return self

    def set_patient_dob(self, dob : str):
        self.patient_model.dob = dob
        return self

    def get_patient_name(self):
        return self.patient_model.patient_name

    def get_patient_email(self):
        return self.patient_model.email_address

    def get_patient_password(self):
        return self.patient_model.password

    def get_patient_id(self):
        return self.patient_model.id_number
    def build(self):
        return self.patient_model