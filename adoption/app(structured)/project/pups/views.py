from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Pup
from project.pups.forms import AddForm, DelForm

pups_blueprint = Blueprint('pups', __name__,
                             template_folder='templates/pups')

@pups_blueprint.route('/add', methods=['GET','POST'])
def add():
    form= AddForm()

    if form.validate_on_submit():
        name=form.name.data
        new_pup=Pup(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('pups.list'))
    return render_template('add.html', form=form)

@pups_blueprint.route('/list')
def list():
    pups=Pup.query.all()
    return render_template('list.html',pups=pups)

@pups_blueprint.route('/delete', methods=['GET','POST'])
def delete():
    form= DelForm()
    if form.validate_on_submit():
        id=form.id.data
        pup = Pup.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('pups.list'))
    return render_template('delete.html', form=form)