#!/usr/bin/env python3
from base import Base
"""
 different storange
"""


class UserSession(Base):
    """
    Creating a user session
    """
    def __init__(self, *args: list, **kwargs: dict):
        """
        class constructor
        """
        self.user_id = 'user_id'
        self.session_id = 'session_id'
