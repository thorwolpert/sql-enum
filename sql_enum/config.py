"""Configuration for the Application."""
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:
    """Base class configuration that should set reasonable defaults.
    Used as the base for all the other configurations.
    """

    LD_SDK_KEY = os.getenv('LD_SDK_KEY', None)
    SECRET_KEY = 'a secret'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ALEMBIC_INI = 'migrations/alembic.ini'
    # POSTGRESQL
    DB_USER = os.getenv('DATABASE_USERNAME', '')
    DB_PASSWORD = os.getenv('DATABASE_PASSWORD', '')
    DB_NAME = os.getenv('DATABASE_NAME', '')
    DB_HOST = os.getenv('DATABASE_HOST', '')
    DB_PORT = os.getenv('DATABASE_PORT', '5432')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=int(DB_PORT),
        name=DB_NAME,
    )

    TESTING = False
    DEBUG = False
