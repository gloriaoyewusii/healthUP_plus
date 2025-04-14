from flask import request

from data.models.medicalrecord.patientinformation import PatientProfile
from data.repositories.patientprofileinterface import PatientInterface


class PatientProfileRepository(PatientInterface):

    @staticmethod
    def save_patient_profile_to_repo(patient_profile : PatientProfile):
        patient_profile.save()
        return patient_profile
    @staticmethod
    def count():
        count = PatientProfile.objects.count({})
        return count
    @staticmethod
    def delete_patient_profile(profile_id):
        return PatientProfile.objects.get(id=profile_id)
    @staticmethod
    def find_patient_profile_by_id(profile_id):
        patient_profile = PatientProfile.objects.get(id=profile_id)
        return patient_profile
    @staticmethod
    def find_patient_profile_by_email(patient_email):
        patient_profile = PatientProfile.objects.get(email=patient_email)
        return patient_profile
    @staticmethod
    def find_all_patient_profiles():
        all_patient_profiles = PatientProfile.objects.all()
        return all_patient_profiles
    @staticmethod
    def update_profile(profile_id, field, value):
        profile = PatientProfileRepository.find_patient_profile_by_id(profile_id)
        if hasattr(profile, field):
            setattr(profile, field, value)
        profile.save()
        return profile

