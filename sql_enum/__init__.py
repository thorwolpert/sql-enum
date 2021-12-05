"""SQL_Enum module."""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sql_enum import models
from sql_enum.models import db

from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    db.init_app(app)
    return app
