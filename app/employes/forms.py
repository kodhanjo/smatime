from flask_wtf import Form
from wtforms import TextAreaField,SelectField,StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Required,Email,Length,Regexp,EqualTo



class RolesForm(Form):
    name=StringField('Role',validators=[Required()])
    submit=SubmitField('Submit Role')