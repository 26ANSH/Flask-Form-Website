from flask import Flask, render_template

def start_app():
    app = Flask(__name__)
    app.config['SECRET_key'] = 'web development with python'
    
    from . views import views
    from . auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
