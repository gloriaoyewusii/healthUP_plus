from mongoengine import connect

from data.models.patients import Patients

connect("healthup_db")
class PatientsRepository:

    @staticmethod
    def save_patient_to_repo(patient : Patients):
        patient.save()

    @staticmethod
    def count():
        count = Patients.objects.count({})
        return count

    @staticmethod
    def delete_patient_from_repo(patient_email : str):
        Patients.objects(patient_email=patient_email).delete()

    @staticmethod
    def find_patient_by_id(patient_id : str):
        patient = Patients.objects.get(id=patient_id)
        return f"{patient.patient_name}" + "\n" + f"{patient.patient_email}"

    @staticmethod
    def find_patient_by_email(patient_email: str):
        patient = Patients.objects.get(patient_email=patient_email)
        return f"Name: {patient.patient_name}" + "\n" + f"Email: {patient.patient_email}"

    @staticmethod
    def find_all_patients():
        all_patients = []
        patients = Patients.objects()
        for patient in patients:
            all_patients.append(patient.patient_name)
        return all_patients


