from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
    
class AddForm(FlaskForm):
    name=StringField('Name of owner:')
    pid=IntegerField("ID of pup to add owner:")
    submit=SubmitField("Add Owner")