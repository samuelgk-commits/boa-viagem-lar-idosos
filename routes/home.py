from flask import Blueprint, render_template

rota_home = Blueprint('home', __name__)

@rota_home.route('/')
def home():
    return render_template('index.html')

