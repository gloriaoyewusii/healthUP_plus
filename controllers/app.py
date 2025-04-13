from datetime import datetime

from flask import Flask, request, jsonify, make_response
from flask_mongoengine import MongoEngine
from marshmallow import Schema, fields
from bson import ObjectId

from data.models.appointments import Appointment
from data.models.availabilitydetails import AvailabilityDetails
from data.models.medicalrecord.patientinformation import PatientProfile
from data.models.patients import Patients
from data.models.status import Status
from data.schemas.appointmentschema import AppointmentSchema
from data.schemas.availabilitydetailschema import AvailabilityDetailSchema
from data.schemas.patientprofileschema import PatientProfileSchema
from data.schemas.patientschema import PatientSchema
from services.doctorservice import DoctorService
from data.repositories.doctorsrepository import DoctorsRepository

from data.models.doctors import Doctors
from data.schemas.doctorschema import DoctorSchema
import bcrypt

from services.patientservice import PatientService


def hash_password(password):
    if password == "":
        raise Exception("Password cannot be empty")
    else:
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        return hashed_password

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'healthup_db',
    'host': 'mongodb://localhost:27017'
}
db = MongoEngine(app)

Schema.TYPE_MAPPING[ObjectId] = fields.String


@app.route('/', methods=['GET'])
def index():
    return "Flask is running"

@app.route('/doctors', methods=['GET'])
def get_doctors():
    all_doctors = Doctors.objects.all()
    doctor_schema = DoctorSchema(many=True)
    doctors_data = doctor_schema.dump(all_doctors)
    return make_response(jsonify(doctors_data))

