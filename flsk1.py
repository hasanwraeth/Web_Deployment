from flask import Flask

app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return "<h1>Hello Puppies!</h1>"

@app.route('/info') #127.0.0.1:5000/info
def info():
    return "<h1>Puppy is cute!</h1>"

@app.route('/pup/<name>') #127.0.0.1:5000/info
def pup(name):
    return "<h1>This is a page for {}</h1>".format(name.upper())

@app.route('/pup/1/<number>') #127.0.0.1:5000/info
def pup1(number):
    return "<h1>100th = {}</h1>".format(number[100])

@app.route('/pup_latin/<name>') #127.0.0.1:5000/info
def pup2(name):
    pupnm=''
    if name[-1]== 'y':
        pupnm = name[:-1] + 'iful'
    else:
        pupnm = name[:] + 'y'
    return "<h1>Puppy latin = {}</h1>".format(pupnm)

if __name__=='__main__':
    app.run(debug=True)
