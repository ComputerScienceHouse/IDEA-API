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
