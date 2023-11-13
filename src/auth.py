from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_required, logout_user, login_user
from . import db
from .forms import ConnexionForm, InscriptionForm

auth = Blueprint('auth',__name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = InscriptionForm()
    if request.method == 'GET':
        return render_template('signup.html', form=form)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        address = request.form.get('address')
        ph_nbr = request.form.get('phone_number')
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email Address already exists')
            return redirect(url_for('auth.register'))
        new_user = User(email = email, password = generate_password_hash(password,method="sha256"), phone_number=ph_nbr, nom=nom, prenom=prenom, address=address)
        db.session.add(new_user)
        db.session.commit()
        print(login_user(user=new_user,force=True,))
        flash("A confirmation email has been sent via email.", "success")
        return redirect(url_for('auth.login_post'))
    
@auth.route('/login',methods=['GET', 'POST'])
def login_post():
    form = ConnexionForm()
    print(request.method)
    if request.method == 'GET':
        return render_template('login.html',form=form)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        next_url = request.form.get('next')
        print(email)
        user = User.query.filter_by(email = email).first()
        print(user)
        print(user.password)
        if not user or not check_password_hash(user.password,password):
            flash('Please check your login details and try again')
            return redirect(url_for('auth.login_post'))
        else :
            login_user(user=user,force=True)
            if next_url :
                return redirect(next_url)
            else :
                return redirect(url_for('main.dashboard')) 
            
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.root'))   
