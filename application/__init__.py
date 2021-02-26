from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_jwt_extended import JWTManager


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
mongo = PyMongo(app)
jwt = JWTManager(app)
CORS(app)


# Import a module / component using its blueprint handler variable (mod_auth)
from application.companies.controllers import mod_companies as companies_module
from application.lists.controllers import mod_lists as lists_module
from application.waybill.controllers import mod_waybills as waybills_module
from application.auth.controllers import mod_auth as auth_module


# Register blueprint(s)
app.register_blueprint(companies_module)
app.register_blueprint(lists_module)
app.register_blueprint(waybills_module)
app.register_blueprint(auth_module)


Settings = mongo.db.Settings


# Sample HTTP error handling
@app.errorhandler(404)
def not_found():
    return 'Not found', 404


@app.errorhandler(500)
def error():
    return '500 Error', 500