@app.route('/register_doctor', methods=['POST'])
def register_doctor():
    doctor_data = request.get_json()

    doctor_name = doctor_data.get('doctor_name')
    doctor_email = doctor_data.get('doctor_email')
    doctor_password = doctor_data.get('doctor_password')
    doctor_specialty = doctor_data.get('doctor_specialty')

    hashed_doctor_password = hash_password(doctor_password)

    try:
        DoctorService.register_as_doctor(doctor_name, doctor_email, hashed_doctor_password, doctor_specialty)
        doctor = Doctors.objects.get(doctor_email=doctor_email)

        doctor_schema = DoctorSchema()
        serialised_doctor = doctor_schema.dump(doctor)
        return make_response(jsonify({"doctor":serialised_doctor}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)
    # return f'Registration failed. Password characters less than 4.'
    # return jsonify({'doctor': doctor_data})

@app.route('/doctors/<doctor_id>', methods=['GET'])
def get_doctor_by_id(doctor_id):
    # doctor = Doctors.objects.get_or_404(doctor_email=doctor_email)
    # doctor_schema = DoctorSchema()
    # doctor_data = doctor_schema.dump(doctor)
    # return make_response(jsonify({"doctor":doctor_data}))

    doctor = DoctorsRepository.find_doctor_by_id(doctor_id)
    # doctor = Doctors.objects.get_or_404(id=ObjectId(doctor_id))
    doctor_schema = DoctorSchema()
    serialised_doctor = doctor_schema.dump(doctor)
    return make_response(jsonify({"doctor":serialised_doctor}), 200)

@app.route('/set_availability', methods=['POST'])
def set_availability():
    availability_data = request.get_json()

    available_date = availability_data.get('date')
    start_time = availability_data.get('start_time')
    end_time = availability_data.get('end_time')
    status = availability_data.get('status')
    # booked_by = availability_data.get('booked_by')
    doctor_id = availability_data.get('doctor_id')
    parsed_date = datetime.strptime(available_date, '%Y-%m-%d').date()

    availability_details = DoctorService.create_availability_details(parsed_date, start_time, end_time, status, doctor_id)
    availability_details_schema = AvailabilityDetailSchema()
    availability_details_data = availability_details_schema.dump(availability_details)
    return make_response(jsonify(availability_details_data))

@app.route('/register_patient', methods=['POST'])
def register_patient():
    patient_data = request.get_json()

    patient_name = patient_data.get('patient_name')
    patient_email = patient_data.get('patient_email')
    patient_password = patient_data.get('patient_password')

    hashed_patient_password = hash_password(patient_password)

    try:
        PatientService.register_as_patient(patient_name, patient_email, hashed_patient_password)

        patient = Patients.objects.get(patient_email=patient_email)

        patient_schema = PatientSchema()
        serialised_patient = patient_schema.dump(patient)
        return make_response(jsonify({"patient": serialised_patient}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)

@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patients.objects.all()
    patient_schema = PatientSchema(many=True)
    all_patients = patient_schema.dump(patients)
    return make_response(jsonify(all_patients))

@app.route('/patients/<patient_id>', methods=['GET'])
def get_patient_by_id(patient_id):
    patient = Patients.objects.get_or_404(id=patient_id)
    patient_schema = PatientSchema()
    serialised_patient = patient_schema.dump(patient)
    return make_response(jsonify(serialised_patient))


@app.route('/doctors/<doctor_id>/view_open_slots', methods=['GET'])
def view_open_slots(doctor_id):
   try:
       open_slots = AvailabilityDetails.objects(doctor_id=doctor_id, status=Status.AVAILABLE)
       if open_slots:
           open_slots_schema = AvailabilityDetailSchema(many=True)
           open_slots_data = open_slots_schema.dump(open_slots)
           return make_response(jsonify({"Open Slots": open_slots_data}))
       else:
           return make_response(jsonify({"No Open Slots Available"}))
   except Exception as e:
       return make_response(jsonify({"error": str(e)}), 400)


@app.route('/view_open_slots/book_appointment/<availability_id>', methods=['PUT'])
def book_appointment(availability_id):
    try:
        available_schedule = AvailabilityDetails.objects.get(id=availability_id, status=Status.AVAILABLE)
        if available_schedule.status == Status.AVAILABLE:
            available_schedule.update(set__status="Pending")
            available_schedule.reload()
        return make_response(jsonify({f"Appointment status":available_schedule.status.value}))
    except Exception as e:
        return f"Appointment slot not available for booking"
    # return make_response(jsonify({f"Appointment status" : available_schedule.status.value}))
@app.route('/approve_request/<availability_id>', methods=['PUT'])
def approve_request(availability_id):
    try:
        pending_request = AvailabilityDetails.objects.get(id=availability_id, status=Status.PENDING)
        if pending_request.status == Status.PENDING:
            pending_request.update(set__status="Booked")
            pending_request.reload()
        return make_response(jsonify({f"Appointment status":pending_request.status.value}))
    except Exception as e:
        return f"Appointment slot not available for booking"

@app.route('/reject_request/<availability_id>', methods=['PUT'])
def reject_request(availability_id):
    try:
        pending_request = AvailabilityDetails.objects.get(id=availability_id, status=Status.PENDING)
        if pending_request.status == Status.PENDING:
            pending_request.update(set__status="Not Available")
            pending_request.reload()
        return make_response(jsonify({f"Appointment status": pending_request.status.value}))
    except Exception as e:
        return f"Appointment slot not available for booking"

@app.route('/create-patient-profile', methods=['POST'])
def create_patient_profile():
    patient_profile = request.json

    patient_id = patient_profile.get('patient_id')
    first_name = patient_profile.get('first_name')
    last_name = patient_profile.get('last_name')
    email = patient_profile.get('email')
    phone_number = patient_profile.get('phone_number')
    address = patient_profile.get('address')
    date_of_birth = patient_profile.get('date_of_birth')
    gender = patient_profile.get('gender')

    try:
        PatientService.create_patient_profile(patient_id, first_name, last_name, phone_number, email, address, date_of_birth, gender)
        patient_profile = PatientProfile.objects.get(patient_id=patient_id)
        patient_schema = PatientProfileSchema()
        patient_data = patient_schema.dump(patient_profile)
        return make_response(jsonify({"Patient Profile":patient_data}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)

@app.route('/find-patient-profile/<profile_id>', methods=['GET'])
def find_patient_profile(profile_id):
    patient_profile = PatientService.find_patient_profile(profile_id)
    patient_profile_schema = PatientProfileSchema()
    patient_profile_data = patient_profile_schema.dump(patient_profile)
    return make_response(jsonify(patient_profile_data))
@app.route('/update-patient-profile/<profile_id>', methods=['PUT'])
def update_patient_profile(profile_id):
    patient_profile = PatientService.find_patient_profile(profile_id)
    update = request.json
    for field, value in update.items():
        if field in patient_profile.keys():
            patient_profile[field] = value
    patient_profile_schema = PatientProfileSchema()
    updated_profile = patient_profile_schema.dump(patient_profile)
    return make_response(jsonify(updated_profile))

# @app.route('/create_appointments', methods=['POST'])
# def create_appointments():
#     appointment_data = request.get_json()
#     doctor_email = appointment_data.get('doctor_email')
#     appointment_day = appointment_data.get('day')
#     appointment_date = appointment_data.get('date')
#     date = datetime.strptime(appointment_date, "%Y-%m-%dT%H:%M:%S")
#
#
#
#     try:
#         doctor = DoctorsRepository.find_doctor_by_email(doctor_email)
#         # doctor = Doctors.objects.get(doctor_email=doctor_email)
#         doctor_schema = DoctorSchema()
#
#         serialised_doctor = doctor_schema.dump(doctor)
#
#         DoctorService.create_appointment_time(doctor_email, appointment_day, date)
#         doctor.doctor_appointment_details = {"day": appointment_day, "date": date}
#         if doctor.doctor_appointment_details is not None:
#             return make_response(jsonify(serialised_doctor))
#     except Exception:
#         return f'Appointment creation failed. Day/Date information not found.'
#
#     # serialised_doctor.doctor_appointment_details = {"day":appointment_day, "date": date}
#
#     # return make_response(jsonify({"doctor":serialised_doctor}), 201)

@app.route('/doctors/<doctor_id>/pending-requests', methods=['GET'])
def get_pending_requests(doctor_id):
    pending_requests = AvailabilityDetails.objects(doctor_id=doctor_id, status=Status.PENDING)
    availability_details_schema = AvailabilityDetailSchema(many=True)
    availability_details_data = availability_details_schema.dump(pending_requests)
    return make_response(jsonify(availability_details_data))

@app.route('/appointments/<doctor_id>', methods=["GET"])
def view_appointments(doctor_id):
    # doctor = DoctorsRepository.find_doctor_by_email(doctor_email)
    appointments = Appointment.objects(doctor_id=doctor_id)
    appointment_schema = AppointmentSchema(many=True)
    serialised_appointments = appointment_schema.dump(appointments)

    return make_response(jsonify(serialised_appointments), 200)

@app.route('/daily_appointments/<doctor_id>/<appointment_day>', methods=['GET'])
def view_daily_appointments(doctor_id, appointment_day):
    days_appointments = DoctorService.view_daily_appointments_for(doctor_id, appointment_day)
    return make_response(jsonify(days_appointments), 200)


# @app.route('/admins', methods=['GET'])
# def get_admins():
#     all_admins = Admin.objects.all()
#     admin_schema = AdminSchema(many=True)
#     serialised_admins = admin_schema.dump(all_admins)
#     return make_response(jsonify(serialised_admins))


# @app.route('/register_admin', methods=['POST'])
# def register_as_admin():
#     admin_data = request.get_json()
#
#     admin_name = admin_data.get('admin_name')
#     admin_email = admin_data.get('admin_email')
#     admin_password = admin_data.get('admin_password')
#
#     hashed_password = hash_password(admin_password)
#     try:
#         AdminService.register_as_admin(admin_name, admin_email, hashed_password)
#         admin = Admin.objects.get(admin_email=admin_email)
#         admin_schema = AdminSchema()
#         serialised_admin = admin_schema.dump(admin)
#         print(serialised_admin)
#         return make_response(jsonify(serialised_admin), 201)
#     except Exception:
#         return make_response(jsonify({'error': 'Invalid credentials'}), 401)

# @app.route('/create_appointment', methods=['POST'])
# def book_appointment():
#
#     appointment_data = request.get_json()
#
#     appointment_date = appointment_data.get('appointment_date')
#     appointment_time = appointment_data.get('appointment_time')
#     patient_name = appointment_data.get('patient_name')
#     is_appointment_completed = appointment_data.get('is_appointment_completed')
#     reason_for_appointment = appointment_data.get('reason_for_appointment')
#     appointment_duration = appointment_data.get('appointment_duration')
#     scheduled_by = appointment_data.get('scheduled_by')
#     doctor_id = appointment_data.get('doctor_id')
#     patient_id = appointment_data.get('patient_id')
#
#     date = datetime.strptime(appointment_date, '%Y-%m-%d').date()
#     appointment = AdminService.create_appointment_time_for(
#         doctor_id,
#         admin_id,
#         patient_name,
#         date,
#         appointment_time,
#         appointment_duration,
#         reason_for_appointment,
#         is_appointment_completed,
#         scheduled_by
#     )
#     appointment_schema = AppointmentSchema()
#     doctor = DoctorsRepository.find_doctor_by_id(doctor_id)
#     print(appointment)
#     serialised_appointment = appointment_schema.dump(appointment)
#     return make_response(jsonify({f"Appointment for {doctor.doctor_name}":serialised_appointment}), 201)


if __name__ == '__main__':
    app.run(debug=True)



