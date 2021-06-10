from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

WP_MSG = 'Introduction to Web Development With Python Hosted by @vidyabhanuansh Co-Sponsored by Microsoft Student Learn Ambassadors Register at '
MSG_URL='event.whoisansh.tech'

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/connect')
def connect():
    return render_template('connect.html')

@views.route('/sucess')
def welcome():
    return render_template('sucess.html', WP_MSG  = WP_MSG, MSG_URL = MSG_URL )