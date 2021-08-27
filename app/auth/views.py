from flask import render_template, redirect
from flask import render_template, redirect, flash, request, url_for
from flask_login import login_user, logout_user, login_required
from . import auth
from . forms import RegistrationForm, LoginForm
from ..models import Role, User
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('employes.index'))

        flash('Invalid username or Password. Please check.')
        return redirect(url_for('employes.index'))

    return render_template('auth/login.html', login_form=login_form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        role=Role.query.filter_by(name='Salonist').first()
        user = User(email=form.email.data,
                username=form.username.data, password=form.password.data,role=role,status=0)
        db.session.add(user)
        db.session.commit()
        flash('Your account have been created successfully!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', registration_form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('employes.index'))