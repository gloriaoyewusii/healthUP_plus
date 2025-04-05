from flask import Flask, request, jsonify, make_response
from flask_mongoengine import MongoEngine
from marshmallow import Schema, fields, post_load
from bson import ObjectId
from data.models.doctors import Doctors
from data.shemas.doctorschema import DoctorSchema

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
    doctors = Doctors.objects.all()
    doctor_schema = DoctorSchema(many=True)
    doctors_data, error = doctor_schema.dump(doctors)
    return make_response(jsonify(doctor_schema.dump(doctors_data)))
    # get_doctors = Doctors.objects.all()
    # doctor_schema = DoctorSchema(many=True)
    # doctors, error = doctor_schema.dump(get_doctors)
    # return jsonify(doctor_schema.dump(doctors))
    # return make_response(jsonify({"doctors" :doctors}))



if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/register_doctor', methods=['POST'])
# def register_doctor():
# #     doctor_data = request.get_json()
#     doctor = Doctors.objects(doctor_email=doctor_data['doctor_email'], doctor_password=doctor_data['doctor_password'])
#     doctor.save()
#     return jsonify({'doctor': doctor_data})

