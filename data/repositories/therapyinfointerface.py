from abc import ABC


class TherapyInfoInterface(ABC):
    @staticmethod
    def save_therapy_info_to_repo(therapy_info):
        pass
    @staticmethod
    def count():
        pass
    @staticmethod
    def delete_therapy_info_of_doctor(therapy_id):
        pass
    @staticmethod
    def find_therapy_info_of_patient_by_id(therapy_id):
        pass
    @staticmethod
    def find_all_therapy_info():
        pass