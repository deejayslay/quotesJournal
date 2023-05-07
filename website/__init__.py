"""
    makes website folder a Python package
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# flask_login manages which pages can be accessed and which pages cannot
from flask_login import LoginManager

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
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"  # redirect url if not logged in
    login_manager.init_app(app)

    # tells Flask which user we're looking for
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))  # get method automatically checks primary key

    return app


# checks if database exists; if it doesn't, db is created
def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Created Database!")
