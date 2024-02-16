from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, SelectField, 
                     TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    breed=StringField('What breed?', validators=[DataRequired()])
    neuter=BooleanField('Neutered?')
    mood=RadioField('Choose mood:', choices=[('mood_one','Happy'),('mood_two','Excited')])
    food_choice=SelectField(u'Pick favorite food:', choices=[('ch','Chicken'),('bf','Beef'),
                                                             ('fs','Fish'),('vg','Vegetable')])
    feedback=TextAreaField('Feedback:')
    submit=SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed']=form.breed.data
        session['neuter']=form.neuter.data
        session['mood']=form.mood.data
        session['food_choice']=form.food_choice.data
        session['feedback']=form.feedback.data
        flash('Clicked Button!')

        return redirect(url_for('thanks'))
    return render_template('indexff.html',form=form)

@app.route('/thanks')
def thanks():
    return render_template('thanksff.html')

if __name__=='__main__':
    app.run(debug=True)
