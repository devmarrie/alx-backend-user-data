#!/usr/bin/env python3
"""
Session db authentiction
and storage for our ske a file
"""
from .session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """
    move them to db
    from current session
    """
    def create_session(self, user_id=None):
        """
        reates and stores new instance of
        UserSession and returns the Session ID
        """
        sess_id = self.create_session(user_id)
        return sess_id

    def user_id_for_session_id(self, session_id=None):
        """
        returns the User ID by requesting UserSession
        """
        user_id = self.user_id_for_session_id(session_id)
        return user_id

    def destroy_session(self, request=None):
        """
        destroy the database session
        """
        destroy = self.destroy_session(request)
        return destroy
