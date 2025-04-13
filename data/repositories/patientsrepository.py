
from data.models.patients import Patients
from data.repositories.patientsinterface import PatientsInterface


class PatientsRepository(PatientsInterface):

    @staticmethod
    def save_patient_to_repo(patient : Patients):
        patient.save()
        return patient

    @staticmethod
    def count():
        count = Patients.objects.count({})
        return count

    @staticmethod
    def delete_patient_from_repo(patient_id):
        return Patients.objects(id=patient_id).delete()

    @staticmethod
    def find_patient_by_id(patient_id : str):
        patient = Patients.objects.get(id=patient_id)
        return patient
    @staticmethod
    def find_patient_by_email(patient_email: str):
        patient = Patients.objects.get(patient_email=patient_email)
        return patient
    @staticmethod
    def find_all_patients():
        all_patients = Patients.objects.all()
        return all_patients
        # all_patients = []
        # patients = Patients.objects()
        # for patient in patients:
        #     all_patients.append(patient.patient_name)
        # return all_patients


