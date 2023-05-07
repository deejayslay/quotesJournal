"""
creates routes
"""

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json

# for API call to Quotes API
import requests

from .models import Note
from . import db


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
    view_note = False
    quote_text = ""
    quote_category = ""
    quote_author = ""
    note_obj = None
    # when new note button is clicked
    if request.method == "POST":
        # new note button clicked
        if request.form.get("new_note") == "note_created":
            new_note = True
            # get quote from quote API
            quote = get_quote()
            quote_text = quote["quote"]
            quote_author = quote["author"]
            quote_category = quote["category"]
            # display note form along with quote
        # when note is viewed
        elif request.form.get("view_note") == "yes":
            view_note = True
            note_id = request.form.get("note_id")
            note_obj = Note.query.get(note_id)

        # new note added and return to home page
        else:
            note = request.form.get("note")
            quote_text = request.form.get("quote_text")
            quote_author = request.form.get("quote_author")
            quote_category = request.form.get("quote_category")

            if len(note) < 100:
                flash("Note needs to be at least 100 characters long", category="error")
                new_note = True  # new_note still hasn't been saved
            else:
                # add to Note db
                new_note_entry = Note(
                    notes=note,
                    quote=quote_text,
                    quote_author=quote_author,
                    quote_category=quote_category,
                    user_id=current_user.id,
                )
                db.session.add(new_note_entry)
                db.session.commit()
                flash("Note added!", category="success")

    return render_template(
        "home.html",
        n=new_note,
        v=view_note,
        user=current_user,
        no=note_obj,
        qt=quote_text,
        qa=quote_author,
        qc=quote_category,
    )


@views.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note["noteId"]
    note = Note.query.get(noteId)  # look for note that has this note id
    if note:
        if note.user_id == current_user.id:  # if note is user's note
            db.session.delete(note)
            db.session.commit()
    return jsonify({})  # must return something


@views.route("/view-note", methods=["POST"])
def view_note():
    note = json.loads(request.data)
    noteId = note["noteId"]
    note = Note.query.get(noteId)  # look for note that has this note id
    if note:
        if note.user_id == current_user.id:  # if note is user's note
            print(note.quote)
        note = {
            "notes": note.notes,
            "date": note.date,
            "quote": note.quote,
            "author": note.quote_author,
            "category": note.quote_category,
        }
    print("monayyyy")
    return render_template("view_note.html", user=current_user)
