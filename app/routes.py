# -*- coding: utf-8 -*-
from app import app,db
from app.models import  User, PKVInvoice, Patients
from flask import render_template, flash, redirect, url_for, Flask, request
from app.forms import LoginForm, InvoiceForm
from flask_login import current_user, login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError
from werkzeug.urls import url_parse
from datetime import datetime

datef = '%Y-%m-%d'

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/invoices", methods=['GET', 'POST'])
@login_required
def invoices():
    form = InvoiceForm()
    form.patient.choices = [(a.id, a.patient) for a in Patients.query.order_by(Patients.patient)]
    form.patient.choices.append((0,''))
    if form.validate_on_submit():
        print "patient:", form.patient.data
        sentat=None;paidat=None;repaidat=None
        if form.sent.data:
            sentat = datetime.utcnow()
        if form.paid.data:
            paidat = datetime.utcnow()
        if form.repaid.data:
            repaidat = datetime.utcnow()

        print "=>", form.patient.data

        inv = PKVInvoice(patient_id=form.patient.data,
                         amount=form.amount.data,
                         comment=form.comment.data,
                         invoice_date=form.invoice_date.data,
                         due_date=form.due_date.data,
                         sent_to_pkv=form.sent.data,
                         sent_at=sentat,
                         paid=form.paid.data,
                         paid_at=paidat,
                         repaid=form.repaid.data,
                         repaid_at=repaidat,
                         )
        try:
            db.session.add(inv)
            db.session.commit()
            flash("Invoice created")
        except IntegrityError, e:
            print e.message
        return redirect(url_for('invoices'))
    invoices = PKVInvoice.query.all()
    return render_template('invoices.html', title='Invoices', form=form, invoices=invoices, date_format=datef)

