from abc import ABC


class PatientInterface(ABC):
    @staticmethod
    def save_patient_profile_to_repo(patient_profile):
        pass
    @staticmethod
    def count():
        pass
    @staticmethod
    def delete_patient_profile(profile_id):
        pass
    @staticmethod
    def find_patient_profile_by_id(profile_id):
        pass
    @staticmethod
    def find_patient_profile_by_email(patient_email):
        pass
    @staticmethod
    def find_all_patient_profiles():
        pass
    @staticmethod
    def update_patient_profile(profile_id):
        pass