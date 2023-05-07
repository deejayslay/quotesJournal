"""
    makes website a Python package
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# define database
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "qjwebsite"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    # import blueprints
    from .views import views
    from .auth import auth

    # register blueprints with Flask app
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # models defined before creating database
    from .models import User, Quote, Note

    create_database(app)

    return app


# checks if database exists; if it doesn't, db is created
def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Created Database!")
