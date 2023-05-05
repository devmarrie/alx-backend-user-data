#!/usr/bin/env python3
"""
Session authentication
"""
from .auth import Auth
import uuid


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
