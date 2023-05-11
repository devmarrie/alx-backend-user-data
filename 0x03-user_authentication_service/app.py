#!/usr/bin/env python3
"""
Basic flask app
"""
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
