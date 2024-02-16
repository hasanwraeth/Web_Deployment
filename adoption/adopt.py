import os
from form import AddForm, DelForm, AddOForm
from flask import Flask, render_template, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

#####################
## SQL DATABASE ##
#####################

basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)
Migrate(app,db)

#####################
## MODELS ##
#####################

class Pup(db.Model):
    __tablename__='pups'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    owner=db.relationship('Owner', backref='pup',uselist=False)

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        if self.owner:
                return f"Pup name is {self.name} and owner is {self.owner.name}."
        else:
                return f"Pup name is {self.name} and has no owner."
    
class Owner(db.Model):
    __tablename__ = 'owners'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    pid=db.Column(db.Integer,db.ForeignKey('pups.id'))

    def __init__(self,name,pid):
        self.name=name
        self.pid=pid
    
###############################
## VIEW FUNCTIONS -- HAVE FORMS
###############################
    
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'])
def add_pup():
    form= AddForm()

    if form.validate_on_submit():
        name=form.name.data
        new_pup=Pup(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('add.html', form=form)

@app.route('/list')
def list_pup():
    pups=Pup.query.all()
    return render_template('list.html',pups=pups)

@app.route('/delete',methods=['GET','POST'])
def del_pup():
    form= DelForm()
    if form.validate_on_submit():
        id=form.id.data
        pup = Pup.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)

@app.route('/addo',methods=['GET','POST'])
def add_owner():
    form= AddOForm()
    if form.validate_on_submit():
        pid=form.pid.data
        pup = Pup.query.get(pid)
        name=form.name.data
        new_owner=Owner(name, pid)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('addo.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)