#Create entries ##
from models import db, Pup, Owner, Toy

rufus = Pup('Rufus')
fido = Pup('Fido')

db.session.add_all([rufus,fido])
db.session.commit()

print(Pup.query.all())

rufus=Pup.query.filter_by(name='Rufus').first()
print(rufus)

hasan= Owner('Hasan',rufus.id)

toy1= Toy('Bone',rufus.id)
toy2= Toy('Ball',rufus.id)

db.session.add_all([hasan, toy1, toy2])
db.session.commit()

rufus=Pup.query.filter_by(name='Rufus').first()
print(rufus.report_toys())