from flask_wtf import Form
from wtforms import Textfield, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class contactform(Form):
    name=Textfield('name of the student',[validators.required('please enter your name')])
    gender=RadioField('gender',choices=[('M','Male'),('F','Female')])
    Address=TextAreaField('Address')
    email=Textfield('email',[validators.required('please enter your email address.'),validators.email('please enter your email')])
    Age=IntegerField('Age')
    language=SelectField('languages',choices=[('cpp','c++'),('py','python'),('js','javascript')])
    submit=SubmitField('send')
