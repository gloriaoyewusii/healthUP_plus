# import re
# from models.doctor import Doctor
from mongoengine import Document, StringField, DateField, EmailField


class DoctorProfile(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    phone_number = StringField(required=True)
    address = StringField(required=True)
    date_of_birth = DateField(required=True)
    specialisation = StringField(required=True)


    # def set_id(self):
    #     self.doctor_model.doctor_id = self.count + 1
    #     self.count += 1
    #     return self
    #
    # def set_doctor_name(self, doctor_name:str):
    #     name_pattern = r'^[A-Za-z]+\s[A-Za-z]+$'
    #     if not re.match(name_pattern, doctor_name):
    #         raise ValueError('Invalid Doctor Name')
    #     self.doctor_model.doctor_name = doctor_name
    #     return self
    #
    # def set_doctor_email(self, doctor_email:str):
    #     email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #     if not re.fullmatch(email_pattern, doctor_email):
    #         raise Exception('Invalid email')
    #     # if self.patients_collection.find({"email": patient_email}):
    #     #     raise Exception('Email already exists')
    #     self.doctor_model.doctor_email = doctor_email
    #     return self
    #
    # def set_doctor_password(self, doctor_password:str):
    #     password_pattern = r'^[a-zA-Z0-9]+$'
    #     if len(doctor_password) < 8 and not re.match(password_pattern, doctor_password):
    #         raise ValueError('Invalid password')
    #     self.doctor_model.doctor_password = doctor_password
    #     return self
    #
    # def set_doctor_dob(self, dob : str):
    #     self.doctor_model.doctor_dob = dob
    #     return self
    # def set_doctor_specialisation(self, doctor_specialisation:str):
    #     self.doctor_model.doctor_specialisation = doctor_specialisation
    #     return self
    #
    # def get_doctor_name(self):
    #     return self.doctor_model.doctor_name
    #
    # def get_doctor_email(self):
    #     return self.doctor_model.doctor_email
    #
    # def get_doctor_password(self):
    #     return self.doctor_model.doctor_password
    #
    # def get_doctor_id(self):
    #     return self.doctor_model.doctor_id
    # def get_doctor_dob(self):
    #     return self.doctor_model.doctor_dob
    # def get_doctor_specialisation(self):
    #     return self.doctor_model.doctor_specialisation
    #
    # def build(self):
    #     return self.doctor_model