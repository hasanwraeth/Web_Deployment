import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db =SQLAlchemy(app)
Migrate(app,db)

class Pup(db.Model):
    __tablename__ = 'pups'
    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.Text)
    toys=db.relationship('Toy', backref='pup',lazy='dynamic')
    owner=db.relationship('Owner', backref='pup',uselist=False)

    def __init__(self, name):
        self.name=name

    def __repr__(self):
        if self.owner:
            return f"Pup name is {self.name} and owner is {self.owner.name}."
        else:
            return f"Pup name is {self.name} and has no owner."
        
    def report_toys(self):
        print("Here are my toys:")
        for toys in self.toys:
            print(toys.name)

class Toy(db.Model):
    __tablename__ = 'toys'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    pid=db.Column(db.Integer,db.ForeignKey('pups.id'))

    def __init__(self,name,pid):
        self.name=name
        self.pid=pid


class Owner(db.Model):
    __tablename__ = 'owners'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    pid=db.Column(db.Integer,db.ForeignKey('pups.id'))

    def __init__(self,name,pid):
        self.name=name
        self.pid=pid
