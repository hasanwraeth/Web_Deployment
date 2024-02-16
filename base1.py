from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thanks')
def thanks():
    fnm=request.args.get('fnm')
    lnm=request.args.get('lnm')
    return render_template('thanks.html',fnm=fnm,lnm=lnm)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)
