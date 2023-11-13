import json
from flask import request, render_template, Blueprint, redirect, url_for, flash, send_from_directory, send_file, jsonify,make_response, abort
from flask_login import login_required, current_user
import random
from .forms import InscriptionForm, ConnexionForm
import numpy as np
import random, string
from flask import Flask

BASE_URL = "http://13.38.65.225"
ALLOWED_EXTENSIONS =  {'png', 'jpg', 'jpeg', 'gif'}
DEV_API_KEY = 'teklia-demo-W3Nn3bSCw78eJABU7psO3vi6'
PROD_API_KEY = 'trial-8KRJPTFWh8nXQyXPM0ORVqzJTidXuUeveNE6T70ARc'
WORD_MODEL="aeraezjrklkdseoziururyptrzsmlkflmqskdflmqdsgkjhkdqgnbvbxvcnwbxvhjqdsf"
STORAGE_BASE_PATH = "data"

main = Blueprint('main',__name__)

# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

@main.route('/', methods=['GET'])
def root():
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main.route('/rendez-vous')
def rendez_vous():
    return render_template('rendez_vous.html')

@main.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@main.route('/urgence')
def urgence():
    return render_template('urgence.html')

@main.route('/medicament')
def medicament():
    return render_template('medicament.html')