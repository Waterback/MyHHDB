# -*- coding: utf-8 -*-
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash  = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'. format(self.username)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#invoice_statement = db.Table('mn_invoice_statement',
#    db.Column('invoice_id', db.Integer, db.ForeignKey('pkvinvoice.id'), primary_key=True),
 #   db.Column('insurance_statement_id', db.Integer, db.ForeignKey('insurance_statement.id'), primary_key=True)
#)

class PKVInvoice(db.Model):
    __tablename__= "pkvinvoice"

    id = db.Column(db.Integer, primary_key=True)
    #patient = db.Column(db.String(64), index=True, nullable=False)
    invoice_date = db.Column(db.Date)
    due_date = db.Column(db.Date)
    #drs = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    amount = db.Column(db.Float)
    comment = db.Column(db.String(250))
    sent_to_pkv = db.Column(db.Boolean)
    sent_at = db.Column(db.DateTime)
    paid = db.Column(db.Boolean)
    paid_at = db.Column(db.DateTime)
    repaid = db.Column(db.Boolean)
    repaid_at = db.Column(db.DateTime)
    state = db.Column(db.String(16))

    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    statement_id = db.Column(db.Integer, db.ForeignKey('insurance_statement.id'), nullable=True)

    def __repr__(self):
        return '<Invoice {}>'.format(self.patient.patient )

class Insurance_statement(db.Model):
    __tablename__= "insurance_statement"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    amount_repaid = db.Column(db.Float)
    invoices = db.relationship('PKVInvoice', backref='statement ', lazy=True)

    def __repr__(self):
        return '<Invoice {}>'.format(self.date)


class Patients(db.Model):
    __tablename = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    patient = db.Column(db.String(64), index=True, nullable=False)
    invoices = db.relationship('PKVInvoice', backref='patient', lazy=True)

    def __init__(self, name):
        self.patient = name

    def __repr__(self):
        return '<Patient %s>' % self.name

class SelfPaid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    amount = db.Column(db.Float)



