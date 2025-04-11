# import bcrypt
# # from mongoengine import disconnect
# # disconnect()
# # connect('healthup_db', alias='admin_alias', host='localhost', port=27017)
# from flask_mongoengine import MongoEngine
# from flask import Flask, request, jsonify, make_response
# from marshmallow import Schema, fields
# from bson import ObjectId
#
#
#
# def hash_password(password):
#     is_empty = ""
#     if password is not is_empty and len(password) == 8:
#         return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#
# app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {
#     'db': "healthup_db",
#     'host': "mongodb://localhost:27017"
# }
# db = MongoEngine(app)
#
# Schema.TYPE_MAPPING[ObjectId] = fields.String
#

#
#

#
# if __name__ == '__main__':
#     app.run(debug=True)
