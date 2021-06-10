from flask import Flask, render_template

#  Connection Parameters
driver = "{ODBC Driver 17 for SQL Server}"
server_name = "ansh-db-server"
database_name = "ansh-db"
server =  f'{server_name}.database.windows.net,1433'
username = 'ansh-db-server-admin'
password = 'mydbpassword@001'

# Connection String
conn_url = f"Driver={driver};Server=tcp:{server};Database={database_name};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
# db = pyodbc()

def page_not_found(e):
  return render_template('404.html'), 404

def start_app():
    app = Flask(__name__)
    app.config['SECRET_key'] = 'web development with python'

    from . views import views
    from . auth import auth

    app.secret_key = 'web development with python'
    app.register_error_handler(404, page_not_found)
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
