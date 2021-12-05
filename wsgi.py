"""Provides the WSGI entry point for running the application
"""
from sql_enum import create_app
from flask_migrate import Migrate
from sql_enum.models import db



# Openshift s2i expects a lower case name of application
application = create_app() # pylint: disable=invalid-name

migrate = Migrate(application, db)

if __name__ == "__main__":
    application.run()