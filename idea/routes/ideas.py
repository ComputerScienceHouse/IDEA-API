"""IDEA API - Ideas

This module contains the endpoints related to the idea object.

Endpoints:
    GET     /ideas
    POST    /ideas

"""
from flask import Blueprint, request, jsonify

from idea.models import Ideas

ideas_bp = Blueprint(__name__, 'ideas_bp')


# pylint: disable=inconsistent-return-statements
@ideas_bp.route('/', methods=['GET', 'POST'])
def ideas():
    """
    This endpoint allows a user to get a list of ideas and also to create new
    ideas.

    :GET: Gets a list of the first 20 ideas by default. Can set 'limit' and
        'offset' url parameters to increase, decrease, or offset that number.
    :POST: Creates a new idea. Requires the Content-Type to be application/json
        and for the value "idea_text" to be present.
    """
    if request.method == 'GET':
        limit = 20
        offset = 0

        if request.args.get("limit"):
            limit = int(request.args.get("limit"))
        if request.args.get("offset"):
            offset = int(request.args.get("offset"))

        all_ideas = Ideas.query\
            .order_by(Ideas.idea_time.desc())\
            .limit(limit)\
            .offset(offset*limit)

        return jsonify({
            "status": "success",
            "data": [idea.to_dict() for idea in all_ideas]
        }), 200
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({
                "status": "error",
                "message": "content-type must be application/json"
            }), 415

        idea_text = request.json.get("idea_text")

        if not idea_text:
            return jsonify({
                "status": "error",
                "message": "missing idea_text parameter"
            }), 422

        new_idea = Ideas.create(idea_text, "test")

        return jsonify({
            "status": "success",
            "data": new_idea.to_dict()
        }), 201
