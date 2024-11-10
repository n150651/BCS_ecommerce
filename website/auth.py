from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('home.html')


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        user_name = request.form['name']
        email = request.form['email']
        dob = datetime.strptime(request.form['dob'], "%Y-%m-%d").date()
        gender = request.form['gender']
        password1 = request.form['password1']
        password2 = request.form['password2']
        if len(user_name) < 2:
            flash("name must be greater than  1 characters.", category='error')
        elif len(email) < 4:
            flash("email must be greater than  3 characters.", category='error')
        elif password1 != password2:
            flash("pasword don\'t matched.", category='error')
        elif len(password1) < 7:
            flash("password should be atleast 7 characters.", category='error')
        else:
            # add user to database
            new_user = User(user_name=user_name, email=email, date_of_birth=dob,
                            gender=gender, password=generate_password_hash(password1))
            db.session.commit()
            flash("Account Created!", category="success")

    return render_template('signup.html')
