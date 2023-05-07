"""
creates routes
"""

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
import json

# for API call to Quotes API
import requests


# use Quotes API to get random quote along with add info about the quote (dict)
def get_quote():
    api_url = "https://api.api-ninjas.com/v1/quotes"
    response = requests.get(
        api_url, headers={"X-Api-Key": "neek5j7w/mZ1jRIobLXuqg==12ZlwmqCd5wBK5jL"}
    )
    if response.status_code == requests.codes.ok:
        # convert response to python dict
        quote = json.loads(response.text)[0]
        return quote
    else:
        print("Error:", response.status_code, response.text)


# current_user checks if user is logged in or not

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])  # decorator
@login_required  # can't get to home page unless logged in
def home():
    new_note = False
    actual_quote = ""
    # when new note button is clicked
    print(request.form.get("new_note"))
    if request.method == "POST":
        # new note button clicked
        if request.form.get("new_note") == "note_created":
            new_note = True
            # get quote from quote API
            quote = get_quote()
            author = quote["author"]
            category = quote["category"]
            actual_quote = quote["quote"]
            # display note form along with quote
        # new note added and return to home page

    return render_template(
        "home.html", n=new_note, user=current_user, quote=actual_quote
    )
