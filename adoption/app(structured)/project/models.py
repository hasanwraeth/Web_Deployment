from project import db

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
    