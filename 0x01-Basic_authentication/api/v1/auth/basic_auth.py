#!/usr/bin/env python3
"""
Inherits from Auth
"""
from .auth import Auth
from typing import Tuple
import base64


class BasicAuth(Auth):
    """
    This class will represent the
    basic auth implementation of the user
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extract the base64 code
        from the authorization header
        """
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif not authorization_header.startswith("Basic "):
            return None
        credentials = authorization_header.split(" ")[-1]
        return credentials

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a
        base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            tobytes = base64_authorization_header.encode('utf-8')
            tob64 = base64.b64decode(tobytes)
            return tob64.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Tuple[str, str]:
        """
        returns the user email and password
        from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        splited = decoded_base64_authorization_header.split(":")
        email = splited[0]
        password = splited[-1]
        return (email, password)
    