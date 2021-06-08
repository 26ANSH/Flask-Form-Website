from flask import Blueprint, render_template
from sqlalchemy import create_engine

conn_str = 'mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 17 for SQL Server};Server=tcp:ansh-db-server.database.windows.net,1433;Database=ansh-db;Uid=ansh-db-server-admin;Pwd=mydbpassword@001;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
engine_azure = create_engine(conn_str,echo=True)

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/register')
def register():
    return render_template('register.html')

@views.route('/connect')
def connect():
    s = engine_azure.table_names()
    return 'Database is '+s
    # return render_template('connect.html')