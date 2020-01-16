"""IDEA API

This file contains most project-level variables that are used by other modules.
It also serves to register Flask blueprints with the app.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# pylint: disable=wrong-import-position
from idea.routes import ideas_bp
# pylint: enable=wrong-import-position

app.register_blueprint(ideas_bp, url_prefix='/ideas')
