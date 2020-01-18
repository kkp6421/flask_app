import os
from threading import Thread
from flask import render_template, current_app
from flask_mail import Message, Mail


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    mail = Mail(app)
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
    app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
    msg = Message(app.config['SAMPLE_MAIL_SUBJECT_PREFIX']+subject,
                  sender=app.config['FLASK_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
