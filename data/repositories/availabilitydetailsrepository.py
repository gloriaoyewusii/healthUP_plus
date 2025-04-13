from data.models.availabilitydetails import AvailabilityDetails
from data.repositories.availabilitydetailsinterface import AvailabilityDetailsInterface


class AvailabilityDetailsRepository(AvailabilityDetailsInterface):
    @staticmethod
    def save_availability_details_to_repo(availability_details:AvailabilityDetails):
        availability_details.save()
        return availability_details
    @staticmethod
    def count():
        count = AvailabilityDetails.objects.count({})
        return count
    @staticmethod
    def delete_availability_details_of_doctor(details_id):
        return AvailabilityDetails.objects.get(id=details_id).delete()
    @staticmethod
    def find_availability_details_of_doctor_by_id(doctor_id):
        return AvailabilityDetails.objects(doctor_id=doctor_id)
    @staticmethod
    def find_availability_details_of_doctor_by_email(doctor_email):
        availability_details = AvailabilityDetails.objects.get(email=doctor_email)
        return availability_details
    @staticmethod
    def find_all_availability_details():
        all_availability_details = AvailabilityDetails.objects.all()
        return all_availability_details