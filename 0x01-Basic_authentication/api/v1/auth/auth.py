#!/usr/bin/env python3
"""
template for all authentication system
you will implement
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        To be updated
        """
        return False

    def authorization_header(self, request=None):
        """
        To be updated
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        To be updated
        """
        return None
