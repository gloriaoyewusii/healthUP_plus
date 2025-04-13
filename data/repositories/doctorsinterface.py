from abc import ABC


class DoctorsInterface(ABC):

    @staticmethod
    def save_doctor_to_repo(doctor):
        pass
    @staticmethod
    def count():
        pass

    @staticmethod
    def delete_doctor_from_repo(doctor_email : str):
        pass

    @staticmethod
    def find_doctor_by_id(doctor_id : str):
        pass

    @staticmethod
    def find_doctor_by_email(doctor_email : str):
        pass

    @staticmethod
    def find_all_doctors():
        pass

    @staticmethod
    def find_all_availability_details():
        pass