
from flask_login import login_required
from app.models import Role,User
from app.employes.forms import RolesForm
from flask import render_template,flash,redirect,url_for
from . import employes
from .. import db


@employes.route('/index')
def index():
    employees=Employees.query.all()
    print(employees)
    return render_template('employes/index.html',employees=employees)
@employes.route('/add',methods=['POST','GET'])
@login_required
def add_employee():
    form=RolesForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data)

        db.session.add(role)
        db.session.commit()
        flash('Role added sucesfuly!', 'success')
        return redirect(url_for('employes.index'))

    return render_template('employes/addform.html',form=form)

