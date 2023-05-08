Quotes Journal

Description: A back-end journaling website, allowing a user to write journaling notes based off a randomly-generated motivational quote. Each user has their own account, and may sign into their account to create new (or delete) journal entries. Mostly done in Python and Flask.

- Note: Starter code taken from Python Flask project tutorial, https://www.youtube.com/watch?v=dam0GPOAvVI&t=4647s

Technologies used:

- Programming Languages: Python, HTML, CSS, JavaScript
- Frameworks: Flask, Bootstrap
- Other: API Ninjas (Quotes API), SQLAlchemy, JSON, Jinja

Files:

- website: holds all info relating to back-end Python Flask website
  - static
    - CSS style sheets for HTML templates
    - index.js
      - uses fetch HTTP request
  - templates
    - all based off base.html
    - uses Jinja templating
    - home.html
      - several different views for home page: view list of notes, view individual note, create new note
  - **init**.py
    - makes website folder a python package
  - auth.py
    - authorization routes
  - views.py
    - view routes
  - models.py
    - database models
- main.py: runs Flask application and starts server
