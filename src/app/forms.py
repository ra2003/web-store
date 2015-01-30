## @package forms
#
#  This file will contain all the logical representation of all the forms used
#  in the application.

from flask_wtf import Form
from wtforms import PasswordField, TextAreaField, StringField
from wtforms.validators import EqualTo, length, InputRequired
from validators import uniqueUser, validEmail


class SingupForm(Form):
    name = StringField('name', [InputRequired()])
    username = StringField('username', [InputRequired(), uniqueUser])
    email = StringField('email', [validEmail])
    password = PasswordField('password', [
        InputRequired(),
        EqualTo('confirm', message="Parolele nu se potrivesc")
    ])
    confirm = PasswordField('repeat_password')


class LoginForm(Form):
    username = StringField('username', [InputRequired()])
    password = PasswordField('password', [InputRequired()])


class AddressForm(Form):
    phone = StringField('phone', [InputRequired()])
    email = StringField('email', [InputRequired()])
    region = StringField('region', [InputRequired()])
    city = StringField('city', [InputRequired()])
    address = StringField('address', [InputRequired()])


class ContactForm(Form):
    name = StringField('name', [InputRequired()])
    email = StringField('email', [InputRequired()])
    message = TextAreaField('message', [InputRequired(), length(max=500)])


class AddNewProductForm(Form):
    name = StringField('name', [InputRequired()])
    price = StringField('price', [InputRequired()])
    stock = StringField('stock', [InputRequired ()])
    description = TextAreaField('description', [InputRequired()])
    category = StringField('category', [InputRequired()])
    pictures = StringField('pictures', [InputRequired()])
    specifications = StringField('specifications', [InputRequired(message="Completeaza ba specificatiile")])