#!/usr/bin/env python3
"""
Session authentication
"""
from .auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    using session auth
    instead of basic auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None:
            return None
        elif not isinstance(user_id, str):
            return None
        else:
            id = str(uuid.uuid4())
            self.user_id_by_session_id[id] = user_id
            return id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID
        """
        if session_id is None:
            return None
        elif not isinstance(session_id, str):
            return None
        else:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        (overload) that returns a User instance based on a cookie value
        """
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        user = User.get(user_id)
        return user
