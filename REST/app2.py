import os
from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app= Flask(__name__)
app.config['SECRET_KEY']='mykey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)
Migrate(app,db)

api = Api(app)

jwt=JWT(app, authenticate, identity)

class Puppy(db.Model):
    name = db.Column(db.String(80),primary_key=True)
    def __init__(self,name):
        self.name=name
    def json(self):
        return {'name':self.name}

class PuppyNames(Resource):
    def get(self, name):
        pup=Puppy.query.filter_by(name=name).first()
        if pup:
            return pup.json()
        else:
        #    for pup in puppies:
        #     if pup['name'] == name:
        #         return pup
            return {'name':None}, 404
    
    def post(self, name):
        pup = Puppy(name=name)
        db.session(pup)
        db.session.commit()
        return pup.json
        # pup = {'name':name}
        # puppies.append(pup)
        # return pup

    def delete(self, name):
        # for ind, pup in enumerate(puppies):
        #     if up['name'] == name:
        #         deleted_pup = puppies.pop(ind)
        pup=Puppy.query.filter_by(name=name).first()
        db.session.delete(pup)
        db.session.commit()
        return {'note':'delete success'}

class AllNames(Resource):
    # @jwt_required()
    def get(self):
        # return {'puppies':puppies}
        puppies = Pupp.quer.all()
        return [pup.json() for pup in puppies]

api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames, '/puppies')

if __name__=='__main__':
    app.run(debug=True)