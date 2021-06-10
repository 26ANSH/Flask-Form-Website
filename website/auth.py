from flask import Blueprint, render_template, request, redirect, url_for
from . import conn_url
import pyodbc
auth = Blueprint('auth', __name__)
cnxn = pyodbc.connect(conn_url)
cursor = cnxn.cursor()


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        emailid = request.form['emailid']
        country = request.form['country']
        # print(fname, lname, emailid, country)

        if lname == '' or country == '' or fname == '' or emailid == '':
            return render_template('error.html', templatevalue="register.html", message="Please Fill all Elements")
        else:
            cursor.execute(f"SELECT * FROM UserData WHERE UserEmail='{emailid}'")
            row_count = cursor.fetchall()
            if len(row_count) != 0:
                return render_template('error.html', templatevalue="sucess.html", message="You Have Already Registered for this Event!!!")
            else:
                cursor.execute(f"INSERT INTO UserData VALUES ('{emailid}', '{fname}', '{lname}', '{country}');") 
                cursor.commit()
                return redirect(url_for('views.welcome'))
    else:
        return render_template('register.html')