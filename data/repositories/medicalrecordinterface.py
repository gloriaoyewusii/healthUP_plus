from abc import ABC


class MedicalRecordInterface(ABC):

    @staticmethod
    def save_medical_record_to_repo(medical_record):
        pass
    @staticmethod
    def count_medical_records():
        pass
    @staticmethod
    def find_medical_record_by_id(medical_record_id):
        pass
    @staticmethod
    def delete_medical_record_by_id(medical_record_id):
        pass
    @staticmethod
    def find_all_medical_records():
        pass