from models.patient import Patient
from abc import ABC, abstractmethod
from pymongo import MongoClient

class PatientRepository(ABC):
    # database_connection = "mongodb://localhost:27017/"
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["healthup_db"]
        self.patients_collection = self.db["patients_collection"]
        self.db.patients.create_index("email", unique=True)


    @abstractmethod
    def save_patient_to_repo(self, patient : Patient):
        pass
    @abstractmethod
    def count(self):
        pass
    @abstractmethod
    def delete_patient_from_repo(self, patient : Patient):
        pass
    @abstractmethod
    def find_patient_by_id(self, patient_id : int):
        pass
    def close_connection(self):
        pass

