"""
"""

from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"


@auth.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # sign up info checks
        if email.count("@") != 1:
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
            flash("Account created", category="success")

    return render_template("sign_up.html")
