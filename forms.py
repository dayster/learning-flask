from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
  first_name = StringField('First name',validators=[DataRequired("Please Enter Your First Name")])
  last_name = StringField('Last name',validators=[DataRequired("Please Enter Your Last Name")])
  email = StringField('Email',validators=[DataRequired("Please Enter Your Email"),Email("Please Enter Your Email Address")])
  password = PasswordField('Password',validators=[DataRequired("Please Enter Your Password"), Length(min=6, message="Passwords must be 6 characters or more")])
  submit = SubmitField('Sign up')

class LoginForm(Form):
	email = StringField('Email',validators=[DataRequired("Please Enter Your Email"),Email("Pleae Enter Your Email")])
	password = PasswordField('Password',validators=[DataRequired("Please Enter Your Password")])
	submit = SubmitField('Login')

class AddressForm(Form):
  address = StringField('Address', validators=[DataRequired("Please enter an address.")])
  submit = SubmitField("Search")
		