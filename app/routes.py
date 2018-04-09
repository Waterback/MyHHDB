# -*- coding: utf-8 -*-
from app import app,db
from app.models import  User, PKVInvoice, Patients
from flask import render_template, flash, redirect, url_for, Flask, request
from app.forms import LoginForm, InvoiceForm
from flask_login import current_user, login_user, login_required, logout_user
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from werkzeug.urls import url_parse
from datetime import datetime, time, date, timedelta, tzinfo

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
        sentat=None;paidat=None;repaidat=None

        inv = PKVInvoice(patient_id=form.patient.data,
                         amount=form.amount.data,
                         comment=form.drs.data,
                         invoice_date=form.invoice_date.data,
                         due_date=form.due_date.data,
                         sent_at=form.sent_at.data,
                         paid_at=form.paid_at.data,
                         repaid_at=form.repaid_at.data,
                         )
        try:
            db.session.add(inv)
            db.session.commit()
            flash("Invoice created")
        except IntegrityError, e:
            flash(e.message)
        return redirect(url_for('invoices'))
    year = request.args.get('year', datetime.now().year, type=int)
    if year <= 1972:
        year = datetime.now().year
    previousyear = year -1
    range = getyearrange_fromyear(year)
    invoices = PKVInvoice.query.filter(PKVInvoice.invoice_date >= range.get('df')).filter(PKVInvoice.invoice_date <= range.get('dt')).all()
    #invoices = PKVInvoice.query.filter(text("invoicedate>=:df and invoice_date<=:dt"))\
     #                           .params(df=range.get('df'), dt=range.get('dt')).order_by(PKVInvoice.invoice_date).all()
    print year, previousyear, "=>", len(invoices)
    print invoices
    return render_template('invoices.html', title='Invoices',
                           form=form, invoices=invoices, date_format=datef, nowyear = datetime.now().year, year=year, previousyear=previousyear)




def getyearrange_fromyear(year):
    return({"df": date(year,1,1), "dt": date(year,12,31)})