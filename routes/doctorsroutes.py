from datetime import datetime

from flask import Flask, request, jsonify, make_response
from flask_mongoengine import MongoEngine
from marshmallow import Schema, fields, post_load
from bson import ObjectId

from data.shemas.appointmentschema import AppointmentSchema
from services.doctorservice import DoctorService
from repositories.doctorsrepository import DoctorsRepository

from data.models import doctors
from data.models.doctors import Doctors
from data.shemas.doctorschema import DoctorSchema
from mongoengine import disconnect

disconnect()

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
    return make_response(jsonify(doctor_schema.dump(doctors_data)))
    # get_doctors = Doctors.objects.all()
    # doctor_schema = DoctorSchema(many=True)
    # doctors, error = doctor_schema.dump(get_doctors)
    # return jsonify(doctor_schema.dump(doctors))
    # return make_response(jsonify({"doctors" :doctors}))

@app.route('/register_doctor', methods=['POST'])
def register_doctor():
    doctor_data = request.get_json()


    doctor_name = doctor_data.get('doctor_name')
    doctor_password = doctor_data.get('doctor_password')
    doctor_email = doctor_data.get('doctor_email')
    doctor_specialty = doctor_data.get('doctor_specialty')


    # doctor = Doctors(
    #     doctor_name=doctor_name,
    #     doctor_email=doctor_email,
    #     doctor_specialty=doctor_specialty,
    #     doctor_password=doctor_password
    # )
    # doctor = Doctors(doctor_name=doctor_data['doctor_name'], doctor_email=doctor_data['doctor_email'],
    #                  doctor_password=doctor_data['doctor_password'], doctor_specialty=doctor_data['doctor_specialty'])

    # doctor_sun.save()


    # doctor_schema.load(doctor_data)
    # doctor_dat = doctor_schema.dump(doctor_sun)
    DoctorService.register_as_doctor(doctor_name, doctor_email, doctor_password, doctor_specialty)
    doctor = Doctors.objects.get(doctor_email=doctor_email)
    doctor_schema = DoctorSchema()
    serialised_doctor = doctor_schema.dump(doctor)
    return make_response(jsonify({"doctor":serialised_doctor}), 201)
    # return jsonify({'doctor': doctor_data})
@app.route('/doctors/<doctor_email>', methods=['GET'])
def get_doctor_by_email(doctor_email):
    # doctor = Doctors.objects.get_or_404(doctor_email=doctor_email)
    # doctor_schema = DoctorSchema()
    # doctor_data = doctor_schema.dump(doctor)
    # return make_response(jsonify({"doctor":doctor_data}))

    doctor = DoctorsRepository.find_doctor_by_email(doctor_email)
    doctor_schema = DoctorSchema()
    serialised_doctor = doctor_schema.dump(doctor)
    return make_response(jsonify({"doctor":serialised_doctor}), 200)

@app.route('/create_appointments', methods=['POST'])
def create_appointments():
    appointment_data = request.get_json()
    doctor_email = appointment_data.get('doctor_email')
    appointment_day = appointment_data.get('appointment_day')
    appointment_date = appointment_data.get('appointment_date')
    app_date = datetime.strptime(appointment_date, "%Y-%m-%dT%H:%M:%S")

    DoctorService.create_appointment_time(doctor_email, appointment_day, app_date)
    doctor = DoctorsRepository.find_doctor_by_email(doctor_email)
    doctor_schema = DoctorSchema()
    serialised_doctor = doctor_schema.dump(doctor)
    return make_response(jsonify({"doctor":serialised_doctor}), 201)

@app.route('/weekly_appointments/<doctor_email>', methods=["GET"])
def view_weekly_appointments(doctor_email):
    # doctor = DoctorsRepository.find_doctor_by_email(doctor_email)
    weeks_appointment = DoctorService.view_weekly_appointments_for(doctor_email)

    return make_response(jsonify(weeks_appointment), 200)

@app.route('/daily_appointments/<doctor_email>/<appointment_day>', methods=['GET'])
def view_daily_appointments(doctor_email, appointment_day):
    days_appointments = DoctorService.view_daily_appointments_for(doctor_email, appointment_day)
    return make_response(jsonify(days_appointments), 200)





if __name__ == '__main__':
    app.run(debug=True)



