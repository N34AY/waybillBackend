from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
mongo = PyMongo(app)
CORS(app)


# Import a module / component using its blueprint handler variable (mod_auth)
from application.companies.controllers import mod_companies as companies_module
from application.lists.controllers import mod_lists as lists_module
from application.waybill.controllers import mod_waybills as waybills_module


# Register blueprint(s)
app.register_blueprint(companies_module)
app.register_blueprint(lists_module)
app.register_blueprint(waybills_module)


Settings = mongo.db.Settings
