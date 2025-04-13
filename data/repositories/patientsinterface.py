from abc import ABC

from data.models.patients import Patients


class PatientsInterface(ABC):

    @staticmethod
    def save_patient_to_repo(patient : Patients):
        pass

    @staticmethod
    def count():
        pass

    @staticmethod
    def delete_patient_from_repo(patient_email : str):
        pass

    @staticmethod
    def find_patient_by_id(patient_id : str):
        pass
    @staticmethod
    def find_patient_by_email(patient_email: str):
        pass
    @staticmethod
    def find_all_patients():
        pass
