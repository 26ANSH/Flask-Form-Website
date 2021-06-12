from threading import Thread
from flask import current_app, render_template
from . import mail
from flask_mail import Message

def send_async_email(app, msg):
    with app.app_context():
        # block only for testing parallel thread
        mail.send(msg)

def send_email(to, fname, render):
    app = current_app._get_current_object()
    msg = Message(subject='Web Development with Python',sender='ansh.vidyabhanu@studentambassadors.com',recipients=[to])
    msg.html = render
    msg.msgId = msg.msgId.split('@')[0] + 'studentambassadors.com'
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()