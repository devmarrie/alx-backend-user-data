#!/usr/bin/env python3
"""
Basic flask app
"""
from flask import Flask, jsonify, request, abort, redirect
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """
    Return json respomse
    {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """
    fetches the data to use from a form
    create the user nd return the email
    valueerror if the user exists
    """
    email = request.form.get("email")
    pwd = request.form.get("password")
    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """
    Handles user log in
    Given an email and password
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.valid_login(email, password)
        sess_id = AUTH.create_session(email)
        res = jsonify({"email": email, "message": "logged in"})
        res.set_cookie("session_id", sess_id)
        return res
    except InvalidRequestError:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """
    log out a user and destroy the session
    """
    try:
        sid = request.cookies.get("session_id")
        res = AUTH.get_user_from_session_id(sid)
        AUTH.destroy_session(res.id)
        return redirect("/")
    except NoResultFound:
        abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """
    Fetches the user profile
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "reset_token": reset_token})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
