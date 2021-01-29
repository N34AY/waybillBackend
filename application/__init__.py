from flask import Flask, render_template, request
from flask_pymongo import PyMongo


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
mongo = PyMongo(app)


# Import a module / component using its blueprint handler variable (mod_auth)
from application.companies.controllers import mod_companies as companies_module

# Register blueprint(s)
app.register_blueprint(companies_module)


Settings = mongo.db.Settings
