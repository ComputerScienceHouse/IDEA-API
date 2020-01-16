"""IDEA Models

This module describes the database models used by IDEA.
"""
from datetime import datetime

import pytz
from sqlalchemy.dialects.postgresql import TEXT, TIMESTAMP

from idea import db


class Ideas(db.Model):
    """
    This model describes the Idea table.

    :id: Unique identifier for an idea
    :idea_text: The actual idea
    :submitter: The submitter of the idea
    :idea_time: The time that the idea was submitted
    """
    id = db.Column(db.Integer, primary_key=True)
    idea_text = db.Column(TEXT)
    submitter = db.Column(TEXT)
    idea_time = db.Column(TIMESTAMP)

    def __init__(self, idea_text: str, submitter: str):
        """
        Creates the idea object, must be committed to the database though

        :param idea_text: The text describing the idea
        :param submitter: The person who submitted the idea
        """
        self.idea_text = idea_text
        self.submitter = submitter
        self.idea_time = str(datetime.now(pytz.utc))

    @classmethod
    def create(cls, idea_text: str, submitter: str) -> dict:
        """
        Creates the idea object and commits it to the database

        :param idea_text: The text describing the idea
        :param submitter: The person who submitted the idea
        :return: A dictionary representation of the object
        """
        new_idea = cls(idea_text, submitter)
        db.session.add(new_idea)
        db.session.commit()
        return new_idea.to_dict()

    def to_dict(self) -> dict:
        """
        :return: A dictionary representation of the object
        """
        return {
            "id": self.id,
            "idea_text": self.idea_text,
            "submitter": self.submitter,
            "idea_time": str(self.idea_time)
        }
