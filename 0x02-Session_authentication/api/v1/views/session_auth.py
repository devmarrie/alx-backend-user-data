#!/usr/bin/env python3
"""
session authentication views
"""
from api.v1.views import app_views
from models.user import User
from flask import request, jsonify, make_response, abort
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def user_session():
    """
    Fetch email and password from a html form using the post mthd
    searches for a user based on their email
    Returns the user and their session
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or len(email) == 0:
        response = make_response(jsonify('{ "error": "email missing" }'), 400)
        return response
    if password is None or len(password) == 0:
        presponse = make_response(
            jsonify('{ "error": "password missing" }'), 400)
        return presponse
    users = User.search({"email": email})
    if not users or users == []:
        return make_response(
            jsonify('{ "error": "no user found for this email" }'), 404)
    for user in users:
        if not user.is_valid_password(password):
            return make_response(jsonify(
                '{ "error": "wrong password" } '), 401)
        from api.v1.app import auth
        sess_id = auth.create_session(user.id)
        res = make_response(jsonify(user.to_json()))
        session_name = os.getenv('SESSION_NAME')
        res.set_cookie(session_name, sess_id)
        return res

@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def del_session():
    """
    Deletes the session after user logout
    """
    from api.v1.app import auth
    if auth.destroy_session(request) == False:
        abort(404)
    else:
        return jsonify({}), 200

