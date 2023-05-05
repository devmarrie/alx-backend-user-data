#!/usr/bin/env python3
"""
 different storange
 from the one we are used to
"""
from base import Base



class UserSession(Base):
    """
    Creating a user session
    """
    def __init__(self, *args: list, **kwargs: dict):
        """
        class constructor
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
