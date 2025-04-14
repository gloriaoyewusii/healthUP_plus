from data.models.availabilitydetails import AvailabilityDetails
from data.models.doctors import Doctors
from data.models.appointments import Appointment
from data.models.medicalrecord.therapyinformation import TherapyInformation
from data.repositories.availabilitydetailsrepository import AvailabilityDetailsRepository

from data.repositories.doctorsrepository import DoctorsRepository
from data.repositories.therapyinforepository import TherapyRepository


class DoctorService:


    @staticmethod
    def register_as_doctor(name : str, email : str, password : str, specialisation : str):

        try:
            doctor = Doctors(doctor_name=name, doctor_email=email, doctor_password=password, doctor_specialty=specialisation)
            DoctorsRepository.save_doctor_to_repo(doctor)
        except Exception as e:
            print(e)

    @staticmethod
    def create_availability_details(date, start_time, end_time, status, doctor_id):
        try:
            availability_details = AvailabilityDetails(date=date, start_time=start_time, end_time=end_time, status=status, doctor_id=doctor_id)
            return AvailabilityDetailsRepository.save_availability_details_to_repo(availability_details)
        except Exception as e:
            print(e)

    @staticmethod
    def create_therapy_info(therapy_data):
        therapy_info = TherapyInformation(**therapy_data)
        return TherapyRepository.save_therapy_info_to_repo(therapy_info)

    @staticmethod
    def find_patient_therapy_record(therapy_id):
        therapy_record = TherapyRepository.find_therapy_info_of_patient_by_id(therapy_id)
        return therapy_record

    @staticmethod
    def update_therapy_info(therapy_id, **therapy_data):
        therapy_info = TherapyRepository.find_therapy_info_of_patient_by_id(therapy_id)
        for field, value in therapy_data.items():
            if hasattr(therapy_info, field):
                setattr(therapy_info, field, value)
        TherapyRepository.save_therapy_info_to_repo(therapy_info)
        return therapy_info





    # @staticmethod
    # def create_appointment_time(doctor_email, appointment_day : str, appointment_date : datetime.datetime):
    #     # appointments = []
    #     try:
    #         DoctorsRepository.save_doctors_open_appointment(doctor_email, appointment_day, appointment_date)
    #         # appointment = DoctorsRepository.save_doctors_open_appointment(doctor_name, appointment_day, appointment_date)
    #         # appointments.append(appointment)
    #         # print(appointments)
    #     except Exception as e:
    #         print(e)
        # try:
        #     # appointment_details = Appointment(day=appointment_day, date=appointment_date)
        #     # Doctors.objects(doctor_name=name).update(doctor_appointment_details=appointment_details)
        #     DoctorsRepository.save_doctors_open_appointment(Doctors.objects(doctor_name=name).update(set_appointment_day=appointment_day))
        #     DoctorsRepository.save_doctors_open_appointment(Doctors.objects(doctor_name=name).update(set_appointment_date=appointment_date))

            # AppointmentRepository.save_appointments_to_repo(Appointment(day=appointment_day, date=appointment_date))
        # except Exception as e:
        #     print(e)

    @staticmethod
    def view_appointments_for(doctor_id, appointment_id):
        dokie = Doctors.objects.get(id=doctor_id)
        appointment = Appointment.objects.get(id=appointment_id)
        if doctor_id == appointment.doctor_id:
            return appointment
        # print(dokie.doctor_appointment_details[0].date)
        # weekly_appointments = []
        # for index in range(len(dokie.doctor_appointment_details)):
        #     weekly_appointments.append(dokie.doctor_appointment_details[index].day)
        #     weekly_appointments.append(dokie.doctor_appointment_details[index].date)
        # print(weekly_appointments)
        #
        # return dokie.doctor_appointment_details




    def __str__(self):
        return f"Name: {Doctors.doctor_name}\nEmail: {Doctors.doctor_email}\nPassword: {Doctors.doctor_password}"

    @staticmethod
    def view_daily_appointments_for(doctor_id, appointment_day):
        doctor = Doctors.objects.get(id=doctor_id, doctor_appointment_details__day=appointment_day)
        day_appointments = []
        for index in range(len(doctor.doctor_appointment_details)):
            if doctor.doctor_appointment_details[index].day == appointment_day:
                day_appointments.append(doctor.doctor_appointment_details[index].date)
        print(day_appointments)
        return day_appointments


