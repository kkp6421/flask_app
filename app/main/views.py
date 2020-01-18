from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, abort
from . import main, errors
from ..models import Permission
from flask_login import login_required
from ..decorators import admin_required, permission_required
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html',
                           current_time=datetime.utcnow())
@main.route('/help')
def help():
    return render_template('main/help.html')

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('main/user.html', user=user)

@main.route('/admin')
@login_required
@admin_required
def for_admin_only():
    return "For Administrators!"

@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "For comment moderators!"
