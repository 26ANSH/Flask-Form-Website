from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/connect')
def connect():
    return render_template('connect.html')

@views.route('/sucess')
def welcome():
    return render_template('sucess.html')