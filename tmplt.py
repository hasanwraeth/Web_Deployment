from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    mvar='Hasan'
    l=list(mvar)
    pdic={'nm':'Sam'}
    login=False
    return render_template('tmplt.html', mvar=mvar, l=l, pdic=pdic, login=login)

if __name__=='__main__':
    app.run()
