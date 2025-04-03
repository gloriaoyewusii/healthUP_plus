from flask import Flask, request, jsonify

from data.models.doctors import Doctors

app = Flask(__name__)

@app.route('/register_doctor', methods=['POST'])
def register_doctor():
    doctor_data = request.get_json()
    doctor = Doctors.objects(doctor_email=doctor_data['doctor_email'], doctor_password=doctor_data['doctor_password'])