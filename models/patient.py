import datetime
import bcrypt


def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password


class Patient:
    def __init__(self):
        self.id_number = 0
        # self.first_name = ""
        # self.last_name = ""
        self.patient_name = None
        self.dob = ""
        # self.dob = datetime.datetime.strptime(dob, "%d/%m/%Y")
        self.email_address = ""
        self.password = hash_password("")


