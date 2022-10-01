# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import Email, DataRequired

# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('name',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])
    round_size = IntegerField('round size',
                             id='roundsize_create',
                             validators=[DataRequired()])
    premoney_value = IntegerField('round size',
                             id='premoney_create',
                             validators=[DataRequired()])
    tam = IntegerField('Total Addressable Market',
                             id='tam_create',
                             validators=[DataRequired()])
    sam = IntegerField('Serviceable Addressable Market',
                             id='sam_create',
                             validators=[DataRequired()])
    som = IntegerField('Serviceable Obtainable Market',
                             id='som_create',
                             validators=[DataRequired()])
    submit = SubmitField('Sign Up')




    # input form
class CalculationForm(FlaskForm):
    companyname = StringField('name',
                         id='username_create',
                         validators=[DataRequired()])
    tam = IntegerField('Total Addressable Market',
                             id='tam_create',
                             validators=[DataRequired()])
    sam = IntegerField('Serviceable Addressable Market',
                             id='sam_create',
                             validators=[DataRequired()])
    som = IntegerField('Serviceable Obtainable Market',
                             id='som_create',
                             validators=[DataRequired()])
    round_size = IntegerField('round size',
                             id='roundsize_create',
                             validators=[DataRequired()])
    premoney_value = IntegerField('round size',
                             id='premoney_create',
                             validators=[DataRequired()])
    dilution_estimate = IntegerField('round size',
                             id='premoney_create',
                             validators=[DataRequired()])