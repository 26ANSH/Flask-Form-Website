from flask import Blueprint, render_template, send_file, url_for

views = Blueprint('views', __name__)

WP_MSG = 'Introduction to Web Development With Python Hosted by @vidyabhanuansh Co-Sponsored by Microsoft Student Learn Ambassadors Register at '
MSG_URL='event.whoisansh.tech'

@views.route('/dwnld')
def download_file():
    return send_file('static/images/event.jpg', as_attachment=True)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/connect')
def connect():
    return render_template('connect.html')

@views.route('/about')
def aboutt():
    return render_template('about.html')