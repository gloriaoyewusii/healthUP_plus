from models.doctor import Doctor
from repositories.doctor_repository import DoctorRepository

class Doctors(DoctorRepository):
    def __init__(self):
        super().__init__()

    def save_doctor_to_repo(self, doctor: Doctor):
        self.doctors_collection.insert_one(doctor.__dict__)
        #
        # if self.patients_collection.find({"id_number":id_number}):
        #     raise Exception('ID number already exists')
        # self.patients_collection.insert_one({"id_number": id_number, "patient_name": patient_name, "dob": dob, "email": email, "password": password})
    def count(self):
        return self.doctors_collection.count_documents({})
    def delete_doctor_from_repo(self, doctor_id : int):
        return self.doctors_collection.delete_one({"doctor_id": doctor_id})
    def find_doctor_by_id(self, doctor_id : int):
        return self.doctors_collection.find_one({"doctor_id": doctor_id})
    def close_connection(self):
        return self.client.close()

