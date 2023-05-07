"""
creates auth routes
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User

# more security for password
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# for API call to Quotes API
import requests

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # check if there exists email and password
        # select query
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category="success")
                login_user(
                    user, remember=True
                )  # remember parameter keeps user logged in
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect Password", category="error")
        else:
            flash("Email not associated with any account", category="error")
    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required  # this route can't be accessed until a user is logged in
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # sign up info checks
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already associated with account.", category="error")
        elif email.count("@") != 1:
            flash("Invalid Email", category="error")
        elif len(email) < 10:
            flash("Invalid Email", category="error")
        elif len(first_name) < 2:
            flash("First Name must be at least 2 characters.", category="error")
        elif len(password1) < 5:
            flash("Password must be at least 5 characters.", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        else:
            # create user
            new_user = User(
                email=email,
                first_name=first_name,
                # hashing method for password
                password=generate_password_hash(password1, method="sha256"),
            )
            db.session.add(new_user)  # add user to database
            db.session.commit()
            flash("Account created", category="success")
            login_user(user, remember=True)
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user=current_user)
