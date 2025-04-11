from abc import ABC


class AvailabilityDetailsInterface(ABC):
    @staticmethod
    def save_availability_details_to_repo(availability_details):
        pass
    @staticmethod
    def count():
        pass
    @staticmethod
    def delete_availability_details_of_doctor(doctor_id):
        pass
    @staticmethod
    def find_availability_details_of_doctor_by_id(details_id):
        pass
    @staticmethod
    def find_availability_details_of_doctor_by_email(doctor_email):
        pass
    @staticmethod
    def find_all_availability_details():
        pass