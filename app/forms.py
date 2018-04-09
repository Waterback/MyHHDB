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
    drs = StringField('Dottores', validators=[])
#    sent = BooleanField('Sent to PKV')
    due_date = DateField('Date Due')
#   paid = BooleanField('Paid')
    informed_me = StringField('Information', validators=[])
    invoice_date = DateField('Invoice date')
#    repaid = BooleanField('Repaid')
    submit = SubmitField('new Invoice')
    sent_at = DateField('Invoice Sent', validators=[Optional()])
    paid_at = DateField('Invoice Paid', validators=[Optional()])
    repaid_at = DateField('Invoice Sent', validators=[Optional()])
    patient = SelectField(
        'Patient', coerce=int,
        validators=[DataRequired()],
    )



