from db import db, Pup

##CREATE##
my_pup = Pup('Rufus', 5)
db.session.add(my_pup)
db.session.commit()

##READ##
all_pups = Pup.query.all()
print (all_pups)

## SELECT BY ID ##
pup_1 = Pup.query.get(1)
print(pup_1)

##FILTER##
pup_rufus = Pup.query.filter_by(name='Finky')
print(pup_rufus.all())

##UPDATE##
pup_1e = Pup.query.get(1)
pup_1e.age= 10
db.session.add(pup_1e)
db.session.commit()

##DELETE##
pup_2e=Pup.query.get(2)
db.session.delete(pup_2e)
db.session.commit()

all_pups = Pup.query.all()
print (all_pups)
