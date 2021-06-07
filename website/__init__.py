from flask import Flask

def start_app():
    app = Flask(__name__)
    app.config['SECRET_key'] = 'web development with python'

    return app