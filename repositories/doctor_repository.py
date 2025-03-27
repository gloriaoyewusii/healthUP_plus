from models.doctor import Doctor
from abc import ABC, abstractmethod
from pymongo import MongoClient

class DoctorRepository(ABC):
    # database_connection = "mongodb://localhost:27017/"
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["healthup_db"]
        self.doctors_collection = self.db["doctors_collection"]
        self.db.doctors.create_index("email", unique=True)


    @abstractmethod
    def save_doctor_to_repo(self, doctor : Doctor):
        pass
    @abstractmethod
    def count(self):
        pass
    @abstractmethod
    def delete_doctor_from_repo(self, doctor : Doctor):
        pass
    @abstractmethod
    def find_doctor_by_id(self, doctor_id : int):
        pass
    # @abstractmethod
    # def close_connection(self):
    #     pass

