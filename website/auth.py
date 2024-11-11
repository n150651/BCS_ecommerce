from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Users, db
from werkzeug.security import generate_password_hash, check_password_hash
from . import views

from datetime import datetime
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password Try Again!", category="error")
        else:
            flash("User does not exist!!", category="error")

    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('home.html')


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        data = request.get_json()
        data['password'] = generate_password_hash(data['password1'])
        data['dob'] = datetime.strptime(data['dob'], "%Y-%m-%d").date()
        # Remove password confirmation field
        data.pop('password2', None)
        data.pop('password1', None)
        new_user = Users(**data)
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        flash("User created!!", category="success")
        return redirect(url_for('views.home'))
        # Ensure 'home' is the correct endpoint
    return render_template('signup.html')
