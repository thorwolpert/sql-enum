"""DB service."""
from flask_sqlalchemy import SQLAlchemy


# by convention in the Flask community these are lower case,
# whereas pylint wants them upper case
db = SQLAlchemy()  # pylint: disable=invalid-name
