from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class PolicyInfoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=20)])
    fullname = StringField('Full Name', validators=[DataRequired(), Length(max=80)])
    phone = IntegerField('Phone Number', validators=[DataRequired(), Length(max=10)])
    policyaddress = TextAreaField('Address', validators=[DataRequired(), Length(max=10)])
    country = StringField('Country', validators=[DataRequired(), Length(min=20)])
    percentage = IntegerField('Percentage', validators=[DataRequired(), Length(min=20)])
    termtype = IntegerField('Term Type', validators=[DataRequired(), Length(min=20)])
    termnumber = IntegerField('Term Number', validators=[DataRequired(), Length(min=20)])
    startdate = DateField('Start Date', format="%d-%m-%Y")
    expirydate = DateField('End Date', format="%d-%m-%Y")
    ltabtn = RadioField('LTA(Long Term Agreement', choices = [('Y', 'Yes'), ('N', 'No')])
    proceed = SubmitField('Proceed')
