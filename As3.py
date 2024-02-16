from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/report')
def report():
    low=False
    up=False
    num=False
    unm=request.args.get('unm')

    low=any(c.islower() for c in unm)
    up=any(c.isupper() for c in unm)
    num=unm[-1].isdigit()

    report = low and up and num

    return render_template('report3.html', report=report, low=low, up=up, num=num)

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
