"""
    makes website a Python package
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

    return app
