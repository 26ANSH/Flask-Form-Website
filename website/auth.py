from flask import Blueprint, render_template, request, session
from flask_mail import Message
from . import conn_url, mail
from .views import WP_MSG, MSG_URL
import pyodbc
auth = Blueprint('auth', __name__)
cnxn = pyodbc.connect(conn_url)
cursor = cnxn.cursor()

def send_ok_mail(rec, name):
    msg = Message(subject='Web Development with Python',
                                sender='ansh.vidyabhanu@studentambassadors.com',
                                recipients=[rec], 
                                body='Thank you '+name+' for registering')
    msg.msgId = msg.msgId.split('@')[0] + 'studentambassadors.com'
    mail.send(msg)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if "registered" in session:
        print("session received",session["registered"])
        return render_template('error.html', templatevalue="sucess.html", message="You Have Already Registered for this Event!!!", WP_MSG  = WP_MSG, MSG_URL = MSG_URL)
    else:
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
                    session["registered"] = 'done'
                    print("session ser",session["registered"])
                    return render_template('error.html', templatevalue="sucess.html", message="You Have Already Registered for this Event!!!", WP_MSG  = WP_MSG, MSG_URL = MSG_URL)
                else:
                    session["registered"] = 'done'

                    # SEnd Mails
                    send_ok_mail(emailid, fname)
                

                    # print("session ser",session["registered"])
                    cursor.execute(f"INSERT INTO UserData VALUES ('{emailid}', '{fname}', '{lname}', '{country}');") 
                    cursor.commit()
                    return render_template('sucess.html', WP_MSG  = WP_MSG, MSG_URL = MSG_URL )
        else:    
            return render_template('register.html')