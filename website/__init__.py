from flask import Flask, render_template

def start_app():
    app = Flask(__name__)
    app.config['SECRET_key'] = 'web development with python'

    return app
