from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/pup/<name>')
def pupnm(name):
    return render_template('pup.html', name=name)

if __name__=='__main__':
    app.run(debug=True)
