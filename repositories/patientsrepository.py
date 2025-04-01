from data.models.patient import Patient


class Patients:

    @staticmethod
    def save_patient_to_repo(patient : Patient):
        patient.save()

    @staticmethod
    def count():
        count = Patient.objects.count({})
        return count

    @staticmethod
    def delete_patient_from_repo(patient : Patient):
        patient.delete()

    @staticmethod
    def find_patient_by_id(patient_id : int):
        patient = Patient.objects.get(id=patient_id)
        return patient

