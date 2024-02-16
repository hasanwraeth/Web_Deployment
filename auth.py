from flask_bcrypt import Bcrypt

bcrypt=Bcrypt()

passw = 'supersecretpassword'

hashed_passw=bcrypt.generate_password_hash(password=passw)

print(hashed_passw)

check = bcrypt.check_password_hash(hashed_passw, 'wronpassword')

print(check)

check2 = bcrypt.check_password_hash(hashed_passw, 'supersecretpassword')

print(check2)

from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass2 = generate_password_hash(password=passw)
print(hashed_pass2)

check3 = check_password_hash(hashed_pass2, 'wronpassword')

print(check3)

check4 = check_password_hash(hashed_pass2, 'supersecretpassword')

print(check4)