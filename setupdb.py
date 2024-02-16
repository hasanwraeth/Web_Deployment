from db import db, Pup

db.create_all()

lab = Pup('Labby', 3)
fink = Pup ('Finky', 4)

print(lab.id)
print(fink.id)

db.session.add_all([lab,fink])

db.session.commit()
print(lab.id)
print(fink.id)