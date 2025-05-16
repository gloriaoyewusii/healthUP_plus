# from data.models.medicalrecord.medicalrecord import MedicalRecord
from data.repositories.medicalrecordinterface import MedicalRecordInterface


class MedicalRecordRepository(MedicalRecordInterface):

    @staticmethod
    def save_medical_record_to_repo(medical_record):
        medical_record.save()
        return medical_record

    @staticmethod
    def count_medical_records():
        count = MedicalRecord.objects.count({})
        return count
    @staticmethod
    def find_medical_record_by_id(medical_record_id):
        medical_record = MedicalRecord.objects.get(id=medical_record_id)
        return medical_record
    @staticmethod
    def delete_medical_record_by_id(medical_record_id):
        medical_record = MedicalRecord.objects.get(id=medical_record_id)
        medical_record.delete()

    @staticmethod
    def find_all_medical_records():
        medical_records = MedicalRecord.objects.all()
        return medical_records