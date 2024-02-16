from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Owner
from project.owners.forms import AddForm

owners_blueprint = Blueprint('owners', __name__,
                             template_folder='templates/owners')

@owners_blueprint.route('/add', methods=['GET','POST'])
def add():
    form= AddForm()
    if form.validate_on_submit():
        pid=form.pid.data
        name=form.name.data
        new_owner=Owner(name, pid)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('pups.list'))
    return render_template('addo.html', form=form)