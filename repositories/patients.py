from models.patient import Patient
from repositories.patient_repository import PatientRepository

class Patients(PatientRepository):
    def __init__(self):
        super().__init__()

    def save_patient_to_repo(self, patient: Patient):
        self.patients_collection.insert_one(patient.__dict__)
        #
        # if self.patients_collection.find({"id_number":id_number}):
        #     raise Exception('ID number already exists')
        # self.patients_collection.insert_one({"id_number": id_number, "patient_name": patient_name, "dob": dob, "email": email, "password": password})
    def count(self):
        return self.patients_collection.count_documents({})
    def delete_patient_from_repo(self, patient_id : int):
        return self.patients_collection.delete_one({"id_number": patient_id})
    def find_patient_by_id(self, patient_id : int):
        return self.patients_collection.find_one({"id_number": patient_id})
    def close_connection(self):
        return self.client.close()

