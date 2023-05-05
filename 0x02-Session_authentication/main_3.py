#!/usr/bin/env python3
""" Cookie server
Use this to run:
API_PORT=5000 AUTH_TYPE=session_auth 
SESSION_NAME=_my_session_id ./main_3.py 
curl "http://0.0.0.0:5000" --cookie "_my_session_id=Hello"
"""
from flask import Flask, request
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return "Cookie value: {}\n".format(auth.session_cookie(request))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")