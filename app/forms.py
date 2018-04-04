# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, DateField, SelectField
from wtforms.validators import DataRequired, Optional

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class InvoiceForm(FlaskForm):
    #patient = StringField('Patient', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    comment = StringField('Comment', validators=[])
    sent = BooleanField('Sent to PKV')
    due_date = DateField('Date Due', validators=[Optional()])
    paid = BooleanField('Paid')
    invoice_date= DateField('Invoice date' )
    repaid = BooleanField('Repaid')
    submit = SubmitField('new Invoice')

    patient = SelectField(
        'Patient', coerce=int,
        validators=[DataRequired()],
    )



