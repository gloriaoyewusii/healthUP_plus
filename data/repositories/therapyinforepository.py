from data.models.medicalrecord.therapyinformation import TherapyInformation
from data.repositories.therapyinfointerface import TherapyInfoInterface


class TherapyRepository(TherapyInfoInterface):
    @staticmethod
    def save_therapy_info_to_repo(therapy_info):
        therapy_info.save()
        return therapy_info
    @staticmethod
    def count():
        count = TherapyInformation.objects.count({})
        return count
    @staticmethod
    def delete_therapy_info_of_patient(therapy_id):
        return TherapyInformation.objects.get(id=therapy_id).delete()
    @staticmethod
    def find_therapy_info_of_patient_by_id(therapy_id):
        therapy_info = TherapyInformation.objects.get(id=therapy_id)
        return therapy_info
    @staticmethod
    def find_all_therapy_info():
        return TherapyInformation.objects.all()