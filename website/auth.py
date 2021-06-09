from flask import Blueprint, render_template, request, redirect, url_for
from .models import user
from . import db
auth = Blueprint('auth', __name__)


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
            check_user = user.query.filter_by(Uemail=emailid).first()
            if check_user:
                return render_template('error.html', templatevalue="sucess.html", message="You Have Already Registered for this Event!!!")
            else:
                new_user = user(Uemail=emailid, Fname=fname, Lname=lname, Ucountry=country)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('views.welcome'))

    else:
        return render_template('register.html')