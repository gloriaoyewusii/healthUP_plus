from flask import Flask, request, jsonify

from data.models.doctors import Doctors
from mongoengine import connect


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/healthup_db"


# connect("healthup_db", host="localhost", port=27017)
@app.route('/register_doctor', methods=['POST'])
def register_doctor():
    doctor_data = request.get_json()
    doctor = Doctors.objects(doctor_email=doctor_data['doctor_email'], doctor_password=doctor_data['doctor_password'])
    doctor.save()
    return jsonify({'doctor': doctor_data})

